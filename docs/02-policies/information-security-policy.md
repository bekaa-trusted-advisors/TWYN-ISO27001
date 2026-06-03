---
**Document Control**
| Campo | Valor |
|-------|-------|
| **Document ID** | SGSI-POLICY-001 |
| **Version** | 1.0 |
| **Author** | BEKAA Consultoria — Ricardo Esper |
| **Approved By** | **[CEO TWYN]** ⚠️ ASSINATURA OBRIGATÓRIA |
| **Approval Date** | [Pendente] |
| **Effective Date** | [Pendente] |
| **Próxima Revisão** | [Anual após aprovação] |
| **ISO 27001:2022 Mapping** | **Clause 5.2 — Leadership** + Control **A.5.1** |
| **Classification** | **PUBLIC** (divulgável a clientes/auditores) |
---

# Information Security Policy
## Política de Segurança da Informação — TWYN

---

## 1. Propósito

Esta **Política de Segurança da Informação** estabelece o compromisso da **TWYN** com a proteção da informação e define os princípios e diretrizes que orientam o **Sistema de Gestão de Segurança da Informação (SGSI)** em conformidade com **ISO/IEC 27001:2022**.

Esta política é aplicável a **todos** os colaboradores, contratados, fornecedores e partes interessadas que interagem com os ativos de informação da TWYN.

---

## 2. Scope (Escopo)

Esta política aplica-se a:
- ✅ Todos os ativos de informação da TWYN (dados, sistemas, infraestrutura)
- ✅ Todos os colaboradores (CLT, PJ, estagiários)
- ✅ Fornecedores e parceiros com acesso a informações da TWYN
- ✅ Clientes B2B que utilizam a plataforma Face ID
- ✅ Todos os ambientes (produção, staging, desenvolvimento)

Escopo detalhado conforme **[SGSI-SCOPE-001]** Documento de Escopo do SGSI.

---

## 3. Information Security Principles (Princípios de Segurança da Informação)

A TWYN compromete-se a proteger a informação através dos seguintes princípios fundamentais:

### 3.1 Confidentiality (Confidencialidade)
Garantir que informações sejam acessíveis **apenas** por pessoas autorizadas e para propósitos legítimos.

**Implementação**:
- Controle de acesso baseado em roles (RBAC)
- Criptografia de dados em repouso e em trânsito
- Princípio do menor privilégio
- NDAs com colaboradores e fornecedores

### 3.2 Integrity (Integridade)
Garantir a **exatidão e completude** da informação e métodos de processamento.

**Implementação**:
- Controle de versão (Git) para código e IaC
- Checksums e assinaturas digitais
- Auditoria de mudanças (CloudTrail, Git logs)
- Segregação de funções (separation of duties)

### 3.3 Availability (Disponibilidade)
Garantir que informações e sistemas estejam **disponíveis** quando necessário.

**Implementação**:
- Arquitetura multi-AZ (AWS)
- Backup automatizado e testado
- Disaster Recovery Plan (DRP)
- Monitoramento 24/7 (CloudWatch, GuardDuty)
- SLA de 99.9% para APIs críticas

### 3.4 Additional CIA+ Principles

**Authenticity (Autenticidade)**:
- MFA obrigatório para acessos administrativos
- Assinatura digital de commits Git (GPG)
- Tokens JWT com expiração para APIs

**Accountability (Responsabilização)**:
- Logs de auditoria imutáveis (CloudTrail)
- Rastreabilidade de ações (quem fez o quê, quando)
- Non-repudiation através de logging

**Compliance (Conformidade)**:
- LGPD (Lei Geral de Proteção de Dados)
- ISO/IEC 27001:2022
- AWS FTR (Foundational Technical Review)
- CIS Benchmark controls

---

## 4. Roles and Responsibilities (Papéis e Responsabilidades)

### 4.1 Top Management (CEO / C-Level)

**Responsabilidades**:
- ✅ Aprovar esta política e revisões
- ✅ Alocar recursos adequados para o SGSI
- ✅ Demonstrar liderança e comprometimento
- ✅ Comunicar a importância de SI a toda organização
- ✅ Nomear formalmente o Gestor SGSI

**Compromisso formal**:
> *"A TWYN compromete-se a estabelecer, implementar, manter e melhorar continuamente o Sistema de Gestão de Segurança da Informação, fornecendo recursos necessários e garantindo conformidade com requisitos legais, regulatórios e contratuais."*
>
> — **Enes Fernando Degasperi**, Chief Executive Officer

