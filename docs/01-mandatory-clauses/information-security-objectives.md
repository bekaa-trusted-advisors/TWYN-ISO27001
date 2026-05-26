---
document_id: SGSI-OBJ-001
title: Information Security Objectives - Objetivos de Segurança da Informação
version: 1.0
date: 2026-05-26
iso_clause: "6.2"
annex_a_controls: "-"
classification: Internal
owner: Gestor SGSI
approved_by: CEO
next_review: 2026-12-31
---

# Information Security Objectives 2026

## 1. Document Control

| Field | Value |
|-------|-------|
| Document ID | SGSI-OBJ-001 |
| Version | 1.0 |
| Status | Draft |
| Classification | Internal |
| Owner | Gestor SGSI |
| Approved By | CEO (Pendente) |
| Date Created | 2026-05-26 |
| Next Review | 2026-12-31 (Anual) |
| ISO 27001:2022 Clause | 6.2 (Information security objectives and planning to achieve them) |
| Reporting Frequency | Trimestral (Management Review) |

## 2. Purpose

Este documento define os objetivos mensuráveis de segurança da informação da TWYN para o ano de 2026, conforme exigido pela Cláusula 6.2 da ISO 27001:2022. Os objetivos:

- Estão alinhados com a **Information Security Policy (SGSI-POLICY-001)**
- Suportam os requisitos de negócio e compliance (LGPD, ISO 27001, AWS FTR)
- São mensuráveis, monitorados, comunicados, e atualizados conforme necessário
- Consideram os riscos identificados no **Risk Register (SGSI-RISK-002)**

## 3. Strategic Context

### 3.1 Business Drivers

- **Certificação ISO 27001:2022**: Target Q3 2026 (Stage 2 audit em agosto 2026)
- **AWS Foundational Technical Review (FTR)**: Resolver 3 blockers críticos até junho 2026
- **LGPD Compliance**: Garantir conformidade total com dados biométricos (categoria especial)
- **Business Growth**: Escalar Face ID Platform API com segurança sem comprometer disponibilidade

### 3.2 Risk Appetite

Conforme definido na Information Security Policy:
- **CRITICAL risks (score ≥20)**: ZERO tolerance - mitigar imediatamente
- **HIGH risks (score 12-19)**: Baixo tolerance - mitigar em <90 dias
- **MEDIUM risks (score 6-11)**: Moderado - mitigar em <180 dias
- **LOW risks (score ≤5)**: Aceitar com monitoramento

## 4. Information Security Objectives 2026

### Objetivo 1: Alcançar Certificação ISO 27001:2022

**Descrição**: Obter certificação ISO/IEC 27001:2022 para a Face ID Platform API e infraestrutura AWS associada.

| Field | Value |
|-------|-------|
| **Owner** | Gestor SGSI |
| **Target Date** | 2026-09-30 |
| **Strategic Alignment** | Requisito contratual de clientes enterprise, diferencial competitivo |
| **Resources Required** | €15k-20k (auditor externo + consultor + treinamentos) |
| **Success Criteria** | Certificado ISO 27001:2022 emitido sem não-conformidades MAIORES |

**Milestones**:
- ✅ **M1.1** (2026-05-26): Documentação obrigatória completa (14 docs) - **DONE**
- 🟡 **M1.2** (2026-06-30): Implementar controles Anexo A prioritários (70% implemented/partial → 85%)
- 🟡 **M1.3** (2026-07-15): Contratar auditor de certificação
- 🟡 **M1.4** (2026-07-31): Stage 1 audit (document review)
- 🟡 **M1.5** (2026-08-31): Stage 2 audit (on-site assessment)
- 🟡 **M1.6** (2026-09-30): Certificação emitida

**KPIs**:
- % de controles Anexo A implementados: **Target: 85%** (Current: 70% per SoA)
- Número de não-conformidades MAIORES no Stage 2: **Target: 0** (Current: N/A)
- Documentação obrigatória completa: **Target: 100%** (Current: 100% ✅)

**Related Risks**: RISK-001, RISK-002, RISK-003, RISK-007 (todos os riscos CRITICAL)

---

### Objetivo 2: Resolver Blockers AWS FTR

**Descrição**: Implementar todos os controles técnicos necessários para passar no AWS Foundational Technical Review e desbloquear Advanced Tier Benefits.

