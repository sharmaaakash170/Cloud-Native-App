from fastapi import APIRouter, Request
from services.metrics import record_event

router = APIRouter()

@router.post("/metrics/custom")
async def custom_metrics(request: Request):
    body = await request.json()
    record_event(body["event"], body.get("value", 1.0))
    return {"status": "ok"}
