---
document_id: TEMPLATE-AUDIT-003
title: Evidence Collection Guide
version: 1.0
---

# Evidence Collection Guide

## Purpose
Guide for collecting and organizing audit evidence for ISO 27001:2022 compliance.

---

## Types of Evidence

### 1. Documentary Evidence
**Examples**:
- Policies and procedures (SGSI-POLICY-*, SOP-*)
- Risk assessments (SGSI-RISK-*)
- Asset inventory (SGSI-ASSETS-001)
- Training records (SGSI-COMP-001)
- Meeting minutes (Management Review)

**Collection**:
- Ensure documents are current (within review period)
- Verify signatures and approval dates
- Check version control

### 2. Technical Evidence
**Examples**:
- AWS Config compliance reports
- CloudTrail logs (access attempts, changes)
- IAM policy documents
- Backup test results
- Penetration test reports

**Collection**:
```bash
# IAM users list
aws iam list-users > evidence/iam-users-YYYY-MM-DD.json

# MFA status
aws iam get-account-summary > evidence/mfa-status.json

# CloudTrail events (root usage)
aws cloudtrail lookup-events --lookup-attributes AttributeKey=Username,AttributeValue=root

# Config compliance
aws configservice describe-compliance-by-config-rule
```

### 3. Testimonial Evidence
**Examples**:
- Employee interviews
- Management review attendance
- Training completion confirmations

**Collection**:
- Prepare interview questions
- Document responses
- Get interviewee sign-off

### 4. Observational Evidence
**Examples**:
- Screenshots of configurations
- Photos of physical security (if applicable)
- Walkthroughs of procedures

**Collection**:
- Timestamp all screenshots
- Redact sensitive info (passwords, keys)
- Organize by control

---

## Evidence Organization

### Folder Structure
```
docs/05-evidence/
├── audit-[YYYY-MM]/
│   ├── 01-documentary/
│   │   ├── policies/
│   │   ├── procedures/
│   │   └── risk-management/
│   ├── 02-technical/
│   │   ├── aws-config-reports/
│   │   ├── cloudtrail-logs/
│   │   └── iam-policies/
│   ├── 03-testimonial/
│   │   └── interview-notes/
│   ├── 04-observational/
│   │   └── screenshots/
│   └── audit-report-IA-[X].md
```

### File Naming
- `YYYY-MM-DD-[control]-[description].ext`
- Example: `2026-07-15-A.5.15-access-control-policy.pdf`

---

## Evidence Requirements by Control

### A.5.1 - IS Policy
- ✅ Policy document (SGSI-POLICY-001)
- ✅ CEO signature (signed PDF)
- ✅ Communication email to staff
- ✅ Acknowledgment records

### A.5.15-5.18 - Access Control
- ✅ Access Control Policy (SGSI-POLICY-002)
- ✅ IAM users list with MFA status
- ✅ Access review records (quarterly)
- ✅ Onboarding/offboarding checklists (sample)

### A.8.13 - Backup
- ✅ Backup configuration (RDS settings)
- ✅ Restoration test report (quarterly)
- ✅ RTO/RPO validation results

### A.8.16 - Monitoring
- ✅ AWS Config enabled (screenshot)
- ✅ GuardDuty findings (sample)
- ✅ Log review records (monthly)

_[Continue for all controls...]_

---

## Collection Checklist

Before audit:
- [ ] Gather all mandatory documents (14 docs)
- [ ] Export technical configurations
- [ ] Schedule interviews
- [ ] Prepare observational walkthroughs
- [ ] Organize evidence folder structure

During audit:
- [ ] Record evidence reviewed in real-time
- [ ] Take screenshots of configurations
- [ ] Document verbal confirmations
- [ ] Note any discrepancies

After audit:
- [ ] Archive evidence (7 years retention)
- [ ] Update SGSI-AUDIT-001 with findings
- [ ] Share evidence folder with auditor (read-only)

---

## Evidence Quality Criteria
**Good Evidence**:
- ✅ Directly relevant to control
- ✅ Timely (current, not outdated)
- ✅ Authentic (verifiable source)
- ✅ Complete (not partial data)
- ✅ Objective (factual, not opinion)

**Poor Evidence**:
- ❌ Undated screenshots
- ❌ Hearsay ("Someone told me...")
- ❌ Incomplete logs
- ❌ Expired documents

---

**Prepared By**: Security Consultant
**For Use By**: Gestor SGSI, Internal Auditors, External Auditors
