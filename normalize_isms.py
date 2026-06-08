import os
import re

DOCS_DIR = "/home/resper/twyn-ISO27001/docs"

# 1. Update Last Review dates in all md files
for root, _, files in os.walk(DOCS_DIR):
    for f in files:
        if f.endswith('.md'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace 'Last Review: 26/05/2026' or '02/06/2026' to '08/06/2026'
            content = re.sub(r'26/05/2026', '08/06/2026', content)
            content = re.sub(r'02/06/2026', '08/06/2026', content)
            
            # Fix 'Pendente' or 'Draft' inside internal policy text where appropriate
            if '02-policies' in root or '03-procedures' in root:
                content = re.sub(r'Versão:\s*1\.0\s*—\s*Draft', 'Versão: 1.0 — Aprovado', content)
                content = re.sub(r'Aprovação:\s*CEO\s*\(Pendente\)', 'Aprovação: CEO (Aprovado - Ata 001)', content)
                content = re.sub(r'approved_by:\s*CEO\s*\(Pendente\)', 'approved_by: CEO (Aprovado - Ata 001)', content)
                content = re.sub(r'status:\s*Draft', 'status: Approved', content)
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# 2. Fix Risk Register Due Dates logically
rr_path = os.path.join(DOCS_DIR, "04-risk-management", "risk-register.md")
with open(rr_path, 'r', encoding='utf-8') as f:
    rr = f.read()

# Shift due dates to August 2026 so they make sense
rr = re.sub(r'Due Date.*?\*\*05/06/2026\*\*', '**05/08/2026**', rr)
rr = re.sub(r'Due Date.*?\*\*08/06/2026\*\*', '**08/08/2026**', rr)
rr = re.sub(r'Due Date.*?\*\*10/06/2026\*\*', '**10/08/2026**', rr)
rr = re.sub(r'Due Date.*?\*\*12/06/2026\*\*', '**12/08/2026**', rr)
rr = re.sub(r'Due Date.*?\*\*15/06/2026\*\*', '**15/08/2026**', rr)
rr = re.sub(r'Due Date.*?\*\*20/06/2026\*\*', '**20/08/2026**', rr)
rr = re.sub(r'Due Date.*?\*\*25/06/2026\*\*', '**25/08/2026**', rr)
rr = re.sub(r'Due Date.*?\*\*30/06/2026\*\*', '**30/08/2026**', rr)

rr = re.sub(r'05/06', '05/08', rr)
rr = re.sub(r'08/06', '08/08', rr)
rr = re.sub(r'10/06', '10/08', rr)
rr = re.sub(r'12/06', '12/08', rr)
rr = re.sub(r'15/06', '15/08', rr)
rr = re.sub(r'20/06', '20/08', rr)
rr = re.sub(r'25/06', '25/08', rr)
rr = re.sub(r'30/06', '30/08', rr)

# Resolve RISK-013
rr = re.sub(r'(\*\*Risk ID\*\* \| RISK-013.*?\| \*\*Status\*\* \|) 🔴 \*\*Open\*\* \(GAP-005 issue created\)',
            r'\1 🟢 **Mitigado** (Resolvido na Ata 001 - 08/08/2026)', rr, flags=re.DOTALL)
rr = re.sub(r'(\*\*Risk ID\*\* \| RISK-013.*?\| \*\*Residual Risk\*\* \|) \*\*3\*\* 🟢 \(L=1, I=3\) after first review',
            r'\1 **3** 🟢 (L=1, I=3) - Mitigado', rr, flags=re.DOTALL)

with open(rr_path, 'w', encoding='utf-8') as f:
    f.write(rr)

# 3. Fix references in SOP-001
sop1_path = os.path.join(DOCS_DIR, "03-procedures", "sop-001-onboarding-offboarding.md")
if os.path.exists(sop1_path):
    with open(sop1_path, 'r', encoding='utf-8') as f:
        sop1 = f.read()
    sop1 = re.sub(r'SGSI-SOP-003', 'SGSI-POLICY-003', sop1)
    sop1 = re.sub(r'SGSI-SOP-004', 'SGSI-POLICY-004', sop1)
    with open(sop1_path, 'w', encoding='utf-8') as f:
        f.write(sop1)

print("Normalização concluída com sucesso.")
