---
**Document Control**
| Field | Value |
|-------|-------|
| **Document ID** | SGSI-RISK-002 |
| **Version** | 1.0 |
| **Author** | BEKAA Consultoria — Ricardo Esper |
| **Approved By** | Ricardo Esper (Bekaa Trusted Advisors) |
| **Last Review** | 26/05/2026 |
| **Next Review** | Q2 2027 (Anual) |
| **ISO 27001:2022 Mapping** | **Clause 6.1.2 — Risk assessment** + **Clause 8.2** |
---

# Risk Register — TWYN SGSI
## Registro de Riscos de Segurança da Informação

---

## 1. Purpose (Propósito)

Este Risk Register documenta **todos os riscos identificados** para os ativos no escopo do SGSI da TWYN, incluindo:
- Análise de probabilidade (Likelihood) e impacto (Impact)
- Nível de risco (Risk Score = L × I)
- Opção de tratamento (Mitigate/Accept/Avoid/Transfer)
- Controles Annex A aplicáveis
- Status atual e responsável

---

## 2. Risk Summary Dashboard

### 2.1 Risk Distribution by Level

| Risk Level | Count | % Total |
|------------|-------|---------|
| 🔴 **CRITICAL** (20-25) | 3 | 17% |
| 🟠 **HIGH** (12-19) | 6 | 33% |
| 🟡 **MEDIUM** (6-11) | 7 | 39% |
| 🟢 **LOW** (3-5) | 2 | 11% |
| **TOTAL** | **18** | 100% |

### 2.2 Risk by Treatment Status

| Status | Count |
|--------|-------|
| 🔴 **Open (Not Started)** | 11 |
| 🟡 **In Treatment** | 4 |
| 🟢 **Mitigated** | 1 |
| ⚪ **Accepted** | 2 |

### 2.3 Top 5 Critical Risks

1. **RISK-001**: Biometric data breach (S3 misconfiguration) — Score: **25** 🔴
2. **RISK-003**: Unauthorized AWS root account access — Score: **20** 🔴
3. **RISK-007**: Ransomware attack on EKS clusters — Score: **20** 🔴
4. **RISK-002**: Lack of AWS Config compliance monitoring — Score: **16** 🟠
5. **RISK-004**: IAM over-permissioning (insider threat) — Score: **16** 🟠

---

## 3. Detailed Risk Register

---

### RISK-001: Biometric Data Breach via S3 Misconfiguration

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-001 |
| **Category** | Data Security |
| **Asset** | S3 buckets containing biometric images (face templates) |
| **Threat** | External attacker gains unauthorized access |
| **Vulnerability** | • S3 bucket misconfiguration (public access)<br>• Lack of encryption at rest (some buckets)<br>• Missing bucket policies |
| **Likelihood** | 5 (Very High) — S3 misconfig is #1 cloud breach cause |
| **Impact** | 5 (Very High) — LGPD violation (Art. 52: multa até 2% faturamento), reputation damage, loss of clients |
| **Risk Score** | **25** 🔴 **CRITICAL** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.8.11 (Data masking)<br>• A.8.10 (Information deletion)<br>• A.5.23 (Cloud services security)<br>• A.8.24 (Use of cryptography) |
| **Actions (RTP)** | 1. Enable **S3 Block Public Access** on all buckets<br>2. Enable **SSE-KMS encryption** (AWS KMS)<br>3. Implement **bucket policies** (least privilege)<br>4. Enable **S3 Access Logging**<br>5. Quarterly audit of all S3 buckets |
| **Owner** | Cloud Infrastructure Lead |
| **Due Date** | **15/06/2026** (20 days) |
| **Status** | 🔴 **Open — High Priority** |
| **Residual Risk** | **6** 🟡 (L=2, I=3) after controls |
| **Last Review** | 26/05/2026 |

---

