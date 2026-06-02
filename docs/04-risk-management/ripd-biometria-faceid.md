---
document_id: SGSI-RIPD-001
title: Relatório de Impacto à Proteção de Dados Pessoais (RIPD) - Face ID Platform API
version: 1.0
date: 2026-06-02
classification: CONFIDENTIAL
owner: Gestor SGSI
approved_by: CEO (Pendente)
annex_a_controls: "A.5.33, A.8.28, A.8.11, A.8.10"
---

# Relatório de Impacto à Proteção de Dados Pessoais (RIPD)

## 1. Identificação do Controlador
**Razão Social:** TWYN T4ISB DO BRASIL TECNOLOGIA E PARTICIPAÇÕES LTDA.
**CNPJ:** 31.122.819/0001-55
**Endereço:** Avenida Paulista, nº 37, Bairro Bela Vista, São Paulo/SP
**Representante Legal (CEO):** Enes Fernando Degasperi (CPF nº 047.969.728-03)
**Gestor SGSI / DPO:** Ricardo Esper (Bekaa Trusted Advisors)

## 2. Descrição do Processo de Tratamento

### 2.1 Nome do Processo
Plataforma de Reconhecimento Facial (Face ID Platform API)

### 2.2 Natureza e Finalidade do Tratamento
O tratamento consiste na coleta, processamento, armazenamento e exclusão de dados biométricos faciais de titulares (usuários finais dos clientes da TWYN) para fins de autenticação e validação de identidade (prevenção à fraude) via API REST.
Os dados são fornecidos diretamente através da integração com o sistema dos clientes (operadores/controladores conjuntos).

### 2.3 Tipos de Dados Pessoais Tratados
- **Dados Sensíveis:** Biometria facial (vetores/embeddings faciais e imagens temporárias).
- **Dados Comuns:** Metadados de requisição, identificadores internos de transação, logs de auditoria.

**Base Legal (LGPD Art. 11):** 
- II, g) - Garantia da prevenção à fraude e à segurança do titular.
- I - Consentimento (coletado primariamente pelo cliente da TWYN).

### 2.4 Ciclo de Vida dos Dados
1. **Coleta:** Recebimento das imagens/vetores via API TLS 1.3.
2. **Processamento:** Extração de características e comparação nos containers K8s na AWS (EKS).
3. **Armazenamento:** Em banco de dados AWS RDS PostgreSQL e S3, criptografados at rest (AWS KMS Customer Managed Key: `alias/twyn-biometric-key`).
4. **Retenção e Descarte:** Os dados brutos (imagens) são descartados logo após a extração dos vetores, a menos que retenção temporária seja exigida para auditoria (máximo de 30 dias). Vetores biométricos são retidos pelo tempo do contrato ou solicitação de exclusão do titular.

## 3. Avaliação de Necessidade e Proporcionalidade
O tratamento de dados biométricos é estritamente necessário para garantir o nível de confiança na autenticação e mitigar riscos de fraudes de identidade, não existindo meio menos intrusivo que atinja a mesma eficácia (por exemplo, apenas senhas estariam suscetíveis a vazamentos e ataques de força bruta). 

## 4. Identificação e Avaliação de Riscos aos Titulares

| ID Risco | Descrição do Risco | Probabilidade | Impacto | Nível de Risco Inerente |
|---|---|---|---|---|
| R-001 | Vazamento de dados biométricos devido a ataque cibernético ao BD | Média | Muito Alto | Alto |
| R-002 | Acesso interno não autorizado a imagens/vetores biométricos | Baixa | Alto | Médio |
| R-003 | Interceptação de dados em trânsito | Baixa | Alto | Médio |
| R-004 | Retenção de dados além do período necessário | Média | Médio | Médio |

## 5. Medidas de Mitigação (Salvaguardas)

| ID Risco | Medidas Técnicas e Administrativas Implementadas/Planejadas | Nível de Risco Residual |
|---|---|---|
| R-001 | Criptografia At Rest via AWS KMS (AES-256); Banco isolado em subrede privada; Controle de acesso IAM/RBAC restrito (SOP-004). | Baixo |
| R-002 | MFA obrigatório para acesso AWS; Auditoria de logs (CloudTrail); Ninguém possui acesso ao root; Princípio do menor privilégio. | Baixo |
| R-003 | TLS 1.3 obrigatório para todas as APIs em trânsito; AWS Certificate Manager. | Baixo |
| R-004 | Scripts de sanitização automatizada de imagens e expiração de logs (Data Lifecycle Policies no S3 e RDS). | Baixo |

## 6. Parecer do DPO / Gestor SGSI
As medidas técnicas e organizacionais adotadas para a plataforma Face ID da TWYN encontram-se adequadas ao nível de criticidade dos dados tratados. Os riscos residuais são aceitáveis frente às salvaguardas (criptografia e isolamento) que reduzem significativamente o impacto potencial aos titulares em caso de incidentes. O presente RIPD deverá ser revisado anualmente ou sempre que houver mudança significativa na arquitetura do tratamento.

**Assinatura:** ___________________________ (Ricardo Esper)
**Data:** 26/05/2026

**Assinatura:** ___________________________ (Enes Fernando Degasperi)
**Data:** 26/05/2026
