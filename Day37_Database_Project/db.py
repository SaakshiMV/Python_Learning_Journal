import sqlite3

DB_NAME = "expenses.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        amount REAL,
        category TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_expense(title, amount, category):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (title, amount, category) VALUES (?, ?, ?)",
        (title, amount, category)
    )

    conn.commit()
    conn.close()
    print("Expense added!")

def get_all_expenses():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    data = cursor.fetchall()

    conn.close()
    return data

def update_expense(expense_id, title, amount, category):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE expenses SET title=?, amount=?, category=? WHERE id=?",
        (title, amount, category, expense_id)
    )

    conn.commit()
    conn.close()

def delete_expense(expense_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))

    conn.commit()
    conn.close()

def get_by_category(category):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM expenses WHERE category=?",
        (category,)
    )

    data = cursor.fetchall()
    conn.close()
    return data

def get_total():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT SUM(amount) FROM expenses")
    total = cursor.fetchone()[0]

    conn.close()
    return total if total else 0
