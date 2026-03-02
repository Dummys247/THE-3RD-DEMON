import requests
import shutil

# Unsplash image: A very abstract, blue digital/cybernetic eye (no face, highly mechanical look)
url = "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?ixlib=rb-1.2.1&auto=format&fit=crop&w=1080&q=80"
output_file = "assets/omni_vision_final.jpg"

print(f"Downloading image from {url}...")
try:
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(output_file, 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
        print(f"Successfully downloaded to {output_file}")
        
        # Verify header
        with open(output_file, 'rb') as f:
            header = f.read(10)
            if header.startswith(b'\xff\xd8'):
                print("VERIFIED: Valid JPEG header.")
            else:
                print(f"WARNING: Header looks like {header}")
    else:
        print(f"Failed to download. Status code: {response.status_code}")
except Exception as e:
    print(f"Error: {e}")
