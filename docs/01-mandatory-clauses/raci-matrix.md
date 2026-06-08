---
document_id: SGSI-RACI-001
title: RACI Matrix - Roles e Responsabilidades SGSI
version: 1.0
date: 2026-06-02
iso_clause: "5.3, 7.2"
annex_a_controls: "A.5.2, A.6.1"
classification: Internal
owner: Ricardo Esper (Bekaa Trusted Advisors) - Gestor SGSI
approved_by: CEO
next_review: 2026-08-26
---

# RACI Matrix - Sistema de Gestão de Segurança da Informação

## 1. Document Control

| Field | Value |
|-------|-------|
| Document ID | SGSI-RACI-001 |
| Version | 1.0 |
| Status | Draft |
| Classification | Internal |
| Owner | Gestor SGSI |
| Approved By | CEO (Pendente) |
| Date Created | 2026-05-26 |
| Next Review | 2026-08-26 |
| ISO 27001:2022 Clause | 5.3 (Organizational roles), 7.2 (Competence) |
| Annex A Controls | A.5.2 (Information security roles), A.6.1 (Screening) |

## 2. Purpose

Este documento define as responsabilidades e papéis para o Sistema de Gestão de Segurança da Informação (SGSI) da TWYN, utilizando o modelo RACI para garantir clareza sobre quem é:

- **R** (Responsible): Responsável pela execução da tarefa
- **A** (Accountable): Autoridade final que aprova e responde pelos resultados (apenas 1 por atividade)
- **C** (Consulted): Consultado antes de decisão ou ação (comunicação bidirecional)
- **I** (Informed): Informado após decisão ou ação (comunicação unidirecional)

## 3. Scope

Esta matriz cobre todas as atividades relacionadas ao SGSI ISO 27001:2022, incluindo:
- Cláusulas obrigatórias (4-10)
- Processos de gestão de riscos
- Controles Anexo A implementados
- Atividades operacionais de segurança
- Auditoria e melhoria contínua

## 4. Roles Defined

### 4.1 Papéis Internos

| Papel | Descrição | Pessoa/Equipe |
|-------|-----------|---------------|
| **CEO** | Chief Executive Officer - Autoridade máxima, responsável por aprovar políticas e alocar recursos | A definir |
| **DevOps Lead** | Líder técnico responsável pela infraestrutura AWS, segurança de rede, e implementação de controles técnicos. Atua como ponto focal técnico interno do SGSI, reportando ao Gestor SGSI em assuntos de segurança da informação | A definir |
| **Dev Team** | Equipe de desenvolvimento responsável pelo código da Face ID Platform API | A definir |
| **DPO/Legal** | Data Protection Officer / Jurídico - Responsável por LGPD, contratos, e compliance legal | A definir (pode ser externo) |
| **HR/People Ops** | Recursos Humanos - Responsável por onboarding/offboarding, treinamentos, e controles de pessoal | A definir |
| **Finance** | Financeiro - Responsável por contratos de fornecedores, seguros, e orçamento de SI | A definir |

### 4.2 Papéis Externos (inclui Gestor SGSI — modelo híbrido)

> **Nota — Modelo Híbrido:** O Gestor SGSI é exercido por consultor externo (terceiro), conforme permitido pela ISO 27001:2022, Cláusula 5.3. O DevOps Lead atua como ponto focal técnico interno. Este modelo foi adotado para garantir expertise especializada, independência na avaliação de riscos e auditorias, e eficiência operacional. A nomeação formal consta na Carta de Nomeação SGSI-EVIDENCE-NOM-001.

| Papel | Descrição | Fornecedor |
|-------|-----------|------------|
| **Gestor SGSI** | ISMS Manager (terceiro/híbrido) — Coordena e gerencia todo o SGSI, ponto focal para certificação ISO 27001. Responsável pela gestão de riscos, auditoria interna, conformidade normativa e reporte direto ao CEO. Nomeação formal: SGSI-EVIDENCE-NOM-001 | Ricardo Esper (Bekaa Trusted Advisors) |
| **External Auditor** | Auditor de certificação ISO 27001:2022 (Stage 1 e Stage 2) | A contratar (Q2 2026) |
| **AWS Support** | Suporte técnico da AWS (Business Support recomendado) | AWS |
| **Penetration Tester** | Empresa de pentesting para testes de intrusão anuais | A contratar (Q3 2026) |

