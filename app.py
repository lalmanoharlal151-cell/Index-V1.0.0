import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import google.generativeai as genai

app = Flask(__name__)
CORS(app)  # फ्रंटएंड और बैकएंड को जोड़ने के लिए

# Google AI Studio की API Key यहाँ सेट करें
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "YOUR_GEMINI_API_KEY_HERE")
genai.configure(api_key=GEMINI_API_KEY)

# Gemini मॉडल सेट करें
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/", methods=["GET"])
def home():
    return "Nexa AI A2A Backend is running successfully!"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")
        
        if not user_message:
            return jsonify({"error": "Message is required"}), 400

        # Gemini से रिस्पॉन्स जनरेट करना
        response = model.generate_content(user_message)
        ai_reply = response.text

        return jsonify({"reply": ai_reply})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

