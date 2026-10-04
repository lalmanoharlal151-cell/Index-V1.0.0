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
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# अपनी OpenAI API Key यहाँ दर्ज करें
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

@app.route('/api/chat', methods=['POST'])
def chat_api():
    try:
        data = request.json
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({"success": False, "error": "मैसेज खाली नहीं हो सकता।"}), 400

        # चैटजीपीटी API को कॉल करना
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": "You are Nexa AI, an advanced Agent-to-Agent (A2A) protocol assistant."
                },
                {
                    "role": "user", 
                    "content": user_message
                }
            ],
            temperature=0.7
        )
        
        reply = response.choices[0].message.content
        return jsonify({"success": True, "reply": reply})
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    # सर्वर को लोकल होस्ट पर शुरू करें
    app.run(host='0.0.0.0', port=5000, debug=True)

import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# OpenAI क्लाइंट सेट करें (अपनी API की यहाँ डाल सकते हैं या पर्यावरण वेरिएबल सेट कर सकते हैं)
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")

@app.route('/')
def home():
    return "Nexa AI Server is Running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_data = request.json
    prompt_text = user_data.get("prompt", "")

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt_text}]
    )

    ai_reply = response.choices[0].message.content
    return jsonify({"response": ai_reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
