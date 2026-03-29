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

    cursor.execute(
        "INSERT INTO expenses (title, amount) VALUES (?, ?)",
        (title, amount)
    )

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
            print(f"ID: {row[0]} | {row[1]} | ₹{row[2]}")

    conn.close()

def update_expense(expense_id, new_title, new_amount):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE expenses SET title = ?, amount = ? WHERE id = ?",
        (new_title, new_amount, expense_id)
    )

    conn.commit()

    if cursor.rowcount == 0:
        print("No expense found with that ID.")
    else:
        print("Expense updated!")

    conn.close()

def delete_expense(expense_id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    conn.commit()

    if cursor.rowcount == 0:
        print("No expense found with that ID.")
    else:
        print("Expense deleted!")

    conn.close()
