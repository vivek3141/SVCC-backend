from flask import Flask, request
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)


@app.route("/submit")
def submit():
    name = request.args.get('name')
    with sqlite3.connect('data.db') as conn:
        c = conn.cursor()
        c.execute("INSERT INTO names VALUES (?)", (name))
        conn.commit()
