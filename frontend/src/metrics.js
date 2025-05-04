export function trackMetric(event, value = 1) {
    fetch("http://localhost:8000/metrics/custom", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ event, value })
    }).catch(err => console.error("Metric send failed:", err));
  }
  