### RISK-002: Lack of AWS Config Compliance Monitoring

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-002 |
| **Category** | Compliance / Monitoring |
| **Asset** | AWS Account 992382542028 (production) |
| **Threat** | Configuration drift, non-compliant resources go undetected |
| **Vulnerability** | • **AWS Config NOT enabled** (GAP-001)<br>• No automated compliance rules<br>• Manual checks only (error-prone) |
| **Likelihood** | 4 (High) — Drift happens constantly in cloud |
| **Impact** | 4 (High) — Failed audit, FTR rejection, non-compliance with CIS Benchmark |
| **Risk Score** | **16** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.8.9 (Configuration management)<br>• A.5.37 (Documented operating procedures) |
| **Actions (RTP)** | 1. **Enable AWS Config** in all regions<br>2. Enable **CIS AWS Foundations Benchmark** rules<br>3. Configure alerting (SNS → Slack/Email)<br>4. Create Config dashboard<br>5. Monthly compliance review |
| **Owner** | Cloud Infrastructure Lead |
| **Due Date** | **10/06/2026** (15 days) |
| **Status** | 🟡 **In Treatment** (GAP-001 issue created) |
| **Residual Risk** | **4** 🟢 (L=2, I=2) after AWS Config enabled |
| **Last Review** | 26/05/2026 |

---

### RISK-003: Unauthorized AWS Root Account Access

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-003 |
| **Category** | Access Control |
| **Asset** | AWS root account (992382542028) |
| **Threat** | Attacker gains root credentials (phishing, leaked keys) |
| **Vulnerability** | • Root account credentials existence<br>• MFA configured but key stored insecurely?<br>• Root used for daily ops (bad practice) |
| **Likelihood** | 4 (High) — Root account = attractive target |
| **Impact** | 5 (Very High) — Complete infrastructure compromise, data deletion possible |
| **Risk Score** | **20** 🔴 **CRITICAL** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.5.15 (Access control)<br>• A.5.17 (Authentication information)<br>• A.5.18 (Access rights)<br>• A.8.5 (Secure authentication) |
| **Actions (RTP)** | 1. **Delete root access keys** (if exist)<br>2. **Enable MFA** on root (hardware token preferred)<br>3. Store root credentials in **physical safe**<br>4. Enable **CloudTrail alert** on any root usage<br>5. Document "break glass" procedure<br>6. Annual root credential rotation |
| **Owner** | CTO |
| **Due Date** | **05/06/2026** (10 days) |
| **Status** | 🟡 **In Treatment** |
| **Residual Risk** | **8** 🟡 (L=2, I=4) after MFA + monitoring |
| **Last Review** | 26/05/2026 |

---

### RISK-004: IAM Over-Permissioning (Insider Threat)

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-004 |
| **Category** | Access Control / Insider Threat |
| **Asset** | AWS IAM roles and policies |
| **Threat** | Disgruntled employee or compromised account deletes/modifies infrastructure |
| **Vulnerability** | • **IAM policies too permissive** (GAP-003)<br>• Many users have `AdministratorAccess`<br>• No quarterly access review process<br>• No segregation of duties |
| **Likelihood** | 4 (High) — Insider threats are common |
| **Impact** | 4 (High) — Service outage, data loss, financial damage |
| **Risk Score** | **16** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.5.18 (Access rights)<br>• A.6.4 (Disciplinary process)<br>• A.8.2 (Privileged access rights) |
| **Actions (RTP)** | 1. **IAM audit**: Review all users/roles (GAP-003)<br>2. Implement **least privilege** (remove AdministratorAccess)<br>3. Create **custom IAM policies** per job function<br>4. Enable **MFA delete** on S3 critical buckets<br>5. Implement **SOP-005** (quarterly IAM recertification)<br>6. Segregation: separate Dev/Ops/Security roles |
| **Owner** | Cloud Infrastructure Lead + SecOps |
| **Due Date** | **30/06/2026** (35 days) |
| **Status** | 🔴 **Open** (GAP-003 issue created) |
| **Residual Risk** | **6** 🟡 (L=2, I=3) after least privilege |
| **Last Review** | 26/05/2026 |

---