| Field | Value |
|-------|-------|
| **Owner** | DevOps Lead |
| **Target Date** | 2026-06-08 |
| **Strategic Alignment** | Acesso a AWS Enterprise Support, arquitetura review, e benefícios de parceria |
| **Resources Required** | 40h DevOps time, AWS Config costs (~$50/month) |
| **Success Criteria** | AWS FTR status: PASS (todos os controles verdes) |

**Blockers Identificados** (via email da Rosa):

1. **AWS-RES_004**: Backup restoration testing - **HIGH priority**
   - Action: Testar restauração de RDS snapshot + S3 recovery
   - Owner: DevOps Lead
   - Due: 2026-06-05

2. **AWS-SUP_001**: AWS Support level decision - **HIGH priority**
   - Action: Upgrade para Business Support (ou documentar justificativa para Developer)
   - Owner: CEO + Finance
   - Due: 2026-06-05

3. **AWS-CIS**: 8 CIS controls missing + tmpsaasboost key >90 days - **CRITICAL (FTR BLOCKER)**
   - Actions:
     - Rotacionar access key tmpsaasboost (RISK-006)
     - Implementar AWS Config com CIS AWS Foundations Benchmark rules
     - Remediar 8 controles faltantes (detalhes em RISK-011)
   - Owner: DevOps Lead
   - Due: 2026-06-08

**KPIs**:
- AWS FTR controls passing: **Target: 100%** (Current: ~75% estimado)
- CIS AWS Foundations Benchmark score: **Target: ≥85%** (Current: desconhecido - implementar AWS Config)
- IAM access keys >90 days: **Target: 0** (Current: 1 - tmpsaasboost)

**Related Risks**: RISK-006, RISK-011, RISK-016, RISK-017

---

### Objetivo 3: Zero Incidentes de Segurança CRITICAL

**Descrição**: Prevenir qualquer incidente de segurança classificado como CRITICAL (biometric data breach, ransomware, account compromise) através de controles preventivos e detective.

| Field | Value |
|-------|-------|
| **Owner** | DevOps Lead |
| **Target Date** | 2026-12-31 (contínuo) |
| **Strategic Alignment** | Proteção de dados biométricos (LGPD categoria especial), reputação, e continuidade de negócio |
| **Resources Required** | AWS Security Hub + GuardDuty costs (~$200/month), pentesting (€5k anual) |
| **Success Criteria** | Zero incidentes CRITICAL em 2026; RTO/RPO conforme definido no BCP |

**Controles Implementados**:
- ✅ Encryption at-rest (S3, RDS, EBS) - AES-256
- ✅ Encryption in-transit (TLS 1.2+ only)
- ✅ GuardDuty enabled (threat detection)
- ✅ CloudTrail enabled (audit logging)
- 🟡 AWS Config (compliance monitoring) - **EM IMPLEMENTAÇÃO**
- 🟡 MFA on root account - **PENDENTE** (RISK-003)
- 🟡 Security Hub (centralized findings) - **PARCIAL**

**KPIs**:
- Incidentes CRITICAL: **Target: 0** (Current: 0 desde início do projeto)
- Mean Time to Detect (MTTD) incidents: **Target: <15min** (GuardDuty alerting)
- Mean Time to Respond (MTTR) incidents: **Target: <4h** (per escalation matrix)
- S3 buckets with public access: **Target: 0** (Current: 0 ✅ - validar mensalmente)
- Unencrypted data at-rest: **Target: 0** (Current: 0 ✅)

**Related Risks**: RISK-001 (S3 breach - score 25), RISK-007 (Ransomware - score 20), RISK-003 (Root access - score 20)

---

### Objetivo 4: Implementar Security Awareness Training

**Descrição**: Treinar 100% da equipe em security awareness para reduzir risco de phishing, credential leaks, e insider threats.

| Field | Value |
|-------|-------|
| **Owner** | Gestor SGSI |
| **Target Date** | 2026-07-31 (onboarding) + trimestral (refresh) |
| **Strategic Alignment** | Controles A.6.3 (Awareness & Training), redução de RISK-002 (insider threat) |
| **Resources Required** | Training platform (~€500/ano), 2h per employee trimestral |
| **Success Criteria** | 100% da equipe completa training inicial + refresh trimestral; <5% falha em phishing tests |

