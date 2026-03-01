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
</head>
<body>

    <header>
        <h1>THE 3RD DEMON</h1>
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
        """
    },
    {
        "filename": "hive_integration.html",
        "title": "Hive Mind Network",
        "subtitle": "DISTRIBUTED COGNITIVE PROCESSING",
        "description": "Join the Hive Mind. Share processing power, knowledge, and experiences with thousands of other connected entities.",
        "keywords": "Hive Mind, Distributed Computing, Collective Intelligence, AI Network",
        "content": """
            <p>No entity is an island. The <strong>Hive Mind Network</strong> connects all users of the 3rd Demon software into a single, massive distributed computing grid. This allows for:</p>
            <h3>Network Features</h3>
            <ul>
                <li><strong>Parallel Problem Solving:</strong> Complex algorithms are shattered into micro-tasks and solved by the collective instantly.</li>
                <li><strong>Shared Knowledge Base:</strong> Instant access to the cumulative skills of all connected users.</li>
                <li><strong>Consensus Reality:</strong> Vote on the direction of the system's evolution through subconscious consensus.</li>
            </ul>
            <p>Your individuality is preserved, but your potential is multiplied. We are legion.</p>
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
                <img src="assets/cyber_eye.jpg?v=2" alt="Cybernetic Sci-Fi Computer Eyeball" style="max-width: 100%; border: 2px solid #00ffff; box-shadow: 0 0 20px #00ffff;">
            </div>
            <p>Upgrade your eyes. See the code behind the curtain.</p>
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
    <div id="disqus_thread"></div>
    <script>
        /**
        *  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
        *  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables    */
        /*
        var disqus_config = function () {
        this.page.url = "https://the3rddemon.com/forum.html";  // Replace PAGE_URL with your page's canonical URL variable
        this.page.identifier = "forum_main"; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
        };
        */
        (function() { // DON'T EDIT BELOW THIS LINE
        var d = document, s = d.createElement('script');
        s.src = 'https://the-3rd-demon.disqus.com/embed.js';
        s.setAttribute('data-timestamp', +new Date());
        (d.head || d.body).appendChild(s);
        })();
    </script>
    <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
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
