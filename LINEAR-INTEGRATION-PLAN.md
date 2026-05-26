# 📋 Plano de Integração: GitHub → Linear

## Status Atual
- **GitHub**: `bekaa-trusted-advisors/TWYN-ISO27001` - 15 issues criadas
- **Linear**: Projeto "Aegis Compliance" (https://linear.app/bekaa/project/aegis-compliance-1218ffb6780f)

## Opções de Integração

### Opção A: Sincronização Automática (Linear ↔ GitHub)
**Setup**:
1. Linear Settings → Integrations → GitHub
2. Connect repository: `bekaa-trusted-advisors/TWYN-ISO27001`
3. Configure bidirectional sync:
   - GitHub Issue → Linear Issue (automatic)
   - Labels → Status mapping
   - Assignees → Members mapping

**Vantagens**:
- ✅ Sync automático em tempo real
- ✅ Comentários sincronizados
- ✅ Status updates refletidos em ambos

**Desvantagens**:
- ⚠️ Pode criar duplicatas se issues já existem
- ⚠️ Requires Linear admin access

---

### Opção B: Migração Manual (GitHub → Linear) ⭐ RECOMENDADO
**Process**:
1. **Criar estrutura em Linear**:
   - Project: "ISO 27001 Certification"
   - Teams: Compliance, DevOps, Management
   - Labels: critical, high, medium, gap, sop, ftr-blocker
   - Custom fields: ISO Control, Due Date, Effort

2. **Importar issues via Linear CSV**:
```csv
Title,Description,Status,Priority,Labels,Assignee,Due Date,Estimate
GAP-001: Enable MFA on AWS root account,"[GitHub issue body]",Todo,Urgent,"gap,critical,car-001",DevOps Lead,2026-06-01,1h
GAP-002: Rotate IAM key...
```

3. **Ou usar Linear API** (script automation):
```bash
# Exemplo com Linear API
for issue in $(gh issue list --repo bekaa-trusted-advisors/TWYN-ISO27001 --json number,title,body,labels); do
  curl -X POST https://api.linear.app/graphql \
    -H "Authorization: $LINEAR_API_KEY" \
    -d "mutation { issueCreate(input: {...}) }"
done
```

**Vantagens**:
- ✅ Full control sobre estrutura
- ✅ Pode customizar campos Linear
- ✅ Evita duplicatas

---

### Opção C: Linear como Primary, GitHub como Documentation
**Strategy**:
- **Linear**: Issue tracking, project management, sprints
- **GitHub**: Documentation repository, code, policies

**Workflow**:
1. Criar todas issues em Linear (Aegis Compliance project)
2. GitHub mantém apenas:
   - Documentação ISO 27001 (14 docs + policies + SOPs)
   - Implementation guides
   - Evidence artifacts
3. Link Linear issues → GitHub docs via URL

**Vantagens**:
- ✅ Melhor UX para project management (Linear > GitHub Projects)
- ✅ GitHub foca em documentação (strengths)
- ✅ Separação clara: tracking vs. documentation

---

## Estrutura Recomendada em Linear

### Projects
- **Aegis Compliance** (já existe)
  - Subprojects:
    - Phase 1: Technical Gaps (GAP-001 to GAP-008)
    - Phase 2: AWS FTR Blockers
    - Phase 3: Procedures & Policies (SOPs)
    - Phase 4: Certification Prep (Auditor, Training)

### Issue Types
- 🔴 **Gap**: Implementation gap (GAP-001 to GAP-008)
- 📝 **SOP**: Standard Operating Procedure (SOP-001 to SOP-005)
- 🎯 **Milestone**: Major deliverable (CERT-001, TRAIN-001)
- 🚨 **Blocker**: Blocks certification (CEO signature, CARs)

### Priorities
- **Urgent**: P0 - CRITICAL blockers (MFA, CEO signature)
- **High**: P1 - FTR blockers, HIGH risks
- **Medium**: P2 - SOPs, training
- **Low**: P3 - Nice-to-have improvements

### Labels
- `iso-27001` - All issues
- `critical`, `high`, `medium`, `low` - Severity
- `ftr-blocker` - AWS FTR dependency
- `car-001`, `car-002`, `car-003`, `car-004` - Corrective Actions
- `devops`, `management`, `policy`, `training` - Category
- `q2-2026`, `q3-2026` - Timeline

### Custom Fields
1. **ISO Control**: A.5.15, A.5.17, etc. (for traceability)
2. **Due Date**: Target completion
3. **Effort**: Hours estimated
4. **Owner**: Gestor SGSI, DevOps Lead, CEO
5. **Status**: Backlog → In Progress → In Review → Done → Blocked

---

## Mapeamento GitHub Issues → Linear

| GitHub Issue | Linear Title | Priority | Labels | Assignee | Due Date |
|--------------|--------------|----------|--------|----------|----------|
| #1 GAP-001 | Enable MFA on AWS root | Urgent | gap, critical, car-001 | DevOps Lead | 2026-06-01 |
| #2 GAP-002 | Rotate IAM key >90d | High | gap, ftr-blocker, car-002 | DevOps Lead | 2026-06-08 |
| #3 GAP-003 | AWS Config + CIS | Urgent | gap, critical, ftr-blocker | DevOps Lead | 2026-06-08 |
| #4 GAP-004 | Backup testing | High | gap, ftr-blocker, car-004 | DevOps Lead | 2026-06-05 |
| #5 GAP-005 | AWS Support decision | High | gap, ftr-blocker, decision | CEO | 2026-06-05 |
| #6 GAP-006 | CEO signature IS Policy | Urgent | gap, blocker, critical | Gestor SGSI | 2026-06-02 |
| #7 GAP-007 | ISO cert for Ricardo | Medium | gap, training | Gestor SGSI | 2026-07-01 |
| #8 GAP-008 | Hire Junior DevOps | Medium | gap, people, spof | CEO | 2026-08-31 |
| #9 SOP-001 | Onboarding/Offboarding | Medium | sop, procedure | Gestor SGSI | 2026-06-15 |
| #10 SOP-002 | Change Management | Medium | sop, procedure, devops | DevOps Lead | 2026-06-20 |
| #11 SOP-003 | Remote Work Security | Medium | sop, procedure | Gestor SGSI | 2026-06-25 |
| #12 SOP-004 | Secrets Management | Medium | sop, procedure, devops | DevOps Lead | 2026-06-30 |
| #13 SOP-005 | IAM Recertification | Medium | sop, procedure | DevOps Lead | 2026-07-05 |
| #14 CERT-001 | Contract ISO auditor | High | certification, budget | Gestor SGSI | 2026-06-30 |
| #15 TRAIN-001 | Training platform | Medium | training, competence | Gestor SGSI | 2026-07-31 |

---

## Scripts de Automação

### 1. Export GitHub Issues to CSV (para importar em Linear)
```bash
#!/bin/bash
gh issue list \
  --repo bekaa-trusted-advisors/TWYN-ISO27001 \
  --json number,title,body,labels,assignees \
  --jq '.[] | [.number, .title, .body, (.labels | map(.name) | join(",")), (.assignees | map(.login) | join(","))] | @csv' \
  > github-issues.csv
```

### 2. Create Linear Issues via API
```python
import requests
import json

LINEAR_API_KEY = "lin_api_xxxxx"  # Get from Linear Settings → API
TEAM_ID = "bekaa-team-id"  # Get from Linear team settings

headers = {
    "Authorization": LINEAR_API_KEY,
    "Content-Type": "application/json"
}

# Example: Create GAP-001 in Linear
mutation = """
mutation IssueCreate {
  issueCreate(input: {
    teamId: "%s"
    title: "GAP-001: Enable MFA on AWS root account"
    description: "See GitHub: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/issues/1"
    priority: 1
    labelIds: ["critical-label-id", "gap-label-id"]
  }) {
    success
    issue {
      id
      url
    }
  }
}
""" % TEAM_ID

response = requests.post(
    "https://api.linear.app/graphql",
    headers=headers,
    json={"query": mutation}
)
print(response.json())
```

---

## Decisão Necessária

**Ricardo, escolha uma opção**:

1. **"opção A"** → Sync automático GitHub ↔ Linear (requires admin access)
2. **"opção B"** → Migração manual ou script (eu preparo CSV/script)
3. **"opção C"** → Linear como primary (criar issues lá, GitHub só docs)
4. **"manter GitHub"** → Não integrar, usar GitHub Projects apenas

**Recomendo Opção C** para melhor UX de project management.

---

## Próximos Passos (Se escolher Opção B ou C)

1. **Você**: Me dá Linear API key (Settings → API)
2. **Eu**: Crio script de migração automatizado
3. **Executo**: Cria todas 15 issues em Linear com labels/priorities
4. **Valida**: Você revisa em Linear e ajusta
5. **Documenta**: Link Linear → GitHub nos READMEs

**ETA**: 30 minutos (script + migration + validation)

---

Preparado por: Consultor ISO 27001 (Bekaa)
Data: 2026-05-26
