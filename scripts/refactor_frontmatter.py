import os
import re

repo_root = r"\\wsl.localhost\Ubuntu\home\resper\twyn-ISO27001"

# 1. Update docs/06-implementation-guides/
guides_dir = os.path.join(repo_root, "docs", "06-implementation-guides")
for f in os.listdir(guides_dir):
    if f.endswith(".md"):
        path = os.path.join(guides_dir, f)
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        if "document_id: GUIDE-GAP-" in content:
            content = content.replace("document_id: GUIDE-GAP-", "document_id: SGSI-GAP-")
            with open(path, "w", encoding="utf-8", newline='\n') as file:
                file.write(content)
            print(f"Updated: {f}")

# 2. Update docs/07-audit-templates/
tmpl_dir = os.path.join(repo_root, "docs", "07-audit-templates")
for f in os.listdir(tmpl_dir):
    if f.endswith(".md"):
        path = os.path.join(tmpl_dir, f)
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        if "document_id: TEMPLATE-AUDIT-" in content:
            content = content.replace("document_id: TEMPLATE-AUDIT-", "document_id: SGSI-TMPL-")
            with open(path, "w", encoding="utf-8", newline='\n') as file:
                file.write(content)
            print(f"Updated: {f}")

# 3. Prepend frontmatter to docs/08-architecture/
arc_dir = os.path.join(repo_root, "docs", "08-architecture")
arc_files = {"arc42.md": "SGSI-ARC-001", "c4-components.md": "SGSI-ARC-002"}
for f, doc_id in arc_files.items():
    path = os.path.join(arc_dir, f)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        if not content.startswith("---"):
            frontmatter = f"---\ndocument_id: {doc_id}\ntitle: {f.replace('.md', '')}\nversion: 1.0\ndate: 2026-06-03\nowner: Gestor SGSI\n---\n\n"
            content = frontmatter + content
            with open(path, "w", encoding="utf-8", newline='\n') as file:
                file.write(content)
            print(f"Prepended frontmatter to: {f}")
