---
document_id: SGSI-SCOPE-001
title: Documento de Escopo do SGSI
version: 1.0
date: 2026-06-08
iso_clause: "4.3"
classification: INTERNAL
owner: BEKAA Consultoria — Ricardo Esper
approved_by: CEO TWYN
---

# Documento de Escopo do SGSI
## Sistema de Gestão de Segurança da Informação — TWYN

### 1. Objetivo

Este documento define o **escopo do Sistema de Gestão de Segurança da Informação (SGSI)** da TWYN em conformidade com ISO/IEC 27001:2022, estabelecendo claramente:
- Quais ativos, processos e sistemas estão **dentro** do escopo de certificação
- Quais estão **fora** do escopo e suas justificativas
- Limites físicos e lógicos do SGSI
- Interfaces com partes externas

### 2. Contexto Organizacional

#### 2.1 Sobre a TWYN
**Razão Social**: TWYN T4ISB DO BRASIL TECNOLOGIA E PARTICIPAÇÕES LTDA.  
**CNPJ**: 31.122.819/0001-55  
**Endereço Principal**: Avenida Paulista, nº 37, Bairro Bela Vista, São Paulo/SP  
**Setor**: Tecnologia — Plataforma de Autenticação Biométrica (Face ID)

**Modelo de Negócio**:
- Plataforma SaaS de autenticação biométrica via reconhecimento facial
- APIs REST hospedadas em AWS
- Clientes B2B (bancos, fintechs, empresas)
- Processamento de dados biométricos sensíveis

#### 2.2 Principais Partes Interessadas

| Parte Interessada | Interesse | Requisitos |
|-------------|----------|--------------|
| **Clientes B2B** | Conformidade regulatória (LGPD, GDPR) | Certificação ISO 27001, SOC 2 Type II, auditorias |
| **Usuários Finais** | Privacidade e proteção de dados biométricos | LGPD compliance, dados não compartilhados |
| **AWS** | Conformidade em cloud | FTR certification, CIS Benchmark |
| **Investidores** | Gestão de risco corporativo | Due diligence de segurança |
| **Reguladores** | LGPD, ANPD | Notificação de incidentes, DPO designado |

### 3. Definição do Escopo do SGSI

#### 3.1 Dentro do Escopo

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
- ✅ **Escritório TWYN**: Avenida Paulista, nº 37, Bairro Bela Vista, São Paulo/SP — workstations administrativas apenas

**Processos de Negócio**:
- ✅ Operação e Hospedagem (Hosting) da Plataforma SaaS
- ✅ Deployment e release management (Operacional)
- ✅ Incident response e gestão de incidentes
- ✅ Change management (mudanças na infraestrutura de produção)
- ✅ Onboarding/offboarding de colaboradores operacionais
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

#### 3.2 Fora do Escopo

**Sistemas Excluídos**:
- ❌ Ambientes de desenvolvimento local (laptops de devs)
- ❌ Ferramentas SaaS corporativas não críticas (Slack, Notion — gerenciados por fornecedores)
- ❌ Website marketing/institucional (WordPress ou similar)
- ❌ Sistemas financeiros/contábeis (se terceirizados)

**Processos Excluídos**:
- ❌ **Desenvolvimento de Software (SDLC)**: A engenharia e a escrita do código-fonte da API estão fora do escopo. O SGSI inicia-se na recepção do artefato para *deploy* (hospedagem e operação na AWS).
- ❌ RH (folha de pagamento, benefícios) — terceirizado
- ❌ Jurídico/contratual — exceto contratos de SI
- ❌ Vendas e marketing — exceto onde intersecta SI

**Justificativas para Exclusões**:
1. **Desenvolvimento de Software**: O foco do certificado é a operação, disponibilidade e segurança da infraestrutura da API (SaaS em nuvem), isolando o processo de engenharia de software da auditoria do SGSI.
2. **Ambientes dev locais**: Não processam dados reais de produção.
3. **SaaS terceiros**: Cobertos por avaliação de fornecedores.
4. **Website marketing**: Não processa dados sensíveis.

#### 3.3 Fronteiras Físicas e Lógicas

**Limite Físico**:
- Datacenters AWS em `us-east-1` e `us-west-2`
- Escritório TWYN em Avenida Paulista, nº 37, Bairro Bela Vista, São Paulo/SP — apenas workstations administrativas

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

### 4. Dependências e Interfaces

#### 4.1 Dependências Externas

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

### 5. Exclusões e Justificativas

Conforme ISO 27001:2022 Annex A, os seguintes controles são **excluídos** com justificativa:

| Controle | Justificativa | Aprovado Por |
|---------|---------------|-------------|
| A.7.1 Physical security perimeters | Infraestrutura 100% cloud (AWS); sem perímetro físico próprio. Covered by AWS SOC 2/ISO certifications. | Ricardo Esper (Bekaa Trusted Advisors) |
| A.7.2 Physical entry | Mesma justificativa acima | Ricardo Esper (Bekaa Trusted Advisors) |

*(Esta tabela será expandida no Statement of Applicability completo)*

### 6. Revisão e Manutenção

**Frequência de Revisão**: Anual ou quando:
- Mudanças significativas de arquitetura
- Novos serviços ou sistemas críticos
- Aquisições ou mudanças organizacionais
- Resultado de auditoria interna/externa
- Mudança de regulamentação aplicável

**Responsável pela Revisão**: Gestor SGSI + CTO

### 7. Aprovação

Este escopo foi revisado e aprovado pelos seguintes responsáveis:

| Função | Nome | Assinatura | Data |
|------|------|-----------|------|
| **CEO / Top Management** | Enes Fernando Degasperi | _______________ | ___/___/2026 |
| **Gestor SGSI** | Ricardo Esper (Bekaa Trusted Advisors) | _______________ | ___/___/2026 |
| **CTO** | Augusto Ferronato | _______________ | ___/___/2026 |

---

## Annex A: Histórico de Alterações do Escopo

| Versão | Data | Autor | Alterações |
|---------|------|--------|---------|
| 1.0 (Draft) | 08/06/2026 | Ricardo Esper (BEKAA) | Initial version for TWYN ISMS scope definition |

---

## Annex B: Documentos Relacionados

- [SGSI-POLICY-001] Information Security Policy
- [SGSI-RISK-001] Risk Assessment Methodology
- [SGSI-SOA-001] Statement of Applicability
- AWS BAA (Business Associate Agreement)
- Architectural diagrams (GitHub: t4isb-infra)

---

**RASCUNHO — PENDENTE DE APROVAÇÃO**
