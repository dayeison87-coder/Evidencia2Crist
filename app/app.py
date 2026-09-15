from flask import Flask, jsonify
import pymysql
import os

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
  try:
    db.ping(reconnect=False)
    return jsonify({"status": "healthy", "database": "connected"}), 200
  except Exception as e:
    return jsonify({"status": "unhealthy", "error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)