## 5. RACI Matrix

### 5.1 Cláusula 4: Contexto da Organização

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | DPO/Legal | HR | Finance | External Auditor |
|-----------|-----|-------------|-------------|----------|-----------|----|---------|--------------------|
| Definir escopo do SGSI (4.3) | A | R | C | I | C | I | I | - |
| Identificar partes interessadas (4.2) | C | R/A | C | I | C | I | I | - |
| Determinar requisitos legais e regulatórios | C | R | C | I | A | I | I | - |
| Revisar escopo anualmente | A | R | C | I | C | I | I | - |

### 5.2 Cláusula 5: Liderança

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | DPO/Legal | HR | Finance | External Auditor |
|-----------|-----|-------------|-------------|----------|-----------|----|---------|--------------------|
| Aprovar Política de SI (5.2) | **A** | R | C | I | C | I | I | - |
| Assinar Política de SI (obrigatório) | **R** | C | I | I | I | I | I | - |
| Comunicar Política de SI (5.2) | I | R/A | R | R | I | R | I | - |
| Alocar recursos para SGSI (5.1) | A | R | C | I | I | I | R | - |
| Atribuir roles e responsabilidades (5.3) | A | R | C | I | I | C | I | - |
| Demonstrar comprometimento da liderança | R/A | R | I | I | I | I | I | - |

### 5.3 Cláusula 6: Planejamento

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | DPO/Legal | HR | Finance | Security Consultant |
|-----------|-----|-------------|-------------|----------|-----------|----|---------|--------------------|
| Realizar risk assessment (6.1.2) | I | A | R | C | C | I | I | C |
| Aprovar risk treatment plan (6.1.3) | A | R | C | I | C | I | I | C |
| Elaborar Statement of Applicability (6.1.3d) | C | A | R | I | C | I | I | C |
| Definir objetivos de SI (6.2) | A | R | C | I | I | I | I | - |
| Planejar mudanças no SGSI (6.3) | A | R | R | C | I | I | C | - |
| Revisar riscos trimestralmente | C | A | R | I | I | I | I | - |

### 5.4 Cláusula 7: Suporte

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | DPO/Legal | HR | Finance | External Auditor |
|-----------|-----|-------------|-------------|----------|-----------|----|---------|--------------------|
| Aprovar orçamento de SI (7.1) | A | R | C | I | I | I | R | - |
| Avaliar competências (7.2) | C | R | I | I | I | A | I | - |
| Conduzir treinamento de conscientização (7.3) | I | R/A | C | R | C | C | I | - |
| Gerenciar documentação do SGSI (7.5) | I | A | R | C | I | I | I | - |
| Controlar versões de documentos | I | R/A | C | C | I | I | I | - |

### 5.5 Cláusula 8: Operação

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | DPO/Legal | HR | Finance | External Auditor |
|-----------|-----|-------------|-------------|----------|-----------|----|---------|--------------------|
| Executar risk assessment (8.2) | I | A | R | C | C | I | I | - |
| Implementar controles técnicos (8.3) | I | C | A | R | I | I | I | - |
| Gerenciar mudanças em produção | I | C | A | R | I | I | I | - |
| Responder a incidentes de SI | I | A | R | R | C | I | I | - |
| Gerenciar acessos e permissões | I | C | A | R | I | C | I | - |

### 5.6 Cláusula 9: Avaliação de Desempenho

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | DPO/Legal | HR | Finance | External Auditor |
|-----------|-----|-------------|-------------|----------|-----------|----|---------|--------------------|
| Monitorar KPIs de SI (9.1) | I | R/A | R | C | I | I | I | - |
| Planejar auditoria interna (9.2.1) | C | A | I | I | I | I | I | - |
| Executar auditoria interna (9.2.2) | I | R | C | C | I | I | I | C |
| Conduzir management review (9.3) | A | R | C | I | I | I | I | - |
| Analisar resultados de auditorias | C | A | R | I | I | I | I | - |

