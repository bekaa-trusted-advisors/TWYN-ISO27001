# 🎯 Linear Setup Guide: Aegis Compliance Project (WOW Version)

**Objetivo**: Transformar o projeto Linear "Aegis Compliance" em um dashboard profissional e impressionante para gestão da certificação ISO 27001:2022.

**Timeline**: 2 horas (setup completo)

**URL do Projeto**: https://linear.app/bekaa/project/aegis-compliance-1218ffb6780f

---

## 📋 Checklist Executivo

- [ ] **Step 1**: Estrutura de labels e prioridades (10 min)
- [ ] **Step 2**: Custom fields criados (10 min)
- [ ] **Step 3**: Importar 15 issues do GitHub (30 min via CSV ou 15 min via API)
- [ ] **Step 4**: Views customizadas (Roadmap, By Priority, By Owner) (20 min)
- [ ] **Step 5**: Project milestones e timeline (15 min)
- [ ] **Step 6**: Dashboard setup (KPIs, progress tracking) (15 min)
- [ ] **Step 7**: Notifications e integrações (10 min)

**Total**: ~2 horas

---

## 🎨 Step 1: Labels & Priorities (10 min)

### 1.1 Acessar Linear Labels

1. Abrir: https://linear.app/bekaa/settings/labels
2. Ou: Settings → Teams → [Your Team] → Labels

### 1.2 Criar Labels (17 labels total)

**Categoria: Severity** (já existem critical, high, medium, low? Se sim, skip)
```
🔴 critical     - Cor: #FF0000 (red)
🟠 high         - Cor: #FF8800 (orange)
🟡 medium       - Cor: #FFCC00 (yellow)
🟢 low          - Cor: #00CC66 (green)
```

**Categoria: Type**
```
🔥 gap          - Cor: #E74C3C (vermelho escuro) - Implementation gaps
📝 sop          - Cor: #3498DB (azul) - Standard Operating Procedures
🚨 blocker      - Cor: #C0392B (vermelho sangue) - Certification blockers
🎯 milestone    - Cor: #9B59B6 (roxo) - Major deliverables
🏗️ infrastructure - Cor: #34495E (cinza escuro) - AWS/DevOps work
```

**Categoria: ISO Control**
```
🔐 iso-27001    - Cor: #2C3E50 (azul escuro) - Todos os issues
📊 ftr-blocker  - Cor: #E67E22 (laranja) - AWS FTR dependency
```

**Categoria: Corrective Actions (CARs)**
```
⚠️ car-001      - Cor: #D35400 (laranja escuro) - MFA root account
⚠️ car-002      - Cor: #D35400 - IAM key rotation
⚠️ car-003      - Cor: #D35400 - AWS Config/CIS
⚠️ car-004      - Cor: #D35400 - Backup testing
```

**Categoria: Teams**
```
👨‍💻 devops       - Cor: #16A085 (verde água)
📋 management   - Cor: #8E44AD (roxo)
📖 policy       - Cor: #2980B9 (azul)
🎓 training     - Cor: #F39C12 (dourado)
```

**Categoria: Timeline**
```
📅 q2-2026      - Cor: #27AE60 (verde)
📅 q3-2026      - Cor: #F1C40F (amarelo)
```

### 1.3 Priorities Mapping

Linear usa 4 níveis de prioridade (já existem por padrão):
- **Urgent** (P0) = 🔴 CRITICAL blockers (MFA, CEO signature, FTR)
- **High** (P1) = 🟠 FTR blockers, HIGH risks
- **Medium** (P2) = 🟡 SOPs, training, medium risks
- **Low** (P3) = 🟢 Nice-to-have improvements

---

## 🏗️ Step 2: Custom Fields (10 min)

### 2.1 Acessar Custom Fields

Settings → Teams → [Your Team] → Custom Fields → "New custom field"

### 2.2 Criar Custom Fields (5 fields)

#### Field 1: ISO Control
```
Type: Text (single line)
Name: ISO Control
Description: ISO 27001:2022 Annex A control (e.g., A.5.15, A.8.9)
```

#### Field 2: Due Date
```
Type: Date
Name: Due Date
Description: Target completion date
```

#### Field 3: Effort (Hours)
```
Type: Number
Name: Effort
Description: Estimated hours to complete
```

