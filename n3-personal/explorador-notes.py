import os

base = "."
for root, dirs, files in os.walk(base):
    level = root.replace(base, "").count(os.sep)
    indent = "  " * level
    print(f"{indent}- {os.path.basename(root)}/")
    for file in files:
        if file.endswith(".md"):
            print(f"{indent}  📄 {file}")
