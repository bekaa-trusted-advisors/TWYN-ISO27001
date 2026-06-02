---
document_id: SGSI-NCR-001
title: Nonconformity Register
version: 1.0
date: 2026-05-26
iso_clause: "10.1"
classification: Internal
owner: Gestor SGSI
---

# Nonconformity Register

## Purpose
Registrar todas as não-conformidades identificadas no SGSI (auditorias, incidentes, reviews) conforme Cláusula 10.1 ISO 27001:2022.

## Nonconformities

| NCR ID | Date Identified | Source | Type | Description | ISO Clause | Annex A | Severity | Root Cause | Status | CAR ID |
|--------|-----------------|--------|------|-------------|------------|---------|----------|------------|--------|--------|
| NCR-001 | 2026-05-26 | Gap Analysis | Finding | AWS root account sem MFA habilitado | 8.1 | A.5.17 | MAJOR | MFA não foi configurado durante setup inicial da conta | Open | CAR-001 |
| NCR-002 | 2026-05-26 | Gap Analysis | Finding | IAM access key "tmpsaasboost" >90 dias sem rotação | 8.1 | A.5.18 | MINOR | Key criada para teste e esquecida | Open | CAR-002 |
| NCR-003 | 2026-05-26 | Gap Analysis | Finding | AWS Config não implementado (8 CIS controls faltando) | 8.1 | A.8.9 | MAJOR | AWS Config não foi provisionado; sem baseline de compliance | Open | CAR-003 |
| NCR-004 | 2026-05-26 | Gap Analysis | Finding | Backup restoration testing nunca realizado | 8.1 | A.8.13 | MAJOR | Processo de DR testing não estabelecido | Open | CAR-004 |

## NCR Status Definitions

- **Open**: NC identificado, aguardando implementação de CA
- **In Progress**: CA em implementação
- **Pending Verification**: CA implementado, aguardando validação de eficácia
- **Closed**: CA verificado como eficaz
- **Rejected**: NC considerado inválido após análise

## Reporting

Gestor SGSI reporta resumo de NCRs no Management Review trimestral:
- Novas NCs no período
- NCs fechadas no período
- NCs overdue (passaram do prazo)
- Tendências (por ISO clause, por Annex A theme, por source)

---

**Last Update**: 2026-05-26
**Next Review**: Trimestral (Management Review)
