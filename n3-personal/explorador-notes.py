import os
from datetime import datetime

base = "/Users/laia/Library/CloudStorage/GoogleDrive-laia.sanchez@gmail.com/My Drive/Notes"
output_file = base + "/_mapa-vault.md"

SKIP_DIRS = {'.obsidian', '.trash', '.space', '.makemd', 'Apple Notes Attachments', 'Imported Notes'}

lines = []
lines.append(f"# Mapa de la Vault\n")
lines.append(f"_Generat: {datetime.now().strftime('%Y-%m-%d %H:%M')}_\n\n")

for root, dirs, files in os.walk(base):
    dirs[:] = sorted([d for d in dirs if d not in SKIP_DIRS and not d.startswith('.')])
    
    level = root.replace(base, "").count(os.sep)
    indent = "  " * level
    
    md_files = [f for f in files if f.endswith(".md") and not f.startswith('_')]
    count = len(md_files)
    folder_name = os.path.basename(root)
    
    if folder_name.startswith('.'):
        continue
    
    lines.append(f"{indent}- **{folder_name}/** ({count} notes)\n")
    
    for file in sorted(md_files):
        lines.append(f"{indent}  - {file}\n")

with open(output_file, "w") as f:
    f.writelines(lines)

print(f"Mapa guardat a {output_file}")