from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import redis
import asyncpg
import os
from dotenv import load_dotenv
from contextlib import asynccontextmanager

load_dotenv()

# Async PostgreSQL connection pool
pool = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Create DB connection pool
    global pool
    pool = await asyncpg.create_pool(
        host=os.getenv('POSTGRES_HOST', 'postgres'),
        port=int(os.getenv('POSTGRES_PORT', 5432)),
        user=os.getenv('POSTGRES_USER', 'postgres'),
        password=os.getenv('POSTGRES_PASSWORD', 'password'),
        database=os.getenv('POSTGRES_DB', 'appdb')
    )
    yield
    # Shutdown: Close pool
    await pool.close()

app = FastAPI(lifespan=lifespan)

# Redis configuration (using connection pool for better performance)
redis_client = redis.Redis(
    host=os.getenv('REDIS_HOST', 'redis'),
    port=int(os.getenv('REDIS_PORT', 6379)),
    db=0,
    decode_responses=True
)

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}


@app.get("/redis")
def redis_test():
    try:
        redis_client.set('test_key', 'Hello from Redis!')
        value = redis_client.get('test_key')
        return {"redis_value": value}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/postgres")
async def postgres_test():
    try:
        async with pool.acquire() as connection:
            result = await connection.fetchrow("SELECT 1")
            return {"postgres_status": "Connected successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=6000)