### 4.2 ISMS Manager (Gestor SGSI)

**Nomeado**: [Nome] — [Email] — [Telefone]  
**Backup**: [Nome Backup]

**Responsabilidades**:
- ✅ Gerenciar o SGSI no dia a dia
- ✅ Coordenar análises de risco e tratamento
- ✅ Conduzir auditorias internas
- ✅ Reportar performance do SGSI para top management
- ✅ Manter documentação do SGSI atualizada
- ✅ Lidar com incidentes de segurança (coordenação)

### 4.3 Information Security Team (Equipe de SI)

**Composição atual**:
- CTO + DevOps Lead + SecOps (em formação)

**Responsabilidades**:
- ✅ Implementar controles técnicos (Annex A)
- ✅ Responder a incidentes de segurança
- ✅ Monitorar ameaças e vulnerabilidades
- ✅ Executar testes de segurança (pentests, DR drills)
- ✅ Revisar logs e alertas

### 4.4 All Employees (Todos os Colaboradores)

**Responsabilidades**:
- ✅ Cumprir esta política e procedimentos relacionados
- ✅ Proteger credenciais de acesso (senhas, tokens)
- ✅ Reportar incidentes ou suspeitas de SI
- ✅ Participar de treinamentos obrigatórios
- ✅ Usar recursos de SI apenas para fins autorizados

### 4.5 Suppliers and Third Parties (Fornecedores)

**Responsabilidades**:
- ✅ Cumprir requisitos contratuais de SI
- ✅ Assinar DPA (Data Processing Agreement) quando aplicável
- ✅ Notificar TWYN de incidentes que afetem nossos dados
- ✅ Submeter-se a avaliações de segurança periódicas

---

## 5. Information Security Objectives (Objetivos de SI)

Os seguintes objetivos **mensuráveis** são estabelecidos para 2026:

| Objective | Target | Measurement | Responsável |
|-----------|--------|-------------|-------|
| **Obter certificação ISO 27001:2022** | Q3 2026 (ago) | Certificado emitido | Gestor SGSI |
| **Zero incidentes críticos de dados** | 0 por ano | Incidentes registrados em [SGSI-INC] | SecOps |
| **100% colaboradores treinados em SI** | Anual | % completude training logs | HR + SGSI |
| **Tempo de resposta a incidentes críticos** | < 1 hora | Média em incident tickets | SecOps |
| **Backup testado trimestralmente** | 4x/ano | DR drill logs | DevOps |
| **Rotação de credentials** | A cada 90 dias | Automated scan via AWS Config | DevOps |
| **Conformidade CIS Benchmark** | ≥ 90% | AWS Security Hub score | Cloud Infra |

Esses objetivos são revisados **anualmente** na Management Review (cláusula 9.3).

---

## 6. Risk Management Approach (Abordagem de Gestão de Riscos)

A TWYN adota uma abordagem **sistemática e baseada em risco** para SI:

### 6.1 Risk Assessment Process

1. **Identificação de ativos** críticos e suas ameaças/vulnerabilidades
2. **Avaliação de risco** usando metodologia **Likelihood × Impact** (escala 1-5)
3. **Priorização** de riscos (matriz de risco)
4. **Documentação** em Risk Register [SGSI-RISK-002]

**Frequência**: Anual ou quando mudanças significativas ocorrerem.

### 6.2 Risk Treatment Options

Para cada risco identificado, uma das seguintes opções é selecionada:

| Option | Description | When to Use |
|--------|-------------|-------------|
| **Mitigate** | Implementar controles para reduzir probabilidade/impacto | Risco alto, controle viável |
| **Accept** | Aceitar o risco residual | Risco baixo, custo > benefício |
| **Avoid** | Eliminar a atividade que gera o risco | Risco inaceitável |
| **Transfer** | Transferir via seguro ou terceirização | Risco especializado |

Todas as decisões de tratamento são documentadas no **Risk Treatment Plan [SGSI-RTP-001]**.

### 6.3 Statement of Applicability (SoA)

A seleção e justificativa de **todos os 93 controles** do Annex A está documentada no **[SGSI-SOA-001]**.

