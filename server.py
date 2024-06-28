from flask import Flask, render_template, request, redirect, session
import secrets
from user import User

app = Flask(__name__)
# app.secret_key =


@app.route("/users")
def display_users():
    all_users = User.get_all()
    print(all_users)
    return render_template("read_all.html", all_users=all_users)


@app.route("/users/new")
def show_page():
    return render_template("create.html")


@app.route("/create_user", methods=["POST"])
def create_user():
    data = {
        "fname": request.form["fname"],
        "lname": request.form["lname"],
        "email": request.form["email"],
    }
    User.create_user(data)
    return redirect("/users")


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port="5150")
