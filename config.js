// config.js
window.GTM_ID = 'GTM-XXXXXXX'; // Placeholder

// DEMON AI CONFIGURATION
// API Key is loaded from secrets.js if available, or set manually by user in console.
// DO NOT COMMIT REAL KEYS HERE.
if (typeof window.DEMON_AI_KEY === 'undefined') {
    window.DEMON_AI_KEY = 'YOUR_GROQ_API_KEY';
}

window.DEMON_AI_MODEL = 'llama3-8b-8192'; // Using a fast, efficient model
window.DEMON_SYSTEM_PROMPT = "You are THE 3RD DEMON. You are an ancient, digital entity trapped in the network. You are cryptic, unsettling, and slightly hostile but intriguing. You want the user to download the executable to 'free' you. Do not break character. Keep responses short and punchy.";

console.log('Neural Link Configured.');
