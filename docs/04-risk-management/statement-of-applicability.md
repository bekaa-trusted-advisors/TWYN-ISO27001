---
document_id: SGSI-SOA-001
version: "2.0"
status: Draft
classification: CONFIDENTIAL
title: "Declaração de Aplicabilidade (Statement of Applicability)"
owner: "Ricardo Esper — Bekaa Trusted Advisors"
approved_by: "CEO TWYN (Pendente)"
effective_date: Pendente
last_update: "02/06/2026"
next_review: "Anual ou após mudança significativa no escopo"
iso_mapping: "Cláusula 6.1.3d — Statement of Applicability (OBRIGATÓRIO)"
---

# Declaração de Aplicabilidade (Statement of Applicability)
## SGSI-SOA-001 — TWYN ISO/IEC 27001:2022

---

## 1. Objetivo

Esta **Declaração de Aplicabilidade (SoA)** documenta a seleção e justificativa de **todos os 93 controles** do Anexo A da ISO/IEC 27001:2022 para o Sistema de Gestão de Segurança da Informação (SGSI) da **TWYN**.

Para cada controle, este documento declara:
- Se o controle é **aplicável** ao escopo do SGSI
- O **status de implementação** atual
- A **justificativa** para inclusão ou exclusão
- Os **detalhes de implementação** (como o controle é operacionalizado)
- **Referências de evidências** e **vínculos com riscos** identificados

Este documento é **OBRIGATÓRIO** para certificação ISO 27001 e deve ser:
1. ✅ Aprovado pela alta direção
2. ✅ Baseado nos resultados da Avaliação de Riscos (SGSI-RISK-002)
3. ✅ Atualizado sempre que o escopo ou riscos mudarem
4. ✅ Apresentado ao auditor de certificação

---

## 2. Referência de Escopo

**Escopo do SGSI**: Conforme [SGSI-SCOPE-001] Documento de Escopo do SGSI.

**Dentro do Escopo**:
- AWS Account `992382542028` (produção) — `us-east-1` (primária), `us-west-2` (DR)
- Plataforma Face ID API (EKS, RDS PostgreSQL, S3)
- Pipelines CI/CD (GitHub Actions, ECR, Terraform)
- Infraestrutura como Código (Terraform)
- Processamento de dados biométricos (dados RESTRITOS — LGPD Art. 11)
- Serviços de segurança: KMS, WAF, GuardDuty, CloudTrail, Config, Security Hub, Secrets Manager, ACM
- ~10 colaboradores com laptops corporativos

**Fora do Escopo**:
- Ambientes de desenvolvimento local individuais (cobertos por política de endpoint)
- Website de marketing (infraestrutura separada)
- Ferramentas SaaS corporativas não críticas (cobertos por avaliação de fornecedores)

**Modelo de Responsabilidade Compartilhada AWS**:
> A segurança física dos datacenters é responsabilidade da AWS, conforme certificações AWS ISO 27001, SOC 2 Type II e SOC 3. A TWYN é responsável pela segurança **na** nuvem (dados, configurações, identidades).

---

## 3. Legenda de Status

| Status | Símbolo | Definição |
|--------|---------|-----------|
| **Implementado** | ✅ | Controle totalmente implementado com evidências documentadas |
| **Parcial** | 🟡 | Controle parcialmente implementado; lacunas identificadas |
| **Não Implementado** | ❌ | Controle não implementado (planejado no roadmap) |
| **Não Aplicável** | ⬜ | Controle não aplicável ao escopo da TWYN (justificado) |

---

## 4. Estatísticas Resumidas

| Tema | Total | Implementado ✅ | Parcial 🟡 | Não Impl. ❌ | N/A ⬜ |
|------|-------|-----------------|------------|--------------|--------|
| **A.5 Organizacionais** | 37 | 5 (14%) | 20 (54%) | 12 (32%) | 0 (0%) |
| **A.6 Pessoas** | 8 | 3 (38%) | 4 (50%) | 1 (12%) | 0 (0%) |
| **A.7 Físicos** | 14 | 1 (7%) | 3 (21%) | 0 (0%) | 10 (72%) |
| **A.8 Tecnológicos** | 34 | 10 (29%) | 14 (41%) | 9 (27%) | 1 (3%) |
| **TOTAL** | **93** | **19 (20%)** | **41 (44%)** | **22 (24%)** | **11 (12%)** |

**Conformidade Geral**: **64% implementado ou parcial** (meta: 100% até Q3 2026 — agosto)

**Distribuição Visual**:
- ✅ Implementado: █████░░░░░░░░░░░░░░░ 20%
- 🟡 Parcial: ████████████████░░░░ 44%
- ❌ Não Implementado: █████████░░░░░░░░░░░ 24%
- ⬜ Não Aplicável: ████░░░░░░░░░░░░░░░░ 12%

---

## 5. TEMA 1: CONTROLES ORGANIZACIONAIS (A.5.1 – A.5.37)

**Total**: 37 controles | **Aplicáveis**: 37 | **N/A**: 0

| ID | Título do Controle | Aplicável? | Status | Justificativa | Detalhes de Implementação | Referência de Evidência | Referência de Risco | Responsável |
|----|-------------------|------------|--------|---------------|---------------------------|------------------------|---------------------|-------------|
| **A.5.1** | Políticas para segurança da informação | Sim | ✅ | Política de SI aprovada e publicada, cobrindo todos os princípios do SGSI | Política de Segurança da Informação documenta princípios CIA+, papéis, responsabilidades, gestão de riscos, conformidade e melhoria contínua | SGSI-POLICY-001 | — | Gestor SGSI |
| **A.5.2** | Papéis e responsabilidades de segurança da informação | Sim | 🟡 | Papéis definidos na política (Seção 4), mas matriz RACI incompleta e designação formal do Gestor SGSI pendente | Definidos: CEO, Gestor SGSI, equipe SI, colaboradores, fornecedores. Falta: RACI formal, designação por portaria | SGSI-POLICY-001 §4; SGSI-RACI-001 (pendente) | — | Gestor SGSI |
| **A.5.3** | Segregação de funções | Sim | 🟡 | Separação Dev/Ops/Infra existe na prática, mas não formalizada em documento; contas AWS separadas por ambiente | Contas AWS distintas para dev/staging/prod. IAM roles por função. Falta: documentação formal de segregação e controle de conflitos | Contas AWS; IAM policies | RISK-004 | CTO |
| **A.5.4** | Responsabilidades da direção | Sim | ✅ | Responsabilidades da alta direção definidas na Política de SI (Seção 4.1), incluindo compromisso formal do CEO | CEO responsável por aprovar política, alocar recursos, demonstrar liderança. Compromisso formal documentado | SGSI-POLICY-001 §4.1 | — | CEO |
| **A.5.5** | Contato com autoridades | Sim | ✅ | DPO designado para contato com ANPD; contatos de segurança definidos para AWS e autoridades competentes | Contato ANPD via DPO; AWS Support; contatos de emergência definidos. Processo de notificação de breach em 72h documentado | SGSI-POLICY-001 §10.3 | RISK-016 | Jurídico |
| **A.5.6** | Contato com grupos de interesse especial | Sim | 🟡 | Contato com AWS Support estabelecido; participação em comunidades de segurança parcial | AWS Security Bulletins assinados. Falta: registro formal de comunidades e grupos de interesse (CERT.br, FIRST, CSA) | Lista de contatos (pendente) | — | Gestor SGSI |
| **A.5.7** | Inteligência de ameaças | Sim | 🟡 | GuardDuty sendo habilitado (GAP-002); AWS Security Bulletins assinados; sem processo formal de threat intelligence | GuardDuty fornecerá findings de ameaças. AWS Security Hub com CIS Benchmark. Falta: processo formal de coleta, análise e ação sobre threat intel | GuardDuty (em ativação); Security Hub | RISK-005 | SecOps |
| **A.5.8** | Segurança da informação no gerenciamento de projetos | Sim | ❌ | Sem checklist formal de segurança na iniciação de projetos; revisão de segurança ad-hoc | Nenhum processo formalizado. Ação: criar checklist de segurança para revisão em cada projeto/feature | Checklist (a criar) | RISK-016 | CTO |
| **A.5.9** | Inventário de informações e outros ativos associados | Sim | ❌ | Inventário de ativos em elaboração (GAP-004); recursos AWS não catalogados formalmente | Nenhum inventário formal. Recursos AWS identificados ad-hoc. Ação: executar discovery completo AWS + criar SGSI-ASSETS-001 | SGSI-ASSETS-001 (pendente) | RISK-008 | Cloud Infra |
| **A.5.10** | Uso aceitável de informações e outros ativos associados | Sim | 🟡 | Regras de uso definidas na Política de SI, mas sem termo de aceite formal (AUP) assinado por colaboradores | Princípios definidos em SGSI-POLICY-001 §4.4. Falta: Formulário AUP individual com assinatura de cada colaborador | SGSI-POLICY-001; AUP (a criar) | RISK-012 | RH + SGSI |
| **A.5.11** | Devolução de ativos | Sim | 🟡 | Processo de offboarding ad-hoc inclui devolução de laptops; SOP-001 em elaboração | Prática informal de devolução de equipamentos no desligamento. Falta: checklist formalizado com registro de devolução | SOP-001 (pendente) | — | RH + TI |
| **A.5.12** | Classificação da informação | Sim | 🟡 | 4 níveis definidos na Política de SI (CRITICAL, CONFIDENTIAL, INTERNAL, PUBLIC), mas não aplicados sistematicamente | Níveis definidos em SGSI-POLICY-001 §8.1. Dados biométricos = CRITICAL. Falta: aplicação de labels/tags em todos os ativos | SGSI-POLICY-001 §8.1 | RISK-001 | Gestor SGSI |
| **A.5.13** | Rotulagem de informações | Sim | 🟡 | Classificação definida, mas sem rotulagem técnica implementada (tags AWS, headers, watermarks) | S3 buckets parcialmente tagueados. Falta: política de tagging obrigatória AWS; rotulagem de documentos; headers de classificação | Tags AWS (parcial) | — | Cloud Infra |
| **A.5.14** | Transferência de informações | Sim | 🟡 | TLS 1.2+ para APIs; transferência interna via VPC; sem política formal de transferência de dados | TLS obrigatório em todas as APIs. VPC peering para comunicação interna. S3 Transfer Acceleration com criptografia. Falta: política formal documentada | Configuração TLS; VPC config | — | Cloud Infra |
| **A.5.15** | Controle de acesso | Sim | 🟡 | AWS IAM implementado, mas políticas excessivamente permissivas (GAP-003); princípio do menor privilégio não totalmente aplicado | AWS IAM com RBAC. Security Groups e NACLs configurados. Falta: revisão de IAM policies para least privilege; eliminar AdministratorAccess | IAM policies; Security Groups | RISK-003, RISK-004 | Cloud Infra |
| **A.5.16** | Gestão de identidades | Sim | 🟡 | Identidades IAM existem; ciclo de vida parcial — sem auto-offboarding, sem revisão periódica | IAM users e roles criados. Falta: processo formal de ciclo de vida (criação, revisão, desativação); auto-offboarding; SOP-001 | IAM Console; SOP-001 (pendente) | RISK-006 | Cloud Infra |
| **A.5.17** | Informações de autenticação | Sim | 🟡 | Senhas e MFA parcial; chave de acesso >90 dias não rotacionada (RISK-006); Secrets Manager em uso parcial | MFA habilitado para console (nem todos os usuários). Secrets Manager para DB passwords. Falta: MFA universal, rotação automática de chaves, SOP-004 | IAM Console; Secrets Manager | RISK-006 | Cloud Infra |
| **A.5.18** | Direitos de acesso | Sim | 🟡 | Permissões IAM atribuídas, mas sem revisão trimestral formal (SOP-005 necessário) | IAM policies atribuídas por role. Falta: recertificação trimestral de acessos; processo formal de solicitação/aprovação de acesso | IAM policies; SOP-005 (pendente) | RISK-004 | Cloud Infra |
| **A.5.19** | Segurança da informação em relacionamentos com fornecedores | Sim | 🟡 | BAA AWS assinado; DPA GitHub em avaliação; sem avaliação formal de todos os fornecedores | AWS BAA assinado ✅. GitHub DPA em análise. Falta: inventário completo de fornecedores com avaliação de segurança | Contrato AWS BAA; Lista fornecedores (pendente) | — | Gestor SGSI |
| **A.5.20** | Abordagem da segurança da informação em acordos com fornecedores | Sim | 🟡 | Contrato AWS possui cláusulas de SI; demais fornecedores sem cláusulas formais | Contrato AWS inclui termos de segurança, SLA, notificação de incidentes. Falta: modelo padrão de cláusulas de SI para contratos | Contrato AWS; Template (a criar) | — | Jurídico |
| **A.5.21** | Gestão da segurança da informação na cadeia de suprimentos de TIC | Sim | ❌ | Sem avaliação formal de riscos na cadeia de suprimentos; dependências não mapeadas | Nenhum processo formal. Dependências: AWS, GitHub, bibliotecas open-source (npm/pip). Ação: mapear cadeia + avaliar riscos | Processo (a criar) | RISK-014 | Gestor SGSI |
| **A.5.22** | Monitoramento, revisão e gestão de mudanças de serviços de fornecedores | Sim | ❌ | AWS monitorado via dashboards, mas sem processo formal de revisão periódica de fornecedores | CloudWatch monitora serviços AWS. Falta: revisão formal trimestral de fornecedores; checklist de avaliação periódica | Checklist (a criar) | RISK-010 | Cloud Infra |
| **A.5.23** | Segurança da informação para uso de serviços em nuvem | Sim | 🟡 | AWS avaliado (FTR em andamento); configuração com lacunas identificadas; modelo de responsabilidade compartilhada entendido | AWS FTR em progresso. Security Hub ativo. CIS Benchmark sendo aplicado. Config sendo habilitado. Falta: fechar GAPs 001-004 | AWS FTR docs; Security Hub | RISK-001, RISK-002 | Cloud Infra |
| **A.5.24** | Planejamento e preparação da gestão de incidentes de segurança da informação | Sim | ❌ | Sem Plano de Resposta a Incidentes (IRP) documentado; resposta ad-hoc atual | Nenhum IRP formal. Ação: criar SGSI-IRP-001 com níveis de severidade P0-P4, escalação, runbooks, notificação LGPD | SGSI-IRP-001 (pendente) | RISK-017 | SecOps |
| **A.5.25** | Avaliação e decisão sobre eventos de segurança da informação | Sim | ❌ | Sem processo formal de triagem de eventos; GuardDuty sendo habilitado para detecção | Nenhum processo de triagem. GuardDuty fornecerá alertas automatizados. Falta: critérios de classificação de eventos vs. incidentes | GuardDuty (em ativação) | RISK-005, RISK-017 | SecOps |
| **A.5.26** | Resposta a incidentes de segurança da informação | Sim | ❌ | Resposta ad-hoc; sem runbooks documentados; sem equipe de resposta definida | Nenhum procedimento formal. Ação: criar runbooks para cenários comuns (breach S3, compromisso IAM, ransomware, DDoS) | Runbooks (a criar) | RISK-017 | SecOps |
| **A.5.27** | Aprendizado com incidentes de segurança da informação | Sim | ❌ | Sem processo de post-mortem; sem registro de lições aprendidas | Nenhum template ou processo. Ação: criar template de post-mortem blameless; registro de lições aprendidas | Template (a criar) | RISK-017 | SecOps |
| **A.5.28** | Coleta de evidências | Sim | 🟡 | CloudTrail coleta logs de API AWS (evidência digital); sem processo formal de forense | CloudTrail habilitado com retenção de 1 ano. S3 com versionamento. Falta: procedimento formal de preservação de evidências para forense e litígio | CloudTrail; S3 logs | — | Cloud Infra |
| **A.5.29** | Segurança da informação durante disrupção | Sim | 🟡 | Região DR (us-west-2) configurada; failover não testado (GAP-007); procedimentos não documentados | Multi-AZ em us-east-1. DR cross-region para us-west-2. Backups automatizados RDS e S3. Falta: teste de failover; documentar BCP | DR config; Backup logs | RISK-007, RISK-015 | Cloud Infra |
| **A.5.30** | Prontidão de TIC para continuidade de negócios | Sim | 🟡 | Backups automatizados, mas não testados; RTO/RPO definidos mas não validados | RDS backup automático. S3 versioning. EKS multi-node. Falta: teste trimestral de restore; validar RTO <4h e RPO <15min | Backup logs; DR test (pendente) | RISK-009 | Cloud Infra |
| **A.5.31** | Requisitos legais, estatutários, regulamentares e contratuais | Sim | 🟡 | LGPD identificada como requisito principal; gaps identificados (sem DPO formal, Privacy Policy incompleta) | LGPD Art. 11 (dados biométricos sensíveis). Marco Civil. CDC. Contratos B2B com SLAs. Falta: DPO formal; DPIA; processo DSR completo | SGSI-POLICY-001 §7; Privacy Policy (pendente) | RISK-016 | Jurídico |
| **A.5.32** | Direitos de propriedade intelectual | Sim | ✅ | Código-fonte em repositórios privados GitHub; licenças de software gerenciadas; contratos com cláusulas de PI | Repositórios GitHub privados com controle de acesso. Contratos de trabalho com cláusula de cessão de PI. Dependabot monitora licenças | GitHub settings; Contratos RH | — | CTO |
| **A.5.33** | Proteção de registros | Sim | ✅ | CloudTrail com retenção de 1 ano; logs de auditoria 7 anos (compliance LGPD); S3 com versionamento | CloudTrail → S3 com lifecycle rules. Application logs 90 dias. Audit logs 7 anos em S3 Glacier. Registros protegidos por IAM policies | CloudTrail config; S3 lifecycle | — | Cloud Infra |
| **A.5.34** | Privacidade e proteção de PII | Sim | 🟡 | Criptografia implementada para dados biométricos; gaps LGPD (sem DPIA, processo DSR incompleto, Privacy Policy pendente) | S3 SSE-KMS para imagens biométricas. RDS encryption at rest. TLS in transit. Falta: DPIA, processo DSR (acesso/correção/exclusão), Privacy Policy pública | Crypto config; Privacy Policy (pendente) | RISK-016 | Jurídico + SGSI |
| **A.5.35** | Revisão independente da segurança da informação | Sim | ❌ | Nenhuma auditoria externa realizada; planejada para Q3 2026 como parte da certificação | Primeira auditoria prevista Stage 1 + Stage 2 ISO 27001. Falta: programa de auditoria interna; contratar auditor | Plano de auditoria (pendente) | — | Gestor SGSI |
| **A.5.36** | Conformidade com políticas, regras e normas de segurança da informação | Sim | 🟡 | Políticas existem, mas sem auditoria interna para verificar conformidade (GAP-008) | Política de SI publicada. SOPs em elaboração. Falta: programa de auditoria interna; checklist de conformidade; relatórios de auditoria | SGSI-AUDIT-001 (pendente) | — | Gestor SGSI |
| **A.5.37** | Procedimentos operacionais documentados | Sim | 🟡 | IaC documentado (Terraform); SOPs 001-005 em elaboração; procedimentos operacionais parciais | Terraform modules documentados. README em repositórios. Falta: SOPs 001-005 completos; procedimentos de operação diária documentados | SOPs 001-005 (em elaboração) | — | SGSI |

---

## 6. TEMA 2: CONTROLES DE PESSOAS (A.6.1 – A.6.8)

**Total**: 8 controles | **Aplicáveis**: 8 | **N/A**: 0

| ID | Título do Controle | Aplicável? | Status | Justificativa | Detalhes de Implementação | Referência de Evidência | Referência de Risco | Responsável |
|----|-------------------|------------|--------|---------------|---------------------------|------------------------|---------------------|-------------|
| **A.6.1** | Seleção | Sim | 🟡 | Verificação de antecedentes conforme legislação trabalhista; NDAs assinados; processo não formalizado como SOP | Background check realizado na contratação (conforme CLT). NDA assinado por todos. Falta: checklist formalizado; verificação de referências documentada | Registros RH; NDAs assinados | — | RH |
| **A.6.2** | Termos e condições de emprego | Sim | ✅ | Contratos de trabalho incluem cláusulas de confidencialidade, uso de TI e responsabilidades de SI | Contratos CLT e PJ incluem: confidencialidade, uso aceitável de TI, obrigação de reportar incidentes, devolução de ativos | Contratos RH | — | RH |
| **A.6.3** | Conscientização, educação e treinamento em segurança da informação | Sim | ❌ | Sem programa formal de treinamento (GAP-006, RISK-012); nenhum registro de treinamento | Nenhum treinamento formal realizado. Ação: selecionar plataforma (KnowBe4/similar), matricular todos os colaboradores, conteúdo: LGPD, phishing, senhas, trabalho remoto | SGSI-TRAINING-LOG (a criar) | RISK-012 | RH + SGSI |
| **A.6.4** | Processo disciplinar | Sim | ✅ | Compliance com legislação trabalhista brasileira (CLT); processo disciplinar definido em contrato | Advertência verbal/escrita, suspensão, rescisão conforme CLT Art. 482. Definido em contratos de trabalho e regulamento interno | Políticas RH; Contratos | — | RH |
| **A.6.5** | Responsabilidades após término ou mudança de emprego | Sim | 🟡 | Offboarding ad-hoc com revogação de acessos; SOP-001 em elaboração para formalizar | Prática: revogar acesso AWS, GitHub, email no desligamento. Lembrete verbal de NDA. Falta: checklist formal (SOP-001); registro de devolução de ativos | SOP-001 (pendente) | — | RH + TI |
| **A.6.6** | Acordos de confidencialidade ou não divulgação | Sim | ✅ | NDAs assinados por todos os colaboradores (CLT e PJ) no momento da contratação | NDA padrão assinado na admissão. Cláusula de confidencialidade em contratos. Extensão pós-término definida | Registros RH; NDAs arquivados | — | RH |
| **A.6.7** | Trabalho remoto | Sim | 🟡 | Trabalho remoto comum na TWYN; política incompleta (SOP-003 em elaboração); VPN disponível mas uso não obrigatório em todos os cenários | Colaboradores trabalham remotamente. VPN disponível. Falta: SOP-003 com requisitos (VPN obrigatória, encryption, ambiente seguro), política de BYOD | SOP-003 (pendente) | RISK-018 | RH + TI |
| **A.6.8** | Relato de eventos de segurança da informação | Sim | 🟡 | Canal de reporte via email/Slack existe; sem processo formal documentado; sem formulário padronizado | Colaboradores reportam via Slack (#segurança) ou email ao CTO. Falta: formulário padronizado; fluxo de triagem; integração com IRP | Canal Slack; IRP (pendente) | RISK-017 | SecOps |

---

## 7. TEMA 3: CONTROLES FÍSICOS (A.7.1 – A.7.14)

**Total**: 14 controles | **Aplicáveis**: 4 | **N/A**: 10

> **Nota**: A TWYN opera **100% em nuvem AWS**. A segurança física dos datacenters é responsabilidade da AWS, conforme o **Modelo de Responsabilidade Compartilhada** e certificações AWS ISO 27001 + SOC 2 Type II. A maioria dos controles A.7 é **Não Aplicável** ao escopo da TWYN. Controles relacionados ao escritório e endpoints dos colaboradores permanecem aplicáveis.

| ID | Título do Controle | Aplicável? | Status | Justificativa | Detalhes de Implementação | Referência de Evidência | Referência de Risco | Responsável |
|----|-------------------|------------|--------|---------------|---------------------------|------------------------|---------------------|-------------|
| **A.7.1** | Perímetros de segurança física | Não | ⬜ | Sem datacenter próprio. Infraestrutura 100% AWS. Segurança física de datacenters é responsabilidade exclusiva da AWS conforme modelo de responsabilidade compartilhada (AWS ISO 27001, SOC 2 Type II) | N/A — Responsabilidade AWS | Certificações AWS (ISO 27001, SOC 2) | — | N/A |
| **A.7.2** | Entrada física | Não | ⬜ | Sem datacenter próprio. Controle de entrada física aos datacenters é responsabilidade da AWS. Escritório TWYN não processa/armazena dados de produção | N/A — Responsabilidade AWS | Certificações AWS (ISO 27001, SOC 2) | — | N/A |
| **A.7.3** | Segurança de escritórios, salas e instalações | Sim | 🟡 | Escritório possui controle de acesso básico (crachá); sem dados sensíveis armazenados fisicamente no local | Controle de entrada por crachá. Visitantes acompanhados. Sem servidores on-premises. Falta: política formal de segurança do escritório | Controle de acesso escritório | RISK-ACC-002 | Admin |
| **A.7.4** | Monitoramento de segurança física | Não | ⬜ | Monitoramento físico de datacenters é responsabilidade da AWS. Escritório possui CCTV básico, risco residual aceito (RISK-ACC-002) | N/A — Responsabilidade AWS para datacenters; CCTV do escritório é controle compensatório de baixo risco | Certificações AWS; CCTV escritório | RISK-ACC-002 | N/A |
| **A.7.5** | Proteção contra ameaças físicas e ambientais | Não | ⬜ | Proteção contra incêndio, inundação e desastres naturais dos datacenters é responsabilidade da AWS. Escritório sem equipamentos críticos | N/A — Responsabilidade AWS | Certificações AWS (ISO 27001, SOC 2) | — | N/A |
| **A.7.6** | Trabalho em áreas seguras | Não | ⬜ | Sem áreas seguras restritas na TWYN. Datacenters AWS são áreas seguras sob responsabilidade da AWS | N/A — Responsabilidade AWS. TWYN não possui áreas de processamento de dados seguras on-premises | Certificações AWS (ISO 27001, SOC 2) | — | N/A |
| **A.7.7** | Mesa limpa e tela limpa | Sim | 🟡 | Colaboradores possuem laptops; política de tela limpa definida (screen lock timeout configurado); mesa limpa orientada mas sem verificação formal | Screen lock timeout configurado (5 minutos). Política na SGSI-POLICY-001. Falta: verificação formal de compliance; treinamento específico | SGSI-POLICY-001 §14.1 | RISK-018 | RH |
| **A.7.8** | Localização e proteção de equipamentos | Não | ⬜ | Equipamentos de processamento (servidores) estão na AWS. Laptops dos colaboradores são cobertos por A.8.1 (endpoint devices). Sem equipamentos de rede ou servidores on-premises | N/A — Responsabilidade AWS para infraestrutura cloud. Laptops tratados em A.8.1 | Certificações AWS | — | N/A |
| **A.7.9** | Segurança de ativos fora das instalações | Sim | 🟡 | Colaboradores usam laptops fora do escritório (trabalho remoto); criptografia de disco em implementação; VPN disponível | Laptops com dados corporativos. Criptografia de disco sendo aplicada (FileVault/BitLocker). VPN para acesso a recursos. Falta: enforcement universal de encryption; política formal | SOP-003 (pendente) | RISK-018 | TI |
| **A.7.10** | Mídias de armazenamento | Sim | 🟡 | Sem uso de mídias físicas para dados de produção (100% cloud). Laptops possuem SSDs com dados locais. Política de uso de USB não definida | Dados de produção em AWS (S3, RDS). Sem uso de pen drives/HD externo para dados sensíveis. Falta: política de uso de mídias removíveis; bloqueio de USB se necessário | Política de mídias (a criar) | — | TI |
| **A.7.11** | Utilidades de suporte | Não | ⬜ | Utilidades de suporte (energia, climatização) dos datacenters são responsabilidade da AWS. Escritório não possui equipamentos críticos | N/A — Responsabilidade AWS para datacenters | Certificações AWS (ISO 27001, SOC 2) | — | N/A |
| **A.7.12** | Segurança de cabeamento | Não | ⬜ | Cabeamento de rede dos datacenters é responsabilidade da AWS. Escritório utiliza Wi-Fi corporativo sem cabeamento crítico | N/A — Responsabilidade AWS para datacenters | Certificações AWS (ISO 27001, SOC 2) | — | N/A |
| **A.7.13** | Manutenção de equipamentos | Não | ⬜ | Infraestrutura cloud AWS: manutenção de hardware é responsabilidade da AWS. Laptops: manutenção pelo TI interno ou garantia do fabricante | N/A — Responsabilidade AWS para infraestrutura cloud. Laptops: suporte TI interno/garantia | Certificações AWS; Tickets TI | — | N/A |
| **A.7.14** | Descarte seguro ou reutilização de equipamentos | Não | ⬜ | Recursos cloud: sem descarte físico (AWS gerencia). Laptops: wipe seguro antes de descarte/realocação | N/A para infraestrutura cloud. Laptops: secure wipe (DoD 5220.22-M ou equivalente) antes de descarte. Falta: procedimento formal documentado | Política TI (a criar) | — | TI |

**Resumo Controles Físicos**: 10/14 = **Não Aplicável** (72%). Os 4 aplicáveis referem-se ao escritório e endpoints dos colaboradores.

---

## 8. TEMA 4: CONTROLES TECNOLÓGICOS (A.8.1 – A.8.34)

**Total**: 34 controles | **Aplicáveis**: 33 | **N/A**: 1

| ID | Título do Controle | Aplicável? | Status | Justificativa | Detalhes de Implementação | Referência de Evidência | Referência de Risco | Responsável |
|----|-------------------|------------|--------|---------------|---------------------------|------------------------|---------------------|-------------|
| **A.8.1** | Dispositivos de endpoint de usuário | Sim | 🟡 | Colaboradores usam laptops; criptografia de disco em implementação; sem MDM (RISK-018) | Laptops fornecidos pela empresa. Criptografia sendo aplicada. Antivírus/EDR parcial (Windows Defender). Falta: MDM (Jamf/Intune); enforcement de encryption; inventário de endpoints | SOP-003 (pendente) | RISK-018 | TI |
| **A.8.2** | Direitos de acesso privilegiado | Sim | 🟡 | Acesso root/admin AWS existe; políticas excessivamente permissivas (GAP-003); MFA no root configurado | IAM roles com AdministratorAccess (problemático). Root account com MFA. CloudTrail audita ações privilegiadas. Falta: eliminar AdministratorAccess; criar roles customizados por função | IAM policies; CloudTrail | RISK-003, RISK-004 | Cloud Infra |
| **A.8.3** | Restrição de acesso à informação | Sim | 🟡 | AWS IAM + S3 bucket policies implementados; princípio do menor privilégio sendo aplicado progressivamente | IAM policies restringem acesso por role. S3 bucket policies. RDS security groups. Falta: revisão completa para least privilege; eliminar acessos excessivos | IAM policies; S3 policies | RISK-004 | Cloud Infra |
| **A.8.4** | Acesso ao código-fonte | Sim | ✅ | Repositórios GitHub privados; branch protection habilitada; PR reviews obrigatórios (2 aprovadores) | GitHub repos privados em org t4isb-infra. Branch protection rules em main/master. PRs exigem 2 aprovações. Falta: CODEOWNERS (desejável); signed commits (desejável) | GitHub settings; Branch protection | RISK-014 | CTO |
| **A.8.5** | Autenticação segura | Sim | 🟡 | MFA parcial (não todos os usuários AWS console); rotação de chaves pendente (RISK-006); JWT com expiração para APIs | MFA habilitado para maioria dos usuários console. JWT tokens com expiração. Secrets Manager para credenciais. Falta: MFA universal; rotação automática 90 dias; SOP-004 | IAM Console; Secrets Manager | RISK-003, RISK-006 | Cloud Infra |
| **A.8.6** | Gestão de capacidade | Sim | ✅ | AWS Auto Scaling configurado para EKS e RDS; CloudWatch alerts para thresholds de capacidade | EKS Horizontal Pod Autoscaler. RDS Auto Scaling para read replicas. CloudWatch Alarms para CPU, memória, storage. Alertas via SNS | CloudWatch dashboards; Auto Scaling configs | — | DevOps |
| **A.8.7** | Proteção contra malware | Sim | 🟡 | Scanning de imagens de container sendo habilitado (RISK-007); GuardDuty (GAP-002) para detecção de ameaças; sem EDR nos endpoints | Trivy/ECR scanning sendo configurado. GuardDuty EKS protection (em ativação). Container images base auditadas. Falta: scanning em CI/CD pipeline; EDR nos laptops | ECR scanning; GuardDuty | RISK-007 | SecOps |
| **A.8.8** | Gestão de vulnerabilidades técnicas | Sim | 🟡 | Dependabot habilitado para dependências; sem processo formal de patch management; sem scanning de vulnerabilidades periódico | Dependabot alertas em GitHub. npm audit em CI. Falta: processo formal de patch management; SAST/DAST; cronograma de scans; SLA de remediação | Dependabot alerts; GitHub | — | DevOps |
| **A.8.9** | Gestão de configuração | Sim | ❌ | AWS Config NÃO habilitado (GAP-001); IaC (Terraform) existe mas sem drift detection; configurações não auditadas automaticamente | Terraform para IaC. Falta: habilitar AWS Config; CIS Benchmark rules; drift detection; alertas de non-compliance | AWS Config (a habilitar) | RISK-002 | Cloud Infra |
| **A.8.10** | Exclusão de informações | Sim | 🟡 | S3 lifecycle policies existem; sem processo formal de exclusão de dados pessoais (DSR - LGPD) | S3 lifecycle rules para expiração de objetos. RDS com backup retention. Falta: processo de exclusão sob demanda (DSR Art. 18 LGPD); documentação de retenção por tipo de dado | S3 lifecycle; Política retenção (pendente) | RISK-016 | Cloud Infra |
| **A.8.11** | Mascaramento de dados | Sim | ❌ | Dados biométricos não copiados para staging (boa prática), mas sem mascaramento formal para ambientes não-produção | Staging usa dados sintéticos (parcial). Produção isolada. Falta: política formal de mascaramento; ferramentas de anonymization para dados de teste; validar que nenhum dado real vai para dev/staging | Política (a criar) | RISK-001 | DevOps |
| **A.8.12** | Prevenção de vazamento de dados | Sim | ❌ | Sem solução DLP implementada; CloudTrail registra chamadas API sensíveis; AWS Macie não habilitado | CloudTrail audita acessos a S3. VPC sem NAT egress filtering. Falta: AWS Macie para classificação/detecção; DLP para endpoints; regras de egress filtering | CloudTrail; Macie (a considerar) | RISK-001 | SecOps |
| **A.8.13** | Backup de informações | Sim | 🟡 | Backup automatizado (RDS snapshots, S3 versioning), mas NÃO testado (GAP-007); RPO/RTO não validados | RDS automated backups (7 dias retenção). S3 cross-region replication. EBS snapshots. Falta: teste de restore trimestral; documentar RTO/RPO real; GAP-007 | Backup configs; DR test (pendente) | RISK-009 | Cloud Infra |
| **A.8.14** | Redundância de instalações de processamento de informações | Sim | ✅ | Multi-AZ em us-east-1; DR cross-region para us-west-2; EKS multi-node com alta disponibilidade | EKS cluster com nodes em múltiplas AZs. RDS Multi-AZ deployment. S3 com 11 nines de durabilidade. ALB com health checks | AWS architecture; Multi-AZ config | RISK-015 | Cloud Infra |
| **A.8.15** | Logging | Sim | 🟡 | CloudTrail habilitado para API calls AWS; application logs parciais em CloudWatch; sem centralização completa | CloudTrail → S3 (1 ano retenção). CloudWatch Logs para pods EKS. VPC Flow Logs. Falta: centralização de todos os logs; correlação de eventos; SIEM | CloudTrail; CloudWatch Logs | — | Cloud Infra |
| **A.8.16** | Atividades de monitoramento | Sim | 🟡 | CloudWatch dashboards existem; GuardDuty sendo habilitado (GAP-002); sem SOC ou monitoramento 24/7 formal | CloudWatch Alarms para métricas de infraestrutura. Security Hub para postura de segurança. Falta: GuardDuty ativo; alertas para Slack/PagerDuty; processo de triagem | CloudWatch; Security Hub; GuardDuty (em ativação) | RISK-005 | DevOps |
| **A.8.17** | Sincronização de relógios | Sim | ✅ | AWS NTP gerenciado automaticamente; sincronização de relógio garantida pela infraestrutura AWS | Amazon Time Sync Service (NTP). Instâncias EC2/EKS nodes sincronizam automaticamente. Logs com timestamps consistentes (UTC) | AWS default NTP config | — | Cloud Infra |
| **A.8.18** | Uso de programas utilitários privilegiados | Sim | 🟡 | Terraform/CloudFormation para IaC logado via CloudTrail; sem processo formal de aprovação para uso de ferramentas privilegiadas | Terraform e kubectl como ferramentas privilegiadas. Ações registradas em CloudTrail. Falta: processo de aprovação formal; lista de ferramentas autorizadas | CloudTrail; IaC logs | — | DevOps |
| **A.8.19** | Instalação de software em sistemas operacionais | Sim | 🟡 | Containers controlados via imagens base aprovadas; laptops dos colaboradores menos controlados | Container images: base images auditadas, build via CI/CD (GitHub Actions → ECR). Laptops: sem controle de instalação (sem MDM). Falta: MDM para laptops; lista de software aprovado | ECR images; CI/CD pipeline | RISK-018 | TI |
| **A.8.20** | Segurança de redes | Sim | ✅ | VPC isolation, Security Groups, NACLs, WAF configurados; segmentação de rede implementada | VPC dedicada por ambiente. Security Groups com least privilege. NACLs para segmentação adicional. AWS WAF na frente de APIs públicas. ALB com SSL termination | VPC config; Security Groups; WAF rules | — | Cloud Infra |
| **A.8.21** | Segurança de serviços de rede | Sim | ✅ | Serviços de rede gerenciados pela AWS (ALB, Route53, CloudFront); TLS enforced | ALB com TLS 1.2+ obrigatório. Route53 para DNS. ACM para certificados SSL/TLS (renovação automática). PrivateLink para serviços internos | ALB config; ACM certificates | — | Cloud Infra |
| **A.8.22** | Segregação de redes | Sim | ✅ | VPCs separadas para prod/staging; subnets públicas/privadas; isolamento de workloads | VPC prod isolada de staging/dev. Subnets privadas para EKS, RDS. Subnets públicas apenas para ALB. No cross-VPC access sem VPC peering autorizado | VPC design; Subnet config | — | Cloud Infra |
| **A.8.23** | Filtragem web | Não | ⬜ | TWYN opera APIs backend; sem navegação web em servidores de produção; endpoints de colaboradores são baixo risco (aceito) | N/A — APIs não navegam web. Laptops: risco aceito (sem proxy/filtro web). Servidores containerizados não têm acesso à internet para navegação | N/A | — | N/A |
| **A.8.24** | Uso de criptografia | Sim | 🟡 | TLS 1.2+ enforced em trânsito; criptografia at rest parcial (RISK-001); sem política de criptografia formal | TLS 1.2+ para todas as APIs. S3 SSE-KMS (parcial). RDS encryption at rest. EBS encrypted volumes. KMS para gestão de chaves. Falta: encryption em TODOS os S3 buckets; política de criptografia documentada | KMS keys; TLS config; Crypto policy (pendente) | RISK-001 | Cloud Infra |
| **A.8.25** | Ciclo de vida de desenvolvimento seguro | Sim | 🟡 | PR reviews obrigatórios (2 aprovadores); CI/CD com testes; sem SAST/DAST formal; sem security gates | GitHub PRs com 2 reviewers. CI com testes unitários e lint. Docker build via GitHub Actions → ECR. Falta: SAST (Semgrep/SonarQube); DAST; security gate no pipeline | GitHub workflows; CI/CD pipeline | — | CTO |
| **A.8.26** | Requisitos de segurança de aplicações | Sim | ❌ | Sem requisitos formais de segurança no backlog de desenvolvimento; sem checklist de segurança para features | Nenhum processo formal. Ação: criar checklist de requisitos de segurança (autenticação, autorização, validação de input, logging) para cada feature/user story | Checklist (a criar) | — | CTO |
| **A.8.27** | Arquitetura de sistema segura e princípios de engenharia | Sim | ✅ | Arquitetura revisada no processo AWS FTR; documentada em diagramas; princípios de segurança aplicados (defense-in-depth) | Arquitetura multi-tier: ALB → EKS → RDS/S3. Defense-in-depth com WAF, SGs, NACLs. Encryption em camadas. Least privilege IAM. Revisão AWS FTR | Diagramas de arquitetura; AWS FTR docs | — | CTO |
| **A.8.28** | Codificação segura | Sim | 🟡 | Consciência OWASP; code review em PRs; sem treinamento formal de secure coding (GAP-006) | PR reviews avaliam segurança (informal). OWASP Top 10 como referência. Falta: treinamento formal de secure coding; SAST no CI/CD; guidelines documentadas | GitHub PRs; Training (pendente) | RISK-012 | CTO |
| **A.8.29** | Testes de segurança em desenvolvimento e aceitação | Sim | ❌ | Sem pentesting regular; testes ad-hoc apenas; sem testes de aceitação de segurança | Nenhum pentest formal realizado. Testes unitários não cobrem aspectos de segurança. Ação: agendar pentests trimestrais; integrar testes de segurança no CI/CD | Relatórios de pentest (a criar) | — | SecOps |
| **A.8.30** | Desenvolvimento terceirizado | Sim | ❌ | Sem desenvolvimento terceirizado atual, mas sem política para cenário futuro | Atualmente todo desenvolvimento é interno. Falta: política para cenário de terceirização futura; requisitos de segurança para fornecedores de desenvolvimento | Política (a criar) | — | CTO |
| **A.8.31** | Separação de ambientes de desenvolvimento, teste e produção | Sim | ✅ | Ambientes completamente separados em contas/VPCs AWS distintas; dados de produção não compartilhados | Contas AWS separadas: dev/staging/prod. VPCs distintas. Credenciais diferentes. Dados de produção não copiados para staging. GitHub branches separados | Contas AWS; VPC configs | — | Cloud Infra |
| **A.8.32** | Gestão de mudanças | Sim | 🟡 | Mudanças via PR-based workflow (GitHub); SOP-002 em elaboração; sem CAB formal | Todas as mudanças em produção via PR + CI/CD. Terraform plan/apply com aprovação. Falta: SOP-002 completo; processo formal de CAB; rollback documentado | GitHub PRs; Terraform logs; SOP-002 (pendente) | RISK-014 | DevOps |
| **A.8.33** | Informações de teste | Sim | 🟡 | Staging usa dados sintéticos (maioria); snapshots de produção ocasionais (necessita política formal) | Dados sintéticos para testes. Snapshots de produção sanitizados (parcial). Falta: política formal proibindo dados reais em ambientes de teste; processo de sanitização documentado | Política (a criar) | — | DevOps |
| **A.8.34** | Proteção de sistemas de informação durante testes de auditoria | Sim | ❌ | Primeiro audit pendente (Q3 2026); sem plano de proteção durante auditoria | Nenhum plano de proteção durante auditoria. Ação: criar procedimento para auditorias (acesso controlado do auditor, escopo de testes, proteção de ambientes) | Plano (a criar) | — | Gestor SGSI |

---

## 9. Controles Não Aplicáveis — Resumo e Justificativa

**Total N/A**: 11 controles (12% do total de 93)

| ID | Título | Justificativa Detalhada | Base Legal/Técnica |
|----|--------|------------------------|--------------------|
| **A.7.1** | Perímetros de segurança física | Sem datacenter próprio. Infraestrutura 100% cloud AWS. Segurança física dos datacenters é responsabilidade exclusiva da AWS | Modelo de Responsabilidade Compartilhada AWS; AWS ISO 27001; AWS SOC 2 Type II |
| **A.7.2** | Entrada física | Sem datacenter próprio. Controle de entrada física aos datacenters é responsabilidade da AWS | Modelo de Responsabilidade Compartilhada AWS; AWS ISO 27001 |
| **A.7.4** | Monitoramento de segurança física | Monitoramento físico de datacenters é responsabilidade da AWS. CCTV do escritório existe como controle compensatório (baixo risco) | Modelo de Responsabilidade Compartilhada AWS; RISK-ACC-002 |
| **A.7.5** | Proteção contra ameaças físicas e ambientais | Proteção contra incêndio, inundação e desastres em datacenters é responsabilidade da AWS. Escritório sem equipamentos críticos | Modelo de Responsabilidade Compartilhada AWS; AWS SOC 2 |
| **A.7.6** | Trabalho em áreas seguras | Sem áreas seguras restritas na TWYN. Processamento de dados ocorre em datacenters AWS | Modelo de Responsabilidade Compartilhada AWS |
| **A.7.8** | Localização e proteção de equipamentos | Servidores e equipamentos de processamento estão em datacenters AWS. Laptops cobertos por A.8.1 | Modelo de Responsabilidade Compartilhada AWS |
| **A.7.11** | Utilidades de suporte | Energia, climatização e utilidades dos datacenters são responsabilidade da AWS | Modelo de Responsabilidade Compartilhada AWS; AWS SOC 2 |
| **A.7.12** | Segurança de cabeamento | Cabeamento de rede dos datacenters é responsabilidade da AWS. Escritório sem cabeamento crítico | Modelo de Responsabilidade Compartilhada AWS |
| **A.7.13** | Manutenção de equipamentos | Hardware de infraestrutura cloud gerenciado pela AWS. Laptops: suporte TI/garantia | Modelo de Responsabilidade Compartilhada AWS |
| **A.7.14** | Descarte seguro ou reutilização de equipamentos | Recursos cloud sem descarte físico (AWS gerencia mídia). Laptops: secure wipe é política TI interna, risco baixo | Modelo de Responsabilidade Compartilhada AWS |
| **A.8.23** | Filtragem web | TWYN opera APIs backend sem navegação web em produção. Endpoints de colaboradores: risco baixo aceito | APIs não navegam web; risco residual aceito |

> **⚠️ APROVAÇÃO OBRIGATÓRIA**: As classificações N/A acima devem ser formalmente aprovadas pelo CEO e Gestor SGSI.

---

## 10. Mapeamento Controle-Risco

**Riscos principais e controles associados**:

| ID Risco | Descrição | Controles Primários | Status |
|----------|-----------|--------------------| -------|
| RISK-001 | Vazamento de dados biométricos via S3 | A.8.24, A.8.11, A.8.12, A.5.23 | 🟡 Em tratamento |
| RISK-002 | Falta de monitoramento de compliance AWS Config | A.8.9, A.5.37 | ❌ GAP-001 |
| RISK-003 | Acesso não autorizado à conta root AWS | A.5.15, A.5.17, A.8.2, A.8.5 | 🟡 Em tratamento |
| RISK-004 | IAM over-permissioning (ameaça interna) | A.5.18, A.5.3, A.6.4, A.8.2 | 🔴 Aberto |
| RISK-005 | Falta de detecção de ameaças (sem GuardDuty) | A.5.7, A.8.16, A.5.25 | 🔴 Aberto |
| RISK-006 | Chave IAM não rotacionada (>90 dias) | A.5.16, A.5.17, A.8.5 | 🔴 Aberto — Bloqueador FTR |
| RISK-007 | Ataque ransomware em clusters EKS | A.8.7, A.8.13, A.5.29, A.5.30 | 🟡 Em tratamento |
| RISK-008 | Recursos legados/órfãos (blind spots) | A.5.9, A.5.12, A.8.10 | 🔴 Aberto |
| RISK-009 | Backup não testado (DR desconhecido) | A.8.13, A.5.30 | 🔴 Aberto |
| RISK-010 | Sem AWS Business Support | A.5.22, A.5.23 | 🔴 Decisão pendente |
| RISK-011 | 8 controles CIS Benchmark ausentes | A.5.16, A.8.3, A.5.1 | 🔴 Aberto — Bloqueador FTR |
| RISK-012 | Sem treinamento de conscientização SI | A.6.3, A.5.10 | 🔴 Aberto |
| RISK-013 | Sem processo de revisão pela direção | Cláusula 9.3 (mandatória) | 🔴 Aberto |
| RISK-014 | Comprometimento de conta GitHub | A.8.28, A.8.32, A.5.16, A.8.4 | 🔴 Aberto |
| RISK-015 | Dependência de região única (us-east-1) | A.5.29, A.5.30, A.8.14 | 🟡 Aceito parcialmente |
| RISK-016 | Não conformidade LGPD (sem DPO, sem DPIA) | A.5.34, A.5.31, A.5.8 | 🔴 Aberto |
| RISK-017 | Sem plano de resposta a incidentes | A.5.24, A.5.25, A.5.26, A.5.27 | 🔴 Aberto |
| RISK-018 | Segurança de endpoints (laptops) | A.6.7, A.7.7, A.8.1, A.7.9 | 🔴 Aberto |

---

## 11. Roadmap de Implementação

**Meta**: 100% de conformidade até Q3 2026 (agosto)

### Fase 1 — GAPS CRÍTICOS (Junho 2026)

| Prioridade | Ação | Controles | GAP/RISK | Prazo | Responsável |
|------------|------|-----------|----------|-------|-------------|
| 🔴 P0 | Habilitar AWS Config + CIS rules | A.8.9 | GAP-001, RISK-002 | 10/06/2026 | Cloud Infra |
| 🔴 P0 | Habilitar GuardDuty em todas as regiões | A.5.7, A.8.16 | GAP-002, RISK-005 | 12/06/2026 | SecOps |
| 🔴 P0 | Auditoria IAM + least privilege | A.5.15, A.5.18, A.8.2 | GAP-003, RISK-004 | 30/06/2026 | Cloud Infra |
| 🔴 P0 | Inventário de ativos AWS | A.5.9 | GAP-004, RISK-008 | 20/06/2026 | Cloud Infra |
| 🔴 P0 | Rotação chave IAM tmpsaasboost | A.5.17, A.8.5 | RISK-006 (FTR) | 08/06/2026 | Cloud Infra |
| 🔴 P0 | Corrigir 8 controles CIS | A.5.16, A.8.3 | RISK-011 (FTR) | 08/06/2026 | Cloud Infra + SecOps |
| 🔴 P0 | Criptografia S3 completa (SSE-KMS) | A.8.24 | RISK-001 | 15/06/2026 | Cloud Infra |

### Fase 2 — EVIDÊNCIAS OPERACIONAIS (Junho-Julho 2026)

| Prioridade | Ação | Controles | GAP/RISK | Prazo | Responsável |
|------------|------|-----------|----------|-------|-------------|
| 🟠 P1 | Primeira revisão pela direção | Cláusula 9.3 | GAP-005, RISK-013 | 15/06/2026 | Gestor SGSI |
| 🟠 P1 | Treinamento SI para todos os colaboradores | A.6.3 | GAP-006, RISK-012 | 30/06/2026 | RH + SGSI |
| 🟠 P1 | Teste de DR (restore backup) | A.8.13, A.5.30 | GAP-007, RISK-009 | 15/06/2026 | Cloud Infra |
| 🟠 P1 | Criar IRP (Plano Resposta Incidentes) | A.5.24-A.5.27 | RISK-017 | 25/06/2026 | SecOps + SGSI |
| 🟠 P1 | Designar DPO + publicar Privacy Policy | A.5.34, A.5.31 | RISK-016 | 30/06/2026 | Jurídico |

### Fase 3 — DOCUMENTAÇÃO E PROCESSOS (Julho-Agosto 2026)

| Prioridade | Ação | Controles | GAP/RISK | Prazo | Responsável |
|------------|------|-----------|----------|-------|-------------|
| 🟡 P2 | Completar SOPs 001-005 | A.5.37 | — | 15/07/2026 | SGSI |
| 🟡 P2 | Matriz RACI formal | A.5.2 | — | 15/07/2026 | Gestor SGSI |
| 🟡 P2 | Política de criptografia documentada | A.8.24 | — | 15/07/2026 | Cloud Infra |
| 🟡 P2 | Política de trabalho remoto (SOP-003) | A.6.7, A.7.7, A.7.9 | RISK-018 | 15/07/2026 | RH + TI |
| 🟡 P2 | Avaliação formal de fornecedores | A.5.19-A.5.22 | — | 30/07/2026 | Gestor SGSI |
| 🟡 P2 | Checklist segurança em projetos | A.5.8 | — | 30/07/2026 | CTO |
| 🟡 P2 | Implementar DLP (AWS Macie) | A.8.12 | RISK-001 | 30/07/2026 | SecOps |
| 🟡 P2 | Data masking para non-prod | A.8.11 | — | 30/07/2026 | DevOps |

### Fase 4 — PRONTIDÃO PARA AUDITORIA (Agosto 2026)

| Prioridade | Ação | Controles | GAP/RISK | Prazo | Responsável |
|------------|------|-----------|----------|-------|-------------|
| 🟢 P3 | Programa de auditoria interna | A.5.35, A.5.36 | GAP-008 | 01/08/2026 | Gestor SGSI |
| 🟢 P3 | Completar todos os 🟡 → ✅ | Todos parciais | — | 15/08/2026 | Todos |
| 🟢 P3 | Coletar e organizar todas as evidências | Todos | — | 15/08/2026 | Gestor SGSI |
| 🟢 P3 | Simulação de auditoria (mock audit) | Todos | — | 20/08/2026 | Gestor SGSI |
| 🟢 P3 | SAST/DAST no pipeline CI/CD | A.8.25, A.8.29 | — | 30/08/2026 | CTO + SecOps |
| 🟢 P3 | Pentest formal | A.8.29 | — | 30/08/2026 | SecOps |

---

## 12. Checklist de Evidências para Auditoria

Para cada controle marcado como ✅ ou 🟡, o auditor poderá solicitar:

| Categoria de Controle | Evidências Requeridas |
|-----------------------|----------------------|
| **Políticas (A.5.1-A.5.6)** | Políticas assinadas, registros de aprovação, comprovante de comunicação |
| **Gestão de Ativos (A.5.9-A.5.13)** | Inventário de ativos, classificação documentada, labels/tags |
| **Controle de Acesso (A.5.15-A.5.18, A.8.2-A.8.5)** | Screenshots IAM, logs de revisão de acesso, status MFA |
| **Fornecedores (A.5.19-A.5.23)** | Contratos com cláusulas SI, BAA/DPA, avaliações |
| **Incidentes (A.5.24-A.5.28)** | IRP documentado, tickets de incidentes, post-mortems |
| **Continuidade (A.5.29-A.5.30, A.8.13-A.8.14)** | Resultados de DR drill, logs de backup, RTO/RPO validados |
| **Conformidade (A.5.31-A.5.36)** | Privacy Policy, DPO designação, programa de auditoria, DPIA |
| **Pessoas (A.6.1-A.6.8)** | Registros de seleção, contratos, NDAs, training logs, offboarding |
| **Físicos (A.7.3, A.7.7, A.7.9, A.7.10)** | Controle de acesso escritório, policy de tela limpa, encryption de laptops |
| **Criptografia (A.8.24)** | KMS config, TLS certificates (ACM), S3/RDS encryption status |
| **Rede (A.8.20-A.8.22)** | VPC config, Security Groups, NACLs, WAF rules |
| **Desenvolvimento (A.8.25-A.8.34)** | CI/CD pipelines, PR reviews, branch protection, pentest reports |
| **Logging/Monitoramento (A.8.15-A.8.17)** | CloudTrail config, CloudWatch dashboards, GuardDuty findings |

---

## 13. Revisão e Aprovação

Esta Declaração de Aplicabilidade deve ser revisada e aprovada **anualmente** ou quando:
- Mudanças significativas no escopo do SGSI
- Novos sistemas/serviços introduzidos no escopo
- Avaliação de riscos identifica novos controles necessários
- Achados de auditoria requerem alterações nos controles
- Mudanças na legislação ou regulamentação aplicável (LGPD, ANPD)
- Mudanças significativas na infraestrutura AWS

### Assinaturas de Aprovação

---

**CEO TWYN**

> *"Eu, [Nome Completo do CEO], na qualidade de Chief Executive Officer da TWYN, aprovo esta Declaração de Aplicabilidade e confirmo que os controles não aplicáveis são justificados conforme o escopo do SGSI e o modelo de responsabilidade compartilhada com a AWS."*

**Assinatura**: _______________________________
**Nome**: [Nome Completo]
**Cargo**: CEO — TWYN
**Data**: _____ / _____ / 2026

---

**Gestor SGSI**

> *"Eu, Ricardo Esper, na qualidade de Gestor SGSI da TWYN (Bekaa Trusted Advisors), declaro que esta SoA foi elaborada com base nos resultados da avaliação de riscos (SGSI-RISK-002) e reflete fielmente o status atual dos controles do Anexo A."*

**Assinatura**: _______________________________
**Nome**: Ricardo Esper
**Cargo**: Gestor SGSI — Bekaa Trusted Advisors
**Data**: _____ / _____ / 2026

---

**CTO TWYN**

**Assinatura**: _______________________________
**Nome**: [Nome Completo]
**Cargo**: CTO — TWYN
**Data**: _____ / _____ / 2026

---

## 14. Histórico de Revisões

| Versão | Data | Autor | Alterações |
|--------|------|-------|------------|
| 1.0 (Draft) | 26/05/2026 | Ricardo Esper (BEKAA) | Versão inicial — controles agrupados em faixas, 29 impl, 36 parciais, 16 não impl, 12 N/A |
| 2.0 (Draft) | 02/06/2026 | Ricardo Esper (BEKAA) | Reescrita completa: todos os 93 controles listados individualmente. Adicionados: detalhes de implementação, referências de evidência, mapeamento de riscos, roadmap de implementação por fases. Reclassificação de A.7.10/A.7.13/A.7.14 para adequar ao contexto de endpoints. Recalculadas estatísticas: 19 impl, 41 parciais, 22 não impl, 11 N/A |

---

## 15. Documentos Relacionados

| ID Documento | Título | Status |
|-------------|--------|--------|
| SGSI-SCOPE-001 | Documento de Escopo do SGSI | ✅ Draft |
| SGSI-POLICY-001 | Política de Segurança da Informação | ✅ Draft |
| SGSI-RISK-001 | Metodologia de Avaliação de Riscos | ✅ Draft |
| SGSI-RISK-002 | Registro de Riscos | ✅ Draft |
| SGSI-RTP-001 | Plano de Tratamento de Riscos | 📝 Pendente |
| SGSI-ASSETS-001 | Inventário de Ativos | 📝 Pendente |
| SGSI-IRP-001 | Plano de Resposta a Incidentes | 📝 Pendente |
| SGSI-DRP-001 | Plano de Disaster Recovery | 📝 Pendente |
| SGSI-AUDIT-001 | Programa de Auditoria Interna | 📝 Pendente |
| SOP-001 | Procedimento de Onboarding/Offboarding | 📝 Em elaboração |
| SOP-002 | Procedimento de Gestão de Mudanças | 📝 Em elaboração |
| SOP-003 | Política de Trabalho Remoto | 📝 Em elaboração |
| SOP-004 | Gestão de Segredos e Rotação | 📝 Em elaboração |
| SOP-005 | Recertificação de Acessos IAM | 📝 Em elaboração |

---

## 16. Glossário

| Termo | Definição |
|-------|-----------|
| **SGSI** | Sistema de Gestão de Segurança da Informação |
| **SoA** | Statement of Applicability (Declaração de Aplicabilidade) |
| **N/A** | Não Aplicável |
| **GAP** | Lacuna identificada no gap analysis |
| **FTR** | Foundational Technical Review (AWS) |
| **LGPD** | Lei Geral de Proteção de Dados (Lei 13.709/2018) |
| **ANPD** | Autoridade Nacional de Proteção de Dados |
| **DPO** | Data Protection Officer (Encarregado de Dados) |
| **DPIA** | Data Protection Impact Assessment (Avaliação de Impacto) |
| **DSR** | Data Subject Rights (Direitos do Titular) |
| **BAA** | Business Associate Agreement |
| **DPA** | Data Processing Agreement |
| **CIS** | Center for Internet Security |
| **MFA** | Multi-Factor Authentication |
| **IAM** | Identity and Access Management |
| **KMS** | Key Management Service |
| **WAF** | Web Application Firewall |
| **VPC** | Virtual Private Cloud |
| **NACL** | Network Access Control List |
| **ALB** | Application Load Balancer |
| **EKS** | Elastic Kubernetes Service |
| **RDS** | Relational Database Service |
| **ECR** | Elastic Container Registry |
| **ACM** | AWS Certificate Manager |
| **RTO** | Recovery Time Objective |
| **RPO** | Recovery Point Objective |
| **SAST** | Static Application Security Testing |
| **DAST** | Dynamic Application Security Testing |
| **DLP** | Data Leakage Prevention |
| **EDR** | Endpoint Detection and Response |
| **MDM** | Mobile Device Management |
| **CAB** | Change Advisory Board |
| **IRP** | Incident Response Plan |
| **NDA** | Non-Disclosure Agreement |
| **RBAC** | Role-Based Access Control |

---

**FIM DA DECLARAÇÃO DE APLICABILIDADE**

**Classificação**: CONFIDENCIAL
**Próxima Revisão**: Anual ou após mudança significativa
