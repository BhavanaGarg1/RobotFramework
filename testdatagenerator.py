def generate_data(db_path="shop.db"):
    from faker import Faker
    import sqlite3
    import random

    fake = Faker()
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # -----------------------------
    # 1. Create Tables
    # -----------------------------
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    address TEXT,
    created_at TEXT
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    description TEXT,
    price REAL,
    stock INTEGER
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    order_date TEXT,
    total REAL,
    FOREIGN KEY(user_id) REFERENCES users(id)
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS order_items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    price REAL,
    FOREIGN KEY(order_id) REFERENCES orders(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
    )
    ''')

    # -----------------------------
    # 2. Populate Users
    # -----------------------------
    user_ids = []
    for _ in range(20):
        name = fake.name()
        email = fake.unique.email()
        address = fake.address().replace('\n', ', ')
        created_at = fake.date_time_this_year().isoformat()

    cursor.execute('''
    INSERT INTO users (name, email, address, created_at)
    VALUES (?, ?, ?, ?)
    ''', (name, email, address, created_at))
    user_ids.append(cursor.lastrowid)

    # -----------------------------
    # 3. Populate Products
    # -----------------------------
    product_ids = []
    for _ in range(10):
        name = fake.word().capitalize()
        description = fake.sentence()
        price = round(random.uniform(10.0, 500.0), 2)
        stock = random.randint(10, 100)

    cursor.execute('''
    INSERT INTO products (name, description, price, stock)
    VALUES (?, ?, ?, ?)
    ''', (name, description, price, stock))
    product_ids.append(cursor.lastrowid)

    # -----------------------------
    # 4. Populate Orders and Order Items
    # -----------------------------
    for _ in range(30):  # 30 orders
        user_id = random.choice(user_ids)
        order_date = fake.date_time_this_year().isoformat()
        total = 0
        order_items = []

    for _ in range(random.randint(1, 4)):  # each order has 1–4 items
        product_id = random.choice(product_ids)
        quantity = random.randint(1, 5)
        cursor.execute('SELECT price FROM products WHERE id = ?', (product_id,))
        price = cursor.fetchone()[0]
        total += price * quantity
        order_items.append((product_id, quantity, price))

    # Insert order
    cursor.execute('''
    INSERT INTO orders (user_id, order_date, total)
    VALUES (?, ?, ?)
    ''', (user_id, order_date, round(total, 2)))
    order_id = cursor.lastrowid

    # Insert order items
    for product_id, quantity, price in order_items:
        cursor.execute('''
        INSERT INTO order_items (order_id, product_id, quantity, price)
        VALUES (?, ?, ?, ?)
        ''', (order_id, product_id, quantity, price))

    # -----------------------------
    # 5. Finalize
    # -----------------------------
    conn.commit()
    conn.close()

    print("Fake data inserted: users, products, orders, order_items!")

    conn.commit()
    conn.close()
    return db_path


# Tables to Create:
# users – customer details
#
# products – catalog of items
#
# orders – orders placed by users
#
# order_items – line items for each order