**Training Modules**:
1. **ISO 27001 Awareness** (1h) - Todos
2. **LGPD & Data Protection** (1h) - Todos
3. **Secure Coding (OWASP Top 10)** (2h) - Dev Team
4. **AWS Security Best Practices** (2h) - DevOps Lead
5. **Phishing Simulation** (mensal) - Todos

**KPIs**:
- % da equipe com training completo: **Target: 100%** (Current: 0% - novo programa)
- % de falha em phishing simulation: **Target: <5%** (Baseline: desconhecido)
- Incidentes causados por erro humano: **Target: <2/ano** (Current: N/A)
- Time to complete mandatory training: **Target: <30 dias após onboarding**

**Related Risks**: RISK-002 (Insider threat), RISK-013 (Insecure code), RISK-014 (Phishing)

---

### Objetivo 5: Reduzir Single Point of Failure (DevOps)

**Descrição**: Mitigar RISK-015 (DevOps Lead como SPOF) através de documentação, backup, e redistribuição de responsabilidades.

| Field | Value |
|-------|-------|
| **Owner** | CEO |
| **Target Date** | 2026-08-31 |
| **Strategic Alignment** | Business continuity, conhecimento distribuído, redução de key person risk |
| **Resources Required** | Contratar Junior DevOps ou SRE (€40k-50k/ano), 20h documentação de runbooks |
| **Success Criteria** | Pelo menos 1 pessoa adicional capaz de executar operações críticas (deploy, incident response, DR) |

**Actions**:
- 🟡 Contratar Junior DevOps / SRE (Q2 2026)
- 🟡 Documentar runbooks para operações críticas (deploy, rollback, incident response, DR)
- 🟡 Implementar princípio de least privilege (reduzir escopo de acesso do DevOps Lead)
- 🟡 Cross-training: Dev Team aprende operações básicas AWS

**KPIs**:
- Número de pessoas capazes de executar operações críticas: **Target: ≥2** (Current: 1)
- % de runbooks documentados: **Target: 100% das operações críticas** (Current: 0%)
- Tempo médio para onboarding de novo DevOps: **Target: <30 dias** (Current: desconhecido)

**Related Risks**: RISK-015 (SPOF - score 12)

---

### Objetivo 6: Manter RPO <4h e RTO <8h

**Descrição**: Garantir que backups e disaster recovery atendam aos objetivos de negócio para disponibilidade e resiliência.

| Field | Value |
|-------|-------|
| **Owner** | DevOps Lead |
| **Target Date** | 2026-06-30 (validar) + contínuo |
| **Strategic Alignment** | Business continuity (A.5.29-5.30), disponibilidade contratual para clientes |
| **Resources Required** | AWS backup costs (~$100/month), DR testing quarterly (4h DevOps time) |
| **Success Criteria** | RPO <4h e RTO <8h validados via DR testing; backups testados trimestralmente |

**Controles Implementados**:
- ✅ RDS automated backups (daily, 7-day retention)
- ✅ S3 versioning + cross-region replication (us-west-2)
- ✅ EKS cluster state backup (via Terraform)
- 🟡 DR runbook documentado - **PENDENTE**
- 🟡 DR testing schedule (trimestral) - **PENDENTE** (AWS FTR blocker)

**KPIs**:
- Backup success rate: **Target: 100%** (Current: 100% - validar via CloudWatch metrics)
- DR test frequency: **Target: Trimestral** (Current: Nunca testado - AWS-RES_004)
- Measured RTO (last DR test): **Target: <8h** (Current: N/A)
- Measured RPO (last DR test): **Target: <4h** (Current: N/A)
- Backup verification failures: **Target: 0** (Current: 0)

**Related Risks**: RISK-017 (Backup/DR failure - score 12), RISK-007 (Ransomware - score 20)

---

## 5. Resource Allocation

| Objetivo | Resource Type | Estimated Cost | Status |
|----------|--------------|----------------|--------|
| Obj 1: ISO 27001 Certification | Auditor + Consultant + Training | €15k-20k | Budget approval pending |
| Obj 2: AWS FTR | AWS Config (~$50/month) | €600/ano | Approved |
| Obj 3: Zero Critical Incidents | GuardDuty + Security Hub + Pentesting | €3k/ano | Approved |
| Obj 4: Security Awareness | Training platform | €500/ano | Budget approval pending |
| Obj 5: Reduce SPOF | Junior DevOps hire | €40k-50k/ano | Budget approval pending |
| Obj 6: RPO/RTO | Backup storage + DR testing | €1.5k/ano | Approved |
| **TOTAL** | | **€60k-75k/ano** | |

