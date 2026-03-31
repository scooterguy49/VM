from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# This is here to make sure that users.db is created in the correct lab directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "users.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)

    cur.execute("SELECT * FROM users")
    if not cur.fetchall():
        cur.execute("INSERT INTO users (username, password) VALUES ('alice', 'password123')")
        cur.execute("INSERT INTO users (username, password) VALUES ('bob', 'secure456')")
        cur.execute("INSERT INTO users (username, password) VALUES ('admin', 'adminpass')")

    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def login():
    message = ""
    query_text = ""

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()

        # INTENTIONALLY VULNERABLE: directly combines user input into the SQL string
        query_text = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        print("Executing query:", query_text)

        cur.execute(query_text)
        user = cur.fetchone()

        conn.close()

        if user:
            message = "Login successful!"
        else:
            message = "Invalid credentials."

    return render_template("login.html", message=message, query_text=query_text)

if __name__ == "__main__":
    init_db()
    app.run(debug=True)