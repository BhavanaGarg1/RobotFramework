import sqlite3
import os
import pytest
from testdatagenerator import generate_data
import logging
import re

@pytest.fixture(scope="module")
def db_conn():
    db_path = "test_shop.db"
    generate_data(db_path)
    conn = sqlite3.connect(db_path)
    yield conn
    conn.close()

    os.remove(db_path)

def test_tables_exist(db_conn):
    cursor = db_conn.cursor()
    tables = ['users', 'products', 'orders', 'order_items']
    for table in tables:
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table}'")
        logging.info(f"Checked table presence, found (len{table}) presence.")
        assert cursor.fetchone(), f"Table '{table}' does not exist."

def test_users_populated(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM users")
    count = cursor.fetchone()[0]
    assert count > 0

def test_orders_have_valid_users(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("""
        SELECT o.id FROM orders o
        LEFT JOIN users u ON o.user_id = u.id
        WHERE u.id IS NULL
    """)
    assert cursor.fetchone() is None, "Some orders reference non-existent users."

def test_order_items_have_valid_orders_and_products(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("""
        SELECT oi.id FROM order_items oi
        LEFT JOIN orders o ON oi.order_id = o.id
        LEFT JOIN products p ON oi.product_id = p.id
        WHERE o.id IS NULL OR p.id IS NULL
    """)
    assert cursor.fetchone() is None, "Some order items reference non-existent orders/products."
