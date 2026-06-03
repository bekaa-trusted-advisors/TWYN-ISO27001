---
**Document Control**
| Campo | Valor |
|-------|-------|
| **Document ID** | SGSI-RISK-001 |
| **Version** | 1.0 |
| **Author** | BEKAA Consultoria — Ricardo Esper |
| **Approved By** | Ricardo Esper (Bekaa Trusted Advisors) |
| **Approval Date** | [Pendente] |
| **Effective Date** | [Pendente] |
| **Próxima Revisão** | [Anual após aprovação] |
| **ISO 27001:2022 Mapping** | **Clause 6.1.2 — Information security risk assessment** |
---

# Risk Assessment Methodology
## Metodologia de Avaliação de Riscos de SI — TWYN SGSI

---

## 1. Propósito

Este documento define a **metodologia formal** utilizada pela TWYN para identificar, analisar e avaliar riscos de segurança da informação, em conformidade com **ISO/IEC 27001:2022 Clause 6.1.2**.

Esta metodologia garante uma abordagem **consistente, repetível e auditável** para avaliação de riscos.

---

## 2. Scope (Escopo)

Esta metodologia aplica-se a:
- ✅ Todos os ativos no escopo do SGSI (ver SGSI-SCOPE-001)
- ✅ Processos de negócio críticos
- ✅ Todos os ambientes (produção, staging)
- ✅ Fornecedores críticos com acesso a dados sensíveis

---

## 3. Risk Assessment Principles (Princípios)

### 3.1 Risk Definition

> **Risco** = Efeito da incerteza sobre os objetivos  
> **Risco de SI** = Probabilidade de uma ameaça explorar uma vulnerabilidade, causando impacto à informação (C-I-A)

### 3.2 Risk Formula

```
RISK SCORE = LIKELIHOOD × IMPACT
```

Ambos medidos em escala de **1 a 5**.

### 3.3 Risk Ownership

- Cada risco identificado **DEVE** ter um owner designado
- Owner é responsável por monitorar e gerenciar o risco
- Owner não precisa ser quem implementa os controles

---

## 4. Risk Assessment Process (Processo)

### 4.1 Process Overview

```
┌─────────────────┐
│ 1. Asset        │
│    Identification│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 2. Threat &     │
│    Vulnerability│
│    Identification│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 3. Risk         │
│    Analysis     │
│    (L × I)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 4. Risk         │
│    Evaluation   │
│    (Matrix)     │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ 5. Risk         │
│    Treatment    │
│    (RMAP)       │
└─────────────────┘
```

---

## 5. Step 1: Asset Identification (Identificação de Ativos)

### 5.1 Asset Categories

| Categoria | Examples | Classification |
|----------|----------|----------------|
| **Data** | Dados biométricos, código-fonte, logs, credentials | CRÍTICO / CONFIDENTIAL |
| **Applications** | Face ID API, pipelines CI/CD, admin dashboards | CRÍTICO / CONFIDENTIAL |
| **Infrastructure** | AWS accounts, EKS clusters, RDS databases, S3 buckets | CRÍTICO |
| **Hardware** | Workstations, laptops (remote work) | INTERNAL |
| **People** | DevOps team, developers, Gestor SGSI | N/A |
| **Services** | AWS, GitHub, DNS providers | CRÍTICO (dependency) |

### 5.2 Asset Attributes

Para cada ativo crítico, documentar:
- **Asset ID** (único)
- **Owner** (business owner)
- **Custodian** (technical owner)
- **Location** (AWS region, repo, etc.)
- **Classification** (CRÍTICO/CONFIDENTIAL/INTERNAL/PUBLIC)
- **CIA Rating**: 
  - Confidentiality: 1-5
  - Integrity: 1-5
  - Availability: 1-5

**Asset Inventory**: Mantido em **[SGSI-ASSETS-001]**

---

## 6. Step 2: Threat & Vulnerability Identification (Identificação de Ameaças e Vulnerabilidades)

### 6.1 Threat Categories (ISO 27005)

| Threat Type | Examples |
|-------------|----------|
| **Accidental** | Human error, misconfiguration, accidental deletion |
| **Environmental** | Fire, flood, power outage, AWS region failure |
| **Deliberate** | Hacking, malware, insider threat, DDoS |
| **Third-party** | Cloud provider breach, supply chain attack |

