import os
import re

# Configuration
PUB_ID = "ca-pub-9583919966792475"
ADS_TXT_CONTENT = "google.com, pub-9583919966792475, DIRECT, f08c47fec0942fa0"
TARGET_DIR = os.getcwd()

def fix_ads_txt():
    """Ensures ads.txt exists and has the correct publisher ID."""
    ads_txt_path = os.path.join(TARGET_DIR, "ads.txt")
    print(f"[*] Checking {ads_txt_path}...")
    
    if os.path.exists(ads_txt_path):
        with open(ads_txt_path, 'r') as f:
            content = f.read().strip()
        if "pub-9583919966792475" not in content:
            print("[!] Incorrect ads.txt found. Updating...")
            with open(ads_txt_path, 'w') as f:
                f.write(ADS_TXT_CONTENT)
        else:
            print("[OK] ads.txt is valid.")
    else:
        print("[!] ads.txt missing. Creating...")
        with open(ads_txt_path, 'w') as f:
            f.write(ADS_TXT_CONTENT)

def fix_html_files():
    """Scans all HTML files to ensure Auto Ads are enabled and clean up placeholders."""
    # The Auto Ads script to inject
    auto_ads_script = f'''
    <!-- GOOGLE ADSENSE AUTO ADS -->
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={PUB_ID}"
     crossorigin="anonymous"></script>
    '''
    
    for root, dirs, files in os.walk(TARGET_DIR):
        if ".git" in root or "site-export" in root:
            continue
            
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                print(f"[*] Scanning {file}...")
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # 1. Ensure Auto Ads script is present in <head>
                if "adsbygoogle.js" not in content and "</head>" in content:
                    print(f"  [+] Injecting Auto Ads script into {file}")
                    content = content.replace("</head>", f"{auto_ads_script}\n</head>")
                
                # 2. Fix broken/placeholder manual slots
                # Pattern for common AdSense placeholders or empty ins tags
                # We replace specific broken manual slots if they use placeholders
                if "REPLACE_WITH_SLOT_ID" in content:
                    print(f"  [!] Found placeholder IDs in {file}. Removing broken manual unit to rely on Auto Ads.")
                    # Regex to remove the entire <ins> block containing the placeholder
                    content = re.sub(r'<ins class="adsbygoogle"[\s\S]*?REPLACE_WITH_SLOT_ID[\s\S]*?</ins>\s*<script>.*?</script>', 
                                     '<!-- AdSlot Removed: Using Auto Ads -->', content)
                
                # 3. Save if changed
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  [OK] Saved fixes for {file}")

def verify_privacy_policy():
    """Checks if privacy.html exists and mentions AdSense."""
    privacy_path = os.path.join(TARGET_DIR, "privacy.html")
    if not os.path.exists(privacy_path):
        print("[!] WARNING: privacy.html not found. AdSense requires a Privacy Policy.")
        return

    with open(privacy_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "Google" not in content or "cookie" not in content.lower():
        print("[!] WARNING: Privacy Policy may be missing required AdSense disclosures.")
    else:
        print("[OK] Privacy Policy appears to have required disclosures.")

if __name__ == "__main__":
    print("--- GOOGLE ADSENSE FIXER SCRIPT ---")
    fix_ads_txt()
    fix_html_files()
    verify_privacy_policy()
    print("\n[SUCCESS] AdSense configuration updated.")
    print("1. Auto Ads enabled on all pages.")
    print("2. ads.txt verified.")
    print("3. Broken manual slots removed.")
    print("NOTE: Changes need to be pushed to GitHub to take effect.")
