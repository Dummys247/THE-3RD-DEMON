
import os
import requests
import sys
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading

ADS_FILE = "ads.txt"
EXPECTED_ID = "pub-9583919966792475"
PORT = 8081

def start_server():
    server_address = ('', PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    httpd.serve_forever()

def verify_ads_txt():
    print(f"[*] Verifying {ADS_FILE}...")
    
    if not os.path.exists(ADS_FILE):
        print(f"[ERROR] {ADS_FILE} not found!")
        return False
        
    with open(ADS_FILE, "r") as f:
        content = f.read()
        
    print(f"[*] Content: {content.strip()}")
    
    if EXPECTED_ID not in content:
        print(f"[ERROR] Expected ID {EXPECTED_ID} not found in {ADS_FILE}!")
        return False
        
    print(f"[SUCCESS] {ADS_FILE} contains correct Publisher ID.")
    return True

def test_http_access():
    print("[*] Testing HTTP access...")
    # Start server in background
    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()
    time.sleep(2) # Wait for server start
    
    try:
        response = requests.get(f"http://localhost:{PORT}/{ADS_FILE}")
        if response.status_code == 200:
            if EXPECTED_ID in response.text:
                print(f"[SUCCESS] {ADS_FILE} is accessible via HTTP and content matches.")
                return True
            else:
                print(f"[ERROR] {ADS_FILE} accessible but content mismatch via HTTP.")
                return False
        else:
            print(f"[ERROR] Failed to access {ADS_FILE} via HTTP. Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"[ERROR] HTTP Request failed: {e}")
        return False

if __name__ == "__main__":
    if verify_ads_txt():
        if test_http_access():
            print("\n[ALL CHECKS PASSED] ads.txt is correctly configured and deployable.")
            sys.exit(0)
        else:
            sys.exit(1)
    else:
        sys.exit(1)
