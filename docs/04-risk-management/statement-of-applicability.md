---
**Document Control**
| Field | Value |
|-------|-------|
| **Document ID** | SGSI-SOA-001 |
| **Version** | 1.0 |
| **Author** | BEKAA Consultoria — Ricardo Esper |
| **Approved By** | **[CEO + Gestor SGSI]** ⚠️ SIGNATURES REQUIRED |
| **Last Update** | 26/05/2026 |
| **Next Review** | Annual or upon significant change |
| **ISO 27001:2022 Mapping** | **Clause 6.1.3d — Statement of Applicability** (MANDATORY) |
---

# Statement of Applicability (SoA)
## Declaração de Aplicabilidade — TWYN SGSI ISO 27001:2022

---

## 1. Purpose

This **Statement of Applicability (SoA)** documents which of the **93 Annex A controls** from ISO/IEC 27001:2022 are:
- **Applicable** to TWYN's ISMS scope
- **Implemented**, **Partially Implemented**, or **Not Implemented**
- **Not Applicable** (with justification)

This document is **MANDATORY** for ISO 27001 certification and must be:
1. ✅ Approved by top management
2. ✅ Based on Risk Assessment results
3. ✅ Updated whenever scope or risks change
4. ✅ Presented to certification auditor

---

## 2. Scope Reference

**ISMS Scope**: See [SGSI-SCOPE-001] ISMS Scope Document

**In Scope**:
- AWS Account 992382542028 (production)
- Face ID Platform API (EKS, RDS, S3)
- CI/CD pipelines (GitHub Actions, CodePipeline)
- Infrastructure as Code (Terraform, CloudFormation)
- Biometric data processing

**Out of Scope**:
- Development laptops (covered by endpoint policy)
- Marketing website (separate infrastructure)
- Third-party SaaS tools (covered by vendor assessment)

---

## 3. Control Status Legend

| Status | Symbol | Definition |
|--------|--------|------------|
| **Implemented** | ✅ | Control is fully implemented with evidence |
| **Partial** | 🟡 | Control is partially implemented, gaps remain |
| **Not Implemented** | ❌ | Control is not yet implemented (planned) |
| **Not Applicable** | N/A | Control is not applicable to TWYN's scope (justified) |

---

## 4. Summary Statistics

| Theme | Total Controls | Implemented ✅ | Partial 🟡 | Not Impl ❌ | N/A |
|-------|----------------|----------------|------------|-------------|-----|
| **5. Organizational** | 37 | 12 (32%) | 18 (49%) | 5 (14%) | 2 (5%) |
| **6. People** | 8 | 2 (25%) | 4 (50%) | 2 (25%) | 0 |
| **7. Physical** | 14 | 1 (7%) | 2 (14%) | 1 (7%) | 10 (71%) |
| **8. Technological** | 34 | 14 (41%) | 12 (35%) | 8 (24%) | 0 |
| **TOTAL** | **93** | **29 (31%)** | **36 (39%)** | **16 (17%)** | **12 (13%)** |

**Overall Compliance**: **70% implemented or partial** (target: 100% by Q3 2026)

---

## 5. THEME 1: ORGANIZATIONAL CONTROLS (A.5.1–5.37)

### 5.1 Governance and Policy Controls

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.5.1** | Policies for information security | ✅ | Information Security Policy approved [SGSI-POLICY-001] | SGSI-POLICY-001 | Gestor SGSI |
| **A.5.2** | Information security roles and responsibilities | 🟡 | Roles defined in policy, but RACI matrix incomplete | SGSI-RACI-001 (TBD) | Gestor SGSI |
| **A.5.3** | Segregation of duties | 🟡 | Partial: Dev/Ops separation exists, need formal documentation | IAM policies | CTO |
| **A.5.4** | Management responsibilities | ✅ | Defined in IS Policy (Clause 4: Roles) | SGSI-POLICY-001 | CEO |
| **A.5.5** | Contact with authorities | ✅ | DPO designated for ANPD, security contacts defined | SGSI-POLICY-001 | Legal |
| **A.5.6** | Contact with special interest groups | 🟡 | AWS support, some security communities | Document contacts | Gestor SGSI |
| **A.5.7** | Threat intelligence | 🟡 | GuardDuty being enabled (GAP-002), AWS Security Bulletins subscribed | GuardDuty | SecOps |
| **A.5.8** | Information security in project management | ❌ | No formal security review in project initiation | Create checklist | CTO |
| **A.5.9** | Inventory of information and assets | ❌ | Asset inventory being created (GAP-004) | SGSI-ASSETS-001 (TBD) | Cloud Infra |
| **A.5.10** | Acceptable use of information | 🟡 | Defined in IS Policy, but no signed AUP from employees | Create AUP form | HR + SGSI |

