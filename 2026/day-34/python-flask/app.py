from flask import Flask
import redis
import psycopg2
import os

app = Flask(__name__)

r = redis.Redis(host='redis', port=6379)

@app.route('/')
def hello():
    # Increment visit counter in Redis
    visits = r.incr('visits')
    
    # Connect to Postgres
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'appdb'),
        user=os.environ.get('DB_USER', 'appuser'),
        password=os.environ.get('DB_PASSWORD', 'apppass')
    )
    conn.close()
    
    
    return f"🚀 Welcome to my Flask app! Total visits: {visits}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