### 6.2 Threat Sources

| Source | Description |
|--------|-------------|
| **External Attackers** | Hackers, APT groups, script kiddies |
| **Insiders** | Disgruntled employees, negligent users |
| **Competitors** | Corporate espionage |
| **Nation-State** | Government-sponsored attacks |
| **Automated** | Bots, worms, ransomware |

### 6.3 Vulnerability Identification

**Methods**:
- ✅ **Automated scanning**: AWS Config, Security Hub, Trivy
- ✅ **Manual review**: Code reviews, architecture reviews
- ✅ **Penetration testing**: Annual or bi-annual
- ✅ **Threat intelligence**: AWS GuardDuty, public CVE databases

**Common vulnerabilities**:
- Unpatched software
- Weak authentication (no MFA)
- Excessive permissions (IAM)
- Unencrypted data
- Missing audit logs
- Single point of failure (no redundancy)

---

## 7. Step 3: Risk Analysis (Análise de Risco)

### 7.1 Likelihood Scale (Probabilidade)

| Level | Score | Description | Frequency |
|-------|-------|-------------|-----------|
| **Very Low** | 1 | Highly unlikely to occur | < 1x per 5 years |
| **Low** | 2 | Unlikely but possible | 1x per 2-5 years |
| **Medium** | 3 | May occur occasionally | 1x per year |
| **High** | 4 | Likely to occur | Multiple times per year |
| **Very High** | 5 | Almost certain to occur | Multiple times per month |

**Factors influencing Likelihood**:
- Threat capability vs. control strength
- Historical data (has it happened before?)
- Industry trends (common attack vectors)
- Attractiveness to attackers (high-value data = higher likelihood)

### 7.2 Impact Scale (Impacto)

| Level | Score | CIA Impact | Business Impact | Examples |
|-------|-------|------------|-----------------|----------|
| **Very Low** | 1 | Insignificant | < R$ 10k loss, no reputation damage | Non-critical internal doc leaked |
| **Low** | 2 | Minor | R$ 10k-50k, minor client concern | Temporary service degradation |
| **Medium** | 3 | Moderate | R$ 50k-250k, some clients affected | Data breach of non-sensitive info |
| **High** | 4 | Major | R$ 250k-1M, significant clients affected | Critical service outage > 4h |
| **Very High** | 5 | Critical | > R$ 1M, loss of key clients, legal action | Biometric data breach (LGPD violation) |

**Impact Categories** (assess each):
- **Confidentiality**: Unauthorized disclosure
- **Integrity**: Data corruption, unauthorized modification
- **Availability**: Service downtime, data loss
- **Financial**: Direct costs (fines, remediation)
- **Reputational**: Brand damage, client trust
- **Legal/Regulatory**: LGPD fines, lawsuits
- **Operational**: Business disruption

**Overall Impact** = **MAX**(C-impact, I-impact, A-impact, Financial, Reputational, Legal)

---

## 8. Step 4: Risk Evaluation (Avaliação de Risco)

### 8.1 Risk Matrix

```
IMPACT →
                 1        2        3        4        5
              (Very    (Low)   (Medium)  (High)  (Very
               Low)                               High)
         5    🟡 5    🟠 10   🔴 15   🔴 20   🔴 25   ← Very High
L        4    🟢 4    🟡 8    🟠 12   🔴 16   🔴 20
I        3    🟢 3    🟢 6    🟡 9    🟠 12   🔴 15
K        2    🟢 2    🟢 4    🟢 6    🟡 8    🟠 10
E        1    🟢 1    🟢 2    🟢 3    🟢 4    🟡 5    ← Very Low
L
I
H
O
O
D
↓
```

### 8.2 Risk Levels and Treatment Priority

| Pontuação de Risco | Risk Level | Color | Treatment Priority | Action |
|------------|------------|-------|-------------------|--------|
| **20-25** | CRÍTICO | 🔴 Red | **IMMEDIATE** | Must treat within 30 days |
| **12-19** | ALTO | 🟠 Orange | **ALTO** | Must treat within 90 days |
| **6-11** | MÉDIO | 🟡 Yellow | **MÉDIO** | Treat within 6 months |
| **3-5** | BAIXO | 🟢 Green | **BAIXO** | Monitor, treat if cost-effective |
| **1-2** | VERY BAIXO | 🟢 Green | **ACCEPT** | Document acceptance |

