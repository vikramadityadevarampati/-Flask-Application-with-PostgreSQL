from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Flask with PostgreSQL!"

@app.route('/data')
def get_data():
    conn = psycopg2.connect("dbname=test user=postgres password=postgres host=db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM sample;")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