### 5.7 Cláusula 10: Melhoria

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | DPO/Legal | HR | Finance | External Auditor |
|-----------|-----|-------------|-------------|----------|-----------|----|---------|--------------------|
| Registrar não-conformidades (10.1) | I | R/A | R | R | I | I | I | - |
| Implementar ações corretivas (10.2) | C | A | R | R | I | I | I | - |
| Propor melhorias contínuas (10.3) | C | A | R | C | C | C | C | - |
| Acompanhar plano de ação corretiva | I | R/A | R | C | I | I | I | - |

## 6. Processos Operacionais de Segurança

### 6.1 Gestão de Riscos

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | DPO/Legal | Security Consultant |
|-----------|-----|-------------|-------------|----------|-----------|---------------------|
| Identificar novos riscos | I | R | R | C | C | C |
| Avaliar likelihood × impact | I | R/A | R | C | I | C |
| Selecionar tratamento de risco | A | R | C | I | C | C |
| Implementar controles mitigadores | I | C | A | R | I | C |
| Monitorar riscos residuais | I | R/A | R | I | I | I |
| Atualizar risk register trimestralmente | I | R/A | R | I | I | C |

### 6.2 Gestão de Incidentes (A.5.24-5.28)

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | DPO/Legal | HR |
|-----------|-----|-------------|-------------|----------|-----------|-----|
| Detectar incidente de SI | I | I | R | R | I | I |
| Classificar severidade do incidente | I | R | R/A | C | C | I |
| Responder e conter incidente | I | C | A | R | I | I |
| Investigar causa raiz | I | R | R/A | C | I | I |
| Notificar partes afetadas (se LGPD aplicável) | C | R | C | I | A | I |
| Documentar lições aprendidas | I | R/A | R | C | I | I |
| Reportar para ANPD (se <72h, LGPD) | A | R | C | I | R | I |

### 6.3 Gestão de Acessos (A.5.15-5.18)

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | HR |
|-----------|-----|-------------|-------------|----------|-----|
| Provisionar novos acessos (onboarding) | I | C | R | I | A |
| Revogar acessos (offboarding) | I | C | R | I | A |
| Revisar permissões trimestralmente (IAM recertification) | I | R | A | C | C |
| Aprovar acesso privilegiado (root, admin) | A | R | R | I | I |
| Auditar logs de acesso (CloudTrail) | I | R | A | C | I |
| Rotacionar credenciais (90 dias) | I | C | A | R | I |

### 6.4 Gestão de Mudanças (A.8.32)

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team |
|-----------|-----|-------------|-------------|----------|
| Submeter change request | I | I | C | R |
| Avaliar impacto de SI da mudança | I | R | R/A | C |
| Aprovar mudança crítica (produção) | I | C | A | I |
| Testar mudança em staging | I | I | R | R/A |
| Executar mudança em produção | I | C | A | R |
| Validar pós-deploy | I | C | R | A |
| Documentar mudança (changelog) | I | I | R | R/A |

### 6.5 Gestão de Fornecedores (A.5.19-5.22)

| Atividade | CEO | Gestor SGSI | DevOps Lead | Finance | DPO/Legal |
|-----------|-----|-------------|-------------|---------|-----------|
| Identificar fornecedores críticos | I | R | R/A | C | I |
| Avaliar risco de fornecedor (due diligence) | I | R/A | R | C | C |
| Negociar cláusulas de SI em contratos | C | R | C | C | A |
| Monitorar compliance de fornecedores | I | R/A | R | I | C |
| Revisar contratos anualmente | A | R | C | R | C |

### 6.6 Backup e Recuperação (A.8.13, A.8.14)

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team |
|-----------|-----|-------------|-------------|----------|
| Configurar backups automatizados | I | C | A | R |
| Testar restauração de backup (trimestral) | I | R | A | R |
| Documentar Recovery Time Objective (RTO) | C | R/A | R | C |
| Documentar Recovery Point Objective (RPO) | C | R/A | R | C |
| Armazenar backups em região diferente | I | C | A | R |
| Criptografar backups (AES-256) | I | C | A | R |