---

## 9. Risk Treatment Options (Opções de Tratamento)

### 9.1 Treatment Strategies

| Strategy | Description | When to Use | Examples |
|----------|-------------|-------------|----------|
| **MITIGATE** (Reduzir) | Implement controls to reduce L or I | Risk > Low and control is feasible | Enable MFA, encryption, firewalls |
| **ACCEPT** (Aceitar) | Accept residual risk | Risk = Low and cost > benefit | Rare edge cases, low-value assets |
| **AVOID** (Evitar) | Eliminate the activity causing risk | Risk = Critical and unmitigable | Don't process high-risk data, cancel risky project |
| **TRANSFER** (Transferir) | Share risk via insurance, SLA, outsource | Risk = specialized or high-cost | Cyber insurance, AWS BAA, third-party SOC |

### 9.2 Risk-Mitigation-Action Plan (RMAP)

For each **MITIGATE** decision, create RMAP entry:

| Campo | Description |
|-------|-------------|
| **Risk ID** | Unique identifier (RISK-001) |
| **Control(s)** | Which Annex A control(s) address this risk |
| **Action Plan** | Specific steps to implement control |
| **Owner** | Who is responsible for implementation |
| **Due Date** | Target completion date |
| **Status** | Not Started / In Progress / Completed |
| **Residual Risk** | Expected risk score after control implementation |

**Document in**: **[SGSI-RTP-001]** Risk Treatment Plan

---

## 10. Residual Risk and Acceptance (Risco Residual)

### 10.1 Residual Risk Definition

> **Residual Risk** = Risk remaining **after** controls are implemented

### 10.2 Residual Risk Acceptance

All residual risks **MUST** be:
1. ✅ Documented in Risk Register
2. ✅ **Aceito formally** by risk owner + Gestor SGSI
3. ✅ Reviewed annually

**Acceptance Criteria**:
- Residual risk ≤ **MÉDIO** (score ≤ 11) → Auto-accept by Gestor SGSI
- Residual risk = **ALTO** (12-19) → Requires CTO approval
- Residual risk = **CRÍTICO** (≥ 20) → Requires **CEO approval** + documented justification

---

## 11. Risk Register (Registro de Riscos)

### 11.1 Risk Register Structure

| Column | Description |
|--------|-------------|
| **Risk ID** | RISK-001, RISK-002, ... |
| **Asset** | Which asset is at risk |
| **Threat** | What can go wrong |
| **Vulnerability** | Weakness that enables threat |
| **Likelihood** | 1-5 score |
| **Impact** | 1-5 score |
| **Risk Score** | L × I |
| **Risk Level** | CRÍTICO/ALTO/MÉDIO/BAIXO |
| **Treatment** | MITIGATE/ACCEPT/AVOID/TRANSFER |
| **Control(s)** | Annex A control IDs |
| **Owner** | Person responsible |
| **Status** | Open / Em Tratamento / Aceito / Closed |
| **Residual Risk** | Score after controls |
| **Review Date** | Last reviewed |

**Maintained in**: **[SGSI-RISK-002]** Risk Register (Excel or Google Sheets)

---

## 12. Risk Assessment Frequency (Frequência)

### 12.1 Scheduled Assessments

| Type | Frequency | Trigger |
|------|-----------|---------|
| **Full Risk Assessment** | **Annual** | Calendar year + certification cycle |
| **Targeted Assessment** | As needed | New project, major change, new threat |
| **Risk Register Review** | **Quarterly** | Check status of open risks |
| **Post-Incident Review** | After incidents | Update risk scores based on lessons learned |

### 12.2 Triggers for Unscheduled Assessment

- 🔴 **Major architectural change** (new AWS service, migration)
- 🔴 **New business process** (new product line, M&A)
- 🔴 **Significant security incident** (breach, major vulnerability)
- 🔴 **Regulatory change** (new LGPD requirement, ISO update)
- 🔴 **Change in threat landscape** (zero-day in core technology)

---

## 13. Roles and Responsibilities (Papéis)

