---
**Document Control**
| Field | Value |
|-------|-------|
| **Document ID** | SGSI-SCOPE-001 |
| **Version** | 1.0 |
| **Author** | BEKAA Consultoria — Ricardo Esper |
| **Approved By** | [CEO TWYN / Gestor SGSI] |
| **Approval Date** | [Pendente] |
| **Effective Date** | [Pendente] |
| **Next Review** | [Anual após aprovação] |
| **ISO 27001:2022 Mapping** | Clause 4.3 — Context of the Organization |
---

# ISMS Scope Document
## Sistema de Gestão de Segurança da Informação — TWYN

### 1. Purpose (Objetivo)

Este documento define o **escopo do Sistema de Gestão de Segurança da Informação (SGSI)** da TWYN em conformidade com ISO/IEC 27001:2022, estabelecendo claramente:
- Quais ativos, processos e sistemas estão **dentro** do escopo de certificação
- Quais estão **fora** do escopo e suas justificativas
- Limites físicos e lógicos do SGSI
- Interfaces com partes externas

### 2. Organizational Context (Contexto Organizacional)

#### 2.1 About TWYN
**Razão Social**: [Nome legal da TWYN]  
**CNPJ**: [CNPJ da TWYN]  
**Endereço Principal**: [Endereço]  
**Setor**: Tecnologia — Plataforma de Autenticação Biométrica (Face ID)

**Modelo de Negócio**:
- Plataforma SaaS de autenticação biométrica via reconhecimento facial
- APIs REST hospedadas em AWS
- Clientes B2B (bancos, fintechs, empresas)
- Processamento de dados biométricos sensíveis

#### 2.2 Key Stakeholders

| Stakeholder | Interest | Requirements |
|-------------|----------|--------------|
| **Clientes B2B** | Conformidade regulatória (LGPD, GDPR) | Certificação ISO 27001, SOC 2 Type II, auditorias |
| **Usuários Finais** | Privacidade e proteção de dados biométricos | LGPD compliance, dados não compartilhados |
| **AWS** | Conformidade em cloud | FTR certification, CIS Benchmark |
| **Investidores** | Gestão de risco corporativo | Due diligence de segurança |
| **Reguladores** | LGPD, ANPD | Notificação de incidentes, DPO designado |

### 3. ISMS Scope Definition (Definição do Escopo)

#### 3.1 In Scope (Dentro do Escopo)

**Sistemas e Aplicações**:
- ✅ **Face ID Platform API** (REST API, produção)
  - Endpoints de autenticação biométrica
  - Processamento de imagens faciais
  - Matching de biometria
  - Integração com clientes via API

- ✅ **Infrastructure as Code (IaC)**
  - Terraform modules (todos os ambientes)
  - CloudFormation templates
  - Versioning via Git (GitHub)

- ✅ **Container Orchestration**
  - Amazon EKS clusters (produção e staging)
  - Kubernetes manifests
  - Helm charts

- ✅ **CI/CD Pipelines**
  - GitHub Actions workflows
  - AWS CodePipeline
  - CodeBuild, CodeDeploy
  - Artifact registry (ECR)

- ✅ **Data Storage & Processing**
  - RDS PostgreSQL (dados transacionais)
  - S3 buckets (armazenamento de imagens — criptografado)
  - DynamoDB (cache e sessões)
  - CloudWatch Logs

- ✅ **Security & Monitoring**
  - AWS IAM (gestão de identidades)
  - AWS Secrets Manager
  - CloudTrail (auditoria)
  - GuardDuty (threat detection) — **sendo ativado**
  - AWS Config (compliance) — **sendo ativado**
  - Security Hub (CIS Benchmark)

**Ambientes AWS**:
- ✅ **Conta Produção**: `992382542028` — escopo PRINCIPAL
- ✅ **Conta Staging**: [Número da conta staging, se houver]
- ❌ Contas de desenvolvimento individual (fora do escopo)

**Localização Física**:
- ✅ **AWS Região**: `us-east-1` (N. Virginia) — primária
- ✅ **AWS Região**: `us-west-2` (Oregon) — DR/backup
- ✅ **Escritório TWYN**: [Endereço] — workstations administrativas apenas

**Processos de Negócio**:
- ✅ Desenvolvimento de software (metodologia ágil)
- ✅ Deployment e release management
- ✅ Incident response e gestão de incidentes
- ✅ Change management (mudanças em produção)
- ✅ Onboarding/offboarding de colaboradores
- ✅ Gestão de acesso e identidades (IAM)
- ✅ Backup e disaster recovery
- ✅ Monitoramento e observability

**Dados no Escopo**:
- ✅ **Dados Biométricos** (imagens faciais, templates) — **ALTA CRITICIDADE**
- ✅ **Dados de Clientes B2B** (contratos, configurações, API keys)
- ✅ **Logs de Auditoria** (CloudTrail, application logs)
- ✅ **Código-fonte** (repositórios GitHub privados)
- ✅ **Credenciais** (AWS secrets, DB passwords, API tokens)
- ✅ **Documentação técnica e de arquitetura**

#### 3.2 Out of Scope (Fora do Escopo)

**Sistemas Excluídos**:
- ❌ Ambientes de desenvolvimento local (laptops de devs)
- ❌ Ferramentas SaaS corporativas não críticas (Slack, Notion — gerenciados por fornecedores)
- ❌ Website marketing/institucional (WordPress ou similar)
- ❌ Sistemas financeiros/contábeis (se terceirizados)

**Processos Excluídos**:
- ❌ RH (folha de pagamento, benefícios) — se terceirizado
- ❌ Jurídico/contratual — exceto contratos de SI
- ❌ Vendas e marketing — exceto onde intersecta SI

**Justificativas para Exclusões**:
1. **Ambientes dev locais**: Não processam dados reais de produção; cobertos por política de workstation segura (Annex A.6.7)
2. **SaaS terceiros**: Cobertos por avaliação de fornecedores (Annex A.5.19-5.22) e contratos DPA
3. **Website marketing**: Não processa dados sensíveis; separado da infraestrutura de produção

#### 3.3 Physical and Logical Boundaries (Limites)

**Limite Físico**:
- Datacenters AWS em `us-east-1` e `us-west-2`
- Escritório TWYN em [Endereço] — apenas workstations administrativas

**Limite Lógico**:
- VPC `vpc-XXXXXXXXX` (produção)
- AWS Account `992382542028`
- Domínio `*.twyn.io` e `*.t4isb.com`
- Repositórios GitHub em `github.com/t4isb-infra/*`

**Limite Organizacional**:
- Equipe de Engenharia (Dev + DevOps + Infra)
- Equipe de SecOps (sendo estruturada)
- Gestor SGSI (a ser designado formalmente)
- CEO e C-level (responsabilidade final)

### 4. Dependencies and Interfaces (Dependências e Interfaces)

#### 4.1 External Dependencies

| Fornecedor | Serviço | Criticidade | Status DPA/BAA |
|------------|---------|-------------|----------------|
| **AWS** | Cloud infrastructure | CRÍTICA | ✅ BAA assinado (HIPAA/LGPD) |
| **GitHub** | Code repository | ALTA | ⏳ Avaliar DPA |
| **[Outros]** | [Serviço] | [Nível] | [Status] |

#### 4.2 Interfaces com Clientes

- **API Gateway**: Interface pública para clientes B2B
- **Webhooks**: Notificações assíncronas para clientes
- **Portal de Documentação**: Acesso público a docs técnicos

#### 4.3 Data Flows

```
Cliente B2B → API Gateway → EKS (Face ID API) → RDS/S3
                                ↓
                          CloudWatch/CloudTrail
```

### 5. Exclusions and Justifications (Exclusões)

Conforme ISO 27001:2022 Annex A, os seguintes controles são **excluídos** com justificativa:

| Control | Justification | Approved By |
|---------|---------------|-------------|
| A.7.1 Physical security perimeters | Infraestrutura 100% cloud (AWS); sem perímetro físico próprio. Covered by AWS SOC 2/ISO certifications. | [Gestor SGSI] |
| A.7.2 Physical entry | Mesma justificativa acima | [Gestor SGSI] |

*(Esta tabela será expandida no Statement of Applicability completo)*

### 6. Review and Maintenance (Revisão e Manutenção)

**Frequência de Revisão**: Anual ou quando:
- Mudanças significativas de arquitetura
- Novos serviços ou sistemas críticos
- Aquisições ou mudanças organizacionais
- Resultado de auditoria interna/externa
- Mudança de regulamentação aplicável

**Responsável pela Revisão**: Gestor SGSI + CTO

### 7. Approval (Aprovação)

Este escopo foi revisado e aprovado pelos seguintes responsáveis:

| Role | Name | Signature | Date |
|------|------|-----------|------|
| **CEO / Top Management** | [Nome] | _______________ | ___/___/2026 |
| **Gestor SGSI** | [Nome] | _______________ | ___/___/2026 |
| **CTO** | [Nome] | _______________ | ___/___/2026 |

---

## Annex A: Scope Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 (Draft) | 26/05/2026 | Ricardo Esper (BEKAA) | Initial version for TWYN ISMS scope definition |

---

## Annex B: Related Documents

- [SGSI-POLICY-001] Information Security Policy
- [SGSI-RISK-001] Risk Assessment Methodology
- [SGSI-SOA-001] Statement of Applicability
- AWS BAA (Business Associate Agreement)
- Architectural diagrams (GitHub: t4isb-infra)

---

**DRAFT — PENDING APPROVAL**
