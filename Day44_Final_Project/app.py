from flask import Flask, render_template, request, redirect
from db import create_table, add_expense, get_expenses, delete_expense, get_total

app = Flask(__name__)

create_table()

@app.route("/")
def home():
    expenses = get_expenses()
    total = get_total()
    return render_template("index.html", expenses=expenses, total=total)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        title = request.form.get("title")
        category = request.form.get("category")
        amount = float(request.form.get("amount"))

        add_expense(title, amount, category)
        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    delete_expense(id)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