Controles **não aplicáveis** (e.g., A.7.1 Physical perimeters) são justificados formalmente.

---

## 7. Compliance and Legal Requirements (Conformidade)

A TWYN compromete-se a cumprir:

### 7.1 Legal and Regulatory

- ✅ **LGPD** (Lei 13.709/2018) — Lei Geral de Proteção de Dados
  - DPO designado: [Nome/Email]
  - Privacy Policy publicada
  - Data Subject Rights implementados

- ✅ **Marco Civil da Internet** (Lei 12.965/2014)

- ✅ **Código de Defesa do Consumidor** (CDC)

### 7.2 Standards and Frameworks

- ✅ **ISO/IEC 27001:2022** — certification target
- ✅ **ISO/IEC 27002:2022** — implementation guidance
- ✅ **CIS Benchmark** (AWS Foundations)
- ✅ **OWASP Top 10** — secure coding practices

### 7.3 Contractual Obligations

- ✅ Contratos com clientes B2B (SLAs, security requirements)
- ✅ AWS Business Associate Agreement (BAA)
- ✅ DPAs (Data Processing Agreements) com sub-processadores

**Processo de compliance**:
1. Identificar novos requisitos (legal scan trimestral)
2. Avaliar gap de compliance
3. Implementar controles necessários
4. Documentar evidências

---

## 8. Asset Management (Gestão de Ativos)

Todos os ativos de informação críticos são **inventariados e classificados**.

### 8.1 Information Classification

| Level | Description | Examples | Controls |
|-------|-------------|----------|----------|
| **CRÍTICO** | Dados biométricos, secrets, PII sensível | Face templates, DB passwords, API keys | Encryption at rest+transit, MFA, audit logs |
| **CONFIDENTIAL** | Dados de negócio sensíveis | Contratos, código-fonte, logs de auditoria | Access control, versioning, backup |
| **INTERNAL** | Informações internas não públicas | Documentação técnica, roadmaps | Acesso restrito a colaboradores |
| **PUBLIC** | Informações divulgáveis | API docs públicos, marketing | Proteção de integridade |

### 8.2 Asset Inventory

Mantido em: **[SGSI-ASSETS-001]** Asset Inventory  
Atualização: Trimestral ou quando mudanças ocorrerem

**Responsável**: Cloud Infrastructure Lead

---

## 9. Access Control (Controle de Acesso)

O acesso a sistemas e informações é **concedido com base em necessidade de negócio** (least privilege).

### 9.1 Access Control Principles

- ✅ **Role-Based Access Control (RBAC)** via AWS IAM
- ✅ **Multi-Factor Authentication (MFA)** obrigatório para:
  - AWS Console (produção)
  - GitHub (repositórios t4isb-infra)
  - VPN corporativa
  - Sistemas críticos (RDS, K8s dashboard)

- ✅ **Segregation of Duties**: Nenhum indivíduo tem controle end-to-end sobre processos críticos

- ✅ **Access Review**: Trimestral (ver SOP-005)

### 9.2 Privileged Access Management

- AWS root account: MFA + guardado em cofre físico
- Acesso via `assume-role` com session limits
- Todas as ações privilegiadas são auditadas (CloudTrail)

Procedimento: **[SOP-005]** IAM Recertification

---

## 10. Incident Management (Gestão de Incidentes)

### 10.1 Security Incident Definition

Qualquer evento que comprometa ou ameace a **Confidencialidade, Integridade ou Disponibilidade** da informação.

**Exemplos**:
- Acesso não autorizado a sistemas
- Vazamento de dados
- Malware/ransomware
- Indisponibilidade prolongada (> SLA)
- Perda ou roubo de dispositivos com dados

### 10.2 Incident Response Process

1. **Detecção**: Automated alerts (GuardDuty, CloudWatch) ou reporte manual
2. **Triagem**: Classificação de severidade (P0-P4)
3. **Resposta**: Contenção, erradicação, recuperação
4. **Comunicação**: Stakeholders internos/externos conforme necessário
5. **Post-Mortem**: Root cause analysis + lessons learned
6. **Improvement**: Atualizar controles/procedimentos

**SLA de Resposta**:
- P0 (Crítico): < 1 hora
- P1 (Alto): < 4 horas
- P2 (Médio): < 1 dia
- P3-P4 (Baixo): < 3 dias

Procedimento: **[SGSI-IRP-001]** Incident Response Policy

