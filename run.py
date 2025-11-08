import os, io, shutil

os.makedirs("site_build", exist_ok=True)

# Copy the homepage into the deploy folder
src = "index.html"
dst = "site_build/index.html"

if os.path.exists(src):
    shutil.copyfile(src, dst)
else:
    with io.open(dst, "w", encoding="utf-8") as f:
        f.write("<!doctype html><title>Fallback</title><h1>Hello from site_build</h1>")

print("Wrote:", dst)
