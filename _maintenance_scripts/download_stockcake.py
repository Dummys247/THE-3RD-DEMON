import cloudscraper
import shutil
import time

# Stockcake URL provided by user
url = "https://images.stockcake.com/public/e/5/6/e56df045-18fa-4905-8e84-144da0218b9a/magnified-cyber-eye-stockcake.jpg"
output_file = "assets/omni_vision_final.jpg"

print(f"Attempting to bypass Cloudflare and download from {url}...")

try:
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url, stream=True)
    
    if response.status_code == 200:
        with open(output_file, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        print(f"Successfully downloaded to {output_file}")
        
        # Verify header
        with open(output_file, 'rb') as f:
            header = f.read(10)
            print(f"Header: {header}")
            if header.startswith(b'\xff\xd8'):
                print("VERIFIED: Valid JPEG header.")
            else:
                print(f"WARNING: Header looks like {header}")
    else:
        print(f"Failed to download. Status code: {response.status_code}")
        print(f"Response snippet: {response.text[:200]}")
except Exception as e:
    print(f"Error: {e}")