### 6.7 Continuidade de Negócios (A.5.29-5.30)

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | Finance |
|-----------|-----|-------------|-------------|----------|---------|
| Desenvolver Business Continuity Plan (BCP) | A | R | R | C | C |
| Identificar processos críticos | C | R/A | R | I | I |
| Definir estratégias de recuperação | C | R | R/A | C | I |
| Testar BCP anualmente | A | R | R | R | I |
| Atualizar BCP após incidentes | C | R/A | R | C | I |

## 7. Annex A Control Themes

### 7.1 Theme 5: Organizational Controls (37 controles)

| Área de Controle | Primary Responsible | Accountable | Consulted | Informed |
|------------------|---------------------|-------------|-----------|----------|
| A.5.1 Policies (IS Policy) | Gestor SGSI | CEO | DevOps Lead, DPO/Legal | All Staff |
| A.5.2-5.6 Roles, Assets, Access | Gestor SGSI | DevOps Lead | HR | All Staff |
| A.5.7 Threat Intelligence | DevOps Lead | Gestor SGSI | Security Consultant | - |
| A.5.8 Project Management | Gestor SGSI | DevOps Lead | Dev Team | - |
| A.5.9-5.12 Asset Management | DevOps Lead | Gestor SGSI | Finance | - |
| A.5.13-5.18 Access Control | DevOps Lead | Gestor SGSI | HR | - |
| A.5.19-5.22 Supplier Security | Gestor SGSI | Finance | DPO/Legal, DevOps Lead | - |
| A.5.23 Cloud Services Security | DevOps Lead | Gestor SGSI | Security Consultant | - |
| A.5.24-5.28 Incident Management | DevOps Lead | Gestor SGSI | DPO/Legal | CEO |
| A.5.29-5.30 BC/DR | Gestor SGSI | CEO | DevOps Lead, Finance | - |

### 7.2 Theme 6: People Controls (8 controles)

| Área de Controle | Primary Responsible | Accountable | Consulted | Informed |
|------------------|---------------------|-------------|-----------|----------|
| A.6.1 Screening (background check) | HR | HR | Gestor SGSI | - |
| A.6.2 Terms of Employment | HR | DPO/Legal | Gestor SGSI | - |
| A.6.3 Awareness & Training | Gestor SGSI | HR | DevOps Lead | All Staff |
| A.6.4 Disciplinary Process | HR | CEO | DPO/Legal | - |
| A.6.5-6.6 Offboarding | HR | DevOps Lead | Gestor SGSI | Finance |
| A.6.7 Remote Work | DevOps Lead | Gestor SGSI | HR | Dev Team |
| A.6.8 Event Reporting | All Staff | Gestor SGSI | DevOps Lead | - |

### 7.3 Theme 7: Physical Controls (14 controles)

| Área de Controle | Primary Responsible | Accountable | Consulted | Informed |
|------------------|---------------------|-------------|-----------|----------|
| A.7.1-7.14 Physical Security | N/A (Cloud-only) | AWS | Gestor SGSI | - |
| A.7.7 Clear Desk/Clear Screen | All Staff | HR | Gestor SGSI | - |
| A.7.14 Secure Disposal (data destruction) | DevOps Lead | Gestor SGSI | - | - |

### 7.4 Theme 8: Technological Controls (34 controles)

| Área de Controle | Primary Responsible | Accountable | Consulted | Informed |
|------------------|---------------------|-------------|-----------|----------|
| A.8.1-8.8 User Endpoints, Mobile | Dev Team | DevOps Lead | Gestor SGSI | - |
| A.8.9-8.12 Configuration, Deletion, Masking | DevOps Lead | Gestor SGSI | Dev Team | - |
| A.8.13-8.14 Backup & Redundancy | DevOps Lead | Gestor SGSI | - | - |
| A.8.15-8.19 Logging & Monitoring | DevOps Lead | Gestor SGSI | Security Consultant | - |
| A.8.20-8.23 Network Security, Web Filtering | DevOps Lead | Gestor SGSI | - | - |
| A.8.24 Cryptography | DevOps Lead | Gestor SGSI | Security Consultant | - |
| A.8.25-8.28 Secure SDLC, Secure Coding | Dev Team | DevOps Lead | Gestor SGSI | - |
| A.8.29-8.34 Testing, Vulnerability Management | DevOps Lead | Gestor SGSI | Pentester | - |