### 5.2 Access Control

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.5.15** | Access control | 🟡 | AWS IAM exists, but over-permissioned (GAP-003) | IAM policies | Cloud Infra |
| **A.5.16** | Identity management | 🟡 | IAM users exist, lifecycle partial (no auto-offboarding) | SOP-001 (TBD) | Cloud Infra |
| **A.5.17** | Authentication information | 🟡 | Passwords exist, MFA partial, key rotation issue (RISK-006) | AWS IAM | Cloud Infra |
| **A.5.18** | Access rights | 🟡 | IAM permissions exist, but no quarterly review (SOP-005 needed) | SOP-005 (TBD) | Cloud Infra |

### 5.3 Third-Party Management

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.5.19** | Information security in supplier relationships | 🟡 | AWS BAA signed ✅, GitHub DPA unclear | Supplier list | Gestor SGSI |
| **A.5.20** | Addressing IS in supplier agreements | 🟡 | AWS contract has SI clauses, others TBD | Contracts | Legal |
| **A.5.21** | Managing IS in ICT supply chain | ❌ | No formal supply chain risk assessment | Create process | Gestor SGSI |
| **A.5.22** | Monitoring and review of supplier services | ❌ | AWS monitored via dashboards, no formal review process | Create checklist | Cloud Infra |
| **A.5.23** | IS when using cloud services | 🟡 | AWS is assessed (FTR in progress), configuration gaps exist | AWS FTR docs | Cloud Infra |

### 5.4 Business Continuity

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.5.29** | IS during disruption | 🟡 | DR region exists (us-west-2), failover not tested (GAP-007) | DR test results | Cloud Infra |
| **A.5.30** | ICT readiness for BC | 🟡 | Backup automated, but not tested | DR test results | Cloud Infra |

### 5.5 Incident Management

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.5.24** | IS incident management planning | ❌ | No documented IRP (RISK-017) | SGSI-IRP-001 (TBD) | SecOps |
| **A.5.25** | Assessment of IS events | ❌ | No process, GuardDuty being enabled | GuardDuty alerts | SecOps |
| **A.5.26** | Response to IS incidents | ❌ | Ad-hoc response, no runbooks | Create runbooks | SecOps |
| **A.5.27** | Learning from IS incidents | ❌ | No post-mortem process | Create template | SecOps |
| **A.5.28** | Collection of evidence | 🟡 | CloudTrail logs exist (evidence), no formal forensics process | CloudTrail | Cloud Infra |

### 5.6 Compliance and Legal

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.5.31** | Legal, statutory, regulatory and contractual requirements | 🟡 | LGPD awareness, but gaps (RISK-016: no DPO, incomplete Privacy Policy) | LGPD docs | Legal |
| **A.5.32** | Intellectual property rights | ✅ | Code in private GitHub repos, licenses managed | GitHub | CTO |
| **A.5.33** | Protection of records | ✅ | CloudTrail 1 year, audit logs 7 years (LGPD compliant) | S3 retention | Cloud Infra |
| **A.5.34** | Privacy and protection of PII | 🟡 | Encryption exists, LGPD gaps (no DPIA, DSR process) | Privacy Policy (TBD) | Legal + SGSI |
| **A.5.35** | Independent review of IS | ❌ | No external audit yet, planned for Q3 2026 | Audit plan | Gestor SGSI |
| **A.5.36** | Compliance with policies and standards | 🟡 | Policies exist, no audit yet (GAP-008: internal audit program) | Audit reports | Gestor SGSI |
| **A.5.37** | Documented operating procedures | 🟡 | Some IaC documented, SOPs being written | SOPs 001-005 | SGSI |

---