### 10.3 Breach Notification

Em caso de **data breach** envolvendo dados pessoais (LGPD):
- Notificar **ANPD** em até **72 horas** (se alto risco)
- Notificar **titulares afetados** se risco a direitos e liberdades
- Documentar em **Breach Register [SGSI-BREACH-LOG]**

---

## 11. Business Continuity and Disaster Recovery (Continuidade de Negócios)

### 11.1 Business Continuity Objectives

| Metric | Target | Current Status |
|--------|--------|----------------|
| **RTO** (Recovery Time Objective) | < 4 horas | ✅ Testado 20/03/2026 |
| **RPO** (Recovery Point Objective) | < 15 minutos | ✅ Backup contínuo |
| **Service Availability** | 99.9% uptime | ⏳ Monitorando |

### 11.2 Disaster Recovery

- **Backup**: Automated daily (RDS, S3 versioning)
- **Multi-AZ**: EKS clusters span availability zones
- **DR Region**: us-west-2 (Oregon) — failover capability
- **DR Testing**: **Trimestral** (ver GAP-007)

Procedimento: **[SGSI-DRP-001]** Disaster Recovery Plan

---

## 12. Supplier Security (Segurança de Fornecedores)

Todos os fornecedores com acesso a dados sensíveis são **avaliados** antes e durante o relacionamento.

### 12.1 Supplier Assessment

**Critérios de avaliação**:
- Certificações de SI (ISO 27001, SOC 2)
- Políticas de segurança
- Histórico de incidentes
- Localização de dados (LGPD compliance)
- Direito de auditoria

### 12.2 Supplier Agreements

**Contratos devem incluir**:
- Cláusulas de confidencialidade
- Data Processing Agreement (DPA) — se aplicável
- Obrigação de notificação de incidentes
- Direito de rescisão por breach
- Service Level Agreements (SLAs)

**Fornecedores críticos atuais**:
- AWS (BAA assinado ✅)
- GitHub (avaliar DPA ⏳)

Procedimento: **[SGSI-SUPP-001]** Supplier Security Assessment

---

## 13. Human Resources Security (Segurança de RH)

### 13.1 Before Employment (Antes da Contratação)

- ✅ Background checks (conforme legislação)
- ✅ Confidentiality Agreement (NDA)
- ✅ Termos de Uso de TI aceitos

### 13.2 During Employment

- ✅ **Treinamento de SI obrigatório**: Anual (ver GAP-006)
- ✅ Awareness contínua: Phishing simulations, newsletters
- ✅ Access reviews trimestrais

### 13.3 Termination or Change

- ✅ **Offboarding checklist**: Revogação de acessos (SOP-001)
- ✅ Devolução de ativos (laptops, tokens)
- ✅ Lembrete de obrigações de confidencialidade
- ✅ Exit interview (se aplicável)

Procedimento: **[SOP-001]** Onboarding/Offboarding

---

## 14. Physical and Environmental Security (Segurança Física)

**Nota**: TWYN opera **100% em cloud (AWS)**. Segurança física de datacenters é responsabilidade da AWS (coberto por AWS ISO 27001 e SOC 2).

### 14.1 Office Security (Escritório TWYN)

- ✅ Acesso restrito (controle de entrada)
- ✅ Clear desk policy
- ✅ Visitantes acompanhados
- ✅ CCTV (se aplicável)

### 14.2 Remote Work (Trabalho Remoto)

Ver **[SOP-003]** Remote Work Policy:
- VPN obrigatória para acesso a recursos internos
- Full disk encryption em laptops
- Autenticação de dispositivos (MDM se aplicável)

---

## 15. Operations Security (Segurança Operacional)

### 15.1 Change Management

Todas as mudanças em produção seguem processo formal:
- Change Request documentado
- Aprovação de Change Advisory Board (CAB)
- Rollback plan obrigatório
- Post-deployment validation

Procedimento: **[SOP-002]** Change Management

### 15.2 Capacity Management

- Monitoramento de recursos (CPU, memória, storage)
- Auto-scaling configurado (EKS, RDS)
- Alertas de threshold

### 15.3 Malware Protection

- AWS GuardDuty (threat intelligence) — ativando (GAP-002)
- Container image scanning (Trivy/ECR scanning)
- Patch management automatizado

---

## 16. Communications Security (Segurança de Comunicações)

