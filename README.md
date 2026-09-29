

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexa A2A - Super AI Connectivity Map</title>
</head>
<body>

    <meta charset="UTF-8">
    meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nexa A2A - Connecting Super AI | India's #1 AI Platform</title>
    <!-- Google Fonts & Font Awesome Icons -->
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=Rajdhani:wght@400;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {
            --bg-color: #080B10;
            --card-bg: rgba(18, 25, 38, 0.7);
            --neon-blue: #00f3ff;
            --neon-purple: #9d00ff;
            --text-color: #e2e8f0;
            --text-muted: #94a3b8;
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Rajdhani', sans-serif;
        }

        body {
            background-color: var(--bg-color);
            color: var(--text-color);
            overflow-x: hidden;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(0, 243, 255, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 90% 80%, rgba(157, 0, 255, 0.08) 0%, transparent 40%);
        }

        /* Header / Navbar */
        header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 8%;
            border-bottom: 1px solid rgba(0, 243, 255, 0.2);
            backdrop-filter: blur(10px);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .logo {
            font-family: 'Orbitron', sans-serif;
            font-size: 24px;
            font-weight: 900;
            color: #fff;
            letter-spacing: 2px;
        }

        .logo span {
            color: var(--neon-blue);
            text-shadow: 0 0 10px var(--neon-blue);
        }

        .badge-top {
            background: linear-gradient(45deg, var(--neon-blue), var(--neon-purple));
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 700;
            color: #fff;
            text-transform: uppercase;
        }

        /* Hero Section */
        .hero {
            text-align: center;
            padding: 60px 20px;
            max-width: 900px;
            margin: 0 auto;
        }

        .hero h1 {
            font-family: 'Orbitron', sans-serif;
            font-size: 2.8rem;
            margin-bottom: 15px;
            background: linear-gradient(180deg, #fff, var(--neon-blue));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-transform: uppercase;
        }

        .hero p {
            font-size: 1.2rem;
            color: var(--text-muted);
            margin-bottom: 30px;
        }

        /* Network Visual Poster Card */
        .network-poster {
            background: var(--card-bg);
            border: 1px solid rgba(0, 243, 255, 0.3);
            border-radius: 20px;
            padding: 40px 20px;
            margin: 20px auto;
            max-width: 1000px;
            box-shadow: 0 0 30px rgba(0, 243, 255, 0.1);
            position: relative;
            backdrop-filter: blur(10px);
        }

        .poster-title {
            font-family: 'Orbitron', sans-serif;
            color: var(--neon-blue);
            margin-bottom: 30px;
            font-size: 1.5rem;
            letter-spacing: 1px;
        }

        /* Diagram Layout */
        .diagram-container {
            display: flex;
            justify-content: space-around;
            align-items: center;
            flex-wrap: wrap;
            gap: 20px;
            position: relative;
            padding: 20px 0;
        }

        .node {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 20px;
            border-radius: 15px;
            width: 200px;
            text-align: center;
            transition: all 0.3s ease;
        }

        .node:hover {
            border-color: var(--neon-blue);
            transform: translateY(-5px);
            box-shadow: 0 0 15px rgba(0, 243, 255, 0.3);
        }

        .node i {
            font-size: 2.5rem;
            color: var(--neon-blue);
            margin-bottom: 10px;
        }

        .node.super-ai {
            border-color: var(--neon-purple);
            box-shadow: 0 0 20px rgba(157, 0, 255, 0.4);
            background: rgba(157, 0, 255, 0.1);
        }

        .node.super-ai i {
            color: var(--neon-purple);
        }

        .connector-line {
            flex: 1;
            height: 2px;
            background: linear-gradient(90deg, var(--neon-blue), var(--neon-purple));
            min-width: 50px;
            position: relative;
        }

        .connector-line::after {
            content: '';
            position: absolute;
            width: 10px;
            height: 10px;
            background: #fff;
            border-radius: 50%;
            top: -4px;
            animation: pulse 2s infinite linear;
        }

        @keyframes pulse {
            0% { left: 0%; opacity: 0; }
            50% { opacity: 1; }
            100% { left: 100%; opacity: 0; }
        }

        /* Features Section */
        .features {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            max-width: 1000px;
            margin: 40px auto;
            padding: 0 20px;
        }

        .feature-card {
            background: var(--card-bg);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 25px;
            border-radius: 15px;
            text-align: left;
        }

        .feature-card h3 {
            color: var(--neon-blue);
            margin-bottom: 10px;
            font-size: 1.3rem;
        }

        .feature-card p {
            color: var(--text-muted);
            font-size: 0.95rem;
            line-height: 1.5;
        }

        /* Live Status Footer */
        footer {
            text-align: center;
            padding: 30px;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            color: var(--text-muted);
            font-size: 0.9rem;
        }

        .status-dot {
            height: 10px;
            width: 10px;
            background-color: #00ff88;
            border-radius: 50%;
            display: inline-block;
            margin-right: 5px;
            box-shadow: 0 0 8px #00ff88;
        }

        @media (max-width: 768px) {
            .hero h1 { font-size: 2rem; }
            .diagram-container { flex-direction: column; }
            .connector-line { width: 2px; height: 40px; min-width: auto; }
        }
    </style>
</head>
<body>

    <!-- Top Navigation -->
    <header>
        <div class="logo">NEXA <span>A2A</span></div>
        <div class="badge-top"><span class="status-dot"></span> Next-Gen AI Active</div>
    </header>

    <!-- Main Hero Section -->
    <section class="hero">
        <h1>सुपर AI को जोड़ने वाला भारत का पहला A2A नेटवर्क</h1>
        <p>Nexa A2A (Agent-to-Agent Protocol) विभिन्न एआई एजेंट्स और भविष्य के Super AI को एक शक्तिशाली नेटवर्क में जोड़ता है।</p>
    </section>

    <!-- Visual Poster / Diagram Section -->
    <div class="network-poster">
        <div class="poster-title"><i class="fa-solid fa-network-wired"></i> NEXA A2A SUPER AI CONNECTIVITY MAP</div>
        
        <div class="diagram-container">
            <div class="node">
                <i class="fa-solid fa-robot"></i>
                <h3>Nexa Agent A</h3>
                <p>Task Processing</p>
            </div>

            <div class="connector-line"></div>

            <div class="node">
                <i class="fa-solid fa-microchip"></i>
                <h3>A2A Protocol</h3>
                <p>Smart Router</p>
            </div>

            <div class="connector-line"></div>

            <div class="node super-ai">
                <i class="fa-solid fa-brain"></i>
                <h3>SUPER AI</h3>
                <p>Central Intelligence</p>
            </div>
        </div>
    </div>

    <!-- Features Overview -->
    <section class="features">
        <div class="feature-card">
            <h3><i class="fa-solid fa-bolt"></i> Ultra Fast A2A Bridge</h3>
            <p>एजेंट-टू-एजेंट प्रोटोकॉल के जरिए बिना किसी रुकावट के डेटा ट्रांसफर और रियल-टाइम कम्युनिकेशन।</p>
        </div>
        <div class="feature-card">
            <h3><i class="fa-solid fa-shield-halved"></i> Secure Integration</h3>
            <p>सुपर एआई और लोकली होस्टेड एआई मॉडल्स के बीच सुरक्षित और एन्क्रिप्टेड कनेक्शन।</p>
        </div>
        <div class="feature-card">
            <h3><i class="fa-solid fa-code-branch"></i> Scalable Architecture</h3>
            <p>भविष्य के एडवांस एआई मॉडल्स और बैकएंड API से सीधे कनेक्ट करने के लिए तैयार डिज़ाइन।</p>
        </div>
    </section>

    <!-- Footer -->
    <footer>
        <p>&copy; 2026 Nexa A2A Project. Made in India for the Future of AI.</p>
    </footer>

</body>
</html>
