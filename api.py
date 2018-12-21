from flask import Flask, request
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)


@app.route("/submit")
def submit():
    name = request.args.get('name')
    try:
        with sqlite3.connect('data.db') as conn:
            c = conn.cursor()
            c.execute("INSERT INTO names VALUES (?)", (name,))
            conn.commit()
    except sqlite3.Error as c:
        return str(c)
    return "Success"


@app.route("/get")
def get():
    try:
        with sqlite3.connect('data.db') as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM names")
            ret = list(map(lambda x: str(x[0]), c.fetchall()))
    except sqlite3.Error:
        return "Error"
    print()
    return "<br>".join(ret)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
