---
document_id: SGSI-TRAIN-001
title: Security Awareness Training Programme 2026
version: 1.0
date: 2026-05-26
iso_clause: "7.2, 7.3"
annex_a_controls: "A.6.3"
classification: Internal
owner: Gestor SGSI
approved_by: CEO
next_review: 2027-01-31
---

# Security Awareness Training Programme 2026

## 1. Document Control

| Field | Value |
|-------|-------|
| Document ID | SGSI-TRAIN-001 |
| Version | 1.0 |
| Status | Draft |
| Classification | Internal |
| Owner | Gestor SGSI (Ricardo Esper) |
| Approved By | CEO (Pendente) |
| Date Created | 2026-05-26 |
| Next Review | 2027-01-31 (Anual) |
| ISO 27001:2022 Clause | 7.2 (Competence), 7.3 (Awareness) |
| Annex A Control | A.6.3 (Information security awareness, education and training) |
| Related Documents | SGSI-COMP-001, SGSI-OBJ-001, SOP-001 |

## 2. Executive Summary

Este documento define o **Security Awareness Training Programme** da TWYN para 2026, desenhado para:

- **Objetivo**: Treinar 100% da equipe em segurança da informação até Q2 2026
- **Compliance**: Atender requisitos ISO 27001:2022 (Cláusula 7.2/7.3) e Anexo A.6.3
- **Redução de Risco**: Mitigar RISK-002 (Insider threat), RISK-013 (Insecure code), RISK-014 (Phishing)
- **Investimento**: €3,500-5,000/ano (plataforma + certificações + tempo de equipe)
- **Timeline**: Implementação em 6 semanas (kick-off 03/06/2026)

**Meta-chave**: <5% de falha em phishing simulations (baseline: unknown)

---

## 3. Programme Structure

### 3.1 Training Tracks

O programa é dividido em **4 tracks** conforme função:

| Track | Target Audience | Duration | Frequency | Priority |
|-------|----------------|----------|-----------|----------|
| **Track 1: Universal** | Todos os colaboradores | 4h | Onboarding + Anual | P0 |
| **Track 2: Development** | Dev Team | 8h | Onboarding + Bi-anual | P1 |
| **Track 3: Operations** | DevOps Lead | 12h | Onboarding + Trimestral | P0 |
| **Track 4: Leadership** | CEO + Gestor SGSI | 24h | Certification-based | P1 |

---

## 4. Track 1: Universal Training (Mandatory for ALL)

**Target**: 100% dos colaboradores (permanentes + contratados)

**Compliance**: ISO 27001:2022 Clause 7.3 (Awareness)

### 4.1 Module 1: ISO 27001 Awareness (1h)

**Objectives**:
- Entender o que é ISO 27001:2022 e por que a TWYN está buscando certificação
- Conhecer os 3 pilares da segurança: Confidencialidade, Integridade, Disponibilidade (CIA)
- Identificar papel de cada colaborador no SGSI

**Content**:
- ✅ O que é ISO 27001? (história, benefícios, requisitos)
- ✅ Estrutura do SGSI da TWYN (scope, policies, controles)
- ✅ Papéis e responsabilidades (RACI Matrix simplificado)
- ✅ Information Security Policy (highlights - versão resumida de SGSI-POLICY-001)
- ✅ Como reportar incidentes de segurança (security@twyn.com)
- ✅ Consequências de não-conformidade (audit findings, riscos)

**Format**: E-learning (vídeo + quiz interativo)

**Pass Criteria**: 80% no quiz final (10 questões)

**Frequency**:
- Onboarding (todos os novos contratados - ver SOP-001)
- Refresh anual (todos - campanhas em janeiro)

**Platform**: KnowBe4 Security Awareness Training (ver seção 7.1)

**Cost per person**: ~€20/ano

---

### 4.2 Module 2: LGPD & Data Protection (1h)

**Objectives**:
- Entender obrigações LGPD para dados biométricos (categoria especial)
- Identificar dados pessoais vs dados sensíveis
- Aplicar princípios de minimização e propósito legítimo

**Content**:
- ✅ Lei Geral de Proteção de Dados (LGPD) - overview
- ✅ Dados biométricos na Face ID Platform: categoria especial (Art. 11)
- ✅ Direitos dos titulares (acesso, retificação, eliminação, portabilidade)
- ✅ Base legal para tratamento (consentimento, contrato, legítimo interesse)
- ✅ Incident response: violação de dados = 72h para notificar ANPD
- ✅ Penalidades LGPD (até 2% do faturamento, máx R$ 50M)
- ✅ Como a TWYN protege dados (encryption at-rest/in-transit, access controls)

**Format**: E-learning (vídeo + quiz + case studies)

**Pass Criteria**: 85% no quiz final (15 questões)

**Frequency**:
- Onboarding (obrigatório)
- Refresh anual (todos - campanhas em janeiro)

**Platform**: KnowBe4 GDPR/LGPD module (customizado para Brasil)

**Cost per person**: Incluído no €20/ano

**Compliance Notes**:
- LGPD Art. 50 (boas práticas de governança) exige treinamento
- Evidência para auditor ISO 27001 (Annex A.6.3)

---

### 4.3 Module 3: Password & MFA Security (30min)

**Objectives**:
- Criar senhas fortes e únicas
- Habilitar MFA em todas as contas corporativas
- Identificar password managers seguros

**Content**:
- ✅ Anatomia de uma senha forte (≥16 chars, passphrases, generator)
- ✅ Por que NUNCA reutilizar senhas (breach databases, credential stuffing)
- ✅ Password managers recomendados (1Password, Bitwarden, LastPass)
- ✅ MFA obrigatório na TWYN (AWS, GitHub, email, Slack)
- ✅ Tipos de MFA: TOTP > SMS > Email (hierarquia de segurança)
- ✅ Como configurar MFA (tutorial passo-a-passo para cada app)

**Format**: E-learning (vídeo curto + hands-on exercise)

**Pass Criteria**: Configurar MFA em pelo menos 2 contas corporativas

**Frequency**:
- Onboarding (Day 1 - ver SOP-001)
- Refresh anual

**Platform**: In-house (tutorial interno) + KnowBe4

**Cost**: Tempo interno (~€50 para criar tutorial)

---

### 4.4 Module 4: Phishing Awareness (30min)

