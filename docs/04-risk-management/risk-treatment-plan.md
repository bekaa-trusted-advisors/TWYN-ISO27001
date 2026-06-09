---
**Document Control**
| Campo | Valor |
|-------|-------|
| **Document ID** | SGSI-RTP-001 |
| **Version** | 1.0 |
| **Author** | BEKAA Consultoria — Ricardo Esper |
| **Approved By** | [Gestor SGSI + CTO] |
| **Last Update** | 08/06/2026 |
| **Próxima Revisão** | Monthly (until all risks treated) |
| **ISO 27001:2022 Mapping** | **Clause 6.1.3 — Information security risk treatment** |
---

# Risk Treatment Plan (RTP)
## Plano de Tratamento de Riscos — TWYN SGSI

---

## 1. Purpose

Este documento define o **plano de ação** para tratar cada risco identificado no Risk Register [SGSI-RISK-002], incluindo:
- Controles Annex A selecionados
- Ações específicas de implementação
- Responsáveis e prazos
- Status de execução

---

## 2. Treatment Strategy Summary

| Tratamento | Risk Count | % Total |
|-----------|------------|---------|
| **MITIGATE** | 16 | 89% |
| **ACCEPT** | 2 | 11% |
| **TRANSFER** | 1 (+ MITIGATE) | 6% |
| **AVOID** | 0 | 0% |

---

## 3. Critical Risks Treatment (IMMEDIATE ACTION)

### RTP-001: RISK-001 — Biometric Data Breach (S3)

**Risk Score**: 25 🔴 CRÍTICO  
**Treatment**: MITIGATE  
**Owner**: Cloud Infrastructure Lead  
**Due**: **15/06/2026** (20 days)

**Annex A Controls**:
- A.8.11 — Data masking
- A.8.10 — Information deletion  
- A.5.23 — Cloud services security
- A.8.24 — Use of cryptography

**Implementation Actions**:

| # | Action | Technical Details | Responsável | Status | Prazo |
|---|--------|-------------------|-------|--------|----------|
| 1.1 | Enable S3 Block Public Access | Run: `aws s3control put-public-access-block` on account level | Cloud Infra | ⏳ Pending | 28/05/2026 |
| 1.2 | Enable SSE-KMS encryption on ALL S3 buckets | Audit all buckets → enable default encryption (KMS key) | Cloud Infra | ⏳ Pending | 05/06/2026 |
| 1.3 | Implement bucket policies (least privilege) | Review/restrict bucket policies → remove wildcards | Cloud Infra | ⏳ Pending | 10/06/2026 |
| 1.4 | Enable S3 Access Logging | Log to dedicated audit bucket (encrypted) | Cloud Infra | ⏳ Pending | 12/06/2026 |
| 1.5 | Quarterly S3 security audit | Schedule recurring review (automated + manual) | Cloud Infra | ⏳ Pending | 15/06/2026 |

**Success Criteria**:
- ✅ All S3 buckets have Block Public Access enabled
- ✅ All buckets with sensitive data are SSE-KMS encrypted
- ✅ No overly permissive bucket policies
- ✅ Access logs enabled and monitored

**Residual Risk**: 6 🟡 MÉDIO (L=2, I=3)

---

### RTP-003: RISK-003 — AWS Root Account Compromise

**Risk Score**: 20 🔴 CRÍTICO  
**Treatment**: MITIGATE  
**Owner**: CTO  
**Due**: **05/06/2026** (10 days)

**Annex A Controls**:
- A.5.15 — Access control
- A.5.17 — Authentication information
- A.5.18 — Access rights
- A.8.5 — Secure authentication

**Implementation Actions**:

| # | Action | Technical Details | Responsável | Status | Prazo |
|---|--------|-------------------|-------|--------|----------|
| 3.1 | Check if root access keys exist | AWS Console → Security Credentials → delete if exist | CTO | ⏳ Pending | 28/05/2026 |
| 3.2 | Enable MFA on root account | Use hardware token (YubiKey) preferred | CTO | ⏳ Pending | 28/05/2026 |
| 3.3 | Store root credentials in physical safe | Document safe location, access procedure | CTO | ⏳ Pending | 30/05/2026 |
| 3.4 | Enable CloudTrail alert on root usage | SNS → email/Slack on any root API call | Cloud Infra | ⏳ Pending | 08/06/2026 |
| 3.5 | Document "break glass" procedure | When/how to use root (emergency only) | Gestor SGSI | ⏳ Pending | 05/06/2026 |
| 3.6 | Annual root credential rotation | Calendar reminder every 12 months | CTO | ⏳ Pending | 05/06/2026 |

**Success Criteria**:
- ✅ Root access keys deleted (if existed)
- ✅ Root MFA enabled (hardware token)
- ✅ Alert configured for any root usage
- ✅ Break-glass procedure documented

**Residual Risk**: 8 🟡 MÉDIO (L=2, I=4)

---

### RTP-007: RISK-007 — Ransomware Attack (EKS)

**Risk Score**: 20 🔴 CRÍTICO  
**Treatment**: MITIGATE + TRANSFER  
**Owner**: Cloud Infrastructure Lead + SecOps  
**Due**: **30/06/2026** (35 days)

**Annex A Controls**:
- A.8.7 — Protection against malware
- A.8.13 — Information backup
- A.5.29 — Information security during disruption
- A.5.30 — ICT readiness for BC

**Implementation Actions**:

| # | Action | Technical Details | Responsável | Status | Prazo |
|---|--------|-------------------|-------|--------|----------|
| 7.1 | Container image scanning | Enable Trivy or AWS ECR image scanning | SecOps | ⏳ Pending | 05/06/2026 |
| 7.2 | Enable GuardDuty EKS protection | AWS Console → GuardDuty → enable EKS runtime monitoring | SecOps | ⏳ Pending | 10/06/2026 |
| 7.3 | Implement pod security policies | Restrict privileged containers, host network | DevOps | ⏳ Pending | 15/06/2026 |
| 7.4 | Execute DR test (backup restore) | Linked to GAP-007 — test EKS/RDS restore | Cloud Infra | ⏳ Pending | 20/06/2026 |
| 7.5 | Purchase cyber insurance | Get quotes → ransomware coverage | Finance + CTO | ⏳ Pending | 25/06/2026 |
| 7.6 | Create ransomware runbook | Incident response playbook (isolate, restore) | SecOps + SGSI | ⏳ Pending | 30/06/2026 |

**Success Criteria**:
- ✅ All container images scanned pre-deployment
- ✅ GuardDuty EKS protection active
- ✅ DR tested successfully (restore < 4h)
- ✅ Cyber insurance policy active

**Residual Risk**: 8 🟡 MÉDIO (L=2, I=4) — with insurance transferring part of financial impact

---

## 4. High Risks Treatment (< 90 days)

### RTP-002: RISK-002 — AWS Config Not Enabled

**Risk Score**: 16 🟠 ALTO  
**Treatment**: MITIGATE  
**Owner**: Cloud Infrastructure Lead  
**Due**: **10/06/2026** (15 days)

**Actions**:
| # | Action | Prazo | Status |
|---|--------|----------|--------|
| 2.1 | Enable AWS Config in all regions (us-east-1, us-west-2) | 05/06/2026 | ⏳ GAP-001 |
| 2.2 | Enable CIS AWS Foundations Benchmark rules (90+ rules) | 07/06/2026 | ⏳ GAP-001 |
| 2.3 | Configure SNS alerting (critical/high findings → Slack) | 08/06/2026 | ⏳ GAP-001 |
| 2.4 | Create Config compliance dashboard | 10/06/2026 | ⏳ GAP-001 |

**Residual Risk**: 4 🟢 (L=2, I=2)

---

### RTP-004: RISK-004 — IAM Over-Permissioning

**Risk Score**: 16 🟠 ALTO  
**Treatment**: MITIGATE  
**Owner**: Cloud Infrastructure + SecOps  
**Due**: **30/06/2026** (35 days)

