---
document_id: SGSI-ASSETS-001
title: Asset Inventory - Inventário de Ativos de Informação
version: 1.0
date: 2026-05-26
iso_clause: "8.1"
annex_a_controls: "A.5.9, A.5.10, A.5.11, A.5.12"
classification: Confidential
owner: Gestor SGSI
approved_by: CEO
next_review: 2026-08-26
---

# Asset Inventory - Inventário de Ativos de Informação

## 1. Document Control

| Field | Value |
|-------|-------|
| Document ID | SGSI-ASSETS-001 |
| Version | 1.0 |
| Status | Draft |
| Classification | **Confidential** |
| Owner | Gestor SGSI |
| Approved By | CEO (Pendente) |
| Date Created | 2026-05-26 |
| Next Review | 2026-08-26 (Trimestral) |
| ISO 27001:2022 Clause | 8.1 (Operational planning and control) |
| Annex A Controls | A.5.9 (Inventory), A.5.10 (Acceptable use), A.5.11 (Return), A.5.12 (Classification) |

## 2. Purpose

Este documento mantém um inventário completo de todos os ativos de informação da TWYN que estão dentro do escopo do SGSI, conforme definido em **SGSI-SCOPE-001**. O inventário permite:

- Identificar e catalogar todos os ativos que processam, armazenam ou transmitem informações
- Atribuir proprietários e responsáveis por cada ativo
- Classificar ativos de acordo com seu valor de negócio e sensibilidade
- Mapear ativos a riscos no **Risk Register (SGSI-RISK-002)**
- Suportar decisões de tratamento de riscos e implementação de controles

## 3. Scope

Este inventário cobre:
- ✅ **Information Assets**: Dados, documentação, propriedade intelectual
- ✅ **Infrastructure Assets**: Serviços AWS, redes, armazenamento
- ✅ **Software Assets**: Aplicações, APIs, ferramentas
- ✅ **Human Assets**: Pessoas com acesso a informações sensíveis
- ❌ **Physical Assets**: N/A (arquitetura 100% cloud-only)

**Período de referência**: 2026-05-26
**Última atualização**: 2026-05-26
**Frequência de atualização**: Trimestral (ou sempre que houver mudanças significativas)

## 4. Asset Classification Framework

### 4.1 Information Classification Levels

| Level | Label | Definition | Examples | Required Controls |
|-------|-------|------------|----------|-------------------|
| **4** | CRITICAL | Perda/exposição causa dano irreparável ao negócio, legal, ou reputacional | Biometric data (face embeddings), chaves de criptografia mestras | Encryption at-rest + in-transit, MFA obrigatório, audit logging, DLP, backup off-site |
| **3** | CONFIDENTIAL | Perda/exposição causa dano significativo ao negócio ou compliance | Customer PII, contratos, credenciais de API, source code | Encryption at-rest, access control, logging, backup |
| **2** | INTERNAL | Uso interno apenas, impacto moderado se exposto | Documentação interna, métricas de negócio, logs de sistema | Access control, basic authentication |
| **1** | PUBLIC | Informação pública sem impacto se divulgada | Marketing materials, documentação pública | Nenhum controle especial |

### 4.2 Asset Types

- **INFO** - Information assets (data, documents, intellectual property)
- **INFRA** - Infrastructure assets (servers, networks, cloud services)
- **SW** - Software assets (applications, APIs, tools)
- **HW** - Hardware assets (devices, physical equipment)
- **PEOPLE** - Human assets (employees, contractors, administrators)

## 5. Asset Inventory

### 5.1 Information Assets (Category: INFO)

| Asset ID | Asset Name | Description | Classification | Owner | Location/System | Related Risks | Status |
|----------|------------|-------------|----------------|-------|-----------------|---------------|--------|
| INFO-001 | Biometric Data (Face Embeddings) | Face biometric templates/embeddings gerados pela Face ID Platform API | **CRITICAL** | DevOps Lead | S3 bucket: twyn-biometric-data (encrypted) | RISK-001, RISK-007 | Active |
| INFO-002 | Customer PII | Dados pessoais de clientes (nome, email, telefone, CPF) | CONFIDENTIAL | DevOps Lead | RDS PostgreSQL (encrypted), S3 backups | RISK-004, RISK-014 | Active |
| INFO-003 | Face ID Platform API Source Code | Código-fonte da API de reconhecimento facial | CONFIDENTIAL | Dev Team | GitHub: twyn-faceid-api (private repo) | RISK-002, RISK-013 | Active |
| INFO-004 | AWS IAM Credentials | Access keys, secret keys, temporary tokens | **CRITICAL** | DevOps Lead | AWS Secrets Manager, .env files (legacy) | RISK-003, RISK-006 | Active |
| INFO-005 | Database Credentials | RDS master passwords, application DB users | **CRITICAL** | DevOps Lead | AWS Secrets Manager | RISK-003 | Active |
| INFO-006 | API Keys (Third-party) | Chaves de APIs externas (payment, logging, monitoring) | CONFIDENTIAL | DevOps Lead | AWS Secrets Manager, GitHub Secrets | RISK-006, RISK-010 | Active |
| INFO-007 | Encryption Keys (KMS) | AWS KMS keys para criptografia de dados em repouso | **CRITICAL** | DevOps Lead | AWS KMS (Account 992382542028) | RISK-008 | Active |
| INFO-008 | CloudTrail Logs | Logs de auditoria de API calls da AWS | CONFIDENTIAL | DevOps Lead | S3 bucket: twyn-cloudtrail-logs (encrypted) | RISK-016 | Active |
| INFO-009 | Application Logs | Logs da Face ID Platform API (requests, errors, performance) | INTERNAL | DevOps Lead | CloudWatch Logs, S3 (archived) | RISK-016 | Active |
| INFO-010 | Backup Data | Backups de RDS, S3, configurações de infraestrutura | **CRITICAL** | DevOps Lead | S3 bucket: twyn-backups-dr (cross-region) | RISK-017 | Active |
| INFO-011 | SGSI Documentation | Políticas, procedimentos, SOPs, risk register | CONFIDENTIAL | Gestor SGSI | GitHub: twyn-sgsi-iso27001 | - | Active |
| INFO-012 | Business Contracts | Contratos com clientes, fornecedores, NDAs | CONFIDENTIAL | Finance/Legal | Google Drive (a confirmar) | - | Active |
| INFO-013 | Employee Personal Data | Dados de RH (contratos, salários, avaliações) | CONFIDENTIAL | HR | Sistema de RH (a confirmar) | - | Active |

### 5.2 Infrastructure Assets (Category: INFRA)

| Asset ID | Asset Name | Description | Classification | Owner | Location | Related Risks | Status |
|----------|------------|-------------|----------------|-------|----------|---------------|--------|
| INFRA-001 | AWS Account 992382542028 | Conta principal AWS em produção | **CRITICAL** | DevOps Lead | AWS (us-east-1 primary) | RISK-003, RISK-005, RISK-011 | Active |
| INFRA-002 | AWS VPC (Production) | Virtual Private Cloud isolando recursos de produção | CONFIDENTIAL | DevOps Lead | us-east-1 | RISK-005, RISK-012 | Active |
| INFRA-003 | EKS Cluster (twyn-faceid-prod) | Kubernetes cluster executando Face ID Platform API | **CRITICAL** | DevOps Lead | us-east-1a, us-east-1b | RISK-001, RISK-009, RISK-011 | Active |
| INFRA-004 | RDS PostgreSQL (twyn-prod-db) | Banco de dados relacional de produção | **CRITICAL** | DevOps Lead | us-east-1 (Multi-AZ) | RISK-001, RISK-004, RISK-017 | Active |
| INFRA-005 | S3 Bucket: twyn-biometric-data | Armazenamento de embeddings biométricos | **CRITICAL** | DevOps Lead | us-east-1 (encryption: AES-256) | RISK-001, RISK-012 | Active |
| INFRA-006 | S3 Bucket: twyn-backups-dr | Backups cross-region para disaster recovery | **CRITICAL** | DevOps Lead | us-west-2 (encryption: SSE-KMS) | RISK-017 | Active |
| INFRA-007 | S3 Bucket: twyn-cloudtrail-logs | Logs de auditoria AWS CloudTrail | CONFIDENTIAL | DevOps Lead | us-east-1 (immutable, versioning) | RISK-016 | Active |
| INFRA-008 | AWS CloudTrail | Serviço de logging de API calls | CONFIDENTIAL | DevOps Lead | Multi-region enabled | RISK-016 | Active |
| INFRA-009 | AWS Config | Serviço de configuração e compliance (CIS benchmarks) | CONFIDENTIAL | DevOps Lead | us-east-1 | RISK-011 (AWS FTR blocker) | Partial |
| INFRA-010 | AWS GuardDuty | Threat detection service | CONFIDENTIAL | DevOps Lead | us-east-1 | RISK-007, RISK-012 | Active |
| INFRA-011 | AWS Security Hub | Security findings aggregation | CONFIDENTIAL | DevOps Lead | us-east-1 | RISK-011 | Active |
| INFRA-012 | AWS IAM | Identity and Access Management | **CRITICAL** | DevOps Lead | Global | RISK-003, RISK-006, RISK-015 | Active |
| INFRA-013 | AWS KMS | Key Management Service | **CRITICAL** | DevOps Lead | us-east-1 | RISK-008 | Active |
| INFRA-014 | AWS Secrets Manager | Gerenciamento de credenciais e secrets | **CRITICAL** | DevOps Lead | us-east-1 | RISK-006, RISK-010 | Active |
| INFRA-015 | Application Load Balancer (ALB) | Load balancer para Face ID API | CONFIDENTIAL | DevOps Lead | us-east-1 (TLS 1.2+) | RISK-012 | Active |
| INFRA-016 | Route 53 (DNS) | Serviço de DNS para domínio da API | CONFIDENTIAL | DevOps Lead | Global | - | Active |
| INFRA-017 | CloudWatch | Monitoring, logging, alerting | INTERNAL | DevOps Lead | us-east-1 | RISK-009, RISK-016 | Active |

### 5.3 Software Assets (Category: SW)

| Asset ID | Asset Name | Description | Classification | Owner | Location | Related Risks | Status |
|----------|------------|-------------|----------------|-------|----------|---------------|--------|
| SW-001 | Face ID Platform API v2.x | API REST de reconhecimento facial biométrico | **CRITICAL** | Dev Team | EKS cluster (production) | RISK-001, RISK-002, RISK-013 | Active |
| SW-002 | CI/CD Pipeline (GitHub Actions) | Pipeline de build, test, deploy automatizado | CONFIDENTIAL | DevOps Lead | GitHub Actions, AWS ECR | RISK-002, RISK-013 | Active |
| SW-003 | Docker Images (Face ID API) | Container images da aplicação | CONFIDENTIAL | Dev Team | AWS ECR (encrypted) | RISK-002, RISK-013 | Active |
| SW-004 | Terraform IaC | Infrastructure as Code para AWS | CONFIDENTIAL | DevOps Lead | GitHub: twyn-terraform (private) | RISK-011 | Active |
| SW-005 | Monitoring Stack | Prometheus, Grafana, alerting | INTERNAL | DevOps Lead | EKS cluster | RISK-009 | Active |
| SW-006 | API Documentation (Swagger/OpenAPI) | Documentação técnica da API | INTERNAL | Dev Team | GitHub Pages (internal) | - | Active |
| SW-007 | AWS CLI / SDKs | Ferramentas de linha de comando para AWS | INTERNAL | DevOps Lead | Developer laptops (out of scope) | - | Active |
| SW-008 | kubectl / helm | Ferramentas de gerenciamento Kubernetes | INTERNAL | DevOps Lead | Developer laptops | - | Active |

### 5.4 Human Assets (Category: PEOPLE)

| Asset ID | Asset Name | Role | Classification | Access Level | Security Clearance | Related Risks | Status |
|----------|------------|------|----------------|--------------|-------------------|---------------|--------|
| PEOPLE-001 | CEO | Chief Executive Officer | **CRITICAL** | Full (strategic decisions only) | Background check required | RISK-003 (root access) | Active |
| PEOPLE-002 | Gestor SGSI | ISMS Manager | **CRITICAL** | Full SGSI documentation | Background check required | - | To be assigned |
| PEOPLE-003 | DevOps Lead | Infrastructure & Security Lead | **CRITICAL** | Full AWS admin (IAM, EC2, RDS, S3) | Background check + technical screening | RISK-003, RISK-015 | Active |
| PEOPLE-004 | Senior Backend Developer | Face ID API Lead Developer | CONFIDENTIAL | Code repository, staging env | Technical screening | RISK-002, RISK-013 | Active |
| PEOPLE-005 | Backend Developer 1 | API Developer | CONFIDENTIAL | Code repository, dev env | Technical screening | RISK-002 | Active |
| PEOPLE-006 | Backend Developer 2 | API Developer | CONFIDENTIAL | Code repository, dev env | Technical screening | RISK-002 | Active |
| PEOPLE-007 | HR/People Ops | Human Resources | CONFIDENTIAL | Employee data, onboarding/offboarding | Background check | - | To be assigned |
| PEOPLE-008 | DPO/Legal | Data Protection Officer | CONFIDENTIAL | LGPD compliance, contracts | Background check | - | External (to be contracted) |
| PEOPLE-009 | Finance | Financial Controller | CONFIDENTIAL | Contracts, payments, insurance | Background check | - | To be assigned |
| PEOPLE-010 | External Security Consultant | ISO 27001 Consultant | CONFIDENTIAL | SGSI documentation, AWS read-only | NDA signed | - | Bekaa (active) |
| PEOPLE-011 | AWS Support Engineers | AWS Business Support | INTERNAL | AWS infrastructure (when tickets opened) | AWS vetting process | - | Active |

### 5.5 Hardware Assets (Category: HW)

**Status**: N/A - TWYN opera 100% em cloud (AWS). Não há hardware físico no escopo do SGSI.

**Nota**: Laptops de desenvolvedores estão **fora do escopo** conforme definido em **SGSI-SCOPE-001**, mas devem seguir a política de Clear Desk/Clear Screen (A.7.7) e Remote Work Policy (SOP-003).

## 6. Asset-to-Risk Mapping

Esta tabela mapeia ativos críticos aos riscos identificados no **Risk Register (SGSI-RISK-002)**.

| Asset ID | Asset Name | Related Risks | Risk Score | Priority |
|----------|------------|---------------|------------|----------|
| INFO-001 | Biometric Data | RISK-001 (S3 breach - 25), RISK-007 (Ransomware - 20) | **CRITICAL** | P0 |
| INFO-004 | AWS IAM Credentials | RISK-003 (Root access - 20), RISK-006 (Key >90d - 12) | **CRITICAL** | P0 |
| INFO-005 | Database Credentials | RISK-003 (Compromise - 20) | **CRITICAL** | P0 |
| INFO-007 | Encryption Keys (KMS) | RISK-008 (Key compromise - 15) | HIGH | P1 |
| INFO-010 | Backup Data | RISK-017 (Backup failure - 12) | HIGH | P1 |
| INFRA-001 | AWS Account 992382542028 | RISK-003, RISK-005, RISK-011 | **CRITICAL** | P0 |
| INFRA-003 | EKS Cluster | RISK-001, RISK-009, RISK-011 | **CRITICAL** | P0 |
| INFRA-004 | RDS PostgreSQL | RISK-001, RISK-004, RISK-017 | **CRITICAL** | P0 |
| INFRA-005 | S3 Bucket: Biometric Data | RISK-001 (Misconfiguration - 25), RISK-012 (Public access - 16) | **CRITICAL** | P0 |
| PEOPLE-003 | DevOps Lead | RISK-003 (Privileged access abuse - 20), RISK-015 (Single point of failure - 12) | **CRITICAL** | P0 |

## 7. Asset Ownership and Accountability

### 7.1 Asset Owner Responsibilities

Cada ativo DEVE ter um **Asset Owner** designado, responsável por:

- ✅ Classificar o ativo de acordo com o framework (Section 4.1)
- ✅ Definir controles de acesso apropriados
- ✅ Aprovar solicitações de acesso ao ativo
- ✅ Revisar permissões de acesso trimestralmente (IAM recertification)
- ✅ Reportar incidentes envolvendo o ativo
- ✅ Participar do processo de risk assessment relacionado ao ativo
- ✅ Garantir que o ativo seja adequadamente protegido conforme sua classificação
- ✅ Atualizar o inventário quando o ativo for modificado ou descontinuado

### 7.2 Current Ownership Distribution

| Owner | Number of Assets | Critical Assets | High-Priority Actions |
|-------|------------------|-----------------|----------------------|
| **DevOps Lead** | 24 (INFO: 9, INFRA: 15) | 11 CRITICAL | Implementar AWS Config rules, rotacionar tmpsaasboost key, enable MFA on root |
| **Dev Team** | 4 (INFO: 1, SW: 3) | 1 CRITICAL | Remediar vulnerabilidades SAST/DAST, secure coding training |
| **Gestor SGSI** | 1 (INFO: 1) | 0 | Manter SGSI documentation atualizada |
| **HR** | 1 (INFO: 1) | 0 | Definir processo de background checks |
| **Finance/Legal** | 1 (INFO: 1) | 0 | Centralizar contratos e NDAs |

**⚠️ OBSERVAÇÃO CRÍTICA**: DevOps Lead é proprietário de 11 ativos CRITICAL, representando um **Single Point of Failure** (RISK-015). Recomenda-se:
- Contratar backup/junior DevOps engineer (Q2 2026)
- Documentar runbooks para operações críticas
- Implementar princípio de least privilege e segregation of duties

## 8. Asset Lifecycle Management

### 8.1 Asset Creation

Quando um novo ativo é criado:

1. ✅ Asset Owner completa formulário de asset creation (ver Anexo A)
2. ✅ Gestor SGSI classifica o ativo (CRITICAL/CONFIDENTIAL/INTERNAL/PUBLIC)
3. ✅ Gestor SGSI adiciona o ativo ao inventário (este documento)
4. ✅ Gestor SGSI atualiza **Risk Register** se o ativo introduz novos riscos
5. ✅ Asset Owner implementa controles de segurança apropriados (encryption, access control, backup)
6. ✅ Gestor SGSI valida que controles foram implementados

### 8.2 Asset Modification

Quando um ativo é modificado (mudança de classificação, owner, localização):

1. ✅ Asset Owner notifica Gestor SGSI via ticket
2. ✅ Gestor SGSI avalia se a mudança requer reavaliação de risco
3. ✅ Se sim: realizar mini risk assessment e atualizar **Risk Register**
4. ✅ Gestor SGSI atualiza este inventário
5. ✅ Se mudança de owner: novo owner assina termo de responsabilidade

### 8.3 Asset Decommissioning

Quando um ativo é descontinuado:

1. ✅ Asset Owner submete decommission request para Gestor SGSI
2. ✅ Gestor SGSI valida que não há dependências críticas
3. ✅ Se o ativo contém dados sensíveis: seguir **Data Deletion Policy (A.8.10)**
   - Dados CRITICAL: Secure deletion com wiping (AWS KMS delete key, S3 bucket force empty)
   - Dados CONFIDENTIAL: Standard deletion com confirmação
4. ✅ Revogar todos os acessos ao ativo
5. ✅ Documentar a data de decommissioning e motivo
6. ✅ Marcar ativo como "Decommissioned" no inventário (não remover - manter histórico)
7. ✅ Atualizar **Risk Register** removendo riscos associados

## 9. Access Control Matrix

### 9.1 Access Levels by Classification

| Classification | Who Can Access | Authentication Required | Audit Logging | Encryption | Backup |
|----------------|----------------|-------------------------|---------------|------------|--------|
| **CRITICAL** | Explicit approval only (CEO or Gestor SGSI) | MFA mandatory | CloudTrail + application logs | At-rest + in-transit (AES-256, TLS 1.2+) | Daily, cross-region, encrypted |
| CONFIDENTIAL | Role-based access (approved by Asset Owner) | Password + MFA recommended | CloudTrail + application logs | At-rest + in-transit | Daily, encrypted |
| INTERNAL | All employees (read-only by default) | Password (AWS SSO or IAM) | CloudTrail only | At-rest (S3 default encryption) | Weekly |
| PUBLIC | No restriction | None | None | None | None |

### 9.2 Privileged Access (High-Risk Assets)

| Asset | Privileged Roles | Access Justification | Review Frequency |
|-------|-----------------|----------------------|------------------|
| AWS Root Account | CEO only | Break-glass emergency only | Never used (alerting enabled) |
| AWS IAM Admin | DevOps Lead | Infrastructure management | Trimestral (IAM recertification) |
| RDS Master User | DevOps Lead | Database administration | Trimestral |
| S3 Biometric Bucket | Face ID API (service account) | Application read/write | Trimestral |
| KMS Master Keys | DevOps Lead | Key management | Trimestral |
| GitHub Admin (twyn-faceid-api) | Dev Team Lead | Repository management | Trimestral |
| Secrets Manager Admin | DevOps Lead | Credential rotation | Trimestral |

## 10. Acceptable Use Policy (A.5.10)

Todos os ativos DEVEM ser usados de acordo com a **Information Security Policy (SGSI-POLICY-001)** e os seguintes princípios:

### 10.1 Mandatory Requirements

- ✅ Ativos CRITICAL/CONFIDENTIAL NÃO podem ser armazenados em dispositivos pessoais não gerenciados
- ✅ Ativos NÃO podem ser compartilhados via canais não criptografados (email sem encryption, Slack free, WhatsApp, etc.)
- ✅ Credenciais (passwords, API keys, tokens) NÃO podem ser commitadas em repositórios Git (NUNCA)
- ✅ Dados de produção NÃO podem ser copiados para ambientes de dev/staging sem anonimização
- ✅ Biometric data (INFO-001) NÃO pode ser acessado fora da AWS por humanos (apenas aplicação)
- ✅ AWS root account NÃO pode ser usado para operações do dia-a-dia (break-glass only)
- ✅ Backups NÃO podem ser deletados sem aprovação do Gestor SGSI

### 10.2 Prohibited Activities

- ❌ Uso de ativos da empresa para atividades ilegais, antiéticas, ou não relacionadas ao trabalho
- ❌ Mining de criptomoedas em infraestrutura AWS
- ❌ Armazenamento de dados pessoais não relacionados ao negócio
- ❌ Download ou instalação de software não autorizado em ambientes de produção
- ❌ Compartilhamento de credenciais entre usuários
- ❌ Desabilitar security controls (CloudTrail, GuardDuty, Config) sem aprovação formal

### 10.3 Consequences of Misuse

Violações da Acceptable Use Policy podem resultar em:
- Advertência formal (primeira violação não intencional)
- Revogação de acesso (violação intencional ou repetida)
- Processo disciplinar ou rescisão de contrato (violações graves)
- Responsabilização legal (se violação resultar em dano à empresa ou terceiros)

## 11. Return of Assets (A.5.11)

### 11.1 Offboarding Checklist

Quando um colaborador ou contratado deixa a empresa:

- ✅ **D-7 dias**: HR notifica Gestor SGSI e DevOps Lead sobre data de saída
- ✅ **D-1 dia**: Documentar knowledge transfer (runbooks, passwords vault access)
- ✅ **D-Day 16:00**: Revogar todos os acessos:
  - AWS IAM user (disable + delete)
  - GitHub access (remove from organization)
  - Secrets Manager / password vault
  - VPN / SSO accounts
  - Email forwarding configured
- ✅ **D-Day 18:00**: Verificar que não restam acessos ativos (IAM audit)
- ✅ **D+1 dia**: Confirmar que laptop foi devolvido (se aplicável, devices out of scope)
- ✅ **D+7 dias**: Revisar CloudTrail logs para atividades suspeitas nas últimas 2 semanas

Detalhes completos em **SOP-001: Onboarding/Offboarding**.

## 12. Asset Inventory Audit Schedule

| Audit Type | Frequency | Responsible | Next Due Date | Deliverable |
|------------|-----------|-------------|---------------|-------------|
| **Full Asset Inventory Review** | Trimestral | Gestor SGSI + All Asset Owners | 2026-08-26 | Updated SGSI-ASSETS-001 |
| **Critical Assets Verification** | Mensal | Gestor SGSI + DevOps Lead | 2026-06-26 | Verification checklist |
| **IAM Access Recertification** | Trimestral | DevOps Lead | 2026-08-26 | IAM access report (SOP-005) |
| **Asset Classification Review** | Anual | Gestor SGSI + CEO | 2027-05-26 | Classification matrix |
| **Decommissioned Assets Cleanup** | Semestral | Gestor SGSI | 2026-11-26 | Cleanup report |

## 13. Integration with Other SGSI Documents

| Document | Relationship | How Assets Are Used |
|----------|--------------|---------------------|
| **SGSI-SCOPE-001** | Defines which assets are in-scope | Assets out of scope (developer laptops) not included in this inventory |
| **SGSI-RISK-002** | Risk Register | Each risk is mapped to one or more assets (Section 6) |
| **SGSI-RTP-001** | Risk Treatment Plan | Controls implemented to protect specific assets |
| **SGSI-SOA-001** | Statement of Applicability | Controls A.5.9-5.12 implemented via this inventory |
| **SGSI-POLICY-001** | Information Security Policy | Acceptable use rules (Section 10) derive from top-level policy |
| **SOP-001** | Onboarding/Offboarding | Asset access provisioning and return (Section 11) |
| **SOP-005** | IAM Recertification | Quarterly review of asset access (Section 9.2) |

## 14. KPIs and Metrics

| Metric | Target | Current | Status |
|--------|--------|---------|--------|
| Asset inventory completeness | 100% of in-scope assets documented | ~95% (pending: HR system, contract storage details) | 🟡 |
| Assets with assigned owner | 100% | 100% | ✅ |
| Critical assets with encryption at-rest | 100% | 100% | ✅ |
| Critical assets with MFA-protected access | 100% | 60% (root account MFA pending) | 🔴 |
| Assets reviewed in last 90 days | 100% | 0% (new inventory) | 🟡 |
| Orphaned IAM users (no owner) | 0 | 1 (tmpsaasboost - RISK-006) | 🔴 |
| Assets with backup > 24h old | 0 | 0 | ✅ |

## 15. Approval and Review

| Field | Value |
|-------|-------|
| **Document Prepared By** | Security Consultant (Bekaa) |
| **Document Reviewed By** | Gestor SGSI (Pendente) |
| **Document Approved By** | CEO (Pendente) |
| **Approval Date** | Pendente |
| **Effective Date** | Após aprovação CEO |
| **Next Review Date** | 2026-08-26 (Trimestral) |

---

## 16. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-05-26 | Security Consultant | Versão inicial - 13 info assets, 17 infra assets, 8 software assets, 11 human assets. Total: 49 assets catalogados. |

---

## Anexo A: Asset Creation Form Template

```markdown
## New Asset Request

**Submitted by**: [Nome]
**Date**: [YYYY-MM-DD]
**Asset Type**: [INFO / INFRA / SW / HW / PEOPLE]

### Asset Details
- **Asset Name**:
- **Description**:
- **Location/System**:
- **Proposed Classification**: [CRITICAL / CONFIDENTIAL / INTERNAL / PUBLIC]
- **Justification for Classification**:

### Access Requirements
- **Initial Asset Owner**:
- **Who needs access**:
- **Access justification**:

### Security Controls Required
- [ ] Encryption at-rest
- [ ] Encryption in-transit
- [ ] MFA for access
- [ ] Audit logging (CloudTrail/application logs)
- [ ] Backup (daily/weekly)
- [ ] Data retention policy

### Risk Assessment
- **Does this asset introduce new risks?**: [Yes/No]
- **If yes, describe**:

---

**Approval**:
☐ Gestor SGSI: ________________ Date: ______
☐ Asset Owner: ________________ Date: ______
```

---

## Anexo B: Asset Decommissioning Form Template

```markdown
## Asset Decommissioning Request

**Submitted by**: [Nome]
**Date**: [YYYY-MM-DD]
**Asset ID**: [e.g., INFO-001]

### Decommissioning Details
- **Asset Name**:
- **Reason for decommissioning**:
- **Proposed decommission date**: [YYYY-MM-DD]
- **Dependencies**: [List any systems or processes that depend on this asset]

### Data Handling
- **Does asset contain sensitive data?**: [Yes/No]
- **If yes, classification level**: [CRITICAL / CONFIDENTIAL / INTERNAL / PUBLIC]
- **Data deletion method**:
  - [ ] Secure wipe (for CRITICAL assets)
  - [ ] Standard deletion
  - [ ] Transfer to archive
  - [ ] N/A (no sensitive data)

### Access Revocation
- [ ] All IAM users/roles revoked
- [ ] API keys/secrets deleted from Secrets Manager
- [ ] Resource tags updated to "decommissioned"
- [ ] Backups retained per data retention policy (yes/no): ______

---

**Approval**:
☐ Gestor SGSI: ________________ Date: ______
☐ Asset Owner: ________________ Date: ______
☐ Decommissioning executed by: ________________ Date: ______
```

---

**⚠️ NEXT STEPS**:
1. **CEO**: Revisar e aprovar este inventário
2. **Gestor SGSI**: Preencher campos "To be assigned" com nomes reais da equipe TWYN
3. **DevOps Lead**: Confirmar todos os asset IDs de infraestrutura AWS (bucket names, RDS instance IDs, EKS cluster names)
4. **HR**: Confirmar onde estão armazenados contratos de funcionários e employee data
5. **Finance**: Confirmar onde estão armazenados contratos de clientes/fornecedores
6. **ALL**: Conduzir primeira **Asset Inventory Review** em 2026-06-26 (1 mês)