**Objectives**:
- Identificar emails de phishing
- Saber como reportar tentativas de phishing
- Não clicar em links ou anexos suspeitos

**Content**:
- ✅ O que é phishing? (tipos: spear phishing, whaling, vishing, smishing)
- ✅ Red flags: remetente desconhecido, urgência artificial, erros gramaticais
- ✅ Verificar links antes de clicar (hover, verificar domínio)
- ✅ Não baixar anexos suspeitos (.exe, .zip, .scr)
- ✅ Como reportar (botão "Report Phishing" no Gmail/Outlook)
- ✅ Exemplos reais de phishing campaigns na indústria tech

**Format**: E-learning + **phishing simulations mensais** (KnowBe4)

**Pass Criteria**:
- 80% no quiz
- <10% click rate em phishing simulations (meta: <5% em 6 meses)

**Frequency**:
- Onboarding
- Phishing simulations **mensais** (automated via KnowBe4)
- Remedial training para quem falha em simulation (obrigatório)

**Platform**: KnowBe4 Phishing Security Test (PST)

**Cost per person**: Incluído no €20/ano

**Success Metrics** (tracked via SGSI-COMP-001):
- Q1 2026: Baseline (desconhecido)
- Q2 2026: <10% click rate
- Q3 2026: <7% click rate
- Q4 2026: <5% click rate (target per SGSI-OBJ-001)

---

### 4.5 Module 5: Remote Work Security (30min)

**Objectives**:
- Trabalhar remotamente com segurança (laptops, Wi-Fi, acesso físico)
- Proteger devices pessoais se BYOD
- Aplicar clear desk / clear screen policy

**Content**:
- ✅ Wi-Fi seguro: evitar redes públicas sem VPN
- ✅ Encryption de disco obrigatória (BitLocker, FileVault)
- ✅ Screen lock automático (<5 min de inatividade)
- ✅ Não deixar laptops desbloqueados em cafés/coworkings
- ✅ Clear desk policy: não deixar documentos confidenciais expostos
- ✅ Backup de dados (Time Machine, OneDrive, Google Drive - encryption at-rest)
- ✅ Lost/stolen device? Reportar IMEDIATAMENTE (security@twyn.com)

**Format**: E-learning (vídeo)

**Pass Criteria**: 80% no quiz

**Frequency**: Onboarding + refresh anual

**Platform**: KnowBe4 + SOP-003 (Remote Work Security Policy)

**Cost**: Incluído no €20/ano

---

## 5. Track 2: Development Team Training

**Target**: Dev Team (programadores, QA, product)

**Compliance**: ISO 27001:2022 Annex A.8.8 (Secure development life cycle)

### 5.1 Module 6: Secure Coding - OWASP Top 10 (4h)

**Objectives**:
- Prevenir vulnerabilidades OWASP Top 10 2021
- Aplicar security-by-design em código
- Code review com foco em segurança

**Content**:
- ✅ **A01: Broken Access Control** - implement RBAC, never trust client-side checks
- ✅ **A02: Cryptographic Failures** - encrypt PII/biometric data, use TLS 1.2+
- ✅ **A03: Injection** - SQL injection, NoSQL injection, command injection, prepared statements
- ✅ **A04: Insecure Design** - threat modeling, secure architecture patterns
- ✅ **A05: Security Misconfiguration** - default credentials, unnecessary features enabled
- ✅ **A06: Vulnerable Components** - dependency scanning (npm audit, Snyk)
- ✅ **A07: Authentication Failures** - MFA, password policies, session management
- ✅ **A08: Software & Data Integrity** - code signing, supply chain security
- ✅ **A09: Logging Failures** - log security events, tamper-proof logs (CloudTrail)
- ✅ **A10: SSRF** - validate URLs, whitelist domains

**Hands-on Labs**:
- Exploit vulnerabilities em ambiente seguro (OWASP WebGoat ou Juice Shop)
- Fix vulnerabilities em sample code
- Peer code review com security checklist

**Format**: Instructor-led (online ou presencial) + labs práticos

**Pass Criteria**:
- 85% no quiz final
- Complete 5/10 labs com sucesso

**Frequency**:
- Onboarding (semana 2)
- Refresh bi-anual (atualizar para OWASP Top 10 mais recente)

**Platform**:
- OWASP WebGoat (self-hosted labs)
- Ou vendor: Secure Code Warrior, HackerOne, Pluralsight

**Cost**:
- Free (OWASP WebGoat)
- Ou €300/pessoa (Secure Code Warrior annual)

**Duration**: 4 horas (2h teoria + 2h labs)

**Related Risks**: RISK-013 (Insecure code - score 9)

---

### 5.2 Module 7: API Security Best Practices (2h)

**Objectives**:
- Proteger Face ID Platform API contra ataques comuns
- Implementar rate limiting, authentication, authorization
- Validar input rigorosamente

**Content**:
- ✅ **OWASP API Security Top 10 2023**:
  - API1: Broken Object Level Authorization (BOLA/IDOR)
  - API2: Broken Authentication
  - API3: Broken Object Property Level Authorization
  - API4: Unrestricted Resource Consumption (rate limiting)
  - API5: Broken Function Level Authorization
  - API6: Unrestricted Access to Sensitive Business Flows
  - API7: Server Side Request Forgery (SSRF)
  - API8: Security Misconfiguration
  - API9: Improper Inventory Management
  - API10: Unsafe Consumption of APIs
- ✅ JWT best practices (strong secret, short expiry, validate signature)
- ✅ Input validation (never trust client input, whitelist approach)
- ✅ Rate limiting (protect against brute force, DDoS)
- ✅ API versioning e deprecation segura
- ✅ Logging & monitoring (CloudWatch, GuardDuty alerts)

**Hands-on Lab**:
- Exploit API vulnerabilities (BOLA, broken auth) em lab environment
- Implementar rate limiting em sample API
- Review Face ID Platform API endpoints (security audit)

**Format**: Workshop técnico (hands-on)

**Pass Criteria**: Complete 3/5 labs

**Frequency**: Onboarding + anual

**Platform**: OWASP crAPI (vulnerable API for training)

**Cost**: Free (self-hosted)

**Duration**: 2 horas

---

### 5.3 Module 8: Secrets Management (1h)

**Objectives**:
- NUNCA commitar secrets em código
- Usar AWS Secrets Manager / Parameter Store
- Rotacionar secrets periodicamente

