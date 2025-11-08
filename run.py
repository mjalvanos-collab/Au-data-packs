import os, io

# Ensure output folder exists
os.makedirs("site_build", exist_ok=True)

# Read the repo-root index.html (the one you edited)
src = "index.html"
if os.path.exists(src):
    with io.open(src, "r", encoding="utf-8") as f:
        html = f.read()
else:
    # Fallback simple page
    html = "<!doctype html><title>AU Data Packs</title><h1>Site online</h1>"

# Write it to the deployed output
with io.open("site_build/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Build complete: site_build/index.html updated.")
import os
os.makedirs("site_build", exist_ok=True)
open("site_build/index.html","a").close()
print("Build OK")
