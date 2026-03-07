import os
import shutil

SOURCE_DIR = "C:\\Users\\Lenovo\\Desktop\\trea projects\\Hyperinversion LTD\\site-export"
DEST_DIR = "."

# ONLY these extensions/files are allowed for Version A
ALLOWED_EXTENSIONS = [".html", ".js", ".css", ".json", ".txt", ".ico", ".png", ".jpg", ".jpeg", ".xml", ".webmanifest"]
ALLOWED_FOLDERS = ["assets", "js", "css", ".well-known"]

print(f"[*] RESTORING VERSION A (Generic Site) from {SOURCE_DIR} -> {DEST_DIR}")

if not os.path.exists(SOURCE_DIR):
    print(f"[!] Source not found.")
    exit(1)

# First, clean the destination of potential App files (Version B artifacts)
APP_FILES_TO_REMOVE = ["app.js", "style.css", "main.py", "backend", "frontend"]
for f in APP_FILES_TO_REMOVE:
    if os.path.exists(f):
        if os.path.isdir(f):
            shutil.rmtree(f)
        else:
            os.remove(f)
        print(f"   [-] Removed App artifact: {f}")

copied_count = 0

for root, dirs, files in os.walk(SOURCE_DIR):
    rel_path = os.path.relpath(root, SOURCE_DIR)
    
    is_allowed_folder = False
    if rel_path == ".":
        is_allowed_folder = True
    else:
        first_part = rel_path.split(os.sep)[0]
        if first_part in ALLOWED_FOLDERS:
            is_allowed_folder = True
            
    if not is_allowed_folder:
        continue

    dest_root = os.path.join(DEST_DIR, rel_path)
    if not os.path.exists(dest_root):
        os.makedirs(dest_root)
        
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if ext in ALLOWED_EXTENSIONS or file in ["CNAME"]:
            src = os.path.join(root, file)
            dst = os.path.join(dest_root, file)
            try:
                shutil.copy2(src, dst)
                copied_count += 1
            except Exception as e:
                print(f"   [!] Error copying {file}: {e}")

print(f"[*] Version A Restored. {copied_count} files copied.")
