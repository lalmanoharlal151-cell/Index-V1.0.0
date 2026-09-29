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