### 16.1 Network Security

- ✅ **VPC isolation**: Prod/staging/dev separados
- ✅ **Security Groups**: Least privilege firewall rules
- ✅ **NACLs** para segmentação adicional
- ✅ **WAF** (AWS WAF) na frente de APIs públicas

### 16.2 Encryption

- ✅ **In Transit**: TLS 1.2+ (HTTPS obrigatório)
- ✅ **At Rest**: 
  - RDS: AWS KMS encryption
  - S3: SSE-KMS (biometric images)
  - EBS: encrypted volumes

### 16.3 Secure Development

- ✅ **Secure coding**: OWASP Top 10 training
- ✅ **Code review**: Pull requests obrigatórios (2 aprovadores)
- ✅ **SAST/DAST**: Automated security scanning em CI/CD
- ✅ **Dependency scanning**: Snyk/Dependabot

Procedimento: **[SGSI-SDLC-001]** Secure Development Lifecycle

---

## 17. Monitoring and Performance (Monitoramento e Performance)

### 17.1 Logging and Monitoring

**Logs coletados**:
- CloudTrail (API calls AWS)
- Application logs (EKS pods)
- VPC Flow Logs
- RDS query logs (slow queries apenas)
- GuardDuty findings

**Retention**: 
- CloudTrail: 1 ano
- Application logs: 90 dias
- Audit logs: 7 anos (LGPD)

### 17.2 Security Metrics (KPIs)

Monitorados mensalmente:
- Tempo médio de resposta a incidentes (MTTR)
- Número de vulnerabilidades críticas abertas
- % de conformidade CIS Benchmark
- % de colaboradores treinados
- Número de acessos privilegiados (alertas)

Reportado na **Management Review** (cláusula 9.3).

---

## 18. Audit and Compliance (Auditoria e Conformidade)

### 18.1 Internal Audits

- **Frequência**: Anual (mínimo)
- **Escopo**: Todos os controles Annex A aplicáveis
- **Responsável**: Gestor SGSI ou auditor externo independente

Procedimento: **[SGSI-AUDIT-001]** Internal Audit Programme

### 18.2 Management Review

- **Frequência**: Anual (mínimo) ou quando mudanças significativas
- **Participantes**: CEO, CTO, Gestor SGSI, Finance (se aplicável)
- **Inputs**: 
  - Resultados de auditorias
  - Incidentes de SI
  - Performance do SGSI (KPIs)
  - Mudanças em requisitos legais
  - Oportunidades de melhoria

- **Outputs**:
  - Decisões sobre melhoria do SGSI
  - Ajustes de recursos
  - Atualização de objetivos

Procedimento: **[SGSI-MGT-REV-001]** Management Review Process

### 18.3 External Audits

- Certificação ISO 27001: Stage 1 + Stage 2 + surveillance audits
- Cliente audits (se solicitado contratualmente)

---

## 19. Continuous Improvement (Melhoria Contínua)

A TWYN segue o ciclo **Plan-Do-Check-Act (PDCA)**:

1. **PLAN**: Estabelecer SGSI, objetivos e processos
2. **DO**: Implementar e operar o SGSI
3. **CHECK**: Monitorar, medir, auditar
4. **ACT**: Manter e melhorar o SGSI

**Mecanismos de melhoria**:
- Lições aprendidas de incidentes (post-mortems)
- Auditorias internas
- Management reviews
- Feedback de stakeholders
- Análise de métricas/KPIs

**Ações corretivas e preventivas** são documentadas em **[SGSI-CAPA-LOG]**.

---

## 20. Training and Awareness (Treinamento e Conscientização)

### 20.1 Mandatory Training

**Todos os colaboradores**:
- ✅ **SI Awareness Training**: Anual (3 horas online)
- ✅ **LGPD Training**: Anual (1 hora)
- ✅ **Phishing Awareness**: Trimestral (simulated phishing)

**Roles técnicos**:
- ✅ **Secure Coding (OWASP)**: Semestral
- ✅ **AWS Security Best Practices**: Anual

**Registro**: Training logs em **[SGSI-TRAINING-LOG]**

### 20.2 Awareness Campaigns

- Newsletters mensais de SI
- Posters no escritório (clear desk, screen lock)
- Security Champions programme (em formação)

---

## 21. Policy Violations and Sanctions (Violações e Sanções)

