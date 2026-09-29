<!DOCTYPE html>
<html lang="hi">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Nexa A2A Interface</title>
  
  <!-- Font Awesome Icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    body {
      background-color: #0f172a;
      color: #f8fafc;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 20px;
    }

    .container {
      width: 100%;
      max-width: 480px;
    }

    .card {
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 16px;
      padding: 30px;
      box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
    }

    .card-header h1 {
      font-size: 1.8rem;
      color: #38bdf8;
      margin-bottom: 8px;
    }

    .subtitle {
      color: #94a3b8;
      font-family: monospace;
      font-size: 0.95rem;
      margin-bottom: 24px;
    }

    .cta-btn {
      width: 100%;
      padding: 14px 24px;
      font-size: 1rem;
      font-weight: 600;
      color: #ffffff;
      background: linear-gradient(135deg, #0284c7, #2563eb);
      border: none;
      border-radius: 10px;
      cursor: pointer;
      transition: all 0.3s ease;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 10px;
    }

    .cta-btn:hover {
      transform: translateY(-2px);
      box-shadow: 0 4px 15px rgba(37, 99, 235, 0.4);
    }
  </style>
</head>
<body>

  <div class="container">
    <div class="card">
      <div class="card-header">
        <h1>Index-V1.0.0</h1>
        <p class="subtitle">// Nexa A2A - Agent Connection Handler</p>
      </div>

      <div class="card-body">
        <button class="cta-btn" onclick="connectAI()">
          <i class="fa-solid fa-link"></i> Connect AI Agent
        </button>
      </div>
    </div>
  </div>

  <script>
    // Nexa A2A - Agent Connection Handler[span_0](start_span)[span_0](end_span)
    function connectAI() {
      const btn = document.querySelector('.cta-btn');

      // Button state update[span_1](start_span)[span_1](end_span)
      btn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Connecting...';[span_2](start_span)[span_2](end_span)
      btn.style.opacity = '0.8';[span_3](start_span)[span_3](end_span)
      btn.disabled = true;

      setTimeout(() => {
        // Alert Notification[span_4](start_span)[span_4](end_span)
        alert('✅ Nexa A2A Agent Connected Successfully!');[span_5](start_span)[span_5](end_span)

        // Button state update[span_6](start_span)[span_6](end_span)
        btn.innerHTML = '<i class="fa-solid fa-check"></i> Connected Successfully';[span_7](start_span)[span_7](end_span)
        btn.style.background = 'linear-gradient(45deg, #10b981, #059669)';[span_8](start_span)[span_8](end_span)
        btn.style.opacity = '1';
        btn.disabled = false;
      }, 2000);[span_9](start_span)[span_9](end_span)

      // Console Log Status[span_10](start_span)[span_10](end_span)
      console.log("Nexa A2A Protocol Initialized...");[span_11](start_span)[span_11](end_span)
    }
  </script>
</body>
</html>
# app.py (Python Flask Server Logic)
from flask import Flask, request, jsonify

app = Flask(__name__)

# A2A Message Protocol Schema
class NexaA2AProtocol:
    def __init__(self, sender_id, receiver_id, payload_type, data):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.payload_type = payload_type # 'command', 'data', 'status'
        self.data = data

    def to_dict(self):
        return {
            "protocol": "Nexa-A2A-v1.0",
            "sender": self.sender_id,
            "receiver": self.receiver_id,
            "payload_type": self.payload_type,
            "payload": self.data
        }

@app.route('/api/a2a-connect', methods=['POST'])
def connect_agent():
    req_data = request.get_json()
    agent_type = req_data.get('agent_type')
    api_key = req_data.get('api_key')

    if api_key:
        # Handshake successful
        handshake = NexaA2AProtocol(
            sender_id="Nexa-Core-SuperAI",
            receiver_id=agent_type,
            payload_type="status",
            data={"status": "CONNECTED", "handshake": True}
        )
        return jsonify({"status": "success", "protocol": handshake.to_dict()}), 200
    
    return jsonify({"status": "error", "message": "Invalid credentials"}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
<!-- AI Agent Connection Modal (पुराने UI के ठीक नीचे चिपकाएँ) -->
<div id="agentModal" class="modal-overlay" style="display: none;">
  <div class="modal-content">
    <h3>Connect AI Agent</h3>
    <label for="agentType">Select Agent Type:</label>
    <select id="agentType">
      <option value="gemini">Gemini AI Agent</option>
      <option value="custom">Custom A2A Protocol Agent</option>
    </select>

    <label for="apiKey">API Key / Agent Endpoint:</label>
    <input type="text" id="apiKey" placeholder="Enter API Key or Endpoint URL">

    <div class="modal-actions">
      <button onclick="connectAgent()" class="btn-submit">Connect</button>
      <button onclick="closeAgentModal()" class="btn-cancel">Cancel</button>
    </div>
  </div>
</div>
# ==========================================
# Nexa A2A - Flask Server & Protocol Logic
# ==========================================

from flask import Flask, request, jsonify

app = Flask(__name__)

class NexaA2AProtocol:
    def __init__(self, sender_id, receiver_id, payload_type, data):
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.payload_type = payload_type  # 'command', 'data', 'status'
        self.data = data

@app.route('/api/a2a-connect', methods=['POST'])
def connect_agent():
    req_data = request.get_json()
    agent_type = req_data.get('agent_type')
    api_key = req_data.get('api_key')
    
    return jsonify({
        "status": "success", 
        "message": "Agent connected successfully",
        "agent_type": agent_type
    })

if __name__ == '__main__':
    app.run(port=5000, debug=True)