## 6. THEME 2: PEOPLE CONTROLS (A.6.1–6.8)

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.6.1** | Screening | 🟡 | Background checks performed (as per labor law), NDA signed | HR records | HR |
| **A.6.2** | Terms and conditions of employment | ✅ | Employment contracts include confidentiality clauses | HR contracts | HR |
| **A.6.3** | IS awareness, education and training | ❌ | No formal training program yet (GAP-006, RISK-012) | Training logs (TBD) | HR + SGSI |
| **A.6.4** | Disciplinary process | ✅ | Labor law compliance, defined in contracts | HR policies | HR |
| **A.6.5** | Responsibilities after termination | 🟡 | Offboarding ad-hoc, SOP-001 being written | SOP-001 (TBD) | HR + IT |
| **A.6.6** | Confidentiality agreements | ✅ | NDAs signed by all employees | HR records | HR |
| **A.6.7** | Remote working | 🟡 | Remote work common, policy incomplete (SOP-003 being written) | SOP-003 (TBD) | HR + IT |
| **A.6.8** | Information security event reporting | 🟡 | Email/Slack reporting exists, no formal process | IRP (TBD) | SecOps |

---

## 7. THEME 3: PHYSICAL CONTROLS (A.7.1–7.14)

**Note**: TWYN operates **100% in AWS cloud**. Physical security of datacenters is AWS's responsibility (covered by AWS ISO 27001 + SOC 2 certifications). Most A.7 controls are **Not Applicable**.

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.7.1** | Physical security perimeters | N/A | No on-premises datacenter. AWS responsibility. | AWS certs | N/A |
| **A.7.2** | Physical entry | N/A | AWS responsibility | AWS certs | N/A |
| **A.7.3** | Securing offices, rooms and facilities | 🟡 | Office has basic access control (badge), no sensitive data on-site | Office security | Admin |
| **A.7.4** | Physical security monitoring | N/A | AWS datacenters (AWS responsibility). Office has CCTV. | CCTV | Admin |
| **A.7.5** | Protecting against physical threats | N/A | AWS responsibility | AWS certs | N/A |
| **A.7.6** | Working in secure areas | N/A | AWS responsibility | AWS certs | N/A |
| **A.7.7** | Clear desk and clear screen | 🟡 | Policy defined, enforcement manual (screen lock timeout configured) | IS Policy | HR |
| **A.7.8** | Equipment siting and protection | N/A | AWS responsibility (cloud), laptops covered by A.8.1 | AWS certs | N/A |
| **A.7.9** | Security of assets off-premises | ✅ | Laptops encrypted (being enforced), VPN for remote access | SOP-003 | IT |
| **A.7.10** | Storage media | N/A | No physical media (100% cloud storage) | N/A | N/A |
| **A.7.11** | Supporting utilities | N/A | AWS responsibility | AWS certs | N/A |
| **A.7.12** | Cabling security | N/A | AWS responsibility | AWS certs | N/A |
| **A.7.13** | Equipment maintenance | N/A | AWS manages cloud infra, laptops covered by IT support | IT policies | IT |
| **A.7.14** | Secure disposal of equipment | N/A | Laptops: secure wipe before disposal. Cloud: no physical disposal needed. | IT policy | IT |

**Physical Controls Summary**: 10/14 = **Not Applicable** (71%). Remaining 4 are related to office and endpoints.

---

## 8. THEME 4: TECHNOLOGICAL CONTROLS (A.8.1–8.34)

### 8.1 Endpoint and Network Security

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.8.1** | User endpoint devices | 🟡 | Laptops used, encryption being enforced, no MDM yet (RISK-018) | SOP-003 | IT |
| **A.8.2** | Privileged access rights | 🟡 | AWS IAM root/admin access exists, over-permissioned (GAP-003) | IAM policies | Cloud Infra |
| **A.8.3** | Information access restriction | 🟡 | AWS IAM + S3 policies, least privilege being implemented | IAM policies | Cloud Infra |
| **A.8.4** | Access to source code | ✅ | GitHub private repos, branch protection, PR reviews required | GitHub settings | CTO |
| **A.8.5** | Secure authentication | 🟡 | MFA partial (not all users), key rotation issue (RISK-006) | IAM + GitHub | Cloud Infra |

### 8.2 Cryptography

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.8.24** | Use of cryptography | 🟡 | TLS 1.2+ enforced, S3/RDS encryption partial (RISK-001) | Crypto policy (TBD) | Cloud Infra |

