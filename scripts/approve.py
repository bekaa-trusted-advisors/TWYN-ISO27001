import os
import re
from datetime import datetime

docs_dir = r"\\wsl.localhost\Ubuntu\home\resper\twyn-ISO27001\docs"
count = 0

for root, dirs, files in os.walk(docs_dir):
    for file in files:
        if file.endswith(".md"):
            filepath = os.path.join(root, file)
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
                
            if "approved_by: CEO (Pendente)" in content:
                content = content.replace("approved_by: CEO (Pendente)", "approved_by: CEO (Aprovado - Ata 001)")
                content = re.sub(r"date: \d{4}-\d{2}-\d{2}", "date: 2026-06-02", content)
                
                with open(filepath, "w", encoding="utf-8", newline='\n') as f:
                    f.write(content)
                count += 1
                print(f"Updated: {file}")

print(f"Total files updated: {count}")
