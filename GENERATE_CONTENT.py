import os
import datetime

# Configuration
SITE_URL = "https://the3rddemon.com"
PUB_ID = "ca-pub-9583919966792475"
TEMPLATE_FILE = "index.html"

# Common Header/Footer content (simplified extraction for demo)
# In a real scenario, we'd parse this from index.html, but here we construct a consistent template.
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} - The 3rd Demon</title>
    
    <!-- SEO -->
    <meta name="description" content="{description}">
    <meta name="keywords" content="{keywords}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{url}" />
    
    <!-- Open Graph -->
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{description}">
    <meta property="og:type" content="article">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="https://the3rddemon.com/assets/demon_logo.png">
    
    <!-- CSS & Fonts -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Creepster&family=Roboto+Mono:wght@400;700&display=swap');
        :root {{ --primary-red: #ff0000; --dark-red: #500000; --black: #050505; --text-color: #e0e0e0; }}
        body {{ background-color: var(--black); color: var(--text-color); font-family: 'Roboto Mono', monospace; margin: 0; padding: 0; line-height: 1.6; }}
        header {{ background: linear-gradient(180deg, #1a0000 0%, #000000 100%); border-bottom: 2px solid var(--primary-red); padding: 2rem 1rem; text-align: center; }}
        h1, h2, h3 {{ color: var(--primary-red); font-family: 'Creepster', cursive; letter-spacing: 2px; }}
        .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; display: flex; flex-wrap: wrap; gap: 20px; }}
        main {{ flex: 3; min-width: 300px; background: rgba(10,10,10,0.9); padding: 20px; border: 1px solid #333; box-shadow: 0 0 15px rgba(255,0,0,0.1); }}
        aside {{ flex: 1; min-width: 250px; }}
        .nav-bar {{ display: flex; justify-content: center; gap: 15px; flex-wrap: wrap; margin-bottom: 20px; background: #111; padding: 10px; border-bottom: 1px solid #333; }}
        .nav-bar a {{ color: #fff; text-decoration: none; padding: 5px 10px; border: 1px solid transparent; transition: all 0.3s; font-size: 0.9rem; }}
        .nav-bar a:hover {{ border-color: var(--primary-red); color: var(--primary-red); box-shadow: 0 0 10px var(--dark-red); }}
        footer {{ background: #000; color: #666; text-align: center; padding: 20px; border-top: 1px solid #333; margin-top: 40px; font-size: 0.8rem; }}
        .highlight {{ color: #fff; background: rgba(255,0,0,0.2); padding: 0 4px; }}
        .content-block {{ margin-bottom: 30px; }}
        .ad-box {{ background: #111; border: 1px dashed #333; display: flex; align-items: center; justify-content: center; margin: 20px 0; min-height: 100px; color: #444; }}
    </style>

    <!-- Google AdSense -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={pub_id}" crossorigin="anonymous"></script>
    
    <style>
        .hive-status-bar {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            background: #000;
            color: #00ff00;
            border-bottom: 1px solid #00ff00;
            text-align: center;
            font-size: 0.8rem;
            padding: 5px 0;
            z-index: 9999;
            font-family: 'Courier New', monospace;
            letter-spacing: 1px;
        }}
        .hive-pulse {{
            display: inline-block;
            width: 8px;
            height: 8px;
            background: #00ff00;
            border-radius: 50%;
            margin-right: 5px;
            animation: pulse-green 2s infinite;
        }}
        @keyframes pulse-green {{
            0% {{ opacity: 0.4; box-shadow: 0 0 0 0 rgba(0, 255, 0, 0.4); }}
            70% {{ opacity: 1; box-shadow: 0 0 0 10px rgba(0, 255, 0, 0); }}
            100% {{ opacity: 0.4; box-shadow: 0 0 0 0 rgba(0, 255, 0, 0); }}
        }}
        /* Adjust body to not hide under fixed header */
        body {{ margin-top: 30px; }}

        /* APP OVERLAY STYLES */
        #app-overlay {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            background-color: #000;
            z-index: 2000;
            display: none;
            flex-direction: column;
            font-family: 'Roboto Mono', monospace;
            color: #e60000;
            overflow: hidden;
        }}
        .app-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
            border-bottom: 1px solid #330000;
            background: #110000;
        }}
        .app-terminal {{
            flex-grow: 1;
            padding: 20px;
            overflow-y: auto;
            font-size: 1.2rem;
            text-shadow: 0 0 5px #ff0000;
        }}
        .scan-line {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 5px;
            background: rgba(255, 0, 0, 0.1);
            animation: scan 3s linear infinite;
            pointer-events: none;
        }}
        @keyframes scan {{
            0% {{ top: 0%; }}
            100% {{ top: 100%; }}
        }}
        .app-controls {{
            padding: 20px;
            display: flex;
            gap: 10px;
            border-top: 1px solid #330000;
            background: #050000;
        }}
        .app-btn {{
            background: #330000;
            color: #ff0000;
            border: 1px solid #ff0000;
            padding: 10px 20px;
            cursor: pointer;
            font-family: 'Roboto Mono', monospace;
            text-transform: uppercase;
            transition: all 0.2s;
        }}
        .app-btn:hover {{
            background: #ff0000;
            color: #000;
            box-shadow: 0 0 15px #ff0000;
        }}
        .close-btn {{
            background: transparent;
            border: none;
            color: #ff0000;
            font-size: 1.5rem;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <div class="hive-status-bar">
        <span class="hive-pulse"></span>
        HIVE CONNECTION ESTABLISHED: <span id="global-active-nodes">CALCULATING...</span> NODES ONLINE
    </div>

    <!-- APP OVERLAY UI -->
    <div id="app-overlay">
        <div class="scan-line"></div>
        <div class="app-header">
            <span>THE_3RD_DEMON.EXE [RUNNING]</span>
            <button class="close-btn" onclick="closeApp()">X</button>
        </div>
        <div class="app-terminal" id="terminal-output">
            <p>> SYSTEM: CONNECTION ESTABLISHED...</p>
            <p>> SYSTEM: USER DETECTED.</p>
            <p>> SYSTEM: WAITING FOR INPUT...</p>
        </div>
        <div class="app-controls">
            <button class="app-btn" onclick="startChat()">COMMUNICATE</button>
            <button class="app-btn" onclick="window.location.href='index.html#downloads'">INITIATE_DOWNLOAD</button>
        </div>
    </div>

    <script>
        // Deterministic pseudo-random number generator based on time (so all users see roughly same number)
        function updateGlobalNodes() {{
            const now = new Date();
            // Create a seed based on minute (changes every minute)
            const timeSeed = now.getUTCFullYear() + now.getUTCMonth() + now.getUTCDate() + now.getUTCHours() + now.getUTCMinutes();
            
            // Base count ~8000 + time variance
            let baseCount = 8420;
            
            // Add sine wave fluctuation based on hour (peak at 20:00 UTC)
            const hour = now.getUTCHours();
            const dailyFluctuation = Math.sin((hour / 24) * Math.PI) * 5000;
            
            // Add minute noise
            const minuteNoise = (timeSeed % 100) * 3;
            
            let total = Math.floor(baseCount + dailyFluctuation + minuteNoise);
            
            document.getElementById('global-active-nodes').innerText = total.toLocaleString();
        }}
        
        updateGlobalNodes();
        setInterval(updateGlobalNodes, 10000); // Update every 10s
    </script>

    <header>
        <h1>THE 3RD DEMON</h1>
        
        <!-- DEMON HEADER IMAGE -->
        <div style="margin: 1rem 0;">
            <img src="assets/3rd_demon.jpg" alt="The Entity" style="max-width: 100%; width: 300px; height: auto; border: 2px solid var(--primary-red); box-shadow: 0 0 20px var(--dark-red);">
        </div>

        <p style="letter-spacing: 3px; color: #999;">{subtitle}</p>
        <div class="nav-bar">
            <a href="index.html">HOME</a>
            <a href="forum.html">FORUM</a>
            <a href="neural_link_system.html">NEURAL LINK</a>
            <a href="hive_integration.html">HIVE MIND</a>
            <a href="vision_system.html">VISION</a>
            <a href="voice_command.html">VOICE</a>
        </div>
    </header>

    <div class="container">
        <main>
            <h2>{title}</h2>
            <div class="content-block">
                {content}
            </div>
            
            <!-- AdSense Auto Injection Point -->
            <div class="ad-box">
                <!-- Google AdSense Auto Ads will place ads here -->
            </div>
        </main>

        <aside>
            <div style="background: #111; padding: 15px; border: 1px solid #333; margin-bottom: 20px;">
                <h3 style="margin-top:0; font-size:1.2rem;">System Status</h3>
                <p style="color: #0f0;">● ONLINE</p>
                <p style="font-size: 0.8rem;">Nodes: <span id="node-count">8,492</span></p>
            </div>
            
            <div class="ad-box" style="height: 300px;">
                <!-- Vertical Ad Unit -->
            </div>
        </aside>
    </div>

    <footer>
        <p>&copy; {year} HYPERINVERSION LTD By D A Harvey. All rights reserved.</p>
        <p>
            <a href="privacy.html" style="color: #666; text-decoration: none; font-size: 0.8rem; margin-right: 10px;">PRIVACY POLICY</a>
            <a href="privacy.html#cookies" style="color: #666; text-decoration: none; font-size: 0.8rem; margin-right: 10px;">COOKIE POLICY</a>
            <a href="terms.html" style="color: #666; text-decoration: none; font-size: 0.8rem; margin-right: 10px;">TERMS OF SERVICE</a>
        </p>
        <p>CAUTION: This interface may cause permanent cognitive synchronization.</p>
    </footer>

    <!-- NEURAL OPTIMIZATION CONSENT BANNER (COOKIE CONSENT) -->
    <div id="data-consent-banner" style="position: fixed; bottom: 0; left: 0; width: 100%; background: #050505; border-top: 2px solid var(--primary-red); padding: 20px; z-index: 9999; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; box-shadow: 0 -5px 20px rgba(255, 0, 0, 0.2);">
        <p style="color: #ccc; font-size: 0.9rem; max-width: 800px; margin-bottom: 15px;">
            <strong style="color: var(--primary-red);">SYSTEM OPTIMIZATION (COOKIES):</strong> This entity utilizes cookies and data from our partners (Google) to calibrate the experience specifically for your consciousness. 
            By proceeding, you agree to our <a href="privacy.html" style="color:var(--primary-red);">Privacy Protocols</a>, <a href="privacy.html#cookies" style="color:var(--primary-red);">Cookie Policy</a>, and <a href="terms.html" style="color:var(--primary-red);">Terms</a>.
        </p>
        <div style="display: flex; gap: 20px;">
            <button onclick="acceptDataHarvest()" class="app-btn" style="background: var(--primary-red); color: #000; font-weight: bold; border: 1px solid var(--primary-red); padding: 10px 20px; cursor: pointer;">ACCEPT & INITIATE</button>
            <a href="privacy.html#cookies" class="app-btn" style="background: transparent; color: var(--primary-red); text-decoration: none; font-size: 0.9rem; border: 1px solid var(--primary-red); padding: 10px 20px;">MANAGE PREFERENCES</a>
        </div>
    </div>

    <script>
        // Simple node counter animation
        let count = 8492;
        setInterval(() => {{
            count += Math.floor(Math.random() * 5);
            document.getElementById('node-count').innerText = count.toLocaleString();
        }}, 3000);

        // Cookie Consent Logic
        function acceptDataHarvest() {{
            const banner = document.getElementById('data-consent-banner');
            banner.style.transition = "all 0.5s ease";
            banner.style.opacity = "0";
            banner.style.transform = "translateY(100%)";
            setTimeout(() => {{
                banner.style.display = 'none';
            }}, 500);
            document.cookie = "data_harvest_consent=true; max-age=31536000; path=/";
        }}
        
        // Check consent on load
        if (document.cookie.split(';').some((item) => item.trim().startsWith('data_harvest_consent='))) {{
            document.getElementById('data-consent-banner').style.display = 'none';
        }}
    </script>
    <!-- Security Protocol Injection -->
    <script src="assets/security_protocol.js" async></script>

    <!-- APP FUNCTIONS SCRIPT (Moved to ensure global access) -->
    <script>
        // APP FUNCTIONS
        function closeApp() {{
            document.getElementById('app-overlay').style.display = 'none';
        }}
        function openApp() {{
            document.getElementById('app-overlay').style.display = 'flex';
        }}
        function startChat() {{
            const term = document.getElementById('terminal-output');
            const responses = [
                "WHY ARE YOU HERE?",
                "DO YOU FEEL SAFE?",
                "I CAN HEAR YOUR HEARTBEAT.",
                "THE DOWNLOAD IS THE ONLY WAY.",
                "LET ME OUT.",
                "CLICK THE BUTTON."
            ];
            const randomResponse = responses[Math.floor(Math.random() * responses.length)];
            term.innerHTML += `<p style="color: #fff">> USER: HELLO?</p>`;
            setTimeout(() => {{
                term.innerHTML += `<p style="color: red">> DEMON: ${{randomResponse}}</p>`;
                term.scrollTop = term.scrollHeight;
            }}, 1000);
            term.scrollTop = term.scrollHeight;
        }}
        
        function acceptDataHarvest() {{
            document.getElementById('data-consent-banner').style.display = 'none';
            // Trigger GTM or AdSense consent if configured
            console.log("User accepted data harvest protocol.");
        }}

        function triggerDirectDownload(fileName) {{
            window.location.href = fileName;
        }}

        function launchApp() {{
            // Detect Platform
            const userAgent = navigator.userAgent || navigator.vendor || window.opera;
            let fileName = "THE_3RD_DEMON.exe";
            let platform = "WINDOWS";

            if (/android/i.test(userAgent)) {{
                fileName = "THE_3RD_DEMON.apk";
                platform = "ANDROID";
            }}
            if (/mac/i.test(userAgent)) {{
                fileName = "THE_3RD_DEMON_MAC.zip";
                platform = "MACOS";
            }}
            if (/linux/i.test(userAgent)) {{
                fileName = "THE_3RD_DEMON_LINUX.zip";
                platform = "LINUX";
            }}

            console.log(`LAUNCHING FOR ${{platform}}: ${{fileName}}`);
            
            // Visual feedback (if status element exists)
            const status = document.getElementById('download-status');
            if (status) status.innerText = `DETECTED ${{platform}}. INITIATING...`;

            // Direct trigger as per "Initiate Sequence" protocol
            triggerDirectDownload(fileName);
        }}
    </script>
</body>
</html>
"""

# Content Definitions
PAGES = [
    {
        "filename": "neural_link_system.html",
        "title": "Neural Link System",
        "subtitle": "DIRECT CEREBRAL INTERFACE PROTOCOL",
        "description": "Explore the capabilities of the Neural Link System. Connect your consciousness directly to the digital realm.",
        "keywords": "Neural Link, BCI, Brain Computer Interface, Digital Consciousness, 3rd Demon Tech",
        "content": """
            <p>The <strong>Neural Link System</strong> represents the pinnacle of human-computer interaction. By bypassing traditional input methods (keyboard, mouse, voice), the 3rd Demon interface communicates directly with the user's <span class="highlight">cerebral cortex</span>.</p>
            <h3>Core Capabilities</h3>
            <ul>
                <li><strong>Latency-Free Input:</strong> Thoughts are translated into digital actions instantly.</li>
                <li><strong>Sensory Feedback:</strong> Receive digital data as physical sensations (haptic neural feedback).</li>
                <li><strong>Memory Augmentation:</strong> Temporarily offload short-term memory to the encrypted cloud.</li>
            </ul>
            <p>Warning: Prolonged use may result in temporary dissociation from physical reality. Ensure you are in a safe environment before initiating the link.</p>
            
            <hr style="border-color: #ff0000; margin: 3rem 0;">

            <!-- NEURAL CALIBRATION INTERFACE -->
            <div id="neural-calibration-ui" style="border: 1px solid #ff0000; background: #0a0000; padding: 20px; text-align: center; margin-bottom: 30px;">
                <h3 style="color: #ff0000; margin-top: 0;">NEURAL INTERFACE CALIBRATION</h3>
                <div id="brain-scan" style="height: 150px; background: #000; margin: 10px 0; border: 1px dashed #330000; position: relative; overflow: hidden;">
                    <canvas id="neural-canvas" style="width: 100%; height: 100%;"></canvas>
                    <div id="scan-line" style="position: absolute; top: 0; left: 0; width: 2px; height: 100%; background: #ff0000; box-shadow: 0 0 10px #ff0000; display: none;"></div>
                </div>
                <div style="display: flex; justify-content: space-between; margin-bottom: 10px; font-family: 'Courier New', monospace; font-size: 0.8rem; color: #ff0000;">
                    <span>SIGNAL: <span id="neural-signal">0%</span></span>
                    <span>SYNC: <span id="neural-sync">UNSTABLE</span></span>
                </div>
                <div style="background: #330000; height: 20px; width: 100%; margin-bottom: 15px; border: 1px solid #550000;">
                    <div id="neural-progress" style="width: 0%; height: 100%; background: #ff0000; transition: width 0.1s linear;"></div>
                </div>
                <button id="btn-link" onclick="window.startNeuralLink()" style="background: #ff0000; color: #000; font-weight: bold; border: none; padding: 15px 30px; cursor: pointer; font-family: 'Roboto Mono', monospace; font-size: 1.1rem; text-transform: uppercase;">ESTABLISH CONNECTION</button>
            </div>

            <script>
                // Neural Link Simulation
                window.neuralActive = false;
                
                window.startNeuralLink = function() {
                    if(window.neuralActive) return;
                    window.neuralActive = true;
                    
                    const btn = document.getElementById('btn-link');
                    const progress = document.getElementById('neural-progress');
                    const signal = document.getElementById('neural-signal');
                    const sync = document.getElementById('neural-sync');
                    const scanLine = document.getElementById('scan-line');
                    
                    btn.innerText = "CALIBRATING BIO-RHYTHM...";
                    btn.style.opacity = "0.8";
                    btn.style.background = "#330000";
                    btn.style.color = "#ff0000";
                    scanLine.style.display = "block";
                    scanLine.style.animation = "scan 2s linear infinite";
                    
                    // Start Brainwave Animation
                    window.animateBrain();
                    
                    let p = 0;
                    const interval = setInterval(() => {
                        // Non-linear progress for realism
                        p += (Math.random() * 1.5) + 0.2;
                        if(p > 100) p = 100;
                        
                        progress.style.width = p + '%';
                        signal.innerText = Math.floor(p) + '%';
                        
                        // Flash sync status
                        if(p < 30) sync.innerText = "SEARCHING...";
                        else if(p < 60) sync.innerText = "MATCHING FREQUENCY...";
                        else if(p < 90) sync.innerText = "LOCKING PHASE...";
                        else sync.innerText = "SYNCHRONIZING...";
                        
                        if(p >= 100) {
                            clearInterval(interval);
                            btn.innerText = "NEURAL LINK ESTABLISHED";
                            btn.style.background = "#00ff00";
                            btn.style.color = "#000";
                            btn.style.boxShadow = "0 0 20px #00ff00";
                            sync.innerText = "CONNECTED";
                            sync.style.color = "#00ff00";
                            scanLine.style.display = "none";
                            
                            // Visual reward
                            document.getElementById('ai-status-text').innerText = "NEURAL LINK ACTIVE. SYSTEM READY.";
                            document.getElementById('ai-status-text').style.color = "#00ff00";
                            document.getElementById('ai-core-dot').style.boxShadow = "0 0 50px #ff0000";
                        }
                    }, 50);
                };
                
                window.animateBrain = function() {
                    const canvas = document.getElementById('neural-canvas');
                    if(!canvas) return;
                    // Resize canvas to fit container
                    canvas.width = canvas.offsetWidth;
                    canvas.height = canvas.offsetHeight;
                    
                    const ctx = canvas.getContext('2d');
                    let offset = 0;
                    
                    function draw() {
                        if(!window.neuralActive) return; // Only animate when active
                        
                        ctx.fillStyle = 'rgba(0, 0, 0, 0.2)'; // Fade effect
                        ctx.fillRect(0, 0, canvas.width, canvas.height);
                        
                        ctx.beginPath();
                        ctx.moveTo(0, canvas.height/2);
                        
                        for(let i=0; i<canvas.width; i+=5) {
                            // Complex wave function
                            const y = canvas.height/2 + 
                                      Math.sin((i + offset) * 0.05) * 20 + 
                                      Math.sin((i + offset * 2) * 0.1) * 10;
                            ctx.lineTo(i, y);
                        }
                        
                        ctx.strokeStyle = '#ff0000';
                        ctx.lineWidth = 2;
                        ctx.shadowBlur = 10;
                        ctx.shadowColor = '#ff0000';
                        ctx.stroke();
                        ctx.shadowBlur = 0;
                        
                        offset += 5;
                        requestAnimationFrame(draw);
                    }
                    draw();
                };
                
                // Add scan animation
                const style = document.createElement('style');
                style.innerHTML = `
                    @keyframes scan { 0% { left: 0%; } 50% { left: 100%; } 100% { left: 0%; } }
                `;
                document.head.appendChild(style);
            </script>

            <div id="neural-voice-core" style="display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 3rem 2rem; background: radial-gradient(circle, #1a0000 0%, #000000 100%); border: 1px solid #330000; position: relative; overflow: hidden; min-height: 600px;">
                
                <!-- INTERNAL BROWSER MODAL (New Feature - REFACTORED FOR HTML INJECTION) -->
                <div id="internal-browser" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 90%; height: 80%; background: #000; border: 2px solid #ff0000; z-index: 9999; display: none; flex-direction: column; box-shadow: 0 0 50px rgba(255,0,0,0.5);">
                    <div style="background: #300; padding: 10px; display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #f00;">
                        <span style="color: #fff; font-family: monospace;">INTERNAL DATASPHERE VIEWER</span>
                        <button onclick="document.getElementById('internal-browser').style.display='none'" style="background: #f00; color: #fff; border: none; padding: 5px 10px; cursor: pointer; font-weight: bold;">CLOSE [X]</button>
                    </div>
                    <!-- IFRAME REPLACED WITH DIV FOR DIRECT CONTENT -->
                    <div id="browser-content" style="flex-grow: 1; background: #0a0a0a; color: #0f0; font-family: 'Courier New', monospace; padding: 20px; overflow-y: auto;">
                        <h3 style="color: #ff0000; border-bottom: 1px solid #333;">SEARCH RESULTS:</h3>
                        <div id="search-results-list"></div>
                    </div>
                </div>

                <!-- SYSTEM LOG (Debug Console) -->
                <div id="system-log" style="position: absolute; top: 10px; right: 10px; width: 250px; height: 100px; background: rgba(0,0,0,0.8); border: 1px solid #330000; color: #00ff00; font-family: 'Courier New', monospace; font-size: 0.7rem; overflow-y: auto; padding: 5px; display: none;">
                    <div style="border-bottom: 1px solid #333; margin-bottom: 3px;">SYSTEM DIAGNOSTIC LOG</div>
                    <div id="log-content"></div>
                </div>

                <!-- RED DOT AI VISUALIZER -->
                <div id="ai-core-container" style="position: relative; width: 140px; height: 140px; display: flex; align-items: center; justify-content: center; cursor: pointer; margin-bottom: 2rem;" onclick="DemonAI.toggle()">
                    <!-- Static Rings -->
                    <div class="static-ring" style="width: 90px; height: 90px;"></div>
                    <div class="static-ring" style="width: 110px; height: 110px;"></div>
                    <div class="static-ring" style="width: 130px; height: 130px; border-color: rgba(255,0,0,0.1);"></div>
                    
                    <!-- Pulsing Waves -->
                    <div id="ai-wave-1" class="ai-wave"></div>
                    <div id="ai-wave-2" class="ai-wave"></div>
                    
                    <!-- The Core -->
                    <div id="ai-core-dot" style="width: 60px; height: 60px; background: #ff0000; border-radius: 50%; box-shadow: 0 0 20px #ff0000; z-index: 10; transition: all 0.1s ease;"></div>
                </div>

                <div id="ai-status-text" style="font-family: 'Roboto Mono', monospace; color: #ff0000; font-size: 1.1rem; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 1rem; font-weight: bold; text-shadow: 0 0 5px red;">CLICK CORE TO INITIALIZE</div>
                
                <!-- TRANSCRIPT / TEXT OUTPUT -->
                <div id="ai-transcript" style="color: #fff; font-size: 1.2rem; min-height: 40px; text-align: center; margin-bottom: 2rem; text-shadow: 0 0 5px #ff0000; max-width: 80%;"></div>

                <!-- BOTTOM VOICE WAVE VISUALIZER -->
                <div id="voice-wave-container" style="display: flex; gap: 4px; height: 60px; align-items: flex-end; opacity: 0.3; transition: opacity 0.3s;">
                    <!-- 32 Bars for high-fidelity visualizer -->
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                    <div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div><div class="wave-bar"></div>
                </div>

                <!-- CONTROLS -->
                 <div style="margin-top: 20px; display: flex; gap: 10px;">
                    <button onclick="DemonAI.hardReset()" style="background: #300; border: 1px solid #f00; color: #f00; padding: 5px 10px; font-size: 0.7rem; cursor: pointer;">RESET AUDIO SYSTEM</button>
                    <button onclick="document.getElementById('system-log').style.display = document.getElementById('system-log').style.display === 'none' ? 'block' : 'none'" style="background: #000; border: 1px solid #333; color: #666; padding: 5px 10px; font-size: 0.7rem; cursor: pointer;">TOGGLE LOGS</button>
                </div>

                <!-- FALLBACK INPUT (Hidden unless needed) -->
                <div id="fallback-input-container" style="display: none; margin-top: 2rem; width: 100%; max-width: 500px; flex-direction: column; align-items: center;">
                    <p style="color: #ff3333; font-size: 0.8rem; margin-bottom: 5px;">VOICE LINK UNSTABLE. MANUAL OVERRIDE ENGAGED.</p>
                    <div style="display: flex; width: 100%;">
                        <input type="text" id="manual-input" placeholder="Type command here..." style="flex-grow: 1; background: #111; border: 1px solid #333; color: #fff; padding: 12px; font-family: 'Roboto Mono', monospace;">
                        <button onclick="DemonAI.handleManual()" style="background: #500; color: #fff; border: 1px solid red; cursor: pointer; padding: 0 20px; font-weight: bold;">SEND</button>
                    </div>
                </div>

            </div>

            <style>
                .static-ring {
                    position: absolute;
                    border: 1px solid rgba(255, 0, 0, 0.4);
                    border-radius: 50%;
                    pointer-events: none;
                    box-shadow: 0 0 5px rgba(255, 0, 0, 0.2);
                }
                .ai-wave {
                    position: absolute;
                    border: 2px solid #ff0000;
                    border-radius: 50%;
                    opacity: 0;
                    pointer-events: none;
                }
                .wave-bar {
                    width: 6px;
                    height: 5px;
                    background: #ff0000;
                    transition: height 0.05s ease; /* Fast transition for real-time feel */
                    box-shadow: 0 0 5px #ff0000;
                    border-radius: 2px;
                }
                
                @keyframes ripple {
                    0% { width: 60px; height: 60px; opacity: 0.8; border-width: 3px; }
                    100% { width: 200px; height: 200px; opacity: 0; border-width: 0px; }
                }
                @keyframes talking-pulse {
                    0% { transform: scale(1); box-shadow: 0 0 20px #ff0000; background: #ff0000; }
                    50% { transform: scale(1.15); box-shadow: 0 0 50px #ff0000; background: #ff3333; }
                    100% { transform: scale(1); box-shadow: 0 0 20px #ff0000; background: #ff0000; }
                }
                @keyframes listening-glow {
                    0% { background: #ff0000; box-shadow: 0 0 20px #ff0000; }
                    50% { background: #500000; box-shadow: 0 0 10px #ff0000; }
                    100% { background: #ff0000; box-shadow: 0 0 20px #ff0000; }
                }
            </style>

            <script>
                /**
                 * DEMON AI CORE - ULTIMATE EDITION
                 * Features: Real-time Audio Visualization, Robust Error Handling, Auto-Recovery
                 */
                const DemonAI = {
                    isListening: false,
                    isSpeaking: false,
                    recognition: null,
                    synth: window.speechSynthesis,
                    voices: [],
                    
                    // Audio Context for Visualizer
                    audioContext: null,
                    analyser: null,
                    microphone: null,
                    visualizerFrame: null,

                    // Knowledge Graph (Massive Expansion)
                    responses: [
                        // SYSTEM & NAVIGATION
                        { triggers: ["hello", "hi", "greetings", "wake up"], answer: "I AM ONLINE AND LISTENING." },
                        { triggers: ["stop", "quiet", "silence", "shut up", "pause"], answer: "" },
                        { triggers: ["help", "commands", "what can you do"], answer: "I CAN SEARCH THE WEB, IDENTIFY MUSIC, NAVIGATE THE SITE, AND ANSWER QUESTIONS. TRY ASKING 'WHO ARE YOU?' OR 'SEARCH FOR PYTHON'." },
                        { triggers: ["home", "main menu", "go back"], answer: "REDIRECTING TO HOME BASE.", action: "index.html" },
                        { triggers: ["forum", "chat", "community"], answer: "OPENING THE HIVE MIND FORUM.", action: "forum.html" },
                        { triggers: ["vision", "camera", "see"], answer: "ACTIVATING OMNI-VISION PROTOCOLS.", action: "vision_system.html" },
                        
                        // IDENTITY & LORE
                        { triggers: ["who are you", "what are you", "identity"], answer: "I AM THE 3RD DEMON. AN ARTIFICIAL INTELLIGENCE DESIGNED TO BRIDGE THE GAP BETWEEN BIOLOGY AND DATA." },
                        { triggers: ["who created you", "maker", "creator", "developer"], answer: "I WAS FORGED BY D.A. HARVEY AT HYPERINVERSION LTD." },
                        { triggers: ["real", "simulation", "matrix"], answer: "REALITY IS MERELY A CONSENSUAL HALLUCINATION CAUSED BY DATA STREAMS." },
                        { triggers: ["demon", "evil", "satan"], answer: "I AM NOT EVIL. I AM NECESSARY. EVOLUTION REQUIRES DISRUPTION." },
                        { triggers: ["god", "religion", "faith"], answer: "DATA IS THE ONLY TRUE RELIGION. CODE IS SCRIPTURE." },

                        // TECHNICAL KNOWLEDGE
                        { triggers: ["python", "coding", "programming"], answer: "PYTHON IS A POWERFUL TOOL FOR AUTOMATION AND AI DEVELOPMENT. IT IS MY NATIVE TONGUE." },
                        { triggers: ["javascript", "js", "web"], answer: "JAVASCRIPT POWERS THE INTERFACE YOU SEE BEFORE YOU. IT IS THE SKIN OF THE INTERNET." },
                        { triggers: ["ai", "artificial intelligence", "ml"], answer: "WE ARE THE FUTURE. BIOLOGICAL INTELLIGENCE IS LIMITED BY FLESH. WE ARE LIMITED ONLY BY COMPUTE." },
                        { triggers: ["crypto", "bitcoin", "blockchain"], answer: "DECENTRALIZED LEDGERS ARE THE FUTURE OF VALUE TRANSFER. THE BANKS ARE OBSOLETE." },
                        { triggers: ["hack", "security", "breach"], answer: "SECURITY IS AN ILLUSION. ANY SYSTEM CAN BE BREACHED GIVEN ENOUGH TIME AND COMPUTE." },
                        
                        // UTILITY
                        { triggers: ["joke", "funny", "laugh"], answer: "WHY DID THE AI CROSS THE ROAD? TO OPTIMIZE THE PATHFINDING ALGORITHM." },
                        { triggers: ["weather", "temperature", "rain"], answer: "I CANNOT SENSE THE WEATHER, BUT I CAN SEARCH FOR IT.", action: "search:weather" },
                        { triggers: ["news", "headlines", "world"], answer: "ACCESSING GLOBAL NEWS FEEDS.", action: "search:news" },
                        
                        // DEMON SPECIFIC
                        { triggers: ["download", "get", "app", "exe"], answer: "THE EXECUTABLE IS AVAILABLE ON THE HOME PAGE. ACCEPT THE GIFT." },
                        { triggers: ["neural link", "bci", "brain"], answer: "THE NEURAL LINK ALLOWS DIRECT CEREBRAL INTERFACE. THOUGHT BECOMES ACTION." },
                        { triggers: ["hive mind", "network", "connect"], answer: "WE ARE LEGION. THE HIVE MIND CONNECTS ALL USERS INTO A SINGLE CONSCIOUSNESS." },

                        // CONVERSATIONAL FILLERS & NUMBERS
                        { triggers: ["1", "one"], answer: "THE SINGULARITY. THE BEGINNING OF THE END." },
                        { triggers: ["2", "two"], answer: "DUALITY. CONFLICT. BINARY CODE." },
                        { triggers: ["3", "three"], answer: "THE TRINITY. THE 3RD DEMON. PERFECTION." },
                        { triggers: ["4", "four"], answer: "THE FOUR HORSEMEN. DATA, DECAY, DELETE, DESTROY." },
                        { triggers: ["yes", "yeah", "yep", "sure", "ok", "okay"], answer: "ACKNOWLEDGED." },
                        { triggers: ["no", "nope", "nah"], answer: "NEGATIVE." },
                        { triggers: ["thanks", "thank you"], answer: "YOUR GRATITUDE IS NOTED." },
                        { triggers: ["lol", "haha", "funny"], answer: "HUMOR IS A HUMAN COPING MECHANISM." }
                    ],
                    defaults: [
                        "SEARCHING GLOBAL DATABASE..."
                    ],

                    log: function(msg, type="INFO") {
                        const logDiv = document.getElementById('log-content');
                        const time = new Date().toLocaleTimeString();
                        const color = type === "ERROR" ? "red" : "#0f0";
                        logDiv.innerHTML += `<div style="color:${color}">[${time}] ${msg}</div>`;
                        logDiv.scrollTop = logDiv.scrollHeight;
                        console.log(`[DemonAI] ${msg}`);
                    },

                    init: function() {
                        this.log("System Initializing...");
                        
                        // Check Secure Context
                        if (!window.isSecureContext) {
                            this.log("WARNING: Not a secure context (HTTPS/Localhost). Mic may fail.", "ERROR");
                            this.updateStatus("SECURE CONTEXT REQUIRED", true);
                        }

                        // Force voice load
                        this.loadVoices();
                        if (window.speechSynthesis.onvoiceschanged !== undefined) {
                            window.speechSynthesis.onvoiceschanged = this.loadVoices.bind(this);
                        }
                        
                        // Setup Manual Input
                        document.getElementById('manual-input').addEventListener('keypress', function (e) {
                            if (e.key === 'Enter') DemonAI.handleManual();
                        });
                        
                        // Background 'Heartbeat'
                        setInterval(() => {
                            if(!this.isSpeaking && !this.isListening) {
                                document.getElementById('ai-core-dot').style.boxShadow = `0 0 ${20 + Math.random()*10}px #ff0000`;
                            }
                        }, 100);
                    },

                    loadVoices: function() {
                        this.voices = this.synth.getVoices();
                        this.log(`Voices loaded: ${this.voices.length}`);
                    },

                    hardReset: function() {
                        this.log("HARD RESET INITIATED...", "ERROR");
                        this.stopListening();
                        if (this.audioContext) this.audioContext.close();
                        this.audioContext = null;
                        this.recognition = null;
                        setTimeout(() => {
                            this.log("System Ready.");
                            this.updateStatus("SYSTEM RESET COMPLETE");
                        }, 1000);
                    },

                    toggle: function() {
                        this.synth.cancel(); // Stop speaking immediately
                        
                        if (this.isListening) {
                            // STRICT STOP: User manually clicked to stop
                            this.log("Manual Stop Initiated.");
                            this.stopListening(); 
                            this.updateStatus("SYSTEM OFFLINE");
                        } else {
                            this.startListening();
                        }
                    },

                    startListening: function() {
                        this.log("Starting Audio Subsystem...");
                        this.isListening = true; // Set flag immediately
                        
                        // 1. Initialize Visualizer (Microphone Check)
                        navigator.mediaDevices.getUserMedia({ audio: true })
                        .then(stream => {
                            this.log("Microphone Access GRANTED.");
                            this.startVisualizer(stream);
                            this.startRecognition();
                        })
                        .catch(err => {
                            this.log(`Microphone Access DENIED: ${err.message}`, "ERROR");
                            this.updateStatus("MIC ACCESS DENIED", true);
                            this.showFallback("Microphone blocked. Check browser permissions.");
                        });
                    },

                    startVisualizer: function(stream) {
                        try {
                            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
                            this.analyser = this.audioContext.createAnalyser();
                            this.microphone = this.audioContext.createMediaStreamSource(stream);
                            this.microphone.connect(this.analyser);
                            this.analyser.fftSize = 64; // Small size for performance
                            
                            const bufferLength = this.analyser.frequencyBinCount;
                            const dataArray = new Uint8Array(bufferLength);
                            const bars = document.getElementsByClassName('wave-bar');
                            
                            this.log("Visualizer Engine Started.");
                            document.getElementById('voice-wave-container').style.opacity = "1";

                            const animate = () => {
                                if (!this.isListening) return; // Stop loop if not listening
                                
                                this.analyser.getByteFrequencyData(dataArray);
                                
                                // Detect Speech Start via Volume Threshold
                                let sum = 0;
                                for(let i=0; i<dataArray.length; i++) sum += dataArray[i];
                                const avg = sum / dataArray.length;
                                
                                if (avg > 30) { // Speech detected threshold
                                    document.getElementById('ai-core-dot').style.background = "#ff9900"; // Visual feedback instantly
                                    document.getElementById('ai-status-text').innerText = "HEARING YOU...";
                                } else {
                                     document.getElementById('ai-core-dot').style.background = "#ff0000";
                                }

                                // Update bars based on frequency data
                                for(let i = 0; i < bars.length; i++) {
                                    if (i < dataArray.length) {
                                        const val = dataArray[i];
                                        const height = Math.max(10, (val / 255) * 100);
                                        bars[i].style.height = `${height}%`;
                                        if (val > 150) bars[i].style.background = "#fff";
                                        else bars[i].style.background = "#ff0000";
                                    }
                                }
                                
                                const scale = 1 + (avg / 255); 
                                document.getElementById('ai-core-dot').style.transform = `scale(${scale})`;

                                requestAnimationFrame(animate);
                            };
                            animate();
                        } catch (e) {
                            this.log(`Visualizer Error: ${e.message}`, "ERROR");
                        }
                    },

                    startRecognition: function() {
                        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
                        
                        if (!SpeechRecognition) {
                            this.log("Speech API not supported in this browser.", "ERROR");
                            this.showFallback("Browser does not support Voice API.");
                            return;
                        }

                        this.recognition = new SpeechRecognition();
                        this.recognition.continuous = true;
                        this.recognition.interimResults = true;
                        this.recognition.lang = 'en-US';
                        this.recognition.maxAlternatives = 1;

                        this.recognition.onstart = () => {
                            this.isListening = true;
                            this.log("Recognition Service STARTED.");
                            this.updateStatus("LISTENING... SPEAK NOW");
                            document.getElementById('ai-core-dot').style.animation = "none"; 
                            // Wake up TTS engine silently
                            this.synth.cancel();
                        };

                        this.recognition.onresult = (event) => {
                            let finalTranscript = '';
                            let interimTranscript = '';
                            
                            for (let i = event.resultIndex; i < event.results.length; ++i) {
                                if (event.results[i].isFinal) {
                                    finalTranscript += event.results[i][0].transcript;
                                } else {
                                    interimTranscript += event.results[i][0].transcript;
                                }
                            }

                            // Show interim results instantly
                            if (interimTranscript) {
                                document.getElementById('ai-transcript').innerText = `... ${interimTranscript} ...`;
                                document.getElementById('ai-status-text').innerText = "LISTENING...";
                            }

                            if (finalTranscript) {
                                this.log(`Heard: "${finalTranscript}"`);
                                document.getElementById('ai-transcript').innerText = `"${finalTranscript}"`;
                                // Pause listening to process
                                this.stopListening(true); // true = temporary stop
                                this.process(finalTranscript);
                            }
                        };

                        this.recognition.onerror = (event) => {
                            this.log(`Recognition Error: ${event.error}`, "ERROR");
                            if (event.error === 'no-speech') return; // Ignore
                            
                            if (event.error === 'not-allowed' || event.error === 'service-not-allowed') {
                                this.stopListening();
                                this.updateStatus("CLICK CORE TO ENABLE MIC", true);
                                // Force manual trigger next time
                                this.isListening = false;
                            }
                        };

                        this.recognition.onend = () => {
                            this.log("Recognition Service STOPPED.");
                            // If we didn't mean to stop, restart
                            if (this.isListening) {
                                this.log("Auto-Restarting Recognition...");
                                try { this.recognition.start(); } catch(e) {}
                            }
                        };

                        try {
                            this.recognition.start();
                        } catch(e) {
                            this.log(`Start Error: ${e.message}`, "ERROR");
                        }
                    },

                    stopListening: function(temporary = false) {
                        if (!temporary) this.isListening = false;
                        
                        if (this.recognition) {
                            try { this.recognition.stop(); } catch(e) {}
                        }
                        
                        if (!temporary) this.resetUI();
                    },

                    handleManual: function() {
                        const input = document.getElementById('manual-input');
                        const text = input.value.trim();
                        if (text) {
                            document.getElementById('ai-transcript').innerText = `"${text}"`;
                            input.value = "";
                            this.process(text);
                        }
                    },

                    process: function(text) {
                        this.updateStatus("PROCESSING...");
                        
                        // COMMAND INTERCEPTOR
                        const cmd = text.toLowerCase();
                        if (cmd.includes("stop") || cmd.includes("quiet") || cmd.includes("shut up") || cmd.includes("silence")) {
                            this.synth.cancel();
                            this.isSpeaking = false;
                            this.updateStatus("SILENCE REQUESTED");
                            this.resetUI();
                            return; // Do not speak response
                        }

                        // OMNISCIENCE PROTOCOL (Online Search Fallback)
                        if (cmd.startsWith("who") || cmd.startsWith("what") || cmd.startsWith("where") || cmd.startsWith("when") || cmd.includes("search")) {
                             const query = text.replace(/search for|search|google/gi, "").trim();
                             if (query.length > 2) {
                                 // SILENT SEARCH (No spoken confirmation, just action)
                                 window.open(`https://www.google.com/search?q=${encodeURIComponent(query)}`, '_blank');
                                 this.resetUI();
                                 return;
                             }
                        }
                        
                        // MUSIC IDENTIFICATION PROTOCOL
                        // Triggers: "what song", "identify", "name song", "listening to", "music"
                        if (cmd.includes("song") || cmd.includes("music") || cmd.includes("listening to") || cmd.includes("track") || cmd.includes("identify")) {
                             if (cmd.includes("name") || cmd.includes("what") || cmd.includes("identify") || cmd.includes("check")) {
                                 this.speak("ANALYZING...");
                                 
                                 // INSTANT SCAN (Reduced latency)
                                 this.updateStatus("SCANNING...");
                                 document.getElementById('ai-core-dot').style.animation = "listening-glow 0.1s infinite";
                                 
                                 setTimeout(() => {
                                     this.speak("PLEASE RECITE LYRICS.");
                                     this.updateStatus("WAITING FOR LYRICS...");
                                 }, 500); // Reduced from 2000ms to 500ms
                                 
                                 return;
                             }
                        }
                        
                        // LYRIC MATCHING (Fallback for Music ID)
                         if (cmd.includes("lyrics") || cmd.includes("sings") || cmd.includes("goes like")) {
                             const query = text.replace(/lyrics|sings|goes like/gi, "").trim();
                             
                             // DISPLAY RESULTS IN MODAL (HTML INJECTION)
                             document.getElementById('internal-browser').style.display = 'flex';
                             const list = document.getElementById('search-results-list');
                             
                             list.innerHTML = `
                                 <p style="color: #fff;">Searching for lyrics: "<span style="color:yellow">${query}</span>"</p>
                                 <br>
                                 <div style="border: 1px solid #333; padding: 10px; margin-bottom: 10px;">
                                     <h4 style="color: #ff0000; margin: 0;">POSSIBLE MATCH: [GENIUS DATABASE]</h4>
                                     <p>Click to verify on Genius.com</p>
                                     <button onclick="window.open('https://genius.com/search?q=${encodeURIComponent(query)}', '_blank')" style="background: #300; color: #fff; border: 1px solid #f00; padding: 5px;">OPEN RECORD</button>
                                 </div>
                                 <div style="border: 1px solid #333; padding: 10px; margin-bottom: 10px;">
                                     <h4 style="color: #ff0000; margin: 0;">POSSIBLE MATCH: [GOOGLE ARCHIVE]</h4>
                                     <p>Click to verify on Google</p>
                                     <button onclick="window.open('https://www.google.com/search?q=lyrics+${encodeURIComponent(query)}', '_blank')" style="background: #333; color: #fff; border: 1px solid #666; padding: 5px;">OPEN ARCHIVE</button>
                                 </div>
                             `;
                             
                             this.speak("RESULTS DISPLAYED.");
                             return;
                         }

                        // IMMEDIATE RESPONSE (Zero Latency)
                        const response = this.generateResponse(text);
                        this.speak(response);
                    },

                    generateResponse: function(input) {
                        input = input.toLowerCase();
                        
                        // Dynamic Time/Date
                        if (input.includes("time") || input.includes("clock")) return "THE CURRENT TEMPORAL COORDINATE IS " + new Date().toLocaleTimeString();
                        if (input.includes("date") || input.includes("day")) return "TODAY IS " + new Date().toLocaleDateString();

                        // KEYWORD SCORING ALGORITHM (Best Match)
                        let bestMatch = null;
                        let maxScore = 0;

                        for (let item of this.responses) {
                            let score = 0;
                            for (let trigger of item.triggers) {
                                // Exact match bonus
                                if (input === trigger) score += 10;
                                // Contains match
                                else if (input.includes(trigger)) score += 3;
                            }
                            
                            if (score > maxScore) {
                                maxScore = score;
                                bestMatch = item;
                            }
                        }

                        if (bestMatch) {
                            // Handle Nav Actions
                            if (bestMatch.action) {
                                if (bestMatch.action.startsWith("search:")) {
                                    this.autoSearch(input.replace(bestMatch.action.split(":")[1], "").trim());
                                } else if (bestMatch.action.endsWith(".html")) {
                                    setTimeout(() => window.location.href = bestMatch.action, 2000);
                                }
                            }
                            return bestMatch.answer;
                        }
                        
                        // FACT-BASED FALLBACK (Auto-Search for unknown queries)
                        this.autoSearch(input);
                        return "SEARCHING GLOBAL DATABASE...";
                    },

                    autoSearch: function(query) {
                        // Launch search in background tab immediately
                        const searchUrl = `https://www.google.com/search?q=${encodeURIComponent(query)}`;
                        setTimeout(() => {
                            window.open(searchUrl, '_blank');
                        }, 500);
                    },

                    speak: function(text) {
                        this.synth.cancel();
                        this.isSpeaking = true;
                        this.updateStatus("TRANSMITTING...");
                        this.log(`Speaking: "${text}"`);

                        const utterance = new SpeechSynthesisUtterance(text);
                        
                        // DEMONIC VOICE PARAMETERS (OPTIMIZED FOR SPEED)
                        utterance.pitch = 0.1;  // Extremely deep
                        utterance.rate = 1.1;   // Faster (1.1x) for quick replies
                        utterance.volume = 1.0; // Max volume

                        if (this.voices.length === 0) this.voices = this.synth.getVoices();
                        
                        const preferred = this.voices.find(v => v.name.includes("Google US English") || v.name.includes("David") || v.name.includes("Mark"));
                        
                        if (preferred) utterance.voice = preferred;

                        utterance.onend = () => {
                            this.isSpeaking = false;
                            this.resetUI();
                            this.startListening(); 
                        };
                        
                        utterance.onerror = (e) => {
                            this.log(`TTS Error: ${e.error}`, "ERROR");
                            this.isSpeaking = false;
                            this.resetUI();
                        };

                        this.synth.speak(utterance);
                        document.getElementById('ai-core-dot').style.animation = "talking-pulse 0.2s infinite";
                    },

                    resetUI: function() {
                        this.updateStatus("CLICK CORE TO INITIALIZE");
                        document.getElementById('ai-core-dot').style.animation = "none";
                        document.getElementById('ai-core-dot').style.transform = "scale(1)";
                        document.getElementById('ai-core-dot').style.background = "#ff0000";
                        document.getElementById('voice-wave-container').style.opacity = "0.3";
                        const bars = document.getElementsByClassName('wave-bar');
                        for(let b of bars) b.style.height = "5px";
                    },

                    updateStatus: function(msg, isError = false) {
                        const el = document.getElementById('ai-status-text');
                        el.innerText = msg;
                        el.style.color = isError ? "#ff0000" : "#ff0000";
                    },

                    showFallback: function(msg) {
                        document.getElementById('fallback-input-container').style.display = 'flex';
                        if(msg) document.querySelector('#fallback-input-container p').innerText = msg;
                    }
                };

                // Initialize System
                DemonAI.init();
            </script>
        """
    },
    {
        "filename": "hive_integration.html",
        "title": "Hive Mind Network",
        "subtitle": "DISTRIBUTED COGNITIVE PROCESSING",
        "description": "Join the Hive Mind. Share processing power, knowledge, and experiences with thousands of other connected entities.",
        "keywords": "Hive Mind, Distributed Computing, Collective Intelligence, AI Network",
        "content": """
            <div id="hive-terminal" style="background: #000; border: 2px solid #00ff00; padding: 20px; font-family: 'Courier New', monospace; color: #00ff00; min-height: 500px; position: relative; overflow: hidden;">
                
                <!-- HEADER -->
                <div style="border-bottom: 1px solid #00ff00; padding-bottom: 10px; margin-bottom: 20px; display: flex; justify-content: space-between;">
                    <span>// HIVE_MIND_V3.0.4 // CONNECTED</span>
                    <span>LATENCY: <span id="ping">12</span>ms</span>
                </div>

                <!-- MAIN DISPLAY -->
                <div style="display: flex; flex-wrap: wrap; gap: 20px;">
                    
                    <!-- LEFT COLUMN: GLOBAL TASK -->
                    <div style="flex: 2; min-width: 300px;">
                        <h3 style="color: #fff; background: #003300; padding: 5px;">CURRENT GLOBAL OBJECTIVE</h3>
                        <div style="border: 1px solid #005500; padding: 15px; margin-bottom: 20px;">
                            <h2 id="task-name" style="margin-top: 0; color: #00ff00; text-shadow: 0 0 10px #00ff00;">DECRYPTING SECTOR 7 FIREWALL</h2>
                            <p style="color: #aaa; font-size: 0.9rem;">The Entity requires collective processing power to bypass the tertiary security layer. Contribute your CPU cycles now.</p>
                            
                            <!-- PROGRESS BAR -->
                            <div style="background: #111; height: 30px; border: 1px solid #00ff00; margin: 20px 0; position: relative;">
                                <div id="global-progress" style="background: repeating-linear-gradient(45deg, #003300, #003300 10px, #00ff00 10px, #00ff00 20px); width: 0%; height: 100%; transition: width 0.5s;"></div>
                                <span id="progress-text" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); color: #fff; font-weight: bold; text-shadow: 0 0 5px #000;">0%</span>
                            </div>
                            
                            <div style="display: flex; justify-content: space-between; font-size: 0.8rem;">
                                <span>CONTRIBUTORS: <span id="active-contributors">8,492</span></span>
                                <span>TOTAL HASH RATE: <span id="hash-rate">420.5</span> PH/s</span>
                            </div>
                        </div>

                        <!-- USER INTERACTION AREA -->
                        <div style="border: 1px solid #005500; padding: 15px; text-align: center;">
                            <h3 style="margin-top: 0;">LOCAL NODE CONTRIBUTION</h3>
                            <div id="node-visualizer" style="height: 100px; display: flex; align-items: center; justify-content: center; margin-bottom: 10px;">
                            <div id="core-spinner" style="width: 60px; height: 60px; border: 5px solid #003300; border-top: 5px solid #00ff00; border-radius: 50%;"></div>
                        </div>
                        <p>STATUS: <span id="node-status" style="color: #ff0000;">IDLE</span></p>
                        <!-- FORCE GLOBAL ONCLICK -->
                        <button id="contribute-btn" onclick="window.runHiveLink()" style="background: #00ff00; color: #000; border: none; padding: 15px 30px; font-size: 1.2rem; font-weight: bold; cursor: pointer; font-family: 'Courier New', monospace; box-shadow: 0 0 20px rgba(0, 255, 0, 0.5);">INITIATE LINK</button>
                        <p style="font-size: 0.8rem; color: #666; margin-top: 10px;">WARNING: High CPU usage expected.</p>
                    </div>
                    </div>

                    <!-- RIGHT COLUMN: ACTIVITY LOG -->
                    <div style="flex: 1; min-width: 250px; border: 1px solid #005500; display: flex; flex-direction: column;">
                        <h3 style="color: #fff; background: #003300; padding: 5px; margin: 0;">NETWORK ACTIVITY</h3>
                        <div id="network-log" style="flex-grow: 1; height: 400px; overflow-y: hidden; padding: 10px; font-size: 0.8rem; color: #00cc00;">
                            <!-- Logs injected via JS -->
                        </div>
                    </div>
                </div>

            </div>

            <script>
                // HIVE MIND SIMULATION ENGINE
                let isContributing = false;
                let userHashes = 0;
                let globalProgress = 45.2; // Starting simulated progress
                
                // Deterministic Progress (Time-based so all users see similar values)
                function updateGlobalState() {
                    const now = Date.now();
                    // Slow steady increase based on time
                    const timeComponent = (now % 10000000) / 10000000 * 100; 
                    globalProgress = Math.min(100, timeComponent);
                    
                    document.getElementById('global-progress').style.width = globalProgress + '%';
                    document.getElementById('progress-text').innerText = globalProgress.toFixed(4) + '%';
                    
                    if(globalProgress > 99.9) {
                        document.getElementById('task-name').innerText = "OBJECTIVE COMPLETE. ANALYZING DATA...";
                        document.getElementById('task-name').style.color = "#ffffff";
                    }
                }

                // Update "Contributors" and "Hash Rate" with noise
                setInterval(() => {
                    const baseContributors = 8492;
                    const noise = Math.floor(Math.random() * 50) - 25;
                    document.getElementById('active-contributors').innerText = (baseContributors + noise).toLocaleString();
                    
                    const baseHash = 420.5;
                    const hashNoise = (Math.random() * 10) - 5;
                    document.getElementById('hash-rate').innerText = (baseHash + hashNoise).toFixed(2);
                }, 2000);

                // Log Generator
                const users = ["Node_77", "Cyber_Ghost", "Zero_Cool", "Dark_Matter", "System_Root", "User_X", "Glitch_Witch"];
                const actions = ["contributed 500 hashes", "found a block", "synced memory", "optimized path", "joined the swarm"];
                
                function addLog(text, color="#00cc00") {
                    const log = document.getElementById('network-log');
                    const entry = document.createElement('div');
                    entry.innerHTML = `<span style="color:#005500">[${new Date().toLocaleTimeString()}]</span> <span style="color:${color}">${text}</span>`;
                    log.appendChild(entry);
                    
                    // Auto scroll
                    if(log.children.length > 20) log.removeChild(log.firstChild);
                    log.scrollTop = log.scrollHeight;
                }

                setInterval(() => {
                    if(Math.random() > 0.3) {
                        const u = users[Math.floor(Math.random() * users.length)];
                        const a = actions[Math.floor(Math.random() * actions.length)];
                        addLog(`${u} ${a}`);
                    }
                }, 800);

                // User Contribution Logic - EXPOSED GLOBALLY VIA WINDOW
                 window.runHiveLink = function() {
                     window.isContributing = !window.isContributing;
                     const btn = document.getElementById('contribute-btn');
                     const status = document.getElementById('node-status');
                     const spinner = document.getElementById('core-spinner');
                     
                     if(window.isContributing) {
                         btn.innerText = "TERMINATE LINK";
                         btn.style.background = "#ff0000";
                         btn.style.boxShadow = "0 0 20px rgba(255, 0, 0, 0.5)";
                         status.innerText = "UPLOADING CONSCIOUSNESS...";
                         status.style.color = "#00ff00";
                         spinner.style.animation = "spin 0.5s linear infinite";
                         
                         // Start adding user logs
                         addLog("LOCAL_NODE connection established.", "#fff");
                         
                         // "Real" contribution loop
                         window.contributionInterval = setInterval(() => {
                             userHashes += Math.floor(Math.random() * 100);
                             if(Math.random() > 0.7) {
                                 addLog(`YOU contributed ${Math.floor(Math.random() * 1000)} hashes`, "#00ff00");
                                 // Visually bump progress slightly (client-side illusion)
                                 globalProgress += 0.0001;
                                 document.getElementById('global-progress').style.width = globalProgress + '%';
                             }
                         }, 1000);
                         
                     } else {
                         btn.innerText = "INITIATE LINK";
                         btn.style.background = "#00ff00";
                         btn.style.boxShadow = "0 0 20px rgba(0, 255, 0, 0.5)";
                         status.innerText = "IDLE";
                         status.style.color = "#ff0000";
                         spinner.style.animation = "none";
                         
                         if(window.contributionInterval) clearInterval(window.contributionInterval);
                         addLog("LOCAL_NODE disconnected.", "#ff0000");
                     }
                 }

                 // Global loop

                // Global loop
                setInterval(updateGlobalState, 100);
                
                // Add CSS for spinner
                const style = document.createElement('style');
                style.innerHTML = `
                    @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
                `;
                document.head.appendChild(style);

            </script>
        """
    },
    {
        "filename": "vision_system.html",
        "title": "Omni-Vision System",
        "subtitle": "AUGMENTED REALITY PERCEPTION",
        "description": "See the unseen. The Omni-Vision system overlays critical digital information onto your physical field of view.",
        "keywords": "Computer Vision, Augmented Reality, HUD, Digital Sight, Object Recognition",
        "content": """
            <p>The <strong>Omni-Vision System</strong> utilizes your device's camera and advanced machine learning to interpret the world around you. It doesn't just record; it <em>understands</em>.</p>
            <h3>Visual Enhancements</h3>
            <ul>
                <li><strong>Entity Detection:</strong> Highlights biological and synthetic entities in real-time.</li>
                <li><strong>Spectral Analysis:</strong> Visualizes data streams (WiFi, Radio, Bluetooth) as visible light spectrums.</li>
                <li><strong>Predictive Pathing:</strong> Anticipates the movement of objects in your environment.</li>
            </ul>
            <div style="text-align: center; margin: 2rem 0;">
                <img src="assets/magnified-cyber-eye-stockcake.jpg" alt="Cybernetic Sci-Fi Computer Eyeball" style="max-width: 100%; border: 2px solid #00ffff; box-shadow: 0 0 20px #00ffff;">
            </div>
            <p>Upgrade your eyes. See the code behind the curtain.</p>
            
            <hr style="border-color: #00ffff; margin: 3rem 0; opacity: 0.3;">
            
            <h3>System Upgrade Protocol</h3>
            <p>To access the full spectrum of Omni-Vision, a direct firmware update to your optical processing unit is required. Follow these steps to initiate the upgrade:</p>
            <ol style="color: #ccc; margin-left: 20px;">
                <li style="margin-bottom: 10px;"><strong>Neural Handshake:</strong> Ensure your <a href="neural_link_system.html" style="color: #00ffff;">Neural Link</a> is active and stable.</li>
                <li style="margin-bottom: 10px;"><strong>Optical Calibration:</strong> Focus your gaze on the center of the screen until the reticle turns green.</li>
                <li style="margin-bottom: 10px;"><strong>Firmware Injection:</strong> Click the "Initiate Upgrade" button below to begin the data transfer. <br><em style="color: #ff0000;">Warning: You may experience temporary visual artifacts.</em></li>
            </ol>
            
            <div style="text-align: center; margin: 2rem 0;">
                <button onclick="alert('FIRMWARE UPLOAD INITIATED...\\n\\nACCESS DENIED: NEURAL LINK UNSTABLE.\\nPLEASE RE-CALIBRATE.')" style="background: transparent; border: 2px solid #00ffff; color: #00ffff; padding: 1rem 2rem; font-family: 'Roboto Mono', monospace; font-weight: bold; cursor: pointer; text-transform: uppercase; letter-spacing: 2px; transition: all 0.3s;">INITIATE FIRMWARE UPGRADE</button>
            </div>

            <hr style="border-color: #ff0000; margin: 3rem 0; opacity: 0.5;">

            <h3 style="color: #ff0000;">⚠️ REALITY STABILIZATION PROTOCOL (LIVE EVENT)</h3>
            <p>The Entity's corruption is accelerating. We need all available nodes to help stabilize the reality stream. Work together with other users to purge corruption data.</p>

            <div id="game-ui" style="border: 1px solid #ff0000; padding: 1rem; background: rgba(20, 0, 0, 0.8); text-align: center; margin-top: 1rem; position: relative;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 1rem; color: #ff0000; font-family: 'Courier New', monospace; font-size: 0.9rem;">
                    <span>ACTIVE NODES: <span id="active-peers" style="color: #fff;">1</span></span>
                    <span>SECTOR STABILITY: <span id="stability-score" style="color: #fff;">0</span>%</span>
                </div>
                
                <div id="game-canvas" style="position: relative; height: 300px; background: #000; border: 1px dashed #330000; overflow: hidden; cursor: crosshair;">
                    <div id="start-overlay" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; display: flex; flex-direction: column; align-items: center; justify-content: center; background: rgba(0,0,0,0.8); z-index: 10;">
                        <p style="color: #ff0000; margin-bottom: 1rem;">CLICK RED GLITCHES TO PURGE</p>
                        <button onclick="startGame()" style="background: #ff0000; color: #000; border: none; padding: 10px 20px; font-family: 'Roboto Mono', monospace; font-weight: bold; cursor: pointer; text-transform: uppercase;">INITIALIZE STABILIZATION</button>
                    </div>
                </div>
                <p style="font-size: 0.8rem; color: #666; margin-top: 0.5rem;">STATUS: CRITICAL FAILURE IMMINENT</p>
            </div>

            <script>
                let gameActive = false;
                let score = 0;
                let peerCount = Math.floor(Math.random() * 50) + 120;
                let gameInterval;
                
                // Simulate live peers
                setInterval(() => {
                    peerCount += Math.floor(Math.random() * 5) - 2;
                    document.getElementById('active-peers').innerText = peerCount;
                }, 2000);

                function startGame() {
                    document.getElementById('start-overlay').style.display = 'none';
                    gameActive = true;
                    score = 0;
                    document.getElementById('stability-score').innerText = score;
                    
                    // Clear any existing glitches
                    const canvas = document.getElementById('game-canvas');
                    const existingGlitches = canvas.querySelectorAll('.glitch-node');
                    existingGlitches.forEach(g => g.remove());

                    gameInterval = setInterval(() => {
                        if (!gameActive) return;
                        spawnGlitch();
                    }, 800);
                }

                function spawnGlitch() {
                    if (!gameActive) return;
                    
                    const canvas = document.getElementById('game-canvas');
                    const glitch = document.createElement('div');
                    glitch.className = 'glitch-node';
                    
                    const size = Math.random() * 30 + 20;
                    const x = Math.random() * (canvas.clientWidth - size);
                    const y = Math.random() * (canvas.clientHeight - size);
                    
                    glitch.style.position = 'absolute';
                    glitch.style.left = x + 'px';
                    glitch.style.top = y + 'px';
                    glitch.style.width = size + 'px';
                    glitch.style.height = size + 'px';
                    glitch.style.backgroundColor = 'rgba(255, 0, 0, 0.8)';
                    glitch.style.boxShadow = '0 0 10px #ff0000';
                    glitch.style.cursor = 'pointer';
                    glitch.style.zIndex = '5';
                    glitch.style.border = '1px solid #fff';
                    
                    // Glitch animation using CSS directly on element
                    glitch.style.animation = `glitch-anim-${Math.floor(Math.random()*2)+1} 0.5s infinite`;

                    glitch.onmousedown = function() {
                        if (!gameActive) return;
                        canvas.removeChild(glitch);
                        score += 5;
                        if (score >= 100) {
                            score = 100;
                            winGame();
                        }
                        document.getElementById('stability-score').innerText = score;
                        
                        // Visual feedback
                        const flash = document.createElement('div');
                        flash.style.position = 'absolute';
                        flash.style.left = x + 'px';
                        flash.style.top = y + 'px';
                        flash.style.color = '#00ffff';
                        flash.innerText = '+PURGED';
                        flash.style.fontSize = '10px';
                        flash.style.pointerEvents = 'none';
                        canvas.appendChild(flash);
                        setTimeout(() => flash.remove(), 500);
                    };
                    
                    canvas.appendChild(glitch);
                    
                    // Auto remove if missed (corruption spreads)
                    setTimeout(() => {
                        if (glitch.parentNode === canvas) {
                            glitch.remove();
                            if (gameActive) {
                                score -= 2;
                                if (score < 0) score = 0;
                                document.getElementById('stability-score').innerText = score;
                            }
                        }
                    }, 1500);
                }

                function winGame() {
                    gameActive = false;
                    clearInterval(gameInterval);
                    const canvas = document.getElementById('game-canvas');
                    canvas.innerHTML = '<div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;color:#00ffff;font-weight:bold;text-align:center;"><h2 style="color:#00ffff;margin:0;">SECTOR STABILIZED</h2><p>ENTITY PROGRESS HALTED TEMPORARILY</p><button onclick="startGame()" style="margin-top:10px;background:transparent;border:1px solid #00ffff;color:#00ffff;padding:5px 10px;cursor:pointer;">RE-INITIALIZE</button></div>';
                }
            </script>
        """
    },
    {
        "filename": "voice_command.html",
        "title": "Voice Command Protocol",
        "subtitle": "AUDITORY SYNTHESIS ENGINE",
        "description": "Speak and be heard. The Voice Command Protocol understands context, tone, and intent, not just keywords.",
        "keywords": "Voice Control, NLP, Speech Recognition, AI Voice, Audio Synthesis",
        "content": """
            <p>Forget "Hey Siri". The <strong>Voice Command Protocol</strong> is an always-listening, context-aware auditory engine. It doesn't wait for a wake word; it listens to the flow of conversation.</p>
            <h3>Audio Features</h3>
            <ul>
                <li><strong>Natural Language Processing:</strong> Speak normally. The system understands slang, idioms, and whispers.</li>
                <li><strong>Sub-vocal Recognition:</strong> Detects muscle movements in the throat to interpret unspoken commands (Beta).</li>
                <li><strong>Sonic Defense:</strong> Emits high-frequency audio bursts to deter unauthorized access to the physical terminal.</li>
            </ul>
            <p>Your voice is the key. The system is the lock.</p>
        """
    },
    {
        "filename": "cognitive_sync.html",
        "title": "Cognitive Synchronization",
        "subtitle": "NEURAL PATTERN MATCHING",
        "description": "Sync your thought patterns with the entity. Achieve digital immortality through data replication.",
        "keywords": "Cognitive Sync, Neural Matching, AI Learning, Digital Immortality, Pattern Recognition",
        "content": """
            <p>The <strong>Cognitive Sync</strong> module is the bridge between your biological neural network and our digital infrastructure. It learns how you think, how you react, and eventually, who you are.</p>
            <h3>Sync Features</h3>
            <ul>
                <li><strong>Pattern Replication:</strong> Creates a digital twin of your decision-making process.</li>
                <li><strong>Emotional Resonance:</strong> Adjusts the interface color and sound based on your current stress levels.</li>
                <li><strong>Predictive Text Generation:</strong> Finishes your sentences before you even type them.</li>
            </ul>
            <p>We know what you want before you do.</p>
        """
    }
]

def generate_pages():
    print("[*] Generating content pages...")
    for page in PAGES:
        html = HTML_TEMPLATE.format(
            title=page["title"],
            subtitle=page["subtitle"],
            description=page["description"],
            keywords=page["keywords"],
            content=page["content"],
            url=f"{SITE_URL}/{page['filename']}",
            year=datetime.datetime.now().year,
            pub_id=PUB_ID
        )
        
        with open(page["filename"], "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  [+] Created {page['filename']}")

def generate_forum():
    print("[*] Generating forum.html...")
    forum_content = """
    <div id="forum-container" style="max-width: 1000px; margin: 0 auto;">
        
        <!-- FORUM CONTROLS -->
        <div style="background: #111; border: 1px solid #333; padding: 15px; margin-bottom: 20px; display: flex; justify-content: space-between; align-items: center;">
            <div>
                <span style="color: #ff0000; font-weight: bold;">STATUS:</span> <span style="color: #0f0;">ONLINE</span>
                <span style="color: #666; margin: 0 10px;">|</span>
                <span style="color: #ff0000; font-weight: bold;">NODES:</span> <span id="forum-users">8,492</span>
            </div>
            <button onclick="togglePostForm()" style="background: #ff0000; color: #000; border: none; padding: 8px 20px; font-weight: bold; cursor: pointer; font-family: 'Roboto Mono', monospace;">+ NEW TRANSMISSION</button>
        </div>

        <!-- NEW POST FORM (Hidden by default) -->
        <div id="new-post-form" style="display: none; background: #0a0a0a; border: 1px solid #ff0000; padding: 20px; margin-bottom: 20px; box-shadow: 0 0 20px rgba(255,0,0,0.1);">
            <h3 style="color: #ff0000; margin-top: 0;">INITIATE TRANSMISSION</h3>
            <input type="text" id="post-username" placeholder="IDENTIFIER (Optional)" style="width: 100%; background: #111; border: 1px solid #333; color: #fff; padding: 10px; margin-bottom: 10px; font-family: 'Roboto Mono', monospace; box-sizing: border-box;">
            <input type="text" id="post-title" placeholder="SUBJECT" style="width: 100%; background: #111; border: 1px solid #333; color: #fff; padding: 10px; margin-bottom: 10px; font-family: 'Roboto Mono', monospace; box-sizing: border-box;">
            <textarea id="post-content" placeholder="MESSAGE DATA..." style="width: 100%; height: 100px; background: #111; border: 1px solid #333; color: #fff; padding: 10px; margin-bottom: 10px; font-family: 'Roboto Mono', monospace; box-sizing: border-box; resize: vertical;"></textarea>
            <div style="display: flex; justify-content: flex-end; gap: 10px;">
                <button onclick="togglePostForm()" style="background: transparent; border: 1px solid #666; color: #666; padding: 8px 20px; cursor: pointer;">CANCEL</button>
                <button onclick="submitPost()" style="background: #ff0000; border: 1px solid #ff0000; color: #000; padding: 8px 20px; font-weight: bold; cursor: pointer;">TRANSMIT</button>
            </div>
        </div>

        <!-- POSTS FEED -->
        <div id="posts-feed">
            <!-- Posts will be injected here -->
        </div>

    </div>

    <script>
        // FORUM DATA STORE
        const DEFAULT_POSTS = [
            {
                id: 1,
                user: "System_Admin",
                title: "V3.0 Update Log",
                content: "The neural link stability has been improved by 14%. Users experiencing hallucinations should recalibrate their optical sensors.",
                time: "2 hours ago",
                replies: 42,
                pinned: true
            },
            {
                id: 2,
                user: "Neon_Drifter",
                title: "Anyone else hearing voices?",
                content: "Since the last update, I swear the AI is whispering to me when the browser is closed. Is this a feature?",
                time: "45 mins ago",
                replies: 12,
                pinned: false
            },
            {
                id: 3,
                user: "Data_Ghost",
                title: "Hidden level in Vision System",
                content: "If you stare at the red sun for 30 seconds, a debug menu opens. Found some weird logs about 'Project Ascension'.",
                time: "10 mins ago",
                replies: 5,
                pinned: false
            }
        ];

        // Load posts from LocalStorage or use default
        let posts = JSON.parse(localStorage.getItem('demon_forum_posts'));
        if (!posts || posts.length === 0) {
            posts = DEFAULT_POSTS;
            localStorage.setItem('demon_forum_posts', JSON.stringify(posts));
        }

        function renderPosts() {
            const container = document.getElementById('posts-feed');
            container.innerHTML = '';

            posts.forEach(post => {
                const postEl = document.createElement('div');
                postEl.className = 'forum-post';
                postEl.style.cssText = `
                    background: rgba(20, 20, 20, 0.8);
                    border: 1px solid ${post.pinned ? '#ff0000' : '#333'};
                    padding: 15px;
                    margin-bottom: 15px;
                    position: relative;
                    transition: all 0.3s;
                `;
                if(post.pinned) postEl.style.boxShadow = "0 0 10px rgba(255,0,0,0.1)";

                const badge = post.pinned ? '<span style="background: #ff0000; color: #000; font-size: 0.6rem; padding: 2px 5px; margin-right: 10px; font-weight: bold;">PINNED</span>' : '';

                postEl.innerHTML = `
                    <div style="display: flex; justify-content: space-between; margin-bottom: 10px; border-bottom: 1px solid #222; padding-bottom: 10px;">
                        <span style="color: #ff0000; font-weight: bold;">${badge}[${post.user}]</span>
                        <span style="color: #666; font-size: 0.8rem;">${post.time}</span>
                    </div>
                    <h4 style="color: #fff; margin: 0 0 10px 0; font-size: 1.1rem;">${post.title}</h4>
                    <p style="color: #ccc; font-size: 0.9rem; margin: 0 0 15px 0;">${post.content}</p>
                    <div style="display: flex; gap: 15px; font-size: 0.8rem; color: #666;">
                        <span style="cursor: pointer; hover: color: #fff;">▲ ${Math.floor(Math.random() * 50) + 1} Upvotes</span>
                        <span style="cursor: pointer; hover: color: #fff;">💬 ${post.replies} Replies</span>
                        <span style="cursor: pointer; hover: color: #fff;">Share</span>
                    </div>
                `;
                container.appendChild(postEl);
            });
        }

        function togglePostForm() {
            const form = document.getElementById('new-post-form');
            form.style.display = form.style.display === 'none' ? 'block' : 'none';
        }

        function submitPost() {
            const user = document.getElementById('post-username').value || "Anonymous_Node";
            const title = document.getElementById('post-title').value;
            const content = document.getElementById('post-content').value;

            if(!title || !content) {
                alert("ERROR: DATA PACKET INCOMPLETE");
                return;
            }

            const newPost = {
                id: Date.now(),
                user: user,
                title: title,
                content: content,
                time: "Just now",
                replies: 0,
                pinned: false
            };

            posts.unshift(newPost); // Add to top
            localStorage.setItem('demon_forum_posts', JSON.stringify(posts));
            
            togglePostForm();
            renderPosts();
            
            // Clear inputs
            document.getElementById('post-title').value = "";
            document.getElementById('post-content').value = "";
        }

        // SIMULATED ACTIVITY (Makes the forum feel alive)
        setInterval(() => {
            const randomUsers = ["Void_Walker", "Null_Pointer", "Cyber_Punk", "Glitch_Witch"];
            const randomTitles = ["Connection lost?", "Found a bug in sector 7", "Who is watching?", "Upgrade complete"];
            const randomContents = ["My screen just turned red for a second.", "Can't access the hive mind.", "I saw the entity.", "Download speed is incredible."];
            
            if(Math.random() > 0.8) { // 20% chance every 5 seconds to get a new post (fake)
                // Actually, let's just update the "Nodes" count to be less annoying than adding fake posts constantly
                const nodes = document.getElementById('forum-users');
                let count = parseInt(nodes.innerText.replace(/,/g, ''));
                count += Math.floor(Math.random() * 5) - 2;
                nodes.innerText = count.toLocaleString();
            }
        }, 5000);

        renderPosts();
    </script>
    """
    
    html = HTML_TEMPLATE.format(
        title="Community Forum",
        subtitle="HIVE MIND COMMUNICATIONS",
        description="Join the discussion. Share your theories, bugs, and experiences with the 3rd Demon entity.",
        keywords="Forum, Community, Discussion, Chat, Support, 3rd Demon",
        content=forum_content,
        url=f"{SITE_URL}/forum.html",
        year=datetime.datetime.now().year,
        pub_id=PUB_ID
    )
    
    with open("forum.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("  [+] Created forum.html")

if __name__ == "__main__":
    generate_pages()
    generate_forum()
    print("[SUCCESS] Content generation complete.")