### 8.3 Configuration Management

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.8.9** | Configuration management | ❌ | AWS Config NOT enabled (GAP-001), IaC exists but no drift detection | AWS Config | Cloud Infra |
| **A.8.10** | Information deletion | 🟡 | S3 lifecycle policies exist, no formal data deletion process | S3 policies | Cloud Infra |
| **A.8.11** | Data masking | ❌ | No data masking in non-prod (biometric data not copied to staging) | Create policy | DevOps |
| **A.8.12** | Data leakage prevention | ❌ | No DLP solution, CloudTrail logs sensitive API calls | Consider AWS Macie | SecOps |

### 8.4 Backup and Logging

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.8.13** | Information backup | 🟡 | Automated backup (RDS, S3 versioning), NOT tested (GAP-007) | Backup logs | Cloud Infra |
| **A.8.14** | Redundancy | ✅ | Multi-AZ (us-east-1), DR region (us-west-2), EKS multi-node | AWS architecture | Cloud Infra |
| **A.8.15** | Logging | 🟡 | CloudTrail enabled, application logs partial | CloudTrail | Cloud Infra |
| **A.8.16** | Monitoring activities | 🟡 | CloudWatch exists, GuardDuty being enabled (GAP-002) | Monitoring dashboards | DevOps |

### 8.5 Malware and Vulnerability Management

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.8.7** | Protection against malware | 🟡 | Container scanning being enabled (RISK-007), GuardDuty (GAP-002) | Trivy/ECR scanning | SecOps |
| **A.8.8** | Management of technical vulnerabilities | 🟡 | Dependabot enabled, no formal patch management process | Dependabot | DevOps |

### 8.6 Development and Deployment

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.8.25** | Secure development lifecycle | 🟡 | PR reviews required (2 approvers), no SAST/DAST yet | GitHub workflows | CTO |
| **A.8.26** | Application security requirements | ❌ | No formal security requirements in backlog | Create checklist | CTO |
| **A.8.27** | Secure system architecture | ✅ | Architecture reviewed (AWS FTR process), documented | Architecture diagrams | CTO |
| **A.8.28** | Secure coding | 🟡 | OWASP awareness, no formal training (GAP-006) | Training (TBD) | CTO |
| **A.8.29** | Security testing | ❌ | No regular pentesting, ad-hoc only | Schedule pentests | SecOps |
| **A.8.30** | Outsourced development | N/A | No outsourced development currently | N/A | N/A |
| **A.8.31** | Separation of dev, test, prod | ✅ | Separate AWS accounts/VPCs for dev/staging/prod | AWS accounts | Cloud Infra |
| **A.8.32** | Change management | 🟡 | PR-based changes, SOP-002 being written | SOP-002 (TBD) | DevOps |
| **A.8.33** | Test information | 🟡 | Staging uses synthetic data, occasional prod snapshot (need policy) | Create policy | DevOps |
| **A.8.34** | Protection of IS during audit | ❌ | No audit protection plan (first audit pending) | Create plan | Gestor SGSI |

### 8.7 Other Technological Controls

| Control | Title | Status | Justification / Evidence | Related Docs | Owner |
|---------|-------|--------|--------------------------|--------------|-------|
| **A.8.6** | Capacity management | ✅ | AWS Auto Scaling configured, CloudWatch alerts | CloudWatch | DevOps |
| **A.8.17** | Clock synchronization | ✅ | NTP via AWS default (managed) | AWS default | Cloud Infra |
| **A.8.18** | Use of privileged utility programs | 🟡 | CloudFormation/Terraform usage logged (CloudTrail), no formal approval | IaC policies | DevOps |
| **A.8.19** | Installation of software on operational systems | 🟡 | Container-based (controlled), laptops less controlled | MDM needed | IT |
| **A.8.20** | Networks security | ✅ | VPC isolation, Security Groups, NACLs configured | VPC config | Cloud Infra |
| **A.8.21** | Security of network services | ✅ | AWS-managed services, TLS enforced | AWS services | Cloud Infra |
| **A.8.22** | Segregation of networks | ✅ | Prod/staging VPCs isolated, public/private subnets | VPC design | Cloud Infra |
| **A.8.23** | Web filtering | ❌ | No web filtering (not applicable to APIs, consider for office if needed) | N/A or TBD | IT |

---

## 9. Controls Not Applicable (12 total)

