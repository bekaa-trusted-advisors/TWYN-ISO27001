import os

docs_dir = r"\\wsl.localhost\Ubuntu\home\resper\twyn-ISO27001\docs"
missing_frontmatter = []

required_keys = ["document_id:", "title:", "version:", "date:"]

for root, _, files in os.walk(docs_dir):
    for f in files:
        if f.endswith(".md"):
            path = os.path.join(root, f)
            with open(path, "r", encoding="utf-8") as file:
                content = file.read()
            
            missing_keys = []
            for key in required_keys:
                if key not in content:
                    missing_keys.append(key)
            
            if missing_keys:
                missing_frontmatter.append((f, missing_keys))

if not missing_frontmatter:
    print("All documents in docs/ are fully normalized with required frontmatter.")
else:
    print("The following documents are missing standard frontmatter keys:")
    for f, keys in missing_frontmatter:
        print(f" - {f}: missing {keys}")