#### Field 4: Owner Role
```
Type: Select (single)
Name: Owner Role
Options:
  - DevOps Lead
  - Gestor SGSI
  - CEO
  - Dev Team
  - Auditor
```

#### Field 5: Status Detail
```
Type: Select (single)
Name: Status Detail
Options:
  - Backlog
  - In Progress
  - In Review
  - Blocked
  - Done
  - Won't Do
```

---

## 📥 Step 3: Importar Issues do GitHub (30 min via CSV)

### Opção A: Import via CSV (RECOMENDADO - mais controle)

#### 3.1 Usar CSV Pronto

Eu criei um CSV completo com todas as 15 issues mapeadas. Ver arquivo: `linear-import.csv`

#### 3.2 Importar no Linear

1. Abrir projeto: https://linear.app/bekaa/project/aegis-compliance-1218ffb6780f
2. No topo direito: "..." (menu) → "Import issues"
3. Upload `linear-import.csv`
4. Mapear colunas:
   - Title → Title
   - Description → Description
   - Priority → Priority
   - Labels → Labels
   - Assignee → Assignee
   - Due Date → Custom Field: Due Date
   - Estimate → Estimate (pontos ou horas)
5. Review preview → "Import X issues"

#### 3.3 Validar Import

Após import, verificar:
- [ ] 15 issues criados
- [ ] Labels aplicados corretamente
- [ ] Prioridades corretas (8 Urgent, 4 High, 3 Medium)
- [ ] Assignees mapeados (DevOps Lead, Gestor SGSI, CEO)

---

### Opção B: Import via API (AVANÇADO - automated)

Se preferir automação completa via script Python, usar: `linear-migration.py`

```bash
# Setup
pip install requests python-dotenv

# Configurar .env
echo "LINEAR_API_KEY=lin_api_xxxxx" > .env
echo "LINEAR_TEAM_ID=bekaa-team-id" >> .env

# Executar migração
python linear-migration.py

# Output esperado:
# ✅ Created: GAP-001: Enable MFA on AWS root account (LIN-123)
# ✅ Created: GAP-002: Rotate IAM key >90d (LIN-124)
# ...
# ✅ 15/15 issues migrated successfully
```

---

## 📊 Step 4: Views Customizadas (20 min)

### 4.1 View 1: Roadmap (Timeline View)

1. No projeto Aegis Compliance → "Views" (topo) → "New view"
2. Nome: "🗓️ Roadmap to Certification"
3. Type: **Timeline** (Gantt-like)
4. Group by: **Milestone** ou **Quarter**
5. Show: Due Date custom field
6. Filtros:
   - Status: Not "Done"
   - Project: Aegis Compliance
7. Sort by: Due Date (ascending)

**Resultado**: Gantt chart visual mostrando todos os blockers e milestones até Q3 2026

---

### 4.2 View 2: By Priority (List View)

1. Views → New view
2. Nome: "🔥 By Priority"
3. Type: **List**
4. Group by: **Priority**
5. Show columns: Title, Assignee, Due Date, Labels, Estimate
6. Sort within groups: Due Date (ascending)
7. Filtros:
   - Status: Not "Done"
   - Project: Aegis Compliance

**Resultado**: 4 swimlanes (Urgent, High, Medium, Low) com issues organizados

---

### 4.3 View 3: By Owner (Board View)

1. Views → New view
2. Nome: "👤 By Owner"
3. Type: **Board**
4. Group by: **Assignee**
5. Columns: DevOps Lead, Gestor SGSI, CEO, Unassigned
6. Filtros:
   - Status: Not "Done"
   - Project: Aegis Compliance

**Resultado**: Kanban board por pessoa responsável

---

### 4.4 View 4: Critical Path (Custom Filter)

1. Views → New view
2. Nome: "⚠️ Critical Path (Blockers)"
3. Type: **List**
4. Filtros:
   - Priority: Urgent
   - Labels: Contains "blocker" OR "ftr-blocker"
   - Status: Not "Done"
5. Sort: Due Date (ascending)

**Resultado**: Only CRITICAL blockers (GAP-001, GAP-003, GAP-006, AWS FTR issues)

---

## 🎯 Step 5: Milestones & Timeline (15 min)

### 5.1 Criar Milestones

Projects → Aegis Compliance → "Milestones" tab → "New milestone"

