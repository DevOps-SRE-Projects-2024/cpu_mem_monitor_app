import psutil
from flask import Flask, render_template, send_from_directory, jsonify, request, redirect, session
from flask_session.__init__ import Session
import os

key = os.urandom(8)
app = Flask(__name__, static_folder='static')
app.secret_key = key
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
# Dictionary to store registered users (for simplicity, you may want to use a database in a real application)
users = {'admin': 'admin'}

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username and password:
            # Check if the username is already taken
            if username in users:
                error_msg = "Username already taken. Please choose a different one."
                return render_template("register.html", error_msg=error_msg)

            # Add the new user to the users dictionary
            users[username] = password
            session["logged_in"] = True
            return redirect("/")

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if username in users and users[username] == password:
            session["logged_in"] = True
            return redirect("/")
        else:
            error_msg = "Invalid username or password. Please try again."
            return render_template("login.html", error_msg=error_msg)

    if session.get("logged_in"):
        return redirect("/")

    return render_template("login.html")


@app.route('/images/background.jpeg')
def serve_static():
    return send_from_directory('static/images', 'background.jpeg')


@app.route("/logout")
def logout():
    session.pop("logged_in", None)
    return redirect("/login")


@app.route("/data")
def data():
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    msg = "OK"
    if cpu_usage > 80 or mem_usage > 80:
        msg = "Warning"
    return jsonify(cpu_usage=cpu_usage, mem_usage=mem_usage, msg=msg)


@app.route("/")
def index():
    if not session.get("logged_in"):
        return redirect("/login")
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    return render_template("index.html", cpu_usage=cpu_usage, mem_usage=mem_usage)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