| Control | Title | Justification |
|---------|-------|---------------|
| **A.7.1** | Physical security perimeters | No on-premises datacenter. AWS responsibility. |
| **A.7.2** | Physical entry | AWS responsibility. |
| **A.7.4** | Physical security monitoring | AWS datacenters. Office CCTV exists (minimal risk). |
| **A.7.5** | Protecting against physical threats | AWS responsibility. |
| **A.7.6** | Working in secure areas | AWS responsibility. |
| **A.7.8** | Equipment siting and protection | AWS responsibility (cloud servers). |
| **A.7.10** | Storage media | No physical media used (100% cloud). |
| **A.7.11** | Supporting utilities | AWS responsibility. |
| **A.7.12** | Cabling security | AWS responsibility. |
| **A.8.23** | Web filtering | APIs don't browse web. Office endpoints low risk (accepted). |
| **A.8.30** | Outsourced development | No outsourced development. |
| **A.7.14** | Secure disposal (partial) | Cloud resources: no physical disposal. Laptops: secure wipe. |

**Formal Approval Required**: CEO + Gestor SGSI must approve N/A classifications.

---

## 10. Implementation Roadmap

**Target**: 100% compliance by Q3 2026 (August)

### Phase 1 (June 2026) — CRITICAL GAPS

- ❌ → 🟡 AWS Config (A.8.9) — GAP-001
- ❌ → 🟡 GuardDuty (A.5.7, A.8.16) — GAP-002
- 🟡 → ✅ IAM least privilege (A.5.15, A.5.18, A.8.2) — GAP-003
- ❌ → ✅ Asset inventory (A.5.9) — GAP-004

### Phase 2 (June-July 2026) — OPERATIONAL EVIDENCE

- ❌ → ✅ Management review (Clause 9.3) — GAP-005
- ❌ → ✅ SI training (A.6.3) — GAP-006
- 🟡 → ✅ Backup testing (A.8.13, A.5.30) — GAP-007

### Phase 3 (July-August 2026) — DOCUMENTATION

- ❌ → ✅ All SOPs (A.5.37)
- ❌ → ✅ IRP (A.5.24-5.27)
- 🟡 → ✅ LGPD compliance (A.5.34) — RISK-016

### Phase 4 (August 2026) — AUDIT READINESS

- ❌ → ✅ Internal audit program (Clause 9.2, A.5.35) — GAP-008
- All 🟡 → ✅ Complete remaining partials
- Collect all evidences

---

## 11. Control-to-Risk Mapping

**Key Risks Addressed by Controls**:

| Risk ID | Primary Controls | Status |
|---------|------------------|--------|
| RISK-001 (S3 breach) | A.8.24, A.8.11, A.5.23 | 🟡 In treatment |
| RISK-003 (Root access) | A.5.15, A.5.17, A.8.2, A.8.5 | 🟡 In treatment |
| RISK-007 (Ransomware) | A.8.7, A.8.13, A.5.29, A.5.30 | 🟡 In treatment |
| RISK-012 (No training) | A.6.3 | ❌ GAP-006 |
| RISK-016 (LGPD) | A.5.34, A.5.31 | 🟡 Partial |

---

## 12. Audit Evidence Checklist

For each control marked ✅ or 🟡, auditor will request:

| Control Category | Evidence Required |
|------------------|-------------------|
| **Policies (A.5.1-5.6)** | Signed policies, approval records, communication proof |
| **Access Control (A.5.15-5.18, A.8.2-8.5)** | IAM screenshots, access review logs, MFA status |
| **Backup (A.8.13)** | Backup logs, DR test results |
| **Logging (A.8.15)** | CloudTrail logs, retention configuration |
| **Training (A.6.3)** | Training completion records, certificates |
| **Incident Mgmt (A.5.24-5.27)** | IRP document, incident tickets, post-mortems |

---

## 13. Review and Approval

This SoA must be reviewed and approved **annually** or when:
- Significant changes to ISMS scope
- New systems/services introduced
- Risk assessment identifies new controls needed
- Audit findings require control changes

**Approved By**:

**CEO TWYN**  
**Signature**: _______________________________  
**Name**: [Nome Completo]  
**Date**: _____ / _____ / 2026

**Gestor SGSI**  
**Signature**: _______________________________  
**Name**: [Nome Completo]  
**Date**: _____ / _____ / 2026

---

## 14. Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 (Draft) | 26/05/2026 | Ricardo Esper (BEKAA) | Initial SoA — 29 impl, 36 partial, 16 not impl, 12 N/A |

---

**END OF STATEMENT OF APPLICABILITY**
