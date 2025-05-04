from prometheus_client import Counter, Summary

# Define metrics
GET_ITEM_CLICK_TOTAL = Counter("get_item_click_total", "Total get item button clicks")
API_RESPONSE_DURATION_SECONDS = Summary("api_response_duration_seconds", "API response duration in seconds")

def record_event(event: str, value: float = 1.0):
    if event == "get_item_click_total":
        GET_ITEM_CLICK_TOTAL.inc()
    elif event == "api_response_duration_seconds":
        API_RESPONSE_DURATION_SECONDS.observe(value)