#### Milestone 1: AWS FTR Resolution
```
Name: AWS FTR Unblocked
Target date: 2026-06-08
Description: Resolve 3 AWS FTR blockers (CIS controls, backup testing, support plan)
Issues: GAP-002, GAP-003, GAP-004, GAP-005 (4 issues)
```

#### Milestone 2: CEO Signature
```
Name: IS Policy Signed by CEO
Target date: 2026-06-02
Description: Information Security Policy formally approved and signed
Issues: GAP-006 (1 issue)
```

#### Milestone 3: Technical Gaps Closed
```
Name: All GAPs Implemented
Target date: 2026-07-01
Description: All 8 technical gaps (GAP-001 to GAP-008) resolved
Issues: GAP-001 to GAP-008 (8 issues)
```

#### Milestone 4: Procedures Documented
```
Name: SOPs Complete
Target date: 2026-07-05
Description: All 5 Standard Operating Procedures written and approved
Issues: SOP-001 to SOP-005 (5 issues)
```

#### Milestone 5: Certification Ready
```
Name: ISO 27001 Audit Ready
Target date: 2026-07-31
Description: All documentation complete, controls implemented, training done
Issues: CERT-001, TRAIN-001 (2 issues)
```

---

## 📈 Step 6: Dashboard & Progress Tracking (15 min)

### 6.1 Project Description (Hero Section)

Editar projeto Aegis Compliance → Description:

```markdown
# 🔐 ISO 27001:2022 Certification Programme

**Target**: Q3 2026 (Stage 2 audit: August 2026)
**Scope**: Face ID Platform API + AWS Infrastructure
**Budget**: €65-75k
**Gestor SGSI**: Ricardo Esper (resper@bekaa.eu)

---

## 📊 Current Status

- **Documentation**: 14/14 mandatory docs complete (100%) ✅
- **Annex A Controls**: 70% implemented (target: 85%)
- **Risks Identified**: 18 (3 CRITICAL, 6 HIGH, 7 MEDIUM, 2 LOW)
- **Open CARs**: 4 (all assigned, in progress)
- **AWS FTR Status**: 🔴 BLOCKED (3 controls to fix)

---

## 🚨 Critical Blockers (Must Fix This Week)

1. **GAP-006**: CEO signature on IS Policy (due: Jun 02)
2. **GAP-001**: Enable MFA on AWS root (due: Jun 01)
3. **GAP-003**: AWS Config + CIS controls (due: Jun 08) - FTR blocker

---

## 🎯 Milestones

- ✅ Documentation Complete (May 26) - DONE
- 🟡 AWS FTR Unblocked (Jun 08) - IN PROGRESS
- 🟡 All GAPs Closed (Jul 01)
- 🟡 SOPs Written (Jul 05)
- 🟡 Audit Ready (Jul 31)
- 🟢 Stage 1 Audit (Jul 31)
- 🟢 Stage 2 Audit (Aug 31)
- 🟢 Certification Issued (Sep 30)

---

## 📚 Resources

- [GitHub Repository](https://github.com/bekaa-trusted-advisors/TWYN-ISO27001)
- [Status Report](https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/blob/main/STATUS-REPORT-2026-05-26.md)
- [Training Program](https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/blob/main/TRAINING-PROGRAM.md)
- [Risk Register](https://github.com/bekaa-trusted-advisors/TWYN-ISO27001/blob/main/docs/04-risk-management/risk-register.md)
```

---

### 6.2 Progress Insights (Linear automatiza isso)

Linear automaticamente mostra:
- **Completion rate**: X/15 issues done (target: 100%)
- **Velocity**: Issues closed per week
- **Blocked issues**: Issues com status "Blocked"
- **Overdue issues**: Issues com due date passada

Para visualizar: Project → "Insights" tab

---

### 6.3 Custom KPIs (Optional - via Integrations)

Se quiser dashboards avançados, integrar com:
- **Notion** (embed Linear views em Notion dashboard)
- **Slack** (notifications para milestones completados)
- **GitHub** (link issues Linear ↔ GitHub PRs automaticamente)

---

## 🔔 Step 7: Notifications & Integrations (10 min)

### 7.1 GitHub Integration

