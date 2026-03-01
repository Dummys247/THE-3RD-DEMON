import time
import requests
import hashlib
import webbrowser
import os

URL = "https://the3rddemon.com"
# We expect the "DEMON AI" version, so let's look for a unique string from that version
EXPECTED_STRING = "DEMON AI"

print(f"[*] Monitoring {URL} for '{EXPECTED_STRING}'...")

attempts = 0
while True:
    attempts += 1
    try:
        # Unique timestamp to bypass cache
        r = requests.get(f"{URL}?v={time.time()}", timeout=10)
        
        if r.status_code == 200:
            content = r.text
            if EXPECTED_STRING in content:
                print("\n[SUCCESS] The 'DEMON AI' version is LIVE!")
                print("   Found 'DEMON AI' in page title/content.")
                webbrowser.open(URL)
                break
            else:
                # Extract current title for debugging
                import re
                title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
                current_title = title_match.group(1) if title_match else "Unknown"
                print(f"\r[Attempt {attempts}] Still old version. (Title: '{current_title}') Waiting...", end="")
        else:
             print(f"\r[Attempt {attempts}] Site returned {r.status_code}. Waiting...", end="")
             
    except Exception as e:
        print(f"\r[Attempt {attempts}] Error: {e}", end="")
        
    time.sleep(5)