| Role | Responsibilities |
|------|------------------|
| **Gestor SGSI** | • Own the risk assessment process<br>• Facilitate risk workshops<br>• Maintain Risk Register<br>• Approve residual risks (≤ MÉDIO) |
| **Asset Owners** | • Identify threats and vulnerabilities for their assets<br>• Assess impact<br>• Own risks related to their assets |
| **CTO** | • Provide technical input on likelihood<br>• Approve ALTO residual risks<br>• Allocate resources for risk treatment |
| **CEO** | • Approve CRÍTICO residual risks<br>• Provide strategic risk appetite guidance |
| **IT/Security Team** | • Identify technical vulnerabilities<br>• Implement risk treatment controls<br>• Monitor threats |

---

## 14. Risk Assessment Tools and Techniques (Ferramentas)

### 14.1 Facilitated Workshops

**Method**: In-person or virtual workshop with stakeholders  
**Duration**: 2-4 hours  
**Participants**: Gestor SGSI, CTO, Asset Owners, DevOps Lead  
**Output**: Identified risks with initial L/I scores

### 14.2 Interviews

**Method**: One-on-one interviews with asset owners  
**Best for**: Detailed deep-dive on specific systems  

### 14.3 Automated Tools

| Tool | Purpose |
|------|---------|
| **AWS Security Hub** | Vulnerability scanning, CIS Benchmark |
| **AWS Config** | Configuration compliance |
| **GuardDuty** | Threat intelligence |
| **Trivy / Snyk** | Container and dependency scanning |

### 14.4 Threat Intelligence Sources

- AWS Security Bulletins
- CVE databases (NVD, MITRE ATT&CK)
- OWASP Top 10
- SANS Top 25
- Industry reports (Verizon DBIR)

---

## 15. Risk Communication and Reporting (Comunicação)

### 15.1 Risk Dashboard

**Metrics to track**:
- Total risks: by level (CRÍTICO/ALTO/MÉDIO/BAIXO)
- Risks by status: Open / Em Tratamento / Aceito / Closed
- Overdue treatments (past due date)
- Top 5 risks (highest scores)

**Audience**: Management Review, Board (if applicable)

### 15.2 Risk Reports

**Frequency**: Quarterly  
**Recipients**: CEO, CTO, Gestor SGSI  
**Content**:
- New risks identified
- Risks closed/mitigated
- Changes in risk scores (trend analysis)
- Overdue treatments (escalation)

---

## 16. Integration with ISO 27001 Controls (Integração com Annex A)

### 16.1 Risk → Control Mapping

Each identified risk should map to **one or more** Annex A controls.

**Example**:
- **Risk**: Unauthorized access to AWS production account
- **Threat**: External attacker / Insider threat
- **Vulnerability**: Weak IAM policies, no MFA
- **Likelihood**: 4 (High)
- **Impact**: 5 (Very High — biometric data breach)
- **Risk Score**: 20 (CRÍTICO 🔴)
- **Treatment**: MITIGATE
- **Controls**:
  - A.5.15 — Access control
  - A.5.17 — Authentication information
  - A.5.18 — Access rights
  - A.8.5 — Secure authentication
- **Actions**:
  - Enable MFA on all IAM users
  - Review and restrict IAM policies (least privilege)
  - Quarterly access recertification (SOP-005)

---

## 17. Documentation and Records (Documentação)

### 17.1 Mandatory Records

| Record | Location | Retention |
|--------|----------|-----------|
| **Risk Assessment Report** (annual) | SGSI-RISK-REPORT-YYYY | 7 years |
| **Risk Register** (living document) | SGSI-RISK-002 | Current + 3 years historical |
| **Risk Treatment Plan** | SGSI-RTP-001 | Current + 3 years |
| **Risk Acceptance Forms** | SGSI-RISK-ACCEPT-YYYY-NNN | 7 years |
| **Workshop minutes** | SGSI-RISK-WORKSHOP-YYYY-MM | 3 years |

### 17.2 Audit Trail

All changes to Risk Register must be logged:
- Date of change
- Who made change
- What changed (before/after)
- Reason for change

**Versioning**: Git (if markdown) or Excel version history

---

## 18. Review and Continuous Improvement (Revisão e Melhoria)

### 18.1 Annual Review of Methodology