1. Settings → Integrations → GitHub → "Connect"
2. Authorize: `bekaa-trusted-advisors` org
3. Select repo: `TWYN-ISO27001`
4. Enable:
   - ✅ Link issues via commit messages (e.g., "Fixes LIN-123")
   - ✅ Auto-close Linear issue quando PR é merged
   - ✅ Sync labels bidirecionalmente

**Uso**:
```bash
# Commit message auto-links to Linear
git commit -m "feat: enable MFA on root account

Fixes LIN-123 (GAP-001)
"
# Quando PR for merged → Linear issue LIN-123 fecha automaticamente
```

---

### 7.2 Slack Notifications (Optional)

1. Settings → Integrations → Slack → "Connect"
2. Select channel: `#iso27001-project` (criar se não existir)
3. Configure notifications:
   - ✅ Issue status changed (In Progress → Done)
   - ✅ Milestone completed
   - ✅ Overdue issues (daily digest)
   - ✅ High priority issues created

---

### 7.3 Email Digests

Settings → Notifications → "Daily digest"
- Enable: ✅ Daily summary email (8am)
- Include:
  - Overdue issues
  - Issues due this week
  - Blocked issues
  - Recently completed

---

## 🎨 Bonus: Visual Polish (10 min)

### Make It Look Amazing

1. **Project Icon**: Settings → Icon → escolher 🔐 (lock) ou 🛡️ (shield)
2. **Project Color**: Settings → Color → Azul escuro (#2C3E50) - matches ISO theme
3. **Cover Image** (optional): Settings → Cover → Upload imagem ISO 27001 logo ou security theme

---

## ✅ Final Checklist: Is Linear WOW?

- [ ] **17 labels** criados e coloridos
- [ ] **5 custom fields** configurados (ISO Control, Due Date, Effort, Owner, Status)
- [ ] **15 issues** importados do GitHub com labels e prioridades
- [ ] **4 custom views** criados (Roadmap, By Priority, By Owner, Critical Path)
- [ ] **5 milestones** definidos com target dates
- [ ] **Project description** impressionante (hero section)
- [ ] **GitHub integration** ativa (bidirectional sync)
- [ ] **Insights** visíveis (completion rate, velocity)
- [ ] **Notifications** configuradas (Slack ou email)
- [ ] **Visual polish** (icon, color, cover)

**Se todos checados → LINEAR IS WOW! 🚀**

---

## 📱 Quick Actions (Mobile/Desktop)

### Para visualizar progresso rapidamente:

1. **Desktop**: https://linear.app/bekaa/project/aegis-compliance-1218ffb6780f
2. **Mobile App**: Linear iOS/Android → Projects → Aegis Compliance
3. **Comando rápido**: `Cmd+K` (Mac) ou `Ctrl+K` (Windows) → "Aegis Compliance"

### Para criar issue rapidamente:

1. `Cmd+K` → "New issue"
2. Title: "[TYPE]-XXX: Description"
3. Project: Aegis Compliance
4. Priority: Urgent/High/Medium/Low
5. Labels: Add relevant (gap, sop, blocker, etc)
6. Assignee: DevOps Lead / Gestor SGSI / CEO
7. `Cmd+Enter` para criar

---

## 🔗 Links Importantes

- **Linear Project**: https://linear.app/bekaa/project/aegis-compliance-1218ffb6780f
- **GitHub Repo**: https://github.com/bekaa-trusted-advisors/TWYN-ISO27001
- **Linear API Docs**: https://developers.linear.app/docs/graphql/working-with-the-graphql-api
- **Linear CSV Import Guide**: https://linear.app/docs/import-from-csv

---

## 🆘 Troubleshooting

### Issue: Labels não aparecem no import
**Fix**: Criar labels ANTES de importar CSV. Labels devem ter nome exato (case-sensitive).

### Issue: Assignees não mapeiam
**Fix**: Assignee no CSV deve ser **email exato** da pessoa no Linear workspace.

### Issue: Custom fields não salvam
**Fix**: Criar custom fields ANTES de importar. CSV usa nome exato do field.

### Issue: GitHub integration não funciona
**Fix**: Verificar permissões GitHub App → precisa ter acesso ao repo `TWYN-ISO27001`.

---

**Prepared by**: Claude Code (Bekaa Trusted Advisors)
**Date**: 2026-05-26
**Version**: 1.0 (WOW Edition)

**Next Step**: Execute Steps 1-7 em sequência (~2h total) → LINEAR WILL BE WOW! 🎯
