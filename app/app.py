import os
from flask import Flask, jsonify
import pymysql

app = Flask(__name__)


def get_db_connection():
  """Crea una conexión con la base de datos usando variables de entorno."""
  return pymysql.connect(
      host=os.getenv('DB_HOST', 'db'),
      user=os.getenv('DB_USER', 'user'),
      password=os.getenv('DB_PASSWORD', 'secret'),
      database=os.getenv('DB_NAME', 'appdb'),
      connect_timeout=3,
  )


@app.route('/health', methods=['GET'])
def health_check():
  connection = None
  try:
    connection = get_db_connection()
    connection.ping(reconnect=False)
    return jsonify({'status': 'healthy', 'database': 'connected'}), 200

  except Exception as e:
    return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

  finally:
    if connection:
      connection.close()


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)