This methodology itself is reviewed **annually** to ensure:
- Scales (L/I) are still appropriate
- Risk appetite aligns with business strategy
- Process is efficient (not too bureaucratic)
- Tools are adequate

**Reviewers**: Gestor SGSI + CTO

### 18.2 Lessons Learned

After each risk assessment cycle:
- 🔄 What worked well?
- 🔄 What was difficult or time-consuming?
- 🔄 Were any risks missed? (compare with incidents)
- 🔄 Did controls effectively reduce risks?

---

## 19. Risk Appetite Statement (Declaração de Apetite ao Risco)

> **"A TWYN tem ZERO tolerância para riscos que possam resultar em:**
> - Vazamento de dados biométricos (LGPD violation)
> - Perda de certificações (ISO 27001, AWS FTR)
> - Indisponibilidade > 4 horas de APIs críticas
> - Violação de contratos com clientes (SLA breach)
>
> **A TWYN aceita riscos residuais BAIXO ou MÉDIO** (score ≤ 11) após implementação de controles razoáveis, desde que formalmente documentados e aprovados."**

---

## 20. References (Referências)

- ISO/IEC 27001:2022 — Clause 6 (Planning)
- ISO/IEC 27005:2022 — Information security risk management
- NIST SP 800-30 — Risk Assessment Guide
- ISO 31000:2018 — Risk management principles
- TWYN Information Security Policy [SGSI-POLICY-001]

---

## 21. Aprovação

**Gestor SGSI**  
**Signature**: _______________________________  
**Name**: Enes Fernando Degasperi  
**Date**: _____ / _____ / 2026

**CTO**  
**Signature**: _______________________________  
**Name**: Enes Fernando Degasperi  
**Date**: _____ / _____ / 2026

---

## Annex A: Risk Assessment Worksheet Template

**Use this template during risk assessment workshops**:

| ID do Risco | Ativo | Ameaça | Vulnerabilidade | L (1-5) | I (1-5) | Pontuação de Risco | Level | Tratamento | Control | Responsável | Prazo |
|---------|-------|--------|---------------|---------|---------|------------|-------|-----------|---------|-------|----------|
| RISK-001 | | | | | | | | | | | |
| RISK-002 | | | | | | | | | | | |
| ... | | | | | | | | | | | |

---

## Annex B: Example Risk Scenarios

### Scenario 1: Data Breach

- **Asset**: S3 bucket with biometric images
- **Threat**: External attacker gains access
- **Vulnerability**: Bucket misconfiguration (public access)
- **Likelihood**: 3 (Medium — common misconfiguration)
- **Impact**: 5 (Very High — LGPD violation, reputation damage)
- **Risk Score**: 15 (ALTO 🟠)
- **Treatment**: MITIGATE
- **Controls**: A.8.1 (User endpoint devices), A.8.10 (Information deletion), A.8.11 (Data masking)
- **Actions**: Enable S3 Block Public Access, enable encryption (SSE-KMS), audit all buckets

### Scenario 2: Insider Threat

- **Asset**: AWS production account
- **Threat**: Disgruntled employee deletes infrastructure
- **Vulnerability**: Over-permissioned IAM role
- **Likelihood**: 2 (Low — rare but possible)
- **Impact**: 4 (High — service outage, data loss)
- **Risk Score**: 8 (MÉDIO 🟡)
- **Treatment**: MITIGATE
- **Controls**: A.5.18 (Access rights), A.6.4 (Disciplinary process)
- **Actions**: Implement least privilege IAM, enable CloudTrail, restrict delete permissions, offboarding checklist

### Scenario 3: Ransomware

- **Asset**: EKS clusters, RDS databases
- **Threat**: Ransomware encrypts production data
- **Vulnerability**: Unpatched container images, no backup tested
- **Likelihood**: 3 (Medium — growing threat)
- **Impact**: 5 (Very High — business disruption, data loss)
- **Risk Score**: 15 (ALTO 🟠)
- **Treatment**: MITIGATE + TRANSFER (insurance)
- **Controls**: A.5.14 (Information transfer), A.8.7 (Protection against malware), A.8.13 (Information backup)
- **Actions**: Regular patching, backup automation, quarterly DR test, cyber insurance

---

**END OF DOCUMENT**