Violações desta política podem resultar em **ações disciplinares**, incluindo:
- Advertência verbal ou escrita
- Suspensão de acesso a sistemas
- Revogação de privilégios
- Rescisão de contrato (casos graves)
- Ações legais (se aplicável)

**Processo disciplinar** segue legislação trabalhista brasileira e contrato de trabalho.

---

## 22. Exceptions (Exceções)

Exceções a esta política devem ser:
1. **Solicitadas formalmente** (via email/ticket)
2. **Justificadas** (business case + análise de risco)
3. **Aprovadas** por Gestor SGSI + CTO
4. **Documentadas** em **[SGSI-EXCEPTIONS-LOG]**
5. **Revisadas** anualmente

Exceções **nunca** são concedidas para:
- Criptografia de dados biométricos
- MFA para acesso produção AWS
- Logging de CloudTrail

---

## 23. Policy Review and Updates (Revisão e Atualizações)

**Frequência de Revisão**: **Anual** ou quando:
- Mudanças significativas na organização (M&A, novos produtos)
- Mudanças em legislação aplicável (nova lei de privacidade)
- Após incidentes graves de SI
- Resultado de auditoria interna/externa
- Mudanças em ameaças (threat landscape)

**Processo de atualização**:
1. Gestor SGSI inicia revisão
2. Stakeholders fornecem feedback
3. Draft atualizado
4. **Aprovação da alta direção** (CEO)
5. Comunicação a todos os colaboradores
6. Versão anterior arquivada

---

## 24. Documentos Relacionados (Documentos Relacionados)

| Doc ID | Title |
|--------|-------|
| SGSI-SCOPE-001 | Documento de Escopo do SGSI |
| SGSI-RISK-001 | Risk Assessment Methodology |
| SGSI-RISK-002 | Risk Register |
| SGSI-RTP-001 | Risk Treatment Plan |
| SGSI-SOA-001 | Statement of Applicability |
| SOP-001 | Onboarding/Offboarding Procedure |
| SOP-002 | Change Management Procedure |
| SOP-003 | Remote Work Policy |
| SOP-004 | Secrets Management and Rotation |
| SOP-005 | IAM Recertification Procedure |
| SGSI-IRP-001 | Incident Response Policy |
| SGSI-DRP-001 | Disaster Recovery Plan |
| SGSI-AUDIT-001 | Internal Audit Programme |

---

## 25. Document History (Histórico)

| Versão | Data | Autor | Alterações | Approved By |
|---------|------|--------|---------|-------------|
| 0.1 (Draft) | 26/05/2026 | Ricardo Esper (BEKAA) | Initial draft | — |
| 1.0 | [Pendente] | Ricardo Esper | Final version for approval | **[CEO TWYN]** |

---

## 26. Approval Signatures (Assinaturas de Aprovação)

### Top Management Commitment

> **"I, Enes Fernando Degasperi, as Chief Executive Officer of TWYN, hereby approve this Information Security Policy and commit to providing necessary resources for the establishment, implementation, maintenance, and continual improvement of the Information Security Management System (ISMS) in accordance with ISO/IEC 27001:2022."**

---

**CEO TWYN**  
**Signature**: _______________________________  
**Name**: Enes Fernando Degasperi  
**Date**: _____ / _____ / 2026

---

**Gestor SGSI**  
**Signature**: _______________________________  
**Name**: Enes Fernando Degasperi  
**Date**: _____ / _____ / 2026

---

**CTO**  
**Signature**: _______________________________  
**Name**: Enes Fernando Degasperi  
**Date**: _____ / _____ / 2026

---

## ⚠️ CRÍTICO NEXT STEPS

1. **[ ]** Preencher placeholders: Enes Fernando Degasperi, 31.122.819/0001-55, Avenida Paulista, nº 37, Bairro Bela Vista, São Paulo/SP, [DPO], Ricardo Esper (Bekaa Trusted Advisors)
2. **[ ]** Obter **assinaturas físicas ou digitais** (Pendente Enes Fernando Degasperi) da alta direção
3. **[ ]** Comunicar política a TODOS os colaboradores (email + treinamento)
4. **[ ]** Armazenar versão assinada em local seguro e controlado
5. **[ ]** Publicar versão pública (sem informações sensíveis) para clientes/auditores

---

**END OF DOCUMENT**