### RISK-005: Lack of Threat Detection (No GuardDuty)

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-005 |
| **Category** | Security Monitoring |
| **Asset** | AWS Account 992382542028 |
| **Threat** | Malicious activity (crypto mining, data exfiltration) goes undetected |
| **Vulnerability** | • **AWS GuardDuty NOT enabled** (GAP-002)<br>• No threat intelligence<br>• Reactive vs. proactive security |
| **Likelihood** | 3 (Medium) — Attacks happen but may not target TWYN specifically |
| **Impact** | 5 (Very High) — Prolonged breach, data loss, compliance failure |
| **Risk Score** | **15** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.5.7 (Threat intelligence)<br>• A.8.16 (Monitoring activities)<br>• A.5.25 (Security event assessment) |
| **Actions (RTP)** | 1. **Enable GuardDuty** in all AWS regions<br>2. Configure **SNS alerts** for HIGH/CRITICAL findings<br>3. Integrate with **incident response process**<br>4. Weekly review of GuardDuty findings<br>5. Tune false positives |
| **Owner** | SecOps Lead |
| **Due Date** | **12/06/2026** (17 days) |
| **Status** | 🔴 **Open** (GAP-002 issue created) |
| **Residual Risk** | **3** 🟢 (L=1, I=3) after GuardDuty |
| **Last Review** | 26/05/2026 |

---