**Actions**:
| # | Action | Prazo | Status |
|---|--------|----------|--------|
| 4.1 | Full IAM audit — list all users/roles with AdministratorAccess | 05/06/2026 | ⏳ GAP-003 |
| 4.2 | Create custom IAM policies per job function (dev, ops, ro) | 15/06/2026 | ⏳ GAP-003 |
| 4.3 | Remove AdministratorAccess, assign least privilege policies | 20/06/2026 | ⏳ GAP-003 |
| 4.4 | Enable MFA delete on S3 critical buckets | 22/06/2026 | ⏳ Pending |
| 4.5 | Implement SOP-005 (quarterly IAM recertification) | 25/06/2026 | ⏳ Pending |
| 4.6 | Segregation of duties: separate Dev/Ops/Security AWS accounts | 30/06/2026 | ⏳ Pending |

**Residual Risk**: 6 🟡 (L=2, I=3)

---

### RTP-005: RISK-005 — No GuardDuty (Threat Detection)

**Risk Score**: 15 🟠 ALTO  
**Treatment**: MITIGATE  
**Owner**: SecOps Lead  
**Due**: **12/06/2026** (17 days)

**Actions**:
| # | Action | Prazo | Status |
|---|--------|----------|--------|
| 5.1 | Enable GuardDuty in all AWS regions | 05/06/2026 | ⏳ GAP-002 |
| 5.2 | Configure SNS alerts (ALTO/CRÍTICO findings → PagerDuty/Slack) | 08/06/2026 | ⏳ GAP-002 |
| 5.3 | Integrate GuardDuty with incident response process (runbook) | 10/06/2026 | ⏳ GAP-002 |
| 5.4 | Weekly review of all GuardDuty findings | 12/06/2026 | ⏳ GAP-002 |

**Residual Risk**: 3 🟢 (L=1, I=3)

---

### RTP-006: RISK-006 — Unrotated Access Key (tmpsaasboost)

**Risk Score**: 12 🟠 ALTO — 🚨 **AWS FTR BLOCKER**  
**Treatment**: MITIGATE  
**Owner**: Cloud Infrastructure Lead  
**Due**: **08/06/2026** (13 days) ⚠️ URGENT

**Actions**:
| # | Action | Prazo | Status |
|---|--------|----------|--------|
| 6.1 | Investigate if tmpsaasboost access key is still in use (check CloudTrail) | 28/05/2026 | ⏳ FTR #18 |
| 6.2 | If NOT in use: delete immediately | 28/05/2026 | ⏳ FTR #18 |
| 6.3 | If in use: rotate key + update application config | 01/06/2026 | ⏳ FTR #18 |
| 6.4 | Implement automated key rotation policy (AWS Config rule) | 05/06/2026 | ⏳ FTR #18 |
| 6.5 | Prefer IAM roles over access keys (document migration plan) | 08/06/2026 | ⏳ FTR #18 |

**Residual Risk**: 4 🟢 (L=2, I=2)

---

### RTP-008 to RTP-017: [Abbreviated — Full Details in Annex A]

