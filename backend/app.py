<<<<<<< HEAD
from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
import os

app = Flask(__name__)
CORS(app)

# Connect to PostgreSQL
DB_URL = os.getenv("DATABASE_URL", "dbname=loans user=postgres password=postgres host=localhost")
conn = psycopg2.connect(DB_URL)
conn.autocommit = True

# Create table if it doesn't exist
with conn.cursor() as cur:
    cur.execute("""
        CREATE TABLE IF NOT EXISTS loans (
            id SERIAL PRIMARY KEY,
            borrower_name TEXT,
            amount NUMERIC,
            interest_rate NUMERIC,
            term_months INTEGER
        )
    """)

@app.route('/api/loans', methods=['GET'])
def get_loans():
    with conn.cursor() as cur:
        cur.execute("SELECT id, borrower_name, amount, interest_rate, term_months FROM loans")
        rows = cur.fetchall()
        loans = [
            {
                "id": row[0],
                "borrower_name": row[1],
                "amount": float(row[2]),
                "interest_rate": float(row[3]),
                "term_months": row[4]
            } for row in rows
        ]
        return jsonify(loans)

@app.route('/api/loans', methods=['POST'])
def add_loan():
    data = request.get_json()
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO loans (borrower_name, amount, interest_rate, term_months) VALUES (%s, %s, %s, %s)",
            (data['borrower_name'], data['amount'], data['interest_rate'], data['term_months'])
        )
    return jsonify({"message": "Loan added"}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
=======
>>>>>>> 6edfe47bd2c7ce28afe14b207b8bcf4215c61dc9
import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Backend is running!"

if __name__ == "__main__":
<<<<<<< HEAD
    port = int(os.environ.get("PORT", 5000))  # Default to 5000
    app.run(host="0.0.0.0", port=port)
=======
    port = int(os.environ.get("PORT", 5000))  # Render sets this env variable
    app.run(host="0.0.0.0", port=port)        # Bind to all interfaces
>>>>>>> 6edfe47bd2c7ce28afe14b207b8bcf4215c61dc9
