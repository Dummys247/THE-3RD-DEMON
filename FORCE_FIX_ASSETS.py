import os
import shutil
import re

# Paths
BASE_DIR = os.getcwd()
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
TARGET_LOGO = os.path.join(ASSETS_DIR, "demon_logo.png")

# Files to replace with the logo
TARGETS = [
    os.path.join(BASE_DIR, "favicon.ico"),
    os.path.join(ASSETS_DIR, "favicon-48x48.png"),
    os.path.join(ASSETS_DIR, "favicon-96x96.png"),
    os.path.join(ASSETS_DIR, "favicon-192x192.png"),
    os.path.join(ASSETS_DIR, "apple-touch-icon.png"),
    # Also check for any other potential favicon files
    os.path.join(ASSETS_DIR, "favicon.ico"), 
]

def fix_favicons():
    print(f"[*] Starting Favicon Fix Protocol...")
    
    if not os.path.exists(TARGET_LOGO):
        print(f"[!] ERROR: Source logo not found at {TARGET_LOGO}")
        return

    for target in TARGETS:
        try:
            shutil.copy2(TARGET_LOGO, target)
            print(f"  [+] Overwritten: {target}")
        except Exception as e:
            print(f"  [!] Failed to overwrite {target}: {e}")

def fix_html_links():
    print(f"[*] Fixing HTML Favicon Links...")
    
    # We want to replace absolute links with relative ones to avoid caching issues
    # and ensure local testing works.
    
    # Pattern to match: href="https://the3rddemon.com/assets/..."
    # Replacement: href="assets/..."
    
    files_to_check = [f for f in os.listdir(BASE_DIR) if f.endswith(".html")]
    
    for filename in files_to_check:
        filepath = os.path.join(BASE_DIR, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = content.replace('href="https://the3rddemon.com/assets/', 'href="assets/')
        
        # Also ensure favicon.ico is relative
        new_content = new_content.replace('href="/favicon.ico"', 'href="favicon.ico"')
        
        if content != new_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  [+] Updated links in: {filename}")
        else:
            print(f"  [.] No changes needed in: {filename}")

def update_generator_script():
    print(f"[*] Updating GENERATE_CONTENT.py template...")
    
    gen_script = os.path.join(BASE_DIR, "GENERATE_CONTENT.py")
    if os.path.exists(gen_script):
        with open(gen_script, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace the template string content
        new_content = content.replace('href="https://the3rddemon.com/assets/', 'href="assets/')
        
        if content != new_content:
            with open(gen_script, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  [+] Updated GENERATE_CONTENT.py")
        else:
            print(f"  [.] GENERATE_CONTENT.py already up to date")

if __name__ == "__main__":
    fix_favicons()
    fix_html_links()
    update_generator_script()
    print("[*] FIX COMPLETE. PLEASE CLEAR BROWSER CACHE.")