| RTP | Risk | Score | Responsável | Prazo | Key Actions |
|-----|------|-------|-------|----------|-------------|
| **RTP-008** | Legacy resources | 12 🟠 | Cloud Infra | 20/06/2026 | Asset inventory → tag/cleanup ([SGSI-GAP-004](../06-implementation-guides/gap-004-backup-testing.md)) |
| **RTP-009** | No backup testing | 15 🟠 | Cloud Infra | 15/06/2026 | Execute DR drill ([SGSI-GAP-007](../06-implementation-guides/gap-007-iso-certification.md)) |
| **RTP-010** | No AWS Biz Support | 8 🟡 | CTO + Finance | 10/06/2026 | Decision: upgrade or accept |
| **RTP-011** | CIS 8 controls missing | 15 🟠 🚨 FTR | Cloud + SecOps | 08/06/2026 | Fix IAM.4/5/15/16, EC2.2/53/54, ACCOUNT.1 |
| **RTP-012** | No SI training | 16 🟠 | HR + SGSI | 30/06/2026 | Enroll all employees ([SGSI-GAP-006](../06-implementation-guides/gap-006-ceo-signature.md)) |
| **RTP-013** | No mgmt review | 15 🟠 | Gestor SGSI | 15/06/2026 | Schedule first review ([SGSI-GAP-005](../06-implementation-guides/gap-005-aws-support-decision.md)) |
| **RTP-014** | GitHub compromise | 15 🟠 | CTO | 20/06/2026 | MFA + branch protection |
| **RTP-015** | Single region dependency | 8 🟡 | Cloud Infra | 30/06/2026 | Accept + test failover |
| **RTP-016** | LGPD non-compliance | 15 🟠 | Legal + SGSI | 30/06/2026 | DPO + Privacy Policy + DPIA |
| **RTP-017** | No IRP | 16 🟠 | SecOps + SGSI | 25/06/2026 | Create IRP document + runbooks |

---

## 5. Aceito Risks (No Treatment Plan)

**RISK-ACC-001**: Third-party SaaS (Slack, Notion) — Score: 4 🟢  
**RISK-ACC-002**: Office physical security — Score: 4 🟢  
→ Formally accepted. No actions. Review annually.

---

## 6. Monitoring and Tracking

### 6.1 Weekly Status Update

**Every Friday**: Gestor SGSI reviews RTP progress with risk owners.

**Metrics tracked**:
- % of actions completed on time
- Overdue actions (escalate to CTO)
- Residual risk trend

### 6.2 Monthly Management Report

**Report to**: CEO, CTO, Gestor SGSI

**Contents**:
- Risks mitigated (moved to closed)
- Overdue treatments (RED flag)
- New risks identified
- Top 5 open risks

---

## 7. Control Implementation Checklist

For each Annex A control, track implementation:

**Example: A.8.24 — Use of cryptography**

| Ativo | Control Status | Evidence | Last Verified |
|-------|----------------|----------|---------------|
| S3 buckets (biometric data) | 🟡 In Progress | SSE-KMS being enabled | 08/06/2026 |
| RDS databases | ✅ Implemented | Encryption at rest enabled | 15/03/2026 |
| EBS volumes | ✅ Implemented | Default encryption on | 10/02/2026 |
| TLS for APIs | ✅ Implemented | ALB enforces HTTPS | 01/01/2026 |

**Overall Control Status**: 🟡 Partial (75% complete)

---

## 8. Escalation Process

| Condition | Escalation Path |
|-----------|-----------------|
| **Action > 7 days overdue** | Gestor SGSI → Risk Owner |
| **Action > 14 days overdue** | Gestor SGSI → CTO |
| **CRÍTICO risk not mitigated by due date** | Gestor SGSI → CEO (immediate) |
| **AWS FTR blocker not resolved** | CTO → All hands (daily standup) |

---

## 9. Completion Criteria

This RTP is considered **COMPLETE** when:
- ✅ All CRÍTICO risks reduced to MÉDIO or lower
- ✅ All ALTO risks have treatment plan executed (may have residual risk)
- ✅ All AWS FTR blockers resolved
- ✅ 14 mandatory ISO 27001 documents created
- ✅ All SOPs (001-005) written and approved
- ✅ First management review completed
- ✅ Internal audit passed (no major NCs)

**Target Date**: **Q3 2026 (August)**

---

## 10. Document Approval

**Gestor SGSI**  
**Signature**: _______________________________  
**Name**: Ricardo Esper  
**Date**: _____ / _____ / 2026

**CTO**  
**Signature**: _______________________________  
**Name**: Ricardo Esper  
**Date**: _____ / _____ / 2026

---

## Annex A: Full Action Tracking Matrix

*[Link to detailed project management tool — Jira, GitHub Projects, or Excel]*

---

**END OF RISK TREATMENT PLAN**  
**Próxima Revisão**: Monthly until all risks treated