**Content**:
- ✅ O que são secrets? (API keys, passwords, certificates, tokens)
- ✅ Por que NUNCA commitar em Git? (leaks públicos, histórico permanente)
- ✅ Como usar AWS Secrets Manager:
  - Armazenar secrets
  - IAM policies para acesso granular
  - Rotação automática (RDS passwords, IAM keys)
- ✅ Como usar .env files corretamente (gitignored, encryption)
- ✅ Pre-commit hooks (detect-secrets, gitleaks) para prevenir leaks
- ✅ O que fazer se secret vazou? (rotacionar imediatamente, revoke, audit logs)

**Hands-on**:
- Configurar pre-commit hook (gitleaks)
- Armazenar um secret em AWS Secrets Manager e recuperar via API
- Simular rotação de senha RDS

**Format**: E-learning + tutorial prático

**Pass Criteria**: Complete hands-on exercise

**Frequency**: Onboarding + quando necessário

**Platform**: Tutorial interno + AWS docs

**Cost**: Tempo interno (~€100 criar tutorial)

**Duration**: 1 hora

**Related**: SOP-004 (Secrets Management)

---

## 6. Track 3: DevOps & Operations Training

**Target**: DevOps Lead (Ricardo como SPOF atual - mitigar RISK-015)

**Compliance**: ISO 27001:2022 Annex A.8.1-8.34 (Technological controls)

### 6.1 Module 9: AWS Security Best Practices (4h)

**Objectives**:
- Implementar controles de segurança AWS conforme Well-Architected Framework
- Configurar IAM, CloudTrail, GuardDuty, Config
- Resolver AWS FTR blockers

**Content**:
- ✅ **IAM Best Practices**:
  - Least privilege (granular policies)
  - MFA obrigatório (root + users)
  - Access key rotation (<90 dias)
  - Service Control Policies (SCPs) se multi-account
- ✅ **Logging & Monitoring**:
  - CloudTrail (all regions, S3 encryption)
  - CloudWatch Logs (retention 90 dias mínimo)
  - GuardDuty (threat detection)
  - AWS Config (compliance monitoring)
- ✅ **Data Protection**:
  - Encryption at-rest (S3, RDS, EBS - KMS)
  - Encryption in-transit (TLS 1.2+, ACM certificates)
  - S3 bucket policies (block public access)
- ✅ **Network Security**:
  - Security Groups (stateful, least privilege)
  - NACLs (stateless, defense in depth)
  - VPC Flow Logs (traffic analysis)
- ✅ **Incident Response**:
  - GuardDuty findings → SNS → on-call
  - Runbooks para top 5 incidents
  - Forensics (snapshot EBS, preserve logs)

**Hands-on Labs**:
- Configurar AWS Config com CIS AWS Foundations Benchmark rules
- Criar IAM policy granular para dev environment
- Simular incident response (GuardDuty finding → containment)

**Format**: AWS Training & Certification (oficial)

**Pass Criteria**: Pass AWS Certified Security - Specialty (opcional mas recomendado)

**Frequency**: Onboarding + atualização quando AWS lança novos serviços

**Platform**: AWS Training (free) + A Cloud Guru / Udemy (€40)

**Cost**:
- Training: €40 (Udemy course)
- Certification (opcional): $300 USD (~€280)

**Duration**: 4 horas (self-paced)

**Related Risks**: RISK-003, RISK-006, RISK-011, RISK-016

---

### 6.2 Module 10: CIS AWS Foundations Benchmark (3h)

**Objectives**:
- Implementar todos os controles CIS AWS Foundations Benchmark Level 1
- Resolver 8 controles faltantes (AWS FTR blocker)
- Automatizar compliance via AWS Config

**Content**:
- ✅ **Identity and Access Management** (CIS 1.x):
  - 1.4: Access keys rotated ≤90 days
  - 1.12: Root account has hardware MFA
  - 1.16: IAM policies attached only to groups/roles
- ✅ **Storage** (CIS 2.x):
  - 2.1.1: S3 buckets block public access
  - 2.1.5: S3 versioning enabled
- ✅ **Logging** (CIS 3.x):
  - 3.1: CloudTrail enabled in all regions
  - 3.4: CloudTrail log file validation enabled
  - 3.6: S3 bucket access logging enabled
- ✅ **Monitoring** (CIS 4.x):
  - 4.1-4.15: CloudWatch alarms para eventos críticos (root login, IAM changes, etc)
- ✅ **Networking** (CIS 5.x):
  - 5.1: Security groups não permitem 0.0.0.0/0 ingress
  - 5.4: VPC Flow Logs enabled

**Hands-on**:
- Implementar CIS 1.4 (rotate access key tmpsaasboost - resolver RISK-006)
- Habilitar CIS 2.1.1 (S3 block public access - já implementado)
- Configurar AWS Config Conformance Pack (cis-aws-foundations-benchmark)

**Format**: Self-paced + tutorial prático

**Pass Criteria**:
- AWS Config mostra >90% compliance em CIS Benchmark
- Resolver os 8 controles faltantes (per AWS FTR email da Rosa)

**Frequency**: Onboarding + trimestral (review compliance drift)

**Platform**: CIS Benchmark PDF (free) + AWS Config

**Cost**: AWS Config (~€50/mês - já orçado)

**Duration**: 3 horas

**Related**: CAR-003 (AWS Config implementation), SGSI-OBJ-001 (Obj 2: AWS FTR)

---

### 6.3 Module 11: Kubernetes Security (EKS) (3h)

**Objectives**:
- Hardening de EKS cluster
- RBAC, Network Policies, Pod Security Standards
- Runtime security com Falco ou GuardDuty for EKS

**Content**:
- ✅ **EKS Security Best Practices**:
  - IRSA (IAM Roles for Service Accounts) - não usar EC2 instance profiles
  - Private EKS endpoint (sem public access)
  - Encryption at-rest (Kubernetes Secrets via KMS)
  - Audit logging (EKS control plane logs → CloudWatch)
- ✅ **RBAC**:
  - Least privilege (evitar cluster-admin)
  - Namespace isolation
  - aws-auth ConfigMap (map IAM → Kubernetes RBAC)
- ✅ **Network Policies**:
  - Calico ou AWS VPC CNI Network Policies
  - Default deny ingress/egress
  - Whitelist por namespace
