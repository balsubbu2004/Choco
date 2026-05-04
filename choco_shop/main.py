from flask import Flask, render_template,request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('orders.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS orders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quantity INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        quantity = request.form.get('quantity')
        conn = get_db_connection()
        conn.execute('INSERT INTO orders (quantity) VALUES (?)', (quantity,))
        conn.commit()
        conn.close()
        return f"You ordered {quantity} chocolates"
    return render_template("home.html")

if __name__ == '__main__':
    init_db()
    app.run()
