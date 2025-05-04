import React, { useState } from "react";
import Item from "./components/Item";
import { trackMetric } from "./metrics";


const BACKEND_BASE_URL = "http://localhost:8000"; // Adjust this in production

function App() {
  const [items, setItems] = useState([]);
  const [itemId, setItemId] = useState("");

  const fetchItem = async () => {
    const cleanId = itemId.trim().replace(/[^\d]/g, ""); // Remove non-numeric chars
    

    if (!cleanId) {
      alert("Please enter a valid numeric ID");
      return;
    }

    try {
      const response = await fetch(`${BACKEND_BASE_URL}/api/items/${cleanId}`);
      const data = await response.json();
      trackMetric("get_item_click_total");
      const start = Date.now();
      const duration = (Date.now() - start) / 1000;
      trackMetric("api_response_duration_seconds", duration);

      if (data.error) {
        alert(data.error);
      } else {
        setItems([data]);
      }
    } catch (error) {
      console.error("Error fetching data:", error);
      alert("Failed to fetch item. Check backend connection.");
    }
  };

  return (
    <div className="App">
      <h1>Cloud Native App - Frontend</h1>

      <input
        type="text"
        value={itemId}
        onChange={(e) => setItemId(e.target.value.replace(/[^\d]/g, ""))} // real-time sanitization
        placeholder="Enter Item ID"
      />

      <button onClick={fetchItem}>Get Item</button>

      <div>
        {items.map((item, index) => (
          <Item key={index} item={item} />
        ))}
      </div>
    </div>
  );
}

export default App;