### RISK-006: Unrotated IAM Access Keys (CIS 1.13 Failure)

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-006 |
| **Category** | Credential Management |
| **Asset** | IAM user `tmpsaasboost` (account 992382542028) |
| **Threat** | Compromised access key (leaked in logs, stolen) |
| **Vulnerability** | • **Access key > 90 days old** (AWS FTR issue #18)<br>• No automated rotation<br>• Key may be in use (can't delete without checking) |
| **Likelihood** | 3 (Medium) — Keys leak frequently (GitHub, logs) |
| **Impact** | 4 (High) — Unauthorized API access, data exfiltration |
| **Risk Score** | **12** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.5.16 (Identity management)<br>• A.5.17 (Authentication information)<br>• A.8.5 (Secure authentication) |
| **Actions (RTP)** | 1. **Investigate** if `tmpsaasboost` key is still in use<br>2. If NOT in use: **delete immediately**<br>3. If in use: rotate key + update app config<br>4. Implement **automated key rotation** (90 days max)<br>5. **Prefer IAM roles** over access keys<br>6. Create **SOP-004** (secrets rotation) |
| **Owner** | Cloud Infrastructure Lead |
| **Due Date** | **08/06/2026** (13 days — FTR blocker) |
| **Status** | 🔴 **Open — FTR Blocker** (AWS FTR issue #18) |
| **Residual Risk** | **4** 🟢 (L=2, I=2) after rotation + automation |
| **Last Review** | 26/05/2026 |

---

### RISK-007: Ransomware Attack on EKS Clusters

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-007 |
| **Category** | Malware / Business Continuity |
| **Asset** | EKS clusters (Face ID API workloads) |
| **Threat** | Ransomware encrypts container images, pods, or underlying EBS volumes |
| **Vulnerability** | • Container images not regularly scanned<br>• No malware protection at runtime<br>• Backup exists but **not tested** (GAP-007) |
| **Likelihood** | 4 (High) — Ransomware targeting cloud infra growing |
| **Impact** | 5 (Very High) — Complete service outage, data loss, ransom payment |
| **Risk Score** | **20** 🔴 **CRITICAL** |
| **Treatment** | **MITIGATE** + **TRANSFER** (cyber insurance) |
| **Related Annex A Controls** | • A.8.7 (Protection against malware)<br>• A.8.13 (Information backup)<br>• A.5.29 (Information security during disruption)<br>• A.5.30 (ICT readiness for business continuity) |
| **Actions (RTP)** | 1. **Container image scanning** (Trivy/ECR scanning)<br>2. Enable **GuardDuty EKS protection**<br>3. Implement **pod security policies**<br>4. **Test DR quarterly** (GAP-007)<br>5. Purchase **cyber insurance** (ransomware coverage)<br>6. Incident response playbook for ransomware |
| **Owner** | Cloud Infrastructure Lead + SecOps |
| **Due Date** | **30/06/2026** (35 days) |
| **Status** | 🟡 **In Treatment** (GAP-007 for backup testing) |
| **Residual Risk** | **8** 🟡 (L=2, I=4) after controls + insurance |
| **Last Review** | 26/05/2026 |

---

### RISK-008: Legacy/Orphaned Resources (Security Blind Spots)

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-008 |
| **Category** | Asset Management |
| **Asset** | Unused EC2 instances, old S3 buckets, orphaned snapshots |
| **Threat** | Forgotten resources contain sensitive data or have vulnerabilities |
| **Vulnerability** | • **No asset inventory** (GAP-004)<br>• Resources created ad-hoc not tracked<br>• No decommissioning process |
| **Likelihood** | 4 (High) — Legacy resources very common in cloud |
| **Impact** | 3 (Medium) — Data leakage, unnecessary attack surface, cost |
| **Risk Score** | **12** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.5.9 (Inventory of information and other associated assets)<br>• A.5.12 (Classification of information)<br>• A.8.10 (Information deletion) |
| **Actions (RTP)** | 1. **Full AWS asset discovery** (AWS Config, scripts)<br>2. **Tag all resources** (owner, project, lifecycle)<br>3. **Identify orphaned** resources (no tags, old)<br>4. **Decommission** legacy resources (GAP-004)<br>5. Create **asset inventory** (SGSI-ASSETS-001)<br>6. Implement tagging policy (mandatory) |
| **Owner** | Cloud Infrastructure Lead |
| **Due Date** | **20/06/2026** (25 days) |
| **Status** | 🔴 **Open** (GAP-004 issue created) |
| **Residual Risk** | **4** 🟢 (L=2, I=2) after inventory + cleanup |
| **Last Review** | 26/05/2026 |

---

### RISK-009: Lack of Backup Testing (Unknown DR Capability)

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-009 |
| **Category** | Business Continuity |
| **Asset** | RDS databases, S3 buckets (backup copies) |
| **Threat** | Disaster occurs but backup restore fails (corrupted, incomplete) |
| **Vulnerability** | • **Backups never tested** (GAP-007)<br>• Unknown RTO/RPO actual values<br>• No documented DR procedure |
| **Likelihood** | 3 (Medium) — Untested backups often fail when needed |
| **Impact** | 5 (Very High) — Data loss, prolonged outage, business failure |
| **Risk Score** | **15** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.8.13 (Information backup)<br>• A.5.30 (ICT readiness for BC) |
| **Actions (RTP)** | 1. **Execute DR drill** immediately (GAP-007)<br>2. Document **actual RTO/RPO** achieved<br>3. Create **DR playbook** (SGSI-DRP-001)<br>4. **Quarterly DR tests** (calendar reminders)<br>5. Automate restore testing (scripted) |
| **Owner** | Cloud Infrastructure Lead |
| **Due Date** | **15/06/2026** (20 days — AWS FTR evidence) |
| **Status** | 🔴 **Open** (GAP-007 + AWS FTR #16) |
| **Residual Risk** | **6** 🟡 (L=2, I=3) after quarterly testing |
| **Last Review** | 26/05/2026 |

---

### RISK-010: No AWS Business Support (Delayed Incident Response)

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-010 |
| **Category** | Third-Party Management |
| **Asset** | AWS infrastructure (entire production) |
| **Threat** | Critical AWS issue but slow support response (Developer plan limits) |
| **Vulnerability** | • **No Business Support plan** (AWS FTR issue #17)<br>• Developer plan: 12-24h response for critical<br>• No Technical Account Manager (TAM) |
| **Likelihood** | 2 (Low) — AWS outages rare but do happen |
| **Impact** | 4 (High) — Extended downtime, SLA breach, revenue loss |
| **Risk Score** | **8** 🟡 **MEDIUM** |
| **Treatment** | **MITIGATE** or **ACCEPT** (cost/benefit) |
| **Related Annex A Controls** | • A.5.22 (Monitoring and review of supplier services)<br>• A.5.23 (Cloud services security) |
| **Actions (RTP)** | **Option A**: Upgrade to **Business Support** (~$100-500/month)<br>**Option B**: Document acceptance + mitigation plan:<br>1. Create **break-glass runbook** for common issues<br>2. Train team on AWS troubleshooting<br>3. Contract **on-demand AWS consultant** (backup)<br>4. Define **SLA allowances** in client contracts |
| **Owner** | CTO + Finance |
| **Due Date** | **10/06/2026** (decision needed for FTR) |
| **Status** | 🔴 **Open — Pending Decision** (AWS FTR #17) |
| **Residual Risk** | **6** 🟡 if Business Support; **8** 🟡 if accept |
| **Last Review** | 26/05/2026 |

---

### RISK-011: CIS Benchmark Controls Missing (8 controls)

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-011 |
| **Category** | Compliance |
| **Asset** | AWS Account 992382542028 |
| **Threat** | Non-compliance with CIS Benchmark = failed FTR audit |
| **Vulnerability** | • **8 controls not detected** in Security Hub (AWS FTR #18)<br>• IAM.4, IAM.5, IAM.15, IAM.16, EC2.2, EC2.53, EC2.54, ACCOUNT.1 |
| **Likelihood** | 5 (Very High) — Already detected in FTR review |
| **Impact** | 3 (Medium) — FTR rejection, but fixable |
| **Risk Score** | **15** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.5.16 (Identity management) — IAM controls<br>• A.8.3 (Information access restriction) — EC2 controls<br>• A.5.1 (Policies for information security) — ACCOUNT.1 |
| **Actions (RTP)** | 1. **Enable missing controls** in Security Hub<br>2. Fix non-compliances:<br>   - IAM.4: Ensure no root access keys<br>   - IAM.5: Enable MFA for console users<br>   - IAM.15/16: IAM permissions via groups/roles only<br>   - EC2.2: Restrict default SG<br>   - EC2.53: No public IPs on instances<br>   - EC2.54: Use IMDSv2<br>   - ACCOUNT.1: Add security contact<br>3. **Re-run CIS Benchmark**<br>4. Submit new report to AWS FTR |
| **Owner** | Cloud Infrastructure + SecOps |
| **Due Date** | **08/06/2026** (13 days — FTR blocker) |
| **Status** | 🔴 **Open — FTR Blocker** (AWS FTR #18) |
| **Residual Risk** | **3** 🟢 (L=1, I=3) after fixes |
| **Last Review** | 26/05/2026 |

---

### RISK-012: No Security Awareness Training

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-012 |
| **Category** | Human Resources Security |
| **Asset** | All TWYN employees |
| **Threat** | Phishing, social engineering, accidental data leak by employees |
| **Vulnerability** | • **No formal SI training** (GAP-006)<br>• No phishing simulations<br>• No training records |
| **Likelihood** | 4 (High) — Human error is #1 security risk |
| **Impact** | 4 (High) — Credential theft, data breach, compliance failure |
| **Risk Score** | **16** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.6.3 (Information security awareness, education and training)<br>• A.5.10 (Acceptable use of information) |
| **Actions (RTP)** | 1. **Select training platform** (KnowBe4, Udemy, custom)<br>2. **Enroll all employees** (mandatory)<br>3. Training content:<br>   - LGPD basics (1h)<br>   - Phishing awareness (1h)<br>   - Password security (30min)<br>   - Secure remote work (30min)<br>4. **Simulated phishing** campaigns (quarterly)<br>5. **Training log** (SGSI-TRAINING-LOG)<br>6. Annual refresher |
| **Owner** | HR + Gestor SGSI |
| **Due Date** | **30/06/2026** (35 days) |
| **Status** | 🔴 **Open** (GAP-006 issue created) |
| **Residual Risk** | **8** 🟡 (L=2, I=4) after training |
| **Last Review** | 26/05/2026 |

---

### RISK-013: No Management Review Process

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-013 |
| **Category** | Governance |
| **Asset** | SGSI itself (management system) |
| **Threat** | SGSI becomes stale, not aligned with business, audit failure |
| **Vulnerability** | • **No management review yet** (GAP-005)<br>• No formal KPI tracking<br>• Top management not engaged |
| **Likelihood** | 5 (Very High) — New SGSI, first review overdue |
| **Impact** | 3 (Medium) — Audit finding, certification delay |
| **Risk Score** | **15** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • **Clause 9.3** (Management review) — MANDATORY |
| **Actions (RTP)** | 1. **Schedule first management review** (GAP-005)<br>2. Prepare review agenda (see Clause 9.3 requirements)<br>3. Collect KPIs: incidents, audit results, metrics<br>4. CEO/CTO attendance mandatory<br>5. Document minutes + action items<br>6. **Quarterly** reviews (calendar recurring) |
| **Owner** | Gestor SGSI |
| **Due Date** | **15/06/2026** (20 days) |
| **Status** | 🔴 **Open** (GAP-005 issue created) |
| **Residual Risk** | **3** 🟢 (L=1, I=3) after first review |
| **Last Review** | 26/05/2026 |

---

### RISK-014: GitHub Account Compromise

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-014 |
| **Category** | Supply Chain / Code Security |
| **Asset** | GitHub repositories (t4isb-infra/*) |
| **Threat** | Attacker gains access to GitHub account, injects malicious code |
| **Vulnerability** | • Unknown if MFA enabled for all devs<br>• Unknown branch protection rules<br>• Unknown if commit signing enforced |
| **Likelihood** | 3 (Medium) — GitHub attacks common but targeting high-value |
| **Impact** | 5 (Very High) — Backdoor in production code, supply chain attack |
| **Risk Score** | **15** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.8.28 (Secure coding)<br>• A.8.32 (Change management)<br>• A.5.16 (Identity management) |
| **Actions (RTP)** | 1. **Enforce MFA** on all GitHub accounts (org-wide)<br>2. **Branch protection** on main: require PR reviews (2 approvers)<br>3. **Signed commits** (GPG) — best practice<br>4. **CODEOWNERS** file (require specific approvers)<br>5. Enable **GitHub Advanced Security** (if budget allows)<br>6. Dependency scanning (Dependabot)<br>7. Assess **GitHub DPA** status |
| **Owner** | CTO |
| **Due Date** | **20/06/2026** (25 days) |
| **Status** | 🔴 **Open** |
| **Residual Risk** | **6** 🟡 (L=2, I=3) after controls |
| **Last Review** | 26/05/2026 |

---

### RISK-015: Single Region Dependency (us-east-1)

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-015 |
| **Category** | Business Continuity / Availability |
| **Asset** | Primary production in us-east-1 (N. Virginia) |
| **Threat** | AWS us-east-1 region outage (rare but impactful) |
| **Vulnerability** | • Most workloads in single region<br>• DR region (us-west-2) exists but **failover not tested**<br>• RTO unknown for cross-region |
| **Likelihood** | 2 (Low) — AWS region outages rare (~1-2x per year globally) |
| **Impact** | 4 (High) — Service outage until region recovers or failover |
| **Risk Score** | **8** 🟡 **MEDIUM** |
| **Treatment** | **ACCEPT** + partial MITIGATE |
| **Related Annex A Controls** | • A.5.29 (Information security during disruption)<br>• A.5.30 (ICT readiness for BC) |
| **Actions (RTP)** | **Accept** regional dependency (multi-region = high cost/complexity)<br>**Mitigate**:<br>1. Ensure DR region (us-west-2) is **kept in sync**<br>2. **Test cross-region failover** (GAP-007 DR drill)<br>3. Document RTO for region failover<br>4. Multi-AZ within region (already done ✅)<br>5. Monitor AWS Health Dashboard |
| **Owner** | Cloud Infrastructure Lead |
| **Due Date** | **30/06/2026** (acceptance + DR test) |
| **Status** | 🟡 **In Treatment** (linked to GAP-007) |
| **Residual Risk** | **8** 🟡 (accept this level) |
| **Last Review** | 26/05/2026 |

---

### RISK-016: LGPD Non-Compliance (No DPO, Incomplete Privacy Policy)

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-016 |
| **Category** | Legal / Regulatory |
| **Asset** | Personal data processing (biometric data) |
| **Threat** | ANPD audit finds LGPD violations |
| **Vulnerability** | • **DPO not formally designated**<br>• Privacy Policy incomplete or not published<br>• Data Subject Rights (DSR) process not documented<br>• No DPIA for biometric processing |
| **Likelihood** | 3 (Medium) — ANPD audits increasing |
| **Impact** | 5 (Very High) — Fines up to 2% revenue (Art. 52), processing ban |
| **Risk Score** | **15** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.5.34 (Privacy and protection of PII)<br>• A.5.8 (Information security in project management) — DPIA |
| **Actions (RTP)** | 1. **Designate DPO** formally (internal or external)<br>2. **Publish Privacy Policy** (website + API docs)<br>3. Implement **DSR process**: access, correction, deletion<br>4. Conduct **DPIA** (Data Protection Impact Assessment) for biometric processing<br>5. **LGPD training** for all employees (GAP-006)<br>6. Create **data processing register** (Art. 37) |
| **Owner** | Legal + Gestor SGSI |
| **Due Date** | **30/06/2026** (35 days) |
| **Status** | 🔴 **Open** |
| **Residual Risk** | **6** 🟡 (L=2, I=3) after compliance |
| **Last Review** | 26/05/2026 |

---

### RISK-017: No Incident Response Plan

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-017 |
| **Category** | Incident Management |
| **Asset** | TWYN operations (response capability) |
| **Threat** | Security incident occurs but chaotic/slow response |
| **Vulnerability** | • **No documented IRP** (Incident Response Plan)<br>• No on-call rotation<br>• No runbooks for common incidents<br>• LGPD breach notification process unclear |
| **Likelihood** | 4 (High) — Incidents will happen eventually |
| **Impact** | 4 (High) — Prolonged breach, LGPD notification failure (fines) |
| **Risk Score** | **16** 🟠 **HIGH** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.5.24 (Information security incident planning and preparation)<br>• A.5.25 (Assessment and decision on information security events)<br>• A.5.26 (Response to information security incidents)<br>• A.5.27 (Learning from information security incidents) |
| **Actions (RTP)** | 1. **Create IRP document** (SGSI-IRP-001)<br>2. Define incident **severity levels** (P0-P4)<br>3. Define **on-call rotation** (PagerDuty or similar)<br>4. Create **runbooks** for common scenarios<br>5. **LGPD breach notification** process (72h to ANPD)<br>6. **Tabletop exercise** (simulate incident)<br>7. Post-incident review template |
| **Owner** | SecOps Lead + Gestor SGSI |
| **Due Date** | **25/06/2026** (30 days) |
| **Status** | 🔴 **Open** |
| **Residual Risk** | **8** 🟡 (L=2, I=4) after IRP + drills |
| **Last Review** | 26/05/2026 |

---

### RISK-018: Developer Laptops (Endpoint Security)

| Field | Value |
|-------|-------|
| **Risk ID** | RISK-018 |
| **Category** | Endpoint Security |
| **Asset** | Developer workstations (remote work) |
| **Threat** | Laptop theft, malware, unencrypted data |
| **Vulnerability** | • Unknown if **full disk encryption** enforced<br>• No MDM (Mobile Device Management)<br>• No endpoint protection (antivirus, EDR)<br>• Remote work policy unclear |
| **Likelihood** | 3 (Medium) — Common threat |
| **Impact** | 3 (Medium) — Source code leak, credentials leak |
| **Risk Score** | **9** 🟡 **MEDIUM** |
| **Treatment** | **MITIGATE** |
| **Related Annex A Controls** | • A.6.7 (Remote working)<br>• A.7.7 (Clear desk and clear screen)<br>• A.8.1 (User endpoint devices) |
| **Actions (RTP)** | 1. **Enforce full disk encryption** (FileVault, BitLocker)<br>2. Create **SOP-003** (Remote Work Policy)<br>3. Consider **MDM** (Jamf, Intune) if budget allows<br>4. **Endpoint protection**: CrowdStrike, Sophos, or built-in (Defender)<br>5. Screen lock timeout (5 min)<br>6. VPN required for internal resources |
| **Owner** | IT/DevOps Lead |
| **Due Date** | **30/06/2026** (35 days) |
| **Status** | 🔴 **Open** |
| **Residual Risk** | **4** 🟢 (L=2, I=2) after controls |
| **Last Review** | 26/05/2026 |

---

## 4. Accepted Risks (Formally Accepted)

### RISK-ACC-001: Third-Party SaaS Tool Compromise (Low-Risk Tools)

| Field | Value |
|-------|-------|
| **Asset** | Non-critical SaaS tools (Slack, Notion marketing) |
| **Risk Score** | **4** 🟢 (L=2, I=2) |
| **Justification** | • Tools don't process production data<br>• Covered by vendor DPAs<br>• Cost of additional controls > benefit |
| **Accepted By** | Gestor SGSI |
| **Acceptance Date** | 26/05/2026 |
| **Review Date** | Q2 2027 |

---

### RISK-ACC-002: Physical Security of Office (Low Risk)

| Field | Value |
|-------|-------|
| **Asset** | TWYN office (administrative workstations only) |
| **Risk Score** | **4** 🟢 (L=2, I=2) |
| **Justification** | • No production servers on-premises (100% cloud)<br>• Basic office security sufficient (access control, CCTV)<br>• Cost of datacenter-grade security not justified |
| **Accepted By** | CTO |
| **Acceptance Date** | 26/05/2026 |
| **Review Date** | Q2 2027 |

---

## 5. Next Actions Summary

### 🔴 CRITICAL (Due < 20 days)

1. **RISK-001** (S3 breach): Enable Block Public Access + SSE-KMS — Due: 15/06
2. **RISK-003** (Root account): Delete keys + MFA + safe — Due: 05/06
3. **RISK-006** (Access key rotation): Fix tmpsaasboost — Due: 08/06 🚨 FTR BLOCKER
4. **RISK-011** (CIS controls): Fix 8 missing controls — Due: 08/06 🚨 FTR BLOCKER

### 🟠 HIGH (Due < 35 days)

5. **RISK-002** (AWS Config): Enable + rules — Due: 10/06
6. **RISK-004** (IAM): Least privilege audit — Due: 30/06
7. **RISK-005** (GuardDuty): Enable + alerts — Due: 12/06
8. **RISK-007** (Ransomware): Container scanning + DR — Due: 30/06
9. **RISK-008** (Legacy): Asset inventory + cleanup — Due: 20/06
10. **RISK-009** (Backup test): Execute DR drill — Due: 15/06
11. **RISK-010** (AWS Support): Make decision — Due: 10/06 🚨 FTR
12. **RISK-012** (Training): Enroll employees — Due: 30/06
13. **RISK-013** (Mgmt Review): Schedule + execute — Due: 15/06
14. **RISK-014** (GitHub): MFA + branch protection — Due: 20/06
15. **RISK-016** (LGPD): DPO + Privacy Policy — Due: 30/06
16. **RISK-017** (IRP): Create plan + runbooks — Due: 25/06

---

## 6. Review Log

| Review Date | Reviewer | Changes |
|-------------|----------|---------|
| 26/05/2026 | Ricardo Esper (BEKAA) | Initial risk assessment (18 risks identified) |

---

**END OF RISK REGISTER**  
**Next Review**: Q2 2027 or upon significant change
