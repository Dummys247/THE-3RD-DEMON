(function() {
    // Configuration
    const STATUS_URL = 'assets/status.json';
    const POLL_INTERVAL = 30000; // 30 seconds
    const RETRY_DELAY = 5000; // 5 seconds
    
    // Determine current mode from meta tag
    function getCurrentMode() {
        const meta = document.querySelector('meta[name="maintenance-mode"]');
        return meta ? meta.getAttribute('content') === 'true' : false;
    }

    // UI Helper: Create/Update Banner
    function showBanner(message, type) {
        let banner = document.getElementById('maintenance-banner');
        if (!banner) {
            banner = document.createElement('div');
            banner.id = 'maintenance-banner';
            Object.assign(banner.style, {
                position: 'fixed',
                top: '0',
                left: '0',
                width: '100%',
                padding: '10px',
                textAlign: 'center',
                zIndex: '9999',
                fontFamily: 'system-ui, sans-serif',
                fontWeight: 'bold',
                boxShadow: '0 2px 4px rgba(0,0,0,0.2)',
                transition: 'transform 0.3s ease'
            });
            document.body.prepend(banner);
        }

        if (type === 'warning') {
            banner.style.backgroundColor = '#f59e0b';
            banner.style.color = '#000';
            banner.textContent = '⚠️ ' + message;
        } else if (type === 'error') {
            banner.style.backgroundColor = '#ef4444';
            banner.style.color = '#fff';
            banner.textContent = '❌ ' + message;
        }
    }

    async function checkStatus() {
        try {
            // Cache busting
            const url = `${STATUS_URL}?t=${new Date().getTime()}`;
            const response = await fetch(url);
            if (!response.ok) throw new Error('Status check failed');
            
            const data = await response.json();
            const currentMode = getCurrentMode();
            
            console.log(`[MaintenanceMonitor] Active: ${data.active}, Current: ${currentMode}`);

            if (data.active && !currentMode) {
                // Maintenance is active, but we are on normal page
                showBanner('Maintenance is starting. Saving your work...', 'warning');
                // Give user a moment, then reload to get maintenance page
                setTimeout(() => window.location.reload(), 5000);
            } else if (!data.active && currentMode) {
                // Maintenance is over, but we are on maintenance page
                console.log('Maintenance finished. Reloading...');
                window.location.reload();
            } else if (data.active && currentMode) {
                // We are on maintenance page, and maintenance is still active. 
                // Just update estimated time if available (optional)
            }
        } catch (e) {
            console.warn('[MaintenanceMonitor] Connection issue:', e);
        }
    }

    // Start Polling
    setInterval(checkStatus, POLL_INTERVAL);
    
    // Initial check
    checkStatus();
})();
