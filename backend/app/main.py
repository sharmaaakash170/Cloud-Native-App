from fastapi import FastAPI
from routers import health, items
from prometheus_client import make_asgi_app
from fastapi.middleware.cors import CORSMiddleware
from routers import metrics


app = FastAPI(title="Cloud Native App")
app.include_router(metrics.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as necessary (e.g., for security reasons, only allow specific origins)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
# app.include_router(health.router)
# app.include_router(items.router)
# main.py
app.include_router(items.router, prefix="/api")
app.include_router(health.router, prefix="/api")


# Prometheus metrics endpoint
app.mount("/metrics", make_asgi_app())
