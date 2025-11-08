
import os
os.makedirs("site_build", exist_ok=True)
open("site_build/index.html","a").close()
print("Build OK")
