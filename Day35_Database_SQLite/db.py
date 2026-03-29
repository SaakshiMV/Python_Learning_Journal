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
        amount REAL
    )
    """)

    conn.commit()
    conn.close()

def add_expense(title, amount):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO expenses (title, amount) VALUES (?, ?)", (title, amount))

    conn.commit()
    conn.close()
    print("Expense added!")

def view_expenses():
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()

    if not rows:
        print("No expenses found.")
    else:
        print("\nExpenses:")
        for row in rows:
            print(row)

    conn.close()
