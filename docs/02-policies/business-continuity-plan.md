---
document_id: SGSI-POLICY-006
title: Business Continuity Plan  
version: 1.0
annex_a_controls: "A.5.29, A.5.30"
---
# Business Continuity Plan (BCP)
## 1. Critical Business Functions
**Face ID Platform API**:
- Priority: P0 (revenue-generating)
- Maximum Tolerable Downtime: 8 hours
- Recovery strategy: Multi-AZ, cross-region failover
## 2. Disaster Scenarios
**Scenario 1: AWS Region Failure**
- Trigger: us-east-1 unavailable >1 hour
- Action: Failover to us-west-2 (RDS read replica + S3 CRR)
- ETA: 4-6 hours
**Scenario 2: Ransomware**
- Trigger: Encrypted files detected
- Action: Isolate systems, restore from backups, rebuild
- ETA: 12-24 hours  
**Scenario 3: Key Person Unavailable (DevOps SPOF)**
- Trigger: DevOps Lead unavailable >48h
- Action: Junior DevOps + external consultant + runbooks
- ETA: Depends on severity
## 3. Emergency Contacts
- CEO: [phone]
- Gestor SGSI: Ricardo Esper - [email/phone]
- DevOps Lead: [phone]
- AWS Support: Business Support (GAP-005)
## 4. Communication Plan
- Internal: Slack #incidents + email
- External: Status page (statuspage.io if available)
- Clients: Email within 2h if impacting service
## 5. Recovery Procedures
See implementation guides: `docs/06-implementation-guides/gap-004-backup-testing.md`
## 6. Approval  
Owner: Gestor SGSI | Approved: CEO (Pendente) | Review: Trimestral
