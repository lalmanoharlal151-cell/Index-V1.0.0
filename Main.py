from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="All In One Pro - Dukan Sathi AI")

class CartItem(BaseModel):
    item_id: int
    quantity: int

class BillRequest(BaseModel):
    items: List[CartItem]

# Dukaan ka sample inventory data
inventory = [
    {"id": 1, "name": "Chini (Sugar)", "price": 45.0, "stock": 100},
    {"id": 2, "name": "Chai Patti", "price": 120.0, "stock": 50},
    {"id": 3, "name": "Dal (Arhar)", "price": 140.0, "stock": 80}
]

@app.get("/")
def home():
    return {"message": "All In One Pro (Dukan Sathi AI) Server Active hai!"}

@app.get("/items")
def get_inventory():
    return {"inventory": inventory}

@app.post("/bill")
def generate_bill(request: BillRequest):
    total_amount = 0.0
    bill_details = []
    
    for cart_item in request.items:
        item = next((i for i in inventory if i["id"] == cart_item.item_id), None)
        if not item:
            raise HTTPException(status_code=404, detail=f"Item ID {cart_item.item_id} nahi mila")
        if item["stock"] < cart_item.quantity:
            raise HTTPException(status_code=400, detail=f"{item['name']} ka stock kam hai")
        
        # Stock update karein
        item["stock"] -= cart_item.quantity
        item_total = item["price"] * cart_item.quantity
        total_amount += item_total
        
        bill_details.append({
            "name": item["name"],
            "price": item["price"],
            "quantity": cart_item.quantity,
            "total": item_total
        })
        
    return {
        "status": "Success",
        "bill_details": bill_details,
        "grand_total": total_amount
    }

