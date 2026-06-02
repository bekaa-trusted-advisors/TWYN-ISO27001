---
document_id: SGSI-CAR-001
title: Corrective Action Log
version: 1.0
date: 2026-05-26
iso_clause: "10.2"
classification: Internal
owner: Gestor SGSI
---

# Corrective Action Register

## Purpose
Registrar ações corretivas para todas as não-conformidades conforme Cláusula 10.2 ISO 27001:2022.

## Corrective Actions

### CAR-001: Enable MFA on AWS Root Account

| Field | Value |
|-------|-------|
| **CAR ID** | CAR-001 |
| **Related NCR** | NCR-001 |
| **Date Opened** | 2026-05-26 |
| **Owner** | DevOps Lead |
| **Priority** | CRITICAL |
| **Due Date** | 2026-06-05 |
| **Status** | Open |

**Root Cause**: MFA não foi configurado durante setup inicial da conta AWS 992382542028.

**Corrective Actions**:
1. Adquirir hardware MFA token ou usar virtual MFA app (Google Authenticator)
2. Login com root account
3. Habilitar MFA nas configurações de segurança
4. Testar MFA fazendo logout e re-login
5. Documentar no runbook de emergency access
6. Configurar CloudWatch alarm para "Root Account Usage" (alertar se root for usado)

**Preventive Actions**:
- Adicionar MFA check no AWS Config rule: "root-account-mfa-enabled"
- Documentar em procedimento de onboarding AWS que MFA é obrigatório

**Evidence of Completion**: Screenshot de AWS console mostrando MFA enabled + CloudWatch alarm configurado

**Verification**: Gestor SGSI ou auditor confirma via AWS console

**Status Updates**:
- 2026-05-26: CAR criado
- [Date]: MFA enabled
- [Date]: Verification completed - CLOSED

---

### CAR-002: Rotate tmpsaasboost IAM Access Key

| Field | Value |
|-------|-------|
| **CAR ID** | CAR-002 |
| **Related NCR** | NCR-002 |
| **Date Opened** | 2026-05-26 |
| **Owner** | DevOps Lead |
| **Priority** | HIGH |
| **Due Date** | 2026-06-08 (AWS FTR blocker) |
| **Status** | Open |

**Root Cause**: Access key "tmpsaasboost" foi criada para teste temporário e não foi rotacionada ou deletada conforme policy (90 dias).

**Corrective Actions**:
1. Identificar onde a key está sendo usada (se ainda está em uso)
2. Se não em uso: Deletar imediatamente
3. Se em uso: Criar nova key, atualizar aplicação, deletar key antiga
4. Verificar no IAM Credential Report que não há mais keys >90 dias

**Preventive Actions**:
- Implementar AWS Config rule: "access-keys-rotated" (90 days)
- Implementar processo SOP-004: Secrets Management and Rotation (trimestral review)
- Criar CloudWatch alarm para keys próximas de expirar (75 dias)

**Evidence of Completion**: IAM Credential Report mostrando todas as keys <90 dias

---

### CAR-003: Implement AWS Config with CIS Benchmarks

| Field | Value |
|-------|-------|
| **CAR ID** | CAR-003 |
| **Related NCR** | NCR-003 |
| **Date Opened** | 2026-05-26 |
| **Owner** | DevOps Lead |
| **Priority** | CRITICAL (AWS FTR blocker) |
| **Due Date** | 2026-06-08 |
| **Status** | Open |

**Root Cause**: AWS Config não foi provisionado; compliance baseline (CIS AWS Foundations Benchmark) não está sendo monitorado.

**Corrective Actions**:
1. Habilitar AWS Config no account 992382542028 (us-east-1)
2. Configurar S3 bucket para armazenar Config snapshots
3. Habilitar CIS AWS Foundations Benchmark conformance pack
4. Remediar 8 controles faltantes identificados no AWS FTR:
   - [Listar os 8 controles específicos após investigação]
5. Configurar alerting para non-compliance no SNS

**Preventive Actions**:
- Monitoring contínuo via AWS Config
- Remediation automática onde possível (AWS Systems Manager)
- Revisar compliance score mensalmente no Security Hub

**Estimated Cost**: ~$50/month (Config + S3 storage)

**Evidence of Completion**: AWS Config dashboard mostrando compliance score ≥85% para CIS Benchmark

---

### CAR-004: Establish and Test Backup Restoration Process

| Field | Value |
|-------|-------|
| **CAR ID** | CAR-004 |
| **Related NCR** | NCR-004 |
| **Date Opened** | 2026-05-26 |
| **Owner** | DevOps Lead |
| **Priority** | HIGH (AWS FTR blocker) |
| **Due Date** | 2026-06-05 |
| **Status** | Open |

**Root Cause**: Processo de DR testing não foi estabelecido; backups existem mas nunca foram testados.

**Corrective Actions**:
1. Documentar DR runbook (RDS restore, S3 recovery, EKS cluster rebuild)
2. Definir RTO (Recovery Time Objective): Target <8h
3. Definir RPO (Recovery Point Objective): Target <4h
4. Executar primeiro DR test:
   - Restore RDS snapshot to test instance
   - Verify data integrity
   - Test application connectivity
   - Document time taken (measure RTO/RPO)
5. Agendar DR tests trimestrais no calendar

**Preventive Actions**:
- Quarterly DR testing schedule (Jan, Apr, Jul, Oct)
- Automated backup verification (checksums, test restores)
- CloudWatch alarms for backup failures

**Evidence of Completion**: DR test report com RTO/RPO medidos + runbook documentado

---

## CAR Status Definitions

- **Open**: Ação definida, aguardando implementação
- **In Progress**: Ação em implementação
- **Pending Verification**: Ação implementada, aguardando validação de eficácia
- **Closed**: Ação verificada como eficaz (NC resolvido)
- **Rejected**: Ação não necessária após reavaliação

## CAR Metrics

| Metric | Value |
|--------|-------|
| Total CARs | 4 |
| Open | 4 |
| In Progress | 0 |
| Pending Verification | 0 |
| Closed | 0 |
| Overdue | 0 |

**Aging Analysis**:
- <30 days: 4
- 30-60 days: 0
- 60-90 days: 0
- >90 days: 0

---

**Last Update**: 2026-05-26
**Next Review**: Semanal (DevOps standup) + Trimestral (Management Review)
