---
document_id: TEMPLATE-AUDIT-001
title: Internal Audit Checklist - ISO 27001:2022 Annex A
version: 1.0
date: 2026-05-26
---

# Internal Audit Checklist

## Audit Information
- **Audit ID**: IA-[number] (e.g., IA-001)
- **Audit Date**: [YYYY-MM-DD]
- **Auditor**: [Name]
- **Auditee**: [Department/Process Owner]
- **Scope**: [Controls being audited]

## Instructions
For each control:
- **Status**: ✅ Implemented | 🟡 Partial | ❌ Not Implemented | ⚪ N/A
- **Evidence**: Document evidence reviewed
- **Findings**: Note any non-conformities
- **Score**: 1-5 (1=Major NC, 5=Full compliance)

---

## ORGANIZATIONAL CONTROLS (A.5.1 - A.5.37)

### A.5.1 - Policies for Information Security
- [ ] IS Policy exists and is current (SGSI-POLICY-001)
- [ ] CEO signature obtained
- [ ] Policy communicated to all staff
- [ ] Annual review scheduled
- **Evidence**: _______
- **Finding**: _______
- **Score**: ___/5

### A.5.2 - Information Security Roles and Responsibilities  
- [ ] Gestor SGSI designated (Ricardo Esper)
- [ ] RACI Matrix documented (SGSI-RACI-001)
- [ ] Roles communicated
- **Evidence**: _______
- **Score**: ___/5

### A.5.15 - Access Control
- [ ] Access Control Policy exists (SGSI-POLICY-002)
- [ ] Least privilege implemented
- [ ] MFA enforced (AWS, GitHub)
- [ ] Access review quarterly (SOP-005)
- **Evidence**: _______
- **Score**: ___/5

### A.5.16 - Identity Management
- [ ] Onboarding/offboarding procedures (SOP-001)
- [ ] IAM users have unique accounts
- [ ] No shared credentials
- **Evidence**: _______
- **Score**: ___/5

### A.5.17 - Authentication Information
- [ ] Password policy enforced (14+ chars, complexity)
- [ ] MFA mandatory
- [ ] Keys rotated <90 days
- **Evidence**: _______
- **Score**: ___/5

### A.5.18 - Access Rights
- [ ] Access rights documented
- [ ] Quarterly recertification (SOP-005)
- [ ] Privilege escalation logged
- **Evidence**: _______
- **Score**: ___/5

_[... Continue for all 93 controls ...]_

---

## PEOPLE CONTROLS (A.6.1 - A.6.8)

### A.6.1 - Screening
- [ ] Background checks for new hires
- [ ] Reference verification
- [ ] NDA signed before access
- **Evidence**: _______
- **Score**: ___/5

### A.6.3 - Information Security Awareness
- [ ] Security awareness training (TRAIN-001)
- [ ] 100% completion tracked
- [ ] Phishing simulations
- **Evidence**: _______
- **Score**: ___/5

_[... Continue ...]_

---

## PHYSICAL CONTROLS (A.7.1 - A.7.14)
**Note**: Most N/A (cloud-only). Audit remote work security instead.

### A.7.4 - Physical Security Monitoring
- [ ] N/A (no physical data center)
- **Rationale**: Cloud-only, documented in SoA

_[... Continue ...]_

---

## TECHNOLOGICAL CONTROLS (A.8.1 - A.8.34)

### A.8.13 - Information Backup
- [ ] RDS automated backups enabled
- [ ] S3 versioning enabled
- [ ] Cross-region replication
- [ ] Backup testing quarterly (GAP-004)
- **Evidence**: _______
- **Score**: ___/5

### A.8.15 - Logging
- [ ] CloudTrail enabled
- [ ] Logs retained 1 year
- [ ] Log review monthly
- **Evidence**: _______
- **Score**: ___/5

### A.8.16 - Monitoring Activities
- [ ] AWS Config enabled
- [ ] GuardDuty enabled
- [ ] Security Hub aggregating findings
- **Evidence**: _______
- **Score**: ___/5

_[... Continue for all tech controls ...]_

---

## Summary

### Compliance Score
- **Total Controls Audited**: ___/93
- **Fully Compliant (5)**: ___
- **Partial (3-4)**: ___
- **Non-Compliant (1-2)**: ___
- **N/A**: ___
- **Overall Score**: ___%

### Non-Conformities Identified
| Control | Type | Description | Action Required |
|---------|------|-------------|-----------------|
| A.X.Y | Major/Minor | ___ | ___ |

### Recommendations
1. ...
2. ...

### Sign-Off
- **Auditor Signature**: _____________ Date: _______
- **Gestor SGSI Signature**: _____________ Date: _______

---

**Next Audit**: [Date]
**Audit Report**: See SGSI-AUDIT-001 for programme schedule
