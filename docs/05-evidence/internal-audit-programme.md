---
document_id: SGSI-AUDIT-001
title: Internal Audit Programme - Programa de Auditoria Interna
version: 1.0
date: 2026-05-26
iso_clause: "9.2"
annex_a_controls: "-"
classification: Internal
owner: Gestor SGSI
approved_by: CEO
next_review: 2026-12-31
---

# Internal Audit Programme 2026

## 1. Document Control

| Field | Value |
|-------|-------|
| Document ID | SGSI-AUDIT-001 |
| Version | 1.0 |
| Classification | Internal |
| Owner | Gestor SGSI |
| Approved By | CEO (Pendente) |
| Date Created | 2026-05-26 |
| Next Review | 2026-12-31 (Anual) |
| ISO 27001:2022 Clause | 9.2 (Internal audit) |

## 2. Purpose

Este programa define o planejamento e execução de auditorias internas do SGSI ISO 27001:2022, conforme exigido pela Cláusula 9.2.

## 3. Internal Audit Schedule 2026

| Audit | Scope | Auditor | Date | Status |
|-------|-------|---------|------|--------|
| **IA-001** | Clauses 4-5 (Context, Leadership) | External or Bekaa | Jul 2026 | Planned |
| **IA-002** | Clause 6 (Risk management) + Annex A Theme 5 | External or Bekaa | Jul 2026 | Planned |
| **IA-003** | Clauses 7-8 (Support, Operation) + Annex A Themes 6,8 | External or Bekaa | Aug 2026 | Planned |
| **IA-004** | Clauses 9-10 (Evaluation, Improvement) | External or Bekaa | Aug 2026 | Planned |

**Frequency**: Anual (cobrindo todo o SGSI em ciclo de 12 meses)

**Pre-Certification Audits**: IA-001 through IA-004 devem ser completados ANTES do Stage 1 audit externo (julho 2026).

## 4. Audit Criteria

- ISO/IEC 27001:2022 clauses 4-10
- ISO/IEC 27001:2022 Annex A (93 controls conforme SoA)
- SGSI policies and procedures (SGSI-POLICY-001, SOPs, etc.)
- Risk Register e Risk Treatment Plan
- Aplicabilidade da LGPD (dados biométricos)

## 5. Audit Process

1. **Planning** (4 weeks before): Gestor SGSI define escopo, auditor, e data
2. **Opening Meeting** (30min): Apresentar escopo e metodologia
3. **Evidence Collection** (2-4h per audit): Document review + interviews + technical verification
4. **Findings Documentation**: Usar template SGSI-AUDIT-FINDING-TEMPLATE
5. **Closing Meeting** (30min): Apresentar findings (conformities, non-conformities, observations)
6. **Audit Report** (5 days after): Gestor SGSI emite relatório formal
7. **Corrective Actions** (30-90 days): Implementar CAs para non-conformities
8. **Follow-up** (após CA deadline): Verificar eficácia das ações

## 6. Finding Classification

- **Conformity**: Control implementado e eficaz
- **Minor Non-Conformity**: Falha isolada, não afeta SGSI como um todo
- **Major Non-Conformity**: Falha sistêmica ou ausência de controle obrigatório
- **Observation**: Opportunity for improvement (não é NC)

## 7. Audit Checklist Sample

Ver anexo: `internal-audit-checklist-iso27001-2022.xlsx` (93 questions covering all Annex A controls)

## 8. Auditor Independence

Auditores NÃO podem auditar seu próprio trabalho. Para TWYN:
- **Option A**: Contratar auditor externo independente (recomendado para pre-cert)
- **Option B**: Bekaa consultant pode auditar (externa à TWYN)
- **Option C**: Se equipe crescer: peer audit (DevOps audita processos de desenvolvimento, etc.)

## 9. Audit Records

Manter por 3 anos:
- Audit plan
- Audit checklist (completed)
- Evidence collected (screenshots, documents, interview notes)
- Audit report
- Corrective action plan + follow-up verification

**Storage**: `docs/05-evidence/internal-audits/2026/`

## 10. Approval

| Field | Value |
|-------|-------|
| **Prepared By** | Security Consultant |
| **Approved By** | CEO (Pendente) |
| **Effective Date** | 2026-06-01 |
