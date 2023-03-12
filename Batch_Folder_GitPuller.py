import os
import subprocess

for root, dirs, files in os.walk('.'):
    for d in dirs:
        path = os.path.join(root, d)
        if os.path.isdir(path):
            cmd = ["git", "-C", path, "pull"]
            subprocess.run(cmd)
            dirs.remove(d)  # Stop os.walk from recursing into deeper directories