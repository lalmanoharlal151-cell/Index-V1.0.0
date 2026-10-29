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
    }return {
    "status": "Success",
    "total_amount": total_amount,
    "bill_details": bill_details
}from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import qrcode
import io
import base64

app = FastAPI(title="All In One Pro - Banking API")

class PaymentRequest(BaseModel):
    upi_id: str
    name: str
    amount: float
    note: str = "Payment for Bill"

@app.post("/api/banking/generate-upi-qr")
def generate_upi_qr(data: PaymentRequest):
    """
    ग्राहकों के लिए UPI QR कोड जनरेट करता है (GPay, PhonePe, Paytm सपोर्टेड)
    """
    try:
        # UPI पेमेंट लिंक बनाना
        upi_link = f"upi://pay?pa={data.upi_id}&pn={data.name}&am={data.amount}&cu=INR&tn={data.note}"
        
        # QR कोड इमेज तैयार करना
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(upi_link)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        # Base64 इमेज स्ट्रिंग में बदलना ताकि फ्रंटएंड आसानी से दिखा सके
        buffer = io.BytesIO()
        img.save(buffer, format="PNG")
        img_str = base64.b64encode(buffer.getvalue()).decode("utf-8")
        
        return {
            "status": "success",
            "upi_link": upi_link,
            "qr_image_base64": f"data:image/png;base64,{img_str}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/banking/check-status/{transaction_id}")
def check_transaction_status(transaction_id: str):
    """
    भुगतान की स्थिति जांचने के लिए API एंडपॉइंट
    """
    # यहाँ आप Razorpay / Cashfree / PhonePe API के साथ स्टेटस वेरीफाई कर सकती हैं
    return {
        "transaction_id": transaction_id,
        "status": "SUCCESS",
        "message": "भुगतान सफलतापूर्वक प्राप्त हुआ!"
    }
from flask import Flask, request, jsonify

# यदि app = Flask(__name__) पहले से है, तो केवल यह रूट नीचे जोड़ें:

@app.route('/api/society-billing', methods=['POST'])
def society_billing():
    data = request.json
    society_name = data.get('society_name')
    operator_name = data.get('operator_name')
    units = float(data.get('units', 0))
    rate = float(data.get('rate', 0))
    status = data.get('status', 'Pending')
    
    # कुल बिल की गणना
    total_amount = units * rate
    
    # प्रतिक्रिया (Response)
    return jsonify({
        "status": "success",
        "message": f"{society_name} के लिए बिल सफलतापूर्वक जनरेट हो गया है।",
        "details": {
            "society": society_name,
            "operator": operator_name,
            "units_supplied": units,
            "rate_per_unit": rate,
            "total_amount": total_amount,
            "payment_status": status
        }
    })# Exported from Render on 2026-10-29T13:34:25Z
version: "1"
services:
- type: web
  name: all-in-one pro
  runtime: python
  repo: https://github.com/lalmanoharlal151-cell/all-in-one
  plan: free
  region: oregon
  buildCommand: pip install -r requirements.txt
  startCommand: main. Py
  autoDeployTrigger: commit
# Exported from Render on 2026-10-29T13:34:25Z
version: "1"
services:
- type: web
  name: all-in-one pro
  runtime: python
  repo: https://github.com/lalmanoharlal151-cell/all-in-one
  plan: free
  region: oregon
  buildCommand: pip install -r requirements.txt
  startCommand: main. Py
  autoDeployTrigger: commit