## 8. Certification Process

| Atividade | CEO | Gestor SGSI | DevOps Lead | Dev Team | Security Consultant | External Auditor |
|-----------|-----|-------------|-------------|----------|---------------------|-------------------|
| Preparar documentação obrigatória | I | R/A | R | C | C | - |
| Contratar auditor de certificação | A | R | I | I | C | - |
| Coordenar Stage 1 audit (document review) | C | R/A | C | I | C | R |
| Implementar ações corretivas pré-Stage 2 | C | A | R | R | C | I |
| Coordenar Stage 2 audit (on-site) | C | R/A | R | C | C | R |
| Responder a não-conformidades | C | A | R | R | C | C |
| Receber certificado ISO 27001:2022 | R | R/A | I | I | I | R |
| Surveillance audits (anuais) | C | R/A | R | I | I | R |

## 9. Competency Requirements

| Papel | Competências Obrigatórias | Treinamentos Recomendados | Frequência |
|-------|---------------------------|---------------------------|------------|
| **CEO** | Entendimento de SI, comprometimento visível | Awareness básico ISO 27001 | Anual |
| **Gestor SGSI** | ISO 27001 Lead Implementer, gestão de riscos, auditoria | ISO 27001 Lead Implementer (40h), ISO 31000 | Certificação obrigatória |
| **DevOps Lead** | AWS security, hardening, logging, IaC | AWS Security Specialty, CIS Benchmarks | Semestral |
| **Dev Team** | Secure coding (OWASP Top 10), SAST/DAST | OWASP Secure Coding, DevSecOps | Anual |
| **DPO/Legal** | LGPD, GDPR, contratos de SI | LGPD Foundation, ISO 27701 | Anual |
| **HR** | Onboarding/Offboarding SI, background checks | Security Awareness for HR | Anual |
| **All Staff** | Security awareness, phishing, password hygiene | Security Awareness Training | Trimestral |

## 10. Escalation Matrix

| Situação | Primeiro Nível | Segundo Nível | Terceiro Nível | SLA |
|----------|----------------|---------------|----------------|-----|
| **Incidente CRÍTICO** (biometric data breach) | DevOps Lead | Gestor SGSI | CEO + DPO/Legal | Imediato (<1h) |
| **Incidente ALTO** (produção indisponível) | DevOps Lead | Gestor SGSI | CEO | <4h |
| **Incidente MÉDIO** (falha de controle) | DevOps Lead | Gestor SGSI | - | <24h |
| **Incidente BAIXO** (security event) | DevOps Lead | Gestor SGSI | - | <72h |
| **Auditoria - Não-conformidade MAIOR** | Gestor SGSI | CEO | External Auditor | <30 dias |
| **Auditoria - Não-conformidade MENOR** | Gestor SGSI | DevOps Lead | - | <90 dias |
| **Mudança em ISMS Scope** | Gestor SGSI | CEO | External Auditor | Aprovação formal |
| **Violação LGPD** | DPO/Legal | CEO | ANPD | <72h |

## 11. Decision Authority

### 11.1 Decisões que REQUEREM aprovação do CEO

- ✅ Aprovação da Política de Segurança da Informação (obrigatória para ISO)
- ✅ Assinatura da Política de SI (requisito de auditoria)
- ✅ Alocação de orçamento significativo (>10k USD)
- ✅ Mudanças no escopo do SGSI
- ✅ Aceitação de riscos CRÍTICOS (score ≥20)
- ✅ Contratação do auditor de certificação
- ✅ Decisão de não implementar controle obrigatório
- ✅ Resposta a incidentes com impacto legal/financeiro significativo

### 11.2 Decisões que REQUEREM aprovação do Gestor SGSI

