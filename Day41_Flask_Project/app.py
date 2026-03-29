from flask import Flask, render_template, request, redirect
from db import create_table, add_expense, get_expenses

app = Flask(__name__)

create_table()

@app.route("/")
def home():
    expenses = get_expenses()
    return render_template("index.html", expenses=expenses)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        amount = float(request.form.get("amount"))

        add_expense(title, amount)
        return redirect("/")

    return render_template("add.html")

if __name__ == "__main__":
    app.run(debug=True)
