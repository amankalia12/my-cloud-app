import os
import psycopg2
from flask import Flask, request, jsonify

app = Flask(__name__)

# These come from the Cloud Environment Variables
DB_URL = os.environ.get('DATABASE_URL')
AUTH_TOKEN = "my-secret-key-123" 

@app.route('/')
def home():
    return "🏠 App is running. Use /data to see DB records."

@app.route('/data')
def get_data():
    # 1. Simple Authentication Check
    user_key = request.headers.get('Authorization')
    if user_key != AUTH_TOKEN:
        return jsonify({"error": "Unauthorized"}), 401

    # 2. Database Action
    try:
        conn = psycopg2.connect(DB_URL)
        cur = conn.cursor()
        cur.execute("SELECT version();") # Simple test query
        db_version = cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"status": "Connected", "db_version": db_version})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)