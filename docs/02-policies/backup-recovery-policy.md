---
document_id: SGSI-POLICY-005  
title: Backup & Recovery Policy
version: 1.0
annex_a_controls: "A.5.29, A.5.30, A.8.13, A.8.14"
---
# Backup & Recovery Policy
## 1. Objectives
- RPO (Recovery Point Objective): <4 hours
- RTO (Recovery Time Objective): <8 hours  
- Backup success rate: 100%
## 2. Backup Strategy
**RDS (PostgreSQL)**:
- Automated daily snapshots (7-day retention)
- Manual snapshots antes de major changes
- Point-in-time recovery enabled
**S3 (biometric data)**:
- Versioning enabled
- Cross-region replication (us-east-1 → us-west-2)
- Lifecycle policy: Delete após X dias
**EKS (application state)**:
- Terraform state em S3 (versioned)
- Kubernetes manifests em Git
- Helm values backed up
**Configuration/Secrets**:
- AWS Secrets Manager (automatic rotation)
- GitHub (infrastructure as code)
## 3. Testing
- Quarterly DR tests (GAP-004, CAR-004)
- Document actual RTO/RPO achieved
- Update runbooks based on test results
## 4. Responsibilities
- DevOps Lead: Execute backups/restores
- Gestor SGSI: Validate compliance
## 5. Approval
Owner: Gestor SGSI | Approved: CEO (Pendente) | Review: 2026-12-31
