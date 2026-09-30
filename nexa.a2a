import datetime
import json
import os
import requests

class NexaA2AReporter:
    def __init__(self, agent_id="NexaCoreAgent", zapier_webhook_url=None):
        self.agent_id = agent_id
        self.zapier_webhook_url = zapier_webhook_url
        self.logs_file = "nexaa2a_reporting_logs.json"
        self._initialize_log_file()

    def _initialize_log_file(self):
        """स्थानीय लॉग फ़ाइल मौजूद न होने पर नया स्ट्रक्चर बनाती है।"""
        if not os.path.exists(self.logs_file):
            with open(self.logs_file, "w", encoding="utf-8") as f:
                json.dump([], f, ensure_ascii=False, indent=2)

    def log_event(self, action_type, status, details):
        """नया इवेंट लॉग करता है और उसे लोकल फ़ाइल में सेव करता है।"""
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = {
            "timestamp": timestamp,
            "agent_id": self.agent_id,
            "action": action_type,
            "status": status,
            "details": details
        }

        # 1. स्थानीय JSON फ़ाइल में लॉग सेव करें
        with open(self.logs_file, "r+", encoding="utf-8") as f:
            logs = json.load(f)
            logs.append(log_entry)
            f.seek(0)
            json.dump(logs, f, ensure_ascii=False, indent=2)

        print(f"[{timestamp}] [{status.upper()}] {action_type}: {details}")

        # 2. अगर Zapier Webhook सेट है तो रिपोर्ट भेजें
        if self.zapier_webhook_url:
            self.send_to_zapier(log_entry)

        return log_entry

    def send_to_zapier(self, data):
        """Zapier/Webhook को रिपोर्टिंग डेटा भेजता है।"""
        try:
            response = requests.post(self.zapier_webhook_url, json=data, timeout=5)
            if response.status_code == 200:
                print(">> रिपोर्ट Zapier को सफलतापूर्वक भेजी गई।")
            else:
                print(f">> Webhook एरर Code: {response.status_code}")
        except Exception as e:
            print(f">> Webhook भेजने में समस्या: {e}")

# ==================== इस्तेमाल करने का तरीका ====================
if __name__ == "__main__":
    # Zapier URL (यदि उपयोग कर रहे हों, वरना None रहने दें)
    ZAPIER_WEBHOOK = None  # उदा: "https://hooks.zapier.com/hooks/catch/12345/abcde/"

    reporter = NexaA2AReporter(agent_id="Nexa-Master-01", zapier_webhook_url=ZAPIER_WEBHOOK)

    # 1. शुरुआत का स्टेटस लॉग करें
    reporter.log_event("SYSTEM_START", "Success", "Nexa A2A रिपोर्टिंग सिस्टम शुरू हो गया है।")

    # 2. किसी एजेंट-टू-एजेंट प्रोसेस का लॉग
    reporter.log_event("A2A_COMMUNICATION", "Pending", "Agent-B को डेटा ट्रांसफर रिक्वेस्ट भेजी गई।")
    
    # 3. टास्क पूरा होने का लॉग
    reporter.log_event("A2A_COMMUNICATION", "Success", "Agent-B से रिस्पॉन्स प्राप्त हुआ।")

/* Base Layout & Theme */
:root {
  --bg-primary: #0f172a;
  --bg-secondary: #1e293b;
  --bg-card: #334155;
  --text-primary: #f8fafc;
  --text-secondary: #94a3b8;
  --accent-color: #38bdf8;
  --accent-hover: #0284c7;
  --border-color: #475569;
  --success-color: #22c55e;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
}

body {
  background-color: var(--bg-primary);
  color: var(--text-primary);
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 16px;
}

/* App Container */
.app-container {
  width: 100%;
  max-width: 480px;
  background-color: var(--bg-secondary);
  border-radius: 16px;
  border: 1px solid var(--border-color);
  padding: 24px;
  box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.5);
}

/* Header */
.app-header {
  text-align: center;
  margin-bottom: 24px;
}

.app-header h1 {
  font-size: 1.5rem;
  color: var(--accent-color);
  margin-bottom: 6px;
}

.subtitle {
  font-size: 0.875rem;
  color: var(--text-secondary);
}

/* Status Panel */
.status-card {
  background-color: var(--bg-card);
  border-radius: 12px;
  padding: 16px;
  margin-bottom: 20px;
}

.status-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 0;
  font-size: 0.9rem;
}

.status-item:not(:last-child) {
  border-bottom: 1px solid var(--border-color);
}

.status-badge {
  padding: 4px 10px;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  background-color: #eab308;
  color: #000;
}

.status-badge.connected {
  background-color: var(--success-color);
  color: #fff;
}

/* Action Area */
.action-area {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.input-box {
  width: 100%;
  padding: 12px 16px;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background-color: var(--bg-primary);
  color: var(--text-primary);
  font-size: 0.95rem;
  outline: none;
}

.input-box:focus {
  border-color: var(--accent-color);
}

.btn-primary {
  width: 100%;
  padding: 12px;
  border-radius: 8px;
  border: none;
  background-color: var(--accent-color);
  color: #0f172a;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.btn-primary:hover {
  background-color: var(--accent-hover);
  color: #fff;
}

/* Console Logs */
.console-card {
  margin-top: 20px;
  background-color: var(--bg-primary);
  border-radius: 8px;
  padding: 12px;
  max-height: 150px;
  overflow-y: auto;
  font-family: monospace;
  font-size: 0.8rem;
  color: var(--text-secondary);
}