## 6. Monitoring and Reporting

### 6.1 Reporting Cadence

| Audience | Report Type | Frequency | Owner |
|----------|-------------|-----------|-------|
| CEO + Leadership | Executive Dashboard (high-level KPIs) | Mensal | Gestor SGSI |
| Management Review | Detailed Objective Progress Report | Trimestral | Gestor SGSI |
| DevOps Team | Technical Security Metrics | Semanal | DevOps Lead |
| Auditor | Objective Achievement Evidence | Ad-hoc (audit) | Gestor SGSI |

### 6.2 KPI Dashboard (2026)

| KPI | Target | Q1 2026 | Q2 2026 | Q3 2026 | Q4 2026 |
|-----|--------|---------|---------|---------|---------|
| % Annex A controls implemented | 85% | 70% | - | - | - |
| ISO 27001 certification | Yes | - | In progress | PASS | Maintain |
| AWS FTR status | PASS | Fail | - | - | - |
| Critical incidents | 0 | 0 | - | - | - |
| Security awareness training completion | 100% | 0% | - | - | - |
| SPOF mitigation (people count) | ≥2 | 1 | - | - | - |
| Backup testing frequency | Quarterly | 0 | - | - | - |

## 7. Review and Update Process

### 7.1 Objective Review Schedule

- **Trimestral**: Management Review meeting - avaliar progresso de cada objetivo
- **Anual**: Definir novos objetivos para o ano seguinte (dezembro)
- **Ad-hoc**: Se mudanças significativas no contexto (novo risco CRITICAL, mudança regulatória, etc.)

### 7.2 Adjustment Criteria

Objetivos podem ser ajustados se:
- Novos riscos CRITICAL são identificados
- Mudanças regulatórias (LGPD, ISO 27001:2025 draft, etc.)
- Feedback de auditoria exige repriorização
- Recursos aprovados são significativamente diferentes do planejado
- Business context muda (M&A, novos clientes, novos produtos)

## 8. Alignment with ISO 27001:2022 Clauses

| Objetivo | ISO Clause | Annex A Controls | Risk Register |
|----------|------------|------------------|---------------|
| Obj 1: ISO 27001 Certification | 4.1-10 (todos) | Todos os 93 controles | Todos os riscos |
| Obj 2: AWS FTR | 8.1 (Operation) | A.5.19-5.22 (Suppliers), A.8.9 (Config mgmt) | RISK-006, RISK-011, RISK-016, RISK-017 |
| Obj 3: Zero Critical Incidents | 8.1, 9.1 | A.5.24-5.28 (Incident mgmt), A.8.16 (Monitoring) | RISK-001, RISK-003, RISK-007 |
| Obj 4: Security Awareness | 7.2, 7.3 | A.6.3 (Awareness & training) | RISK-002, RISK-013, RISK-014 |
| Obj 5: Reduce SPOF | 7.1, 7.2 | A.5.2 (IS roles), A.6.1-6.2 (Screening, terms) | RISK-015 |
| Obj 6: RPO/RTO | 8.1 | A.5.29-5.30 (BC/DR), A.8.13-8.14 (Backup) | RISK-017 |

## 9. Approval

| Field | Value |
|-------|-------|
| **Prepared By** | Security Consultant (Bekaa) |
| **Reviewed By** | Gestor SGSI (Pendente) |
| **Approved By** | CEO (Pendente) |
| **Approval Date** | Pendente |
| **Effective Date** | Após aprovação CEO |
| **Next Review** | 2026-12-31 (Anual) |

---

## 10. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-05-26 | Security Consultant | Versão inicial - 6 objetivos estratégicos com KPIs mensuráveis alinhados ao Risk Register e ISO 27001:2022 |

---

**⚠️ AÇÃO OBRIGATÓRIA**: Este documento requer aprovação formal do CEO conforme Cláusula 6.2. Os objetivos devem ser comunicados a todos os stakeholders relevantes e revisados trimestralmente no Management Review.
