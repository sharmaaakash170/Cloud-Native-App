from fastapi import APIRouter, HTTPException
import redis
import psycopg2
import os
from psycopg2 import pool

router = APIRouter()

# Redis client (with connection handling)
redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=6379,
    socket_connect_timeout=5,
    socket_timeout=5
)

# PostgreSQL connection pool
postgres_pool = None

def get_db_connection():
    global postgres_pool
    if postgres_pool is None:
        postgres_pool = psycopg2.pool.SimpleConnectionPool(
            minconn=1,
            maxconn=10,
            host=os.getenv("POSTGRES_HOST", "postgres"),
            database="postgres",
            user="postgres",
            password="postgres"
        )
    return postgres_pool.getconn()

@router.get("/items/{item_id}")
def read_item(item_id: int):
    try:
        # Try Redis cache
        cached = redis_client.get(f"item:{item_id}")
        if cached:
            return {"item_id": item_id, "data": cached.decode(), "source": "cache"}
        
        # Fallback to DB
        conn = get_db_connection()
        with conn.cursor() as cur:
            cur.execute("SELECT name FROM items WHERE id = %s;", (item_id,))
            row = cur.fetchone()
            if row:
                redis_client.set(f"item:{item_id}", row[0])
                return {"item_id": item_id, "data": row[0], "source": "db"}
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        raise HTTPException(status_code=503, detail="Service unavailable")
    finally:
        if 'conn' in locals():
            postgres_pool.putconn(conn)