- ✅ **Pod Security**:
  - Pod Security Standards (Restricted profile)
  - Não rodar containers as root
  - Read-only root filesystem
  - Resource limits (CPU, memory - evitar noisy neighbor)
- ✅ **Image Security**:
  - Scan images (Trivy, Snyk, ECR image scanning)
  - Base images mínimas (Alpine, Distroless)
  - Private ECR registry (não Docker Hub público)
- ✅ **Runtime Security**:
  - GuardDuty for EKS (behavioral threat detection)
  - Falco (runtime anomaly detection)

**Hands-on Labs**:
- Criar RBAC role com least privilege
- Implementar Network Policy (deny all → whitelist Face ID API)
- Scan imagem com Trivy e corrigir vulnerabilidades CRITICAL

**Format**: Self-paced + labs

**Pass Criteria**: Complete 3/5 labs

**Frequency**: Onboarding + atualização quando Kubernetes/EKS lança novas features

**Platform**:
- EKS Best Practices Guide (AWS - free)
- Kubernetes Security Specialist (CKS) certification prep (opcional)

**Cost**:
- Free (AWS docs + hands-on)
- CKS certification (opcional): $395 USD (~€370)

**Duration**: 3 horas

---

### 6.4 Module 12: Incident Response & Forensics (2h)

**Objectives**:
- Executar playbooks de incident response
- Forensics em ambiente AWS (snapshots, logs)
- Post-incident review (RCA, CAR)

**Content**:
- ✅ **Incident Response Process** (ver SGSI-POLICY-003):
  - Detection → Classification → Containment → Eradication → Recovery → Lessons Learned
- ✅ **Runbooks para Top 5 Incidents**:
  1. S3 bucket compromise (RISK-001)
  2. GuardDuty finding: CryptoCurrency mining
  3. Unauthorized IAM access (compromised credentials)
  4. Ransomware (RISK-007)
  5. DDoS attack
- ✅ **Forensics Techniques**:
  - Snapshot EBS volumes (preserve evidence)
  - Export CloudTrail logs (tamper-proof)
  - Memory dump de EC2 instance (via SSM)
  - VPC Flow Logs analysis (identificar attacker IP)
- ✅ **Communication**:
  - Stakeholder updates (CEO, clientes se breach)
  - Legal/compliance (LGPD 72h notification se PII breach)
  - Post-incident report template

**Hands-on**:
- Simular incident: GuardDuty finding "UnauthorizedAccess:IAMUser/InstanceCredentialExfiltration"
- Executar containment: revoke IAM credentials, snapshot instance, isolate em quarantine SG
- Write post-incident report

**Format**: Tabletop exercise (simulação)

**Pass Criteria**: Complete 1 tabletop exercise

**Frequency**: Onboarding + bi-anual (refresher)

**Platform**: Tutorial interno + SGSI-POLICY-003 (Incident Response Policy)

**Cost**: Tempo interno (~€200 criar runbooks)

**Duration**: 2 horas

**Related**: SGSI-POLICY-003, SGSI-NCR-001, SGSI-CAR-001

---

## 7. Track 4: Leadership & Management Training

**Target**: CEO + Gestor SGSI (Ricardo Esper)

**Compliance**: ISO 27001:2022 Clause 5.1 (Leadership and commitment), 9.3 (Management review)

### 7.1 Module 13: ISO 27001:2022 Lead Implementer (24h)

**Objectives**:
- Certificação oficial ISO 27001 Lead Implementer
- Expertise em implementar, gerenciar, e auditar SGSI
- Capacitar Gestor SGSI para liderar projeto até certificação

**Content**:
- ✅ **Day 1-2: ISO 27001:2022 Foundations**
  - Cláusulas 4-10 (structure, context, leadership, planning, operation, evaluation, improvement)
  - Annex A.5-8 (93 controles)
  - Documentação obrigatória (14 docs)
- ✅ **Day 3: Risk Management**
  - ISO 31000 (risk management principles)
  - Risk assessment methodologies (qualitative vs quantitative)
  - Risk treatment strategies (mitigate, accept, transfer, avoid)
- ✅ **Day 4: Implementation**
  - Gap analysis
  - Project planning (timeline, resources, budget)
  - Control implementation (prioritization)
  - Change management (stakeholder buy-in)
- ✅ **Day 5: Audit & Certification**
  - Internal audit techniques
  - Management review preparation
  - Stage 1 vs Stage 2 audits
  - Handling non-conformities (NCR/CAR process)
  - Surveillance audits (anos 2-3)

**Certification Exam**:
- Written exam: 12 essay questions (3h)
- Pass criteria: ≥70%
- Valid: 3 anos (recertification required)

**Format**: Instructor-led (5 dias presenciais ou online)

**Pass Criteria**: Pass ISO 27001 Lead Implementer exam

**Frequency**:
- Gestor SGSI: Obrigatório (Q2 2026)
- CEO: Recomendado (awareness de 2 dias é suficiente)
- Recertification: a cada 3 anos

**Platform**: Certified Training Organizations (CTOs):
- **PECB** (Recommended) - €2,400
- **BSI Group** - €2,600
- **TÜV SÜD** - €2,500
- **IRCA** - €2,300

**Cost**:
- Lead Implementer (5 dias): **€2,400**
- Exam fee: Incluído
- Travel (se presencial): €500 (Lisboa ou São Paulo)

**Duration**: 40 horas (5 dias full-time)

**ROI**:
- Reduz custo de consultoria externa (€10k-15k)
- Gestor SGSI interno garante continuidade pós-certificação
- Required para manter certificação (surveillance audits anos 2-3)

**Related**: SGSI-OBJ-001 (Obj 1: ISO 27001 certification)

---

### 7.2 Module 14: LGPD Data Protection Officer (DPO) Training (16h)

**Objectives**:
- Capacitar Gestor SGSI como DPO (Data Protection Officer)
- Compliance LGPD para dados biométricos
- Gestão de incidentes de privacidade

**Content**:
- ✅ **Day 1: LGPD Foundations**
  - 10 princípios (finalidade, adequação, necessidade, transparência, etc)
  - Bases legais (Art. 7 - dados pessoais, Art. 11 - dados sensíveis)
  - Direitos dos titulares (Art. 18 - acesso, retificação, eliminação, portabilidade)
  - Agentes de tratamento (controlador vs operador)
- ✅ **Day 2: DPO Role & Responsibilities**
  - Atribuições do DPO (Art. 41)
  - Relação com ANPD (Autoridade Nacional de Proteção de Dados)
  - RIPD (Relatório de Impacto à Proteção de Dados Pessoais)
  - Canal de comunicação com titulares
- ✅ **Day 3: Technical & Organizational Measures**
  - Encryption (at-rest, in-transit)
  - Pseudonymization & anonymization
  - Access controls (least privilege)
  - Retention policies (storage limitation)
- ✅ **Day 4: Incident Management**
  - O que é uma violação de dados pessoais?
  - Obrigação de notificação (ANPD + titulares) - 72h
  - Comunicação de incidente (modelo de notificação)
  - Evidências e investigação

**Certification**: Certificado de conclusão (não há exame oficial ANPD)

**Format**: Online (2 dias)

**Pass Criteria**: Attendance + completion

**Frequency**: Obrigatório para Gestor SGSI (Q2 2026)

**Platform**:
- **Exin Privacy & Data Protection Foundation** - €800
- **IAPP CIPP/E** (adaptado para LGPD) - €1,200
- Ou curso nacional brasileiro (SENAC, FGV) - R$ 2,000-3,000 (~€350-500)

**Cost**: **€800** (Exin)

**Duration**: 16 horas (2 dias)

**Related**: SGSI-POLICY-001 (Information Security Policy - Section 8 LGPD), RISK-001 (S3 breach)

---

### 7.3 Module 15: Management Review Preparation (2h)

**Objectives**:
- CEO entende seu papel no SGSI (ISO 27001 Clause 5.1)
- Preparar inputs para Management Review trimestral
- Tomar decisões informadas sobre recursos e investimentos

**Content**:
- ✅ **CEO Responsibilities per ISO 27001**:
  - Aprovar Information Security Policy (SGSI-POLICY-001) - **CRÍTICO**
  - Commitment visível (comunicar importância à equipe)
  - Alocar recursos (€65-75k/ano para programa ISO 27001)
  - Participar de Management Reviews trimestrais (obrigatório)
  - Demonstrar liderança ao auditor (entrevista com CEO em Stage 2)
- ✅ **Management Review Inputs** (per Clause 9.3):
  - Status de ações de reviews anteriores
  - Mudanças em issues internas/externas (novos riscos, compliance changes)
  - Feedback sobre performance do SGSI (KPIs, incidents)
  - Resultados de auditorias (internas + externa)
  - NCRs/CARs abertos vs fechados
  - Oportunidades de melhoria contínua
- ✅ **Management Review Outputs**:
  - Decisões sobre melhorias necessárias
  - Decisões sobre mudanças no SGSI
  - Alocação de recursos adicionais (budget, pessoas)

**Hands-on**:
- Review template de Management Review (SGSI-MREVIEW-001)
- Prática: analisar KPI dashboard e identificar trends
- Prática: aprovar formalmente Information Security Policy (assinatura)

**Format**: Workshop executivo (presencial ou Zoom)

**Pass Criteria**: CEO assina Information Security Policy

**Frequency**:
- Onboarding (antes de Stage 1 audit)
- Refresh anual

**Platform**: Sessão interna (Gestor SGSI apresenta)

**Cost**: Tempo interno (~2h CEO + 2h Gestor SGSI)

**Duration**: 2 horas

**Critical Action**: **CEO ASSINAR SGSI-POLICY-001** - blocker para certificação

**Related**: GAP-006 (CEO signature), SGSI-MREVIEW-001

---

## 8. Training Platforms & Vendors

### 8.1 KnowBe4 Security Awareness Training

**Why KnowBe4?**
- #1 security awareness platform worldwide
- 1,000+ training modules (ISO 27001, GDPR/LGPD, phishing, passwords)
- Automated phishing simulations (mensal)
- Compliance tracking dashboard (evidência para auditor)
- SCORM-compliant (integration com LMS se necessário)

**Pricing**:
- **€20/user/year** para <50 users (TWYN qualifica)
- Inclui:
  - Biblioteca de 1,000+ módulos
  - Unlimited phishing simulations
  - Compliance reports
  - Email support

**ROI**:
- Reduz risco de phishing (RISK-014 - score 8)
- Automated training saves HR time (~€2k/ano)
- Single source of truth para compliance (ISO 27001, LGPD)

**Implementation**:
- Setup: 1 dia (admin dashboard, enroll users, schedule campaigns)
- First campaign: Semana 1 (Universal Training Track 1)
- Phishing simulations: Start Month 2 (mensal)

**Contract**: Anual (renovação automática)

**Alternatives** (se budget constraint):
- **Cofense PhishMe** (só phishing) - €10/user/year
- **SANS Security Awareness** (premium) - €40/user/year
- Free (DIY): YouTube + internal quizzes (não recomendado - sem tracking)

---

### 8.2 OWASP WebGoat / Juice Shop (Free)

**Why OWASP?**
- Hands-on learning (exploit vulnerabilities em ambiente seguro)
- Covers OWASP Top 10 2021 + API Top 10 2023
- Free, open-source, self-hosted

**Setup**:
- Docker container (5 min deploy)
- No custo (infraestrutura pode usar AWS Free Tier)

**Usage**:
- Track 2 Module 6 (Secure Coding)
- Track 2 Module 7 (API Security)

---

### 8.3 AWS Training & Certification

**Why AWS?**
- Official training (atualizado com novos serviços)
- Free tier (basics) + paid courses (advanced)
- Hands-on labs (sandbox environment)

**Relevant Courses**:
- **AWS Security Fundamentals** (free, 2h)
- **AWS Security Best Practices** (free, 4h)
- **Exam Prep: AWS Certified Security - Specialty** (€40, 10h)

**Certification** (opcional mas recomendado):
- **AWS Certified Security - Specialty** ($300 USD)
- Valid: 3 anos
- Employer pays (part of professional development budget)

---

### 8.4 PECB ISO 27001 Lead Implementer

**Why PECB?**
- Top certification body para ISO standards
- Recognized by IAF (International Accreditation Forum)
- 5-day intensive course (hands-on)

**Cost**: **€2,400** (includes exam, materials, certificate)

**Format**:
- Presencial (Lisboa: APCER, TÜV Portugal)
- Online (live instructor)

**Schedule**: Check https://pecb.com/en/education-and-certification-for-individuals/iso-iec-27001

---

## 9. Implementation Timeline

### Phase 1: Setup (Weeks 1-2) - Jun 03-14, 2026

**Actions**:
- ✅ Contratar KnowBe4 (€20/user × 10 users estimado = €200/ano)
- ✅ Setup admin dashboard (enroll users, assign roles)
- ✅ Deploy OWASP WebGoat (Docker container em AWS Free Tier)
- ✅ Criar tutorial interno (Module 3: Password/MFA, Module 8: Secrets)
- ✅ Schedule CEO signature session (Module 15 - 2h workshop)

**Deliverables**:
- KnowBe4 account ativo
- 10 users enrolled
- OWASP WebGoat acessível (internal URL)

**Owner**: Gestor SGSI

---

### Phase 2: Universal Training Rollout (Weeks 3-4) - Jun 17-28, 2026

**Actions**:
- ✅ Launch Track 1 (Modules 1-5) para TODOS os colaboradores
- ✅ Email announcement (CEO endorse a importância)
- ✅ Deadline: 2 semanas para completar (by Jun 28)
- ✅ Reminder emails (Week 3: +50% complete, Week 4: stragglers)

**Success Metric**: 100% completion rate by Jun 28

**Owner**: Gestor SGSI + HR

---

### Phase 3: Role-Specific Training (Weeks 5-8) - Jul 01-26, 2026

**Actions**:
- ✅ Track 2 (Development): Launch Modules 6-8
  - Week 5: Module 6 (OWASP Top 10 - 4h)
  - Week 6: Module 7 (API Security - 2h)
  - Week 7: Module 8 (Secrets Management - 1h)
  - Week 8: Buffer (catch-up)
- ✅ Track 3 (DevOps): Launch Modules 9-12
  - Week 5: Module 9 (AWS Security - 4h)
  - Week 6: Module 10 (CIS Benchmark - 3h)
  - Week 7: Module 11 (EKS Security - 3h)
  - Week 8: Module 12 (Incident Response - 2h)

**Success Metric**:
- Dev Team: 100% complete by Jul 26
- DevOps: 100% complete by Jul 26

**Owner**: Gestor SGSI

---

### Phase 4: Leadership Training (Weeks 6-10) - Jul 08 - Aug 02, 2026

**Actions**:
- ✅ **Week 6**: Gestor SGSI matricula em ISO 27001 Lead Implementer (5 dias - Jul 08-12)
- ✅ **Week 8**: Gestor SGSI completa DPO training (2 dias - Jul 22-23)
- ✅ **Week 9**: CEO participa de Module 15 (Management Review prep - 2h workshop - Jul 29)
- ✅ **Week 9**: **CEO ASSINA Information Security Policy** (CRITICAL - Jul 29)

**Success Metric**:
- Gestor SGSI: ISO 27001 Lead Implementer certificado
- CEO: Information Security Policy assinada (resolver GAP-006)

**Owner**: CEO + Gestor SGSI

---

### Phase 5: Continuous Operations (Aug 2026 onwards)

**Actions**:
- ✅ **Mensal**: Phishing simulations (automated via KnowBe4)
- ✅ **Trimestral**: Remedial training para quem falha em phishing (automated)
- ✅ **Trimestral**: Review training completion rates (Management Review input)
- ✅ **Anual**: Refresh training (Universal Track 1) - Janeiro 2027
- ✅ **Anual**: Update content (OWASP Top 10 2024 quando lançar)

**Success Metric**:
- Phishing click rate: <5% by Q4 2026 (per SGSI-OBJ-001)
- Training completion: 100% (no stragglers >30 dias)

**Owner**: Gestor SGSI (ongoing)

---

## 10. Budget Summary

| Item | Quantity | Unit Cost | Total | Frequency | Annual Cost |
|------|----------|-----------|-------|-----------|-------------|
| **KnowBe4** | 10 users | €20/user/year | €200 | Anual | €200 |
| **OWASP WebGoat** | Self-hosted | Free | €0 | One-time | €0 |
| **AWS Training** | 1 DevOps | €40 (Udemy) | €40 | One-time | €40 |
| **AWS Certification** (opcional) | 1 DevOps | €280 | €280 | 3 anos | €93/ano |
| **ISO 27001 Lead Implementer** | 1 Gestor SGSI | €2,400 | €2,400 | 3 anos | €800/ano |
| **LGPD DPO Training** | 1 Gestor SGSI | €800 | €800 | One-time | €800 |
| **Internal tutorials** | Dev time | ~€300 | €300 | One-time | €100/ano (maint) |
| **Employee time** | 10 people × 8h avg | ~€50/h | €4,000 | Anual | €4,000 |
| **TOTAL YEAR 1** | | | **€8,020** | | |
| **TOTAL RECURRING (Year 2+)** | | | | | **€5,133/ano** |

**Budget Breakdown**:
- **Platforms/Tools**: €240/ano (KnowBe4 + AWS)
- **Certifications**: €1,693/ano (amortized over 3 years)
- **Employee time**: €4,000/ano (8h/person × €50/h avg)

**ROI**:
- **Risk Reduction**: RISK-002 (Insider threat - €50k impact) reduced by 60% = €30k saved
- **Risk Reduction**: RISK-013 (Insecure code - €20k impact) reduced by 70% = €14k saved
- **Risk Reduction**: RISK-014 (Phishing - €15k impact) reduced by 80% = €12k saved
- **Avoided Costs**: External consultant (€10k-15k) - Gestor SGSI certificado substitui
- **Total ROI**: €56k saved / €8k invested = **7:1 ROI**

---

## 11. Compliance Mapping

### ISO 27001:2022 Clauses

| Clause | Requirement | How Training Addresses |
|--------|-------------|------------------------|
| 7.2 | Competence | Competence matrix (SGSI-COMP-001) tracks training completion |
| 7.3 | Awareness | Track 1 (Universal) ensures ALL employees aware of IS responsibilities |
| 9.3 | Management review | CEO trained (Module 15) to participate effectively |

### Annex A Controls

| Control | Title | How Training Addresses |
|---------|-------|------------------------|
| A.6.3 | Information security awareness, education and training | All 4 tracks cover this control |
| A.8.8 | Secure development life cycle | Track 2 (Modules 6-8) trains developers on secure coding |
| A.8.16 | Monitoring activities | Track 3 (Module 9) trains DevOps on CloudWatch, GuardDuty |
| A.5.24 | Information security incident management planning | Track 3 (Module 12) trains DevOps on incident response |

### Risk Register

| Risk ID | Title | Mitigation via Training |
|---------|-------|-------------------------|
| RISK-002 | Unauthorized internal access (Insider threat - score 12) | Track 1 Module 2 (LGPD) + Module 3 (Access control) |
| RISK-013 | Insecure application code (score 9) | Track 2 Modules 6-7 (OWASP Top 10, API Security) |
| RISK-014 | Phishing attack leading to credential theft (score 8) | Track 1 Module 4 (Phishing awareness + simulations) |
| RISK-015 | Single point of failure (DevOps Lead - score 12) | Track 3 (cross-train, document runbooks) |

---

## 12. Success Metrics & KPIs

### Training Completion Metrics

| Metric | Target | Measurement | Frequency |
|--------|--------|-------------|-----------|
| **Universal Training (Track 1) completion** | 100% | KnowBe4 dashboard | Onboarding + Anual |
| **Role-specific training completion** | 100% | KnowBe4 + manual tracking | Onboarding + per schedule |
| **Time to complete onboarding training** | <30 dias | SGSI-COMP-001 | Per new hire |
| **Stragglers (>30 days overdue)** | 0 | KnowBe4 dashboard | Mensal review |

### Security Behavior Metrics

| Metric | Baseline (Q2 2026) | Q3 2026 | Q4 2026 | Target |
|--------|--------------------|---------|---------| -------|
| **Phishing simulation click rate** | Unknown (estabelecer) | <10% | <7% | <5% |
| **Password reuse rate** | Unknown | <20% | <10% | <5% |
| **Incidents caused by human error** | N/A | Track | Track | <2/ano |
| **% users with MFA enabled** | ~60% (estimado) | 90% | 100% | 100% |

### Compliance Metrics

| Metric | Target | Evidence | Auditor Review |
|--------|--------|----------|----------------|
| **ISO 27001 Lead Implementer certified** | 1 (Gestor SGSI) | Certificate | Stage 1 |
| **Training records complete** | 100% | SGSI-COMP-001 | Stage 2 |
| **CEO signature on IS Policy** | Yes | SGSI-POLICY-001 signed | Stage 1 |
| **Phishing simulation program active** | Yes | KnowBe4 reports | Stage 2 |

---

## 13. Onboarding Integration (SOP-001)

Este programa de training está integrado com **SOP-001 (Onboarding/Offboarding)**:

### Day 1 (First Day)
- ✅ Welcome email com links para Track 1 (Universal Training)
- ✅ Hands-on: Configure MFA (Module 3) - OBRIGATÓRIO antes de receber acesso
- ✅ Read Information Security Policy (SGSI-POLICY-001) - assinar acceptance

### Week 1
- ✅ Complete Track 1 Modules 1-5 (4h total)
- ✅ Pass quizzes (80% minimum)
- ✅ Primeiro phishing simulation (baseline)

### Week 2
- ✅ Role-specific training begins (Track 2 ou 3 conforme função)
- ✅ Hands-on labs (OWASP, AWS, etc)

### Week 3-4
- ✅ Complete role-specific training
- ✅ Shadow senior team member (pair programming, runbooks)

### Day 30
- ✅ Checklist review (HR + Gestor SGSI)
- ✅ All training complete? (SGSI-COMP-001 updated)
- ✅ Provisioned accounts verified (MFA enabled)

---

## 14. Audit Evidence

Para demonstrar conformidade ao auditor ISO 27001 (Stage 2), mantenha evidências:

### Documentary Evidence
- ✅ Este documento (SGSI-TRAIN-001) - Training Programme aprovado
- ✅ SGSI-COMP-001 (Competence Records) - training completion per person
- ✅ Certificados de conclusão (KnowBe4, ISO 27001 Lead Implementer, DPO)
- ✅ Materiais de training (slides, videos, quizzes)

### Technical Evidence
- ✅ KnowBe4 dashboard (screenshots):
  - Training completion rates (100% target)
  - Phishing simulation results (trend: decreasing click rate)
  - Remedial training assigned
- ✅ OWASP WebGoat completion logs (dev team)
- ✅ AWS Training certificates (DevOps)

### Testimonial Evidence
- ✅ Entrevista com CEO: demonstrar commitment e awareness
- ✅ Entrevista com Gestor SGSI: demonstrar expertise (Lead Implementer)
- ✅ Entrevista com DevOps Lead: demonstrar technical competence
- ✅ Entrevista com Dev Team: demonstrar secure coding awareness

### Observational Evidence
- ✅ Auditor observa: todos os users têm MFA habilitado (compliance)
- ✅ Auditor testa: phishing simulation real-time (reaction time)
- ✅ Auditor verifica: password manager usage (1Password, Bitwarden)

---

## 15. Continuous Improvement

### Annual Review (Janeiro 2027)
- ✅ Update content: OWASP Top 10 2024 (se lançado)
- ✅ Review phishing click rate trends → ajustar dificuldade de simulations
- ✅ Survey employee feedback (training relevance, duration)
- ✅ Budget review (renovar KnowBe4, novas certificações?)

### Quarterly Metrics Review (Management Review)
- ✅ Training completion: 100%? Stragglers?
- ✅ Phishing click rate: on track para <5%?
- ✅ Incidents causados por erro humano: aceitável?
- ✅ New risks identified? (need new training modules?)

### Ad-hoc Updates
- ✅ Novo controle Annex A → criar training module
- ✅ Novo serviço AWS (ex: ECS Fargate) → update Module 9
- ✅ Incident real → criar case study para training
- ✅ Audit finding → remediate via training (se gap de competence)

---

## 16. Roles & Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Gestor SGSI** | Programa owner, track completion, report metrics, facilitate trainings, maintain SGSI-COMP-001 |
| **CEO** | Approve budget, endorse programme (email announcement), complete Module 15, sign IS Policy |
| **DevOps Lead** | Complete Track 3, mentor junior DevOps (quando contratado), maintain runbooks |
| **Dev Team** | Complete Tracks 1+2, apply secure coding practices, peer code reviews |
| **HR** | Send onboarding emails (Day 1), track completion (30-day checklist), escalate stragglers |
| **All Employees** | Complete mandatory training, report phishing attempts, follow policies |

---

## 17. Frequently Asked Questions (FAQ)

### Q1: O que acontece se eu não completar o training no prazo?
**A**:
- Onboarding: Acesso limitado até completar (security risk)
- Anual refresh: Reminder emails → escalation para manager → última advertência → disciplinary action (raro)

### Q2: Posso pular módulos que já conheço?
**A**: Não. Compliance exige evidência de completion para TODOS. Se já é expert, será rápido (provavelmente vai aceitar >90% no quiz).

### Q3: Quanto tempo preciso dedicar?
**A**:
- Universal (todos): 4h/ano
- Development: +7h (onboarding) + 4h/ano (refresh)
- DevOps: +12h (onboarding) + 6h/ano (refresh)
- Leadership: +40h (Lead Implementer - one-time)

### Q4: Posso fazer training fora do horário de trabalho?
**A**: Não recomendado. Training é parte do trabalho (paid time). Faça durante horário comercial.

### Q5: O que acontece se eu falhar no phishing simulation?
**A**:
- Primeira falha: Automated reminder (não punitivo - é treinamento)
- Falhas repetidas (>3x): Remedial training obrigatório (30 min extra)
- Objetivo: educar, não punir

### Q6: A certificação ISO 27001 Lead Implementer é obrigatória para todos?
**A**: Não. Apenas para Gestor SGSI (obrigatório) e CEO (recomendado mas não obrigatório - awareness de 2 dias é suficiente).

### Q7: Quem paga pelas certificações?
**A**: Employer (TWYN/Bekaa) paga certificações relacionadas ao trabalho (ISO 27001, AWS, DPO). Budget aprovado: €3,500 (ano 1).

### Q8: Posso usar este training para CPD (Continuing Professional Development)?
**A**: Sim. Certificações contam para CPD credits (CISSP, CISM, etc). Peça certificado de conclusão ao Gestor SGSI.

---

## 18. Next Steps (Immediate Actions)

### For Gestor SGSI (Ricardo Esper):
1. ✅ **HOJE**: Aprovar este documento (SGSI-TRAIN-001)
2. ✅ **Semana 1 (Jun 03-07)**:
   - Contratar KnowBe4 (€200/ano)
   - Matricular em ISO 27001 Lead Implementer (PECB - Jul 08-12, €2,400)
   - Matricular em LGPD DPO Training (Jul 22-23, €800)
3. ✅ **Semana 2 (Jun 10-14)**:
   - Setup KnowBe4 (enroll users, configurar phishing simulations)
   - Deploy OWASP WebGoat (Docker)
   - Criar tutoriais internos (Password/MFA, Secrets)
4. ✅ **Semana 3 (Jun 17)**: Launch Track 1 (email announcement CEO-endorsed)

### For CEO:
1. ✅ **HOJE**: Aprovar budget (€8,020 ano 1)
2. ✅ **Semana 3 (Jun 17)**: Enviar email endorse (importância de security training)
3. ✅ **Week 9 (Jul 29)**:
   - Participar de Module 15 (2h workshop)
   - **ASSINAR Information Security Policy** (SGSI-POLICY-001) - CRÍTICO

### For DevOps Lead:
1. ✅ **Semana 1-2 (Jun 03-14)**: Complete Track 1 (Universal)
2. ✅ **Semana 5-8 (Jul 01-26)**: Complete Track 3 (Modules 9-12)
3. ✅ **Q3 2026**: Considerar AWS Certified Security - Specialty (opcional - €280)

### For Dev Team:
1. ✅ **Semana 1-2 (Jun 03-14)**: Complete Track 1 (Universal)
2. ✅ **Semana 5-8 (Jul 01-26)**: Complete Track 2 (Modules 6-8)

---

## 19. References

### ISO Standards
- ISO/IEC 27001:2022 - Information security, cybersecurity and privacy protection
- ISO/IEC 27002:2022 - Information security controls (guidance for Annex A)
- ISO 31000:2018 - Risk management guidelines

### Frameworks
- OWASP Top 10 2021 - https://owasp.org/Top10/
- OWASP API Security Top 10 2023 - https://owasp.org/API-Security/
- CIS AWS Foundations Benchmark v1.5.0 - https://www.cisecurity.org/benchmark/amazon_web_services
- AWS Well-Architected Framework (Security Pillar) - https://aws.amazon.com/architecture/well-architected/

### Regulations
- LGPD (Lei Geral de Proteção de Dados) - Lei nº 13.709/2018 - https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- ANPD (Autoridade Nacional de Proteção de Dados) - https://www.gov.br/anpd/

### Training Providers
- KnowBe4 - https://www.knowbe4.com/
- PECB - https://pecb.com/
- OWASP - https://owasp.org/
- AWS Training - https://aws.amazon.com/training/

### Internal Documents
- SGSI-POLICY-001 (Information Security Policy)
- SGSI-COMP-001 (Competence Records)
- SGSI-OBJ-001 (Information Security Objectives)
- SOP-001 (Onboarding/Offboarding)
- SOP-004 (Secrets Management)
- SGSI-POLICY-003 (Incident Response Policy)

---

## 20. Approval

| Field | Value |
|-------|-------|
| **Prepared By** | Security Consultant (Bekaa Trusted Advisors) |
| **Reviewed By** | Gestor SGSI (Ricardo Esper) - Pendente |
| **Approved By** | CEO - Pendente |
| **Approval Date** | Pendente |
| **Effective Date** | 2026-06-03 (após aprovação) |
| **Next Review** | 2027-01-31 (Anual) |

---

## 21. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-05-26 | Security Consultant | Versão inicial - 4 tracks, 15 modules, 8-week implementation, €8k budget, integrated com SOP-001 |

---

**⚠️ CRITICAL ACTIONS**:
1. **Gestor SGSI**: Matricular em ISO 27001 Lead Implementer (Q2 2026 - Jul 08-12)
2. **CEO**: Assinar Information Security Policy (Week 9 - Jul 29) - **BLOCKER para certificação**
3. **ALL**: Complete Universal Training (Track 1) by Jun 28, 2026

**STATUS**: Draft - aguardando aprovação CEO + Gestor SGSI

---

**END OF DOCUMENT**
