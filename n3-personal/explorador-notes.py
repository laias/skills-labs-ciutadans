import os
from datetime import datetime

base = "/Users/laia/Library/CloudStorage/GoogleDrive-laia.sanchez@gmail.com/My Drive/Notes"
output_file = base + "/_mapa-vault.md"

lines = []
lines.append(f"# Mapa de la Vault\n")
lines.append(f"_Generat: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n\n")

for root, dirs, files in os.walk(base):
    level = root.replace(base, "").count(os.sep)
    indent = "  " * level
    lines.append(f"{indent}- **{os.path.basename(root)}/**\n")
    for file in files:
        if file.endswith(".md"):
            lines.append(f"{indent}  - {file}\n")

with open(output_file, "w") as f:
    f.writelines(lines)

print(f"Mapa guardat a {output_file}")