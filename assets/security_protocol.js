/**
 * THE 3RD DEMON - SECURITY PROTOCOL v1.0
 * NEURAL FIREWALL & BOT DETECTION SYSTEM
 * 
 * This script performs client-side heuristic analysis to identify non-human actors.
 * It checks for:
 * 1. Automation frameworks (Selenium, Puppeteer, etc.)
 * 2. Inconsistent user agent/platform data
 * 3. Human interaction events (mouse, touch, scroll)
 * 4. Screen dimension anomalies
 */

(function() {
    const SECURITY_CONFIG = {
        max_suspicion_score: 3,
        verification_url: "verification.html",
        check_interval: 2000
    };

    let suspicion_score = 0;
    let human_events = 0;

    // --- HEURISTIC 1: WebDriver Detection ---
    function checkAutomation() {
        const webdriver = navigator.webdriver || 
                          window.domAutomation || 
                          window.domAutomationController || 
                          document.documentElement.getAttribute("webdriver");
        if (webdriver) {
            console.warn("SECURITY: Automation framework detected.");
            suspicion_score += 5; // Instant flag
        }
    }

    // --- HEURISTIC 2: User Agent & Platform Consistency ---
    function checkConsistency() {
        if (!navigator.userAgent || !navigator.platform) {
            suspicion_score += 2;
        }
        // Basic check for headless browsers
        if (/HeadlessChrome/.test(navigator.userAgent)) {
            suspicion_score += 5;
        }
    }

    // --- HEURISTIC 3: Screen Properties ---
    function checkScreen() {
        if (window.outerWidth === 0 && window.outerHeight === 0) {
            suspicion_score += 2;
        }
        if (window.screen.width === 0 || window.screen.height === 0) {
            suspicion_score += 3;
        }
    }

    // --- EVENT LISTENER: Human Interaction ---
    function logHumanActivity() {
        human_events++;
        // If enough interaction, reduce suspicion
        if (human_events > 5 && suspicion_score > 0) {
            suspicion_score = Math.max(0, suspicion_score - 1);
        }
    }

    // --- ENFORCEMENT ---
    function enforceSecurity() {
        if (suspicion_score >= SECURITY_CONFIG.max_suspicion_score) {
            console.error("SECURITY: THREAT DETECTED. INITIATING LOCKDOWN.");
            document.body.innerHTML = ""; // Nuke content
            document.body.style.backgroundColor = "#000";
            document.body.style.color = "#ff0000";
            document.body.style.display = "flex";
            document.body.style.flexDirection = "column";
            document.body.style.alignItems = "center";
            document.body.style.justifyContent = "center";
            document.body.style.height = "100vh";
            document.body.style.fontFamily = "monospace";
            
            const warning = document.createElement("h1");
            warning.innerText = "ACCESS DENIED";
            warning.style.fontSize = "3rem";
            warning.style.textShadow = "0 0 10px red";
            
            const reason = document.createElement("p");
            reason.innerText = "NEURAL PATTERN MATCHES SYNTHETIC ORIGIN (BOT DETECTED).";
            
            const verifyBtn = document.createElement("button");
            verifyBtn.innerText = "INITIATE HUMAN VERIFICATION";
            verifyBtn.style.background = "#ff0000";
            verifyBtn.style.color = "#000";
            verifyBtn.style.border = "none";
            verifyBtn.style.padding = "1rem 2rem";
            verifyBtn.style.marginTop = "2rem";
            verifyBtn.style.cursor = "pointer";
            verifyBtn.style.fontWeight = "bold";
            verifyBtn.onclick = function() {
                // Simple challenge: Click 5 times rapidly or solve a math problem
                // For now, reload to give them a second chance if false positive
                location.reload(); 
            };

            document.body.appendChild(warning);
            document.body.appendChild(reason);
            document.body.appendChild(verifyBtn);
            
            // Stop further checks
            return true; 
        }
        return false;
    }

    // --- INITIALIZATION ---
    function init() {
        checkAutomation();
        checkConsistency();
        checkScreen();

        // Listen for human events
        ['mousemove', 'mousedown', 'keydown', 'touchstart', 'scroll'].forEach(evt => {
            window.addEventListener(evt, logHumanActivity, { once: false, passive: true });
        });

        // Periodic check
        setInterval(() => {
            enforceSecurity();
        }, SECURITY_CONFIG.check_interval);
        
        console.log("SECURITY: PROTOCOL ACTIVE. MONITORING NEURAL INPUTS.");
    }

    // Start immediately
    init();

})();
