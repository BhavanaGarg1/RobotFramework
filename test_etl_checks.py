# Duplicate check on email
# Null checks on name, email
# Transformation/format check (e.g. valid email format)
#  Uniqueness of primary key
# Length Validation for name

import re
import logging

def test_user_email_unique(db_conn):
    cursor = db_conn.cursor()
    cursor.execute('''
        SELECT email, COUNT(*) FROM users
        GROUP BY email
        HAVING COUNT(*) > 1
    ''')
    duplicates = cursor.fetchall()
    logging.info(f"Checked email uniqueness, found {len(duplicates)} duplicates.")
    assert not duplicates, f"Duplicate emails found: {duplicates}"

def test_user_required_fields_not_null(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users WHERE name IS NULL OR email IS NULL")
    nulls = cursor.fetchone()[0]
    logging.info(f"Checked for NULLs in name/email, found {nulls} nulls.")
    assert nulls == 0, "Found NULL in name or email fields"

def test_user_email_format_valid(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT email FROM users")
    invalid = []
    for (email,) in cursor.fetchall():
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            invalid.append(email)
    logging.info(f"Checked for user email format, found {len(invalid)} emails")
    assert not invalid, f"Invalid email formats found: {invalid}"

def test_user_id_unique_primary_key(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT id, COUNT(*) FROM users GROUP BY id HAVING COUNT(*) > 1")
    dupes = cursor.fetchall()
    logging.info(f"Checked for user IDs, found {len(dupes)} userId duplicated")
    assert not dupes, "Duplicate user IDs found"

def test_user_name_length_reasonable(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT name FROM users WHERE LENGTH(name) < 3 OR LENGTH(name) > 50")
    names = cursor.fetchall()
    logging.info(f"Checked for user length, found {len(names)} invalid user names")
    assert not names, "Some user names are too short or too long"

#pytest tests/ --html=report.html --self-contained-html


