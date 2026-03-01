import os
import re
from datetime import datetime

# Configuration
SITE_URL = "https://the3rddemon.com"
SITE_NAME = "The 3rd Demon"
SITE_DESCRIPTION = "The 3rd Demon is an advanced AI entity and digital experience. Download the official neural interface, explore the lore, and join the hive mind."
KEYWORDS = "The 3rd Demon, AI entity, digital horror, neural interface, download game, ARG, artificial intelligence, hive mind"
TARGET_DIR = os.getcwd()

def generate_sitemap():
    """Generates a clean sitemap.xml for the custom domain."""
    print("[*] Generating sitemap.xml...")
    sitemap_content = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_content += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for root, dirs, files in os.walk(TARGET_DIR):
        if ".git" in root or "site-export" in root:
            continue
            
        for file in files:
            if file.endswith(".html"):
                # Calculate relative path and URL
                rel_path = os.path.relpath(os.path.join(root, file), TARGET_DIR)
                if rel_path == "index.html":
                    url = SITE_URL + "/"
                    priority = "1.0"
                else:
                    url = SITE_URL + "/" + rel_path.replace("\\", "/")
                    priority = "0.8"
                
                # Get last modified date
                last_mod = datetime.now().strftime("%Y-%m-%d")
                
                sitemap_content += f'  <url>\n'
                sitemap_content += f'    <loc>{url}</loc>\n'
                sitemap_content += f'    <lastmod>{last_mod}</lastmod>\n'
                sitemap_content += f'    <changefreq>weekly</changefreq>\n'
                sitemap_content += f'    <priority>{priority}</priority>\n'
                sitemap_content += f'  </url>\n'

    sitemap_content += '</urlset>'
    
    with open("sitemap.xml", "w", encoding="utf-8") as f:
        f.write(sitemap_content)
    print("[OK] sitemap.xml created.")

def generate_robots():
    """Generates robots.txt pointing to the correct sitemap."""
    print("[*] Generating robots.txt...")
    content = f"User-agent: *\nAllow: /\nSitemap: {SITE_URL}/sitemap.xml\n"
    with open("robots.txt", "w", encoding="utf-8") as f:
        f.write(content)
    print("[OK] robots.txt created.")

def optimize_html_files():
    """Injects optimized SEO meta tags and Schema.org markup into HTML files."""
    
    # JSON-LD Schema Markup (Structured Data)
    schema_markup = f'''
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "SoftwareApplication",
      "name": "{SITE_NAME}",
      "applicationCategory": "GameApplication",
      "operatingSystem": "Windows",
      "offers": {{
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "USD"
      }},
      "description": "{SITE_DESCRIPTION}"
    }}
    </script>
    '''

    for root, dirs, files in os.walk(TARGET_DIR):
        if ".git" in root or "site-export" in root:
            continue
            
        for file in files:
            if file.endswith(".html"):
                file_path = os.path.join(root, file)
                print(f"[*] Optimizing {file}...")
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # 1. Update Canonical URL
                if '<link rel="canonical"' in content:
                    content = re.sub(r'<link rel="canonical" href=".*?" />', f'<link rel="canonical" href="{SITE_URL}/" />', content)
                else:
                    content = content.replace("</head>", f'<link rel="canonical" href="{SITE_URL}/" />\n</head>')

                # 2. Update/Inject Description
                if '<meta name="description"' in content:
                    # Update existing
                    content = re.sub(r'<meta name="description" content=".*?"', f'<meta name="description" content="{SITE_DESCRIPTION}"', content)
                else:
                    # Inject
                    content = content.replace("<head>", f'<head>\n    <meta name="description" content="{SITE_DESCRIPTION}">')

                # 3. Update/Inject Keywords
                if '<meta name="keywords"' in content:
                    content = re.sub(r'<meta name="keywords" content=".*?"', f'<meta name="keywords" content="{KEYWORDS}"', content)
                else:
                    content = content.replace("<head>", f'<head>\n    <meta name="keywords" content="{KEYWORDS}">')

                # 4. Inject Schema Markup (if not present)
                if "application/ld+json" not in content:
                    content = content.replace("</head>", f"{schema_markup}\n</head>")

                # 5. Fix Image URLs in Open Graph (make absolute)
                content = content.replace('content="assets/', f'content="{SITE_URL}/assets/')
                content = content.replace('href="assets/', f'href="{SITE_URL}/assets/')
                
                # Save if changed
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"  [OK] Optimized {file}")

if __name__ == "__main__":
    print("--- SEO OPTIMIZER SCRIPT ---")
    generate_sitemap()
    generate_robots()
    optimize_html_files()
    print("\n[SUCCESS] SEO configuration updated.")
    print("1. Sitemap generated for the3rddemon.com")
    print("2. Robots.txt updated.")
    print("3. Meta tags and Schema.org markup injected.")