- Aprovação de risk treatment plan
- Aprovação de Statement of Applicability (SoA)
- Aprovação de novas políticas ou SOPs
- Aceitar riscos MÉDIOS ou BAIXOS
- Implementar novos controles técnicos
- Mudanças em processos do SGSI
- Plano de auditoria interna
- Ações corretivas de auditoria

### 11.3 Decisões que REQUEREM aprovação do DevOps Lead

- Mudanças críticas em produção
- Implementação de controles técnicos AWS
- Aprovação de configurações de segurança
- Permissões de acesso privilegiado (não-root)
- Arquitetura de rede e firewall rules
- Configuração de logging e monitoring

## 12. Communication Plan

| Evento | Quem Comunica | Para Quem | Método | Frequência |
|--------|---------------|-----------|--------|------------|
| Management Review | Gestor SGSI | CEO, Leadership | Reunião formal + relatório | Trimestral |
| Risk Register Updates | Gestor SGSI | CEO, DevOps Lead | Email + dashboard | Mensal |
| Security Incidents | DevOps Lead | Gestor SGSI, CEO (se crítico) | Ticket + Slack | Imediato |
| Audit Findings | External Auditor | Gestor SGSI, CEO | Relatório formal | Pós-auditoria |
| Policy Changes | Gestor SGSI | All Staff | Email + intranet | Ad-hoc |
| Security Awareness | Gestor SGSI | All Staff | Training platform | Trimestral |
| Compliance Status | Gestor SGSI | CEO | Dashboard + slides | Mensal |

## 13. Approval and Review

| Field | Value |
|-------|-------|
| **Document Prepared By** | Security Consultant (Bekaa) |
| **Document Reviewed By** | Ricardo Esper — Gestor SGSI (Bekaa Trusted Advisors) |
| **Document Approved By** | CEO (Pendente) |
| **Approval Date** | Pendente |
| **Effective Date** | Após aprovação CEO |
| **Next Review Date** | 2026-08-26 (3 meses) |
| **Distribution List** | CEO, Gestor SGSI, DevOps Lead, HR, All Management |

---

## 14. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-05-26 | Security Consultant | Versão inicial - RACI completo cobrindo Cláusulas 4-10, Anexo A, e processos operacionais |
| 1.1 | 2026-06-02 | Ricardo Esper (Bekaa) | Formalização do Gestor SGSI: Ricardo Esper (Bekaa Trusted Advisors) designado como Gestor SGSI sob modelo híbrido (terceiro). Atualização de papéis, contatos de emergência e referência à Carta de Nomeação SGSI-EVIDENCE-NOM-001 |

---

## 15. Anexos

### Anexo A: Exemplo de Aplicação RACI

**Cenário**: Implementar controle A.8.9 (Configuration Management) para atender AWS FTR

**RACI aplicado**:
- **R** (Responsible): DevOps Lead - Implementa AWS Config, documenta baselines, corrige drifts
- **A** (Accountable): Gestor SGSI - Aprova plano, valida evidências, assina off
- **C** (Consulted): Security Consultant - Aconselha sobre CIS benchmarks e AWS Config rules
- **I** (Informed): CEO, Finance - Notificados sobre custos e status de implementação

### Anexo B: Contatos de Emergência

| Papel | Nome | Email | Telefone | Disponibilidade |
|-------|------|-------|----------|-----------------|
| CEO | A definir | - | - | 24/7 (crítico) |
| Gestor SGSI | Ricardo Esper (Bekaa Trusted Advisors) | resper@bekaa.eu | - | Horário comercial; estendida para incidentes críticos |
| DevOps Lead | A definir | - | - | 24/7 (on-call) |
| DPO/Legal | A definir | - | - | Horário comercial |
| AWS Support | AWS | via Console | - | 24/7 (Business Support) |

---

**⚠️ AÇÃO OBRIGATÓRIA**: Este documento requer aprovação formal do CEO antes de entrar em vigor. A assinatura do CEO é requisito de auditoria ISO 27001:2022 (Cláusula 5.1).

**📋 STATUS**: DRAFT - Gestor SGSI formalizado (Ricardo Esper, Bekaa Trusted Advisors). Aguardando definição dos demais nomes/emails da equipe TWYN e aprovação do CEO.
