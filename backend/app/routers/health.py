from fastapi import APIRouter, HTTPException
import redis
import psycopg2
import os

router = APIRouter()

@router.get("/health")
def health_check():
    # Check Redis
    redis_client = redis.Redis(
        host=os.getenv("REDIS_HOST", "redis"),
        port=6379,
        socket_connect_timeout=2
    )
    try:
        if not redis_client.ping():
            raise HTTPException(status_code=503, detail="Redis unavailable")
    except Exception:
        raise HTTPException(status_code=503, detail="Redis connection failed")
    finally:
        redis_client.close()

    # Check PostgreSQL
    try:
        conn = psycopg2.connect(
            host=os.getenv("POSTGRES_HOST", "postgres"),
            database="postgres",
            user="postgres",
            password="postgres",
            connect_timeout=2
        )
        with conn.cursor() as cur:
            cur.execute("SELECT 1")
        conn.close()
    except Exception:
        raise HTTPException(status_code=503, detail="PostgreSQL unavailable")

    return {"status": "healthy", "services": ["redis", "postgresql"]}