import requests
import os

# Wikimedia Commons - High quality eye close-up (Reliable, no 403 blocks)
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Eye_iris.jpg/800px-Eye_iris.jpg"
output = "assets/cyber_eye.jpg"

try:
    headers = {'User-Agent': 'Python/3.9'}
    print(f"Downloading from: {url}")
    r = requests.get(url, headers=headers, timeout=15)
    
    if r.status_code == 200:
        with open(output, 'wb') as f:
            f.write(r.content)
        print(f"Success: Downloaded {os.path.getsize(output)} bytes.")
    else:
        print(f"Failed: HTTP {r.status_code}")
        
except Exception as e:
    print(f"Error: {e}")
