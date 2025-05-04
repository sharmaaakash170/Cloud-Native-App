import React from 'react';

function Item({ item }) {
  return (
    <div>
      <h2>Item ID: {item.item_id}</h2>
      <p>Data: {item.data}</p>
      <p>Source: {item.source}</p>
    </div>
  );
}

export default Item;
