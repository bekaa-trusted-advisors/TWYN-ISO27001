---
document_id: SGSI-POLICY-006
title: "Plano de Continuidade de Negócios (BCP)"
version: "1.0"
status: "Draft"
classification: "CONFIDENTIAL"
owner: "Gestor SGSI"
approved_by: "CEO (Pendente)"
effective_date: "[Pendente]"
next_review: "[Anual após aprovação]"
annex_a_controls: "A.5.29, A.5.30"
related_documents: "SGSI-POLICY-001, SGSI-DRP-001, SGSI-IRP-001, SGSI-RISK-002"
---

# Plano de Continuidade de Negócios (BCP)

## TWYN — Face ID Platform

---

## Sumário

1. [Propósito e Objetivos](#1-propósito-e-objetivos)
2. [Escopo](#2-escopo)
3. [Referências Normativas](#3-referências-normativas)
4. [Termos e Definições](#4-termos-e-definições)
5. [Análise de Impacto no Negócio (BIA)](#5-análise-de-impacto-no-negócio-bia)
6. [Cenários de Risco](#6-cenários-de-risco)
7. [Estratégias de Recuperação](#7-estratégias-de-recuperação)
8. [Equipe de Continuidade de Negócios](#8-equipe-de-continuidade-de-negócios)
9. [Critérios e Procedimentos de Ativação](#9-critérios-e-procedimentos-de-ativação)
10. [Plano de Comunicação](#10-plano-de-comunicação)
11. [Procedimentos de Recuperação por Cenário](#11-procedimentos-de-recuperação-por-cenário)
12. [Retorno à Operação Normal](#12-retorno-à-operação-normal)
13. [Programa de Testes do BCP](#13-programa-de-testes-do-bcp)
14. [Treinamento e Conscientização](#14-treinamento-e-conscientização)
15. [Manutenção e Revisão do Documento](#15-manutenção-e-revisão-do-documento)
16. [Considerações LGPD](#16-considerações-lgpd)
17. [Plano de Mitigação de SPOF](#17-plano-de-mitigação-de-spof)
18. [Indicadores de Desempenho (KPIs)](#18-indicadores-de-desempenho-kpis)
19. [Documentos Relacionados](#19-documentos-relacionados)
20. [Histórico de Revisões](#20-histórico-de-revisões)
21. [Aprovação](#21-aprovação)

---

## 1. Propósito e Objetivos

### 1.1 Propósito

Este Plano de Continuidade de Negócios (BCP) estabelece os procedimentos, responsabilidades e recursos necessários para garantir que a **TWYN** mantenha a capacidade de operar seus processos críticos de negócio durante e após eventos disruptivos, minimizando impactos financeiros, operacionais, legais e reputacionais.

Este documento atende aos requisitos da **ISO/IEC 27001:2022**, especificamente:

- **Cláusula A.5.29** — Segurança da informação durante disrupção
- **Cláusula A.5.30** — Prontidão de TIC para continuidade de negócios

### 1.2 Objetivos

Os objetivos deste plano são:

1. **Proteger vidas** — Prioridade absoluta em qualquer cenário de crise
2. **Manter operações críticas** — Garantir a continuidade da plataforma Face ID API dentro dos RTO/RPO definidos
3. **Proteger dados sensíveis** — Assegurar a integridade e confidencialidade dos dados biométricos (LGPD)
4. **Minimizar impacto financeiro** — Reduzir perdas de receita e custos de recuperação
5. **Preservar reputação** — Comunicação transparente e eficiente com stakeholders
6. **Atender requisitos regulatórios** — Conformidade com LGPD, contratos B2B e ISO 27001
7. **Garantir recuperação estruturada** — Retorno à operação normal de forma ordenada e documentada

### 1.3 Metas Quantitativas

| Meta | Valor Alvo |
|------|-----------|
| Recovery Time Objective (RTO) | < 4 horas |
| Recovery Point Objective (RPO) | < 15 minutos |
| Disponibilidade do serviço (SLA) | ≥ 99,5% uptime |
| Tempo máximo de notificação interna | ≤ 30 minutos após detecção |
| Tempo máximo de notificação a clientes | ≤ 2 horas após confirmação de impacto |
| Frequência de testes BCP | Mínimo 2x/ano |

---

## 2. Escopo

### 2.1 Abrangência

Este plano aplica-se a:

- ✅ **Plataforma Face ID API** — Sistema principal de geração de receita (produção em AWS us-east-1)
- ✅ **Infraestrutura AWS** — EKS, RDS Multi-AZ, S3, CloudFront, Route 53, IAM
- ✅ **Infraestrutura DR** — AWS us-west-2 (S3 Cross-Region Replication, RDS read replica potencial)
- ✅ **Dados biométricos** — Templates faciais classificados como RESTRICTED (LGPD Art. 11)
- ✅ **Sistemas de suporte** — GitHub, CI/CD pipelines, ferramentas de monitoramento
- ✅ **Recursos humanos** — Todos os ~10 colaboradores da TWYN
- ✅ **Fornecedores críticos** — AWS, GitHub, ferramentas de terceiros
- ✅ **Processos organizacionais** — Faturamento, suporte a clientes, desenvolvimento

### 2.2 Exclusões

- ❌ Segurança física de escritórios (coberto por política separada)
- ❌ Continuidade de negócios de fornecedores (coberto por SLAs e avaliações de fornecedores — SGSI-SUPP-001)

### 2.3 Premissas

- A infraestrutura AWS está operacional em pelo menos uma região (us-east-1 ou us-west-2)
- Os backups estão atualizados e acessíveis conforme política de backup
- A equipe de continuidade está treinada e com acesso aos runbooks
- Canais de comunicação de emergência (telefone, e-mail secundário) estão disponíveis

---

## 3. Referências Normativas

| Documento | Descrição |
|-----------|-----------|
| ISO/IEC 27001:2022 | Sistemas de gestão de segurança da informação |
| ISO/IEC 27002:2022 | Controles de segurança da informação |
| ISO 22301:2019 | Sistemas de gestão de continuidade de negócios |
| ISO 22317:2015 | Análise de impacto no negócio (BIA) |
| LGPD (Lei 13.709/2018) | Lei Geral de Proteção de Dados |
| SGSI-POLICY-001 | Política de Segurança da Informação da TWYN |
| SGSI-IRP-001 | Política de Resposta a Incidentes |
| SGSI-DRP-001 | Plano de Recuperação de Desastres |
| SGSI-RISK-002 | Registro de Riscos |

---

## 4. Termos e Definições

| Termo | Definição |
|-------|-----------|
| **BCP** | Business Continuity Plan — Plano de Continuidade de Negócios |
| **BIA** | Business Impact Analysis — Análise de Impacto no Negócio |
| **RTO** | Recovery Time Objective — Tempo máximo aceitável para restaurar um processo/serviço |
| **RPO** | Recovery Point Objective — Perda máxima aceitável de dados (em tempo) |
| **MTD** | Maximum Tolerable Downtime — Tempo máximo tolerável de indisponibilidade total |
| **MBCO** | Minimum Business Continuity Objective — Nível mínimo aceitável de serviço durante crise |
| **SPOF** | Single Point of Failure — Ponto único de falha |
| **DR** | Disaster Recovery — Recuperação de Desastres |
| **CRR** | Cross-Region Replication — Replicação entre regiões AWS |
| **EKS** | Elastic Kubernetes Service — Serviço gerenciado de Kubernetes da AWS |
| **RDS** | Relational Database Service — Serviço de banco de dados relacional da AWS |
| **ANPD** | Autoridade Nacional de Proteção de Dados |

---

## 5. Análise de Impacto no Negócio (BIA)

### 5.1 Processos Críticos de Negócio

Os processos de negócio da TWYN foram identificados, priorizados e classificados conforme sua criticidade:

| # | Processo | Prioridade | Descrição | Proprietário |
|---|----------|-----------|-----------|-------------|
| 1 | **Face ID API — Produção** | P0 — Crítico | API principal de verificação facial. Gera receita direta. | DevOps Lead |
| 2 | **Banco de Dados Biométrico (RDS)** | P0 — Crítico | Armazena templates biométricos e dados de transações. | DevOps Lead |
| 3 | **Armazenamento de Imagens (S3)** | P0 — Crítico | Imagens faciais para processamento. Dados RESTRICTED (LGPD). | DevOps Lead |
| 4 | **Pipeline CI/CD** | P1 — Alto | GitHub Actions + deploy para EKS. Necessário para hotfixes. | DevOps Lead |
| 5 | **Monitoramento e Alertas** | P1 — Alto | CloudWatch, GuardDuty, alertas operacionais. | Junior DevOps |
| 6 | **Suporte ao Cliente** | P2 — Médio | Atendimento a clientes B2B, resolução de problemas. | CEO |
| 7 | **Faturamento e Financeiro** | P2 — Médio | Emissão de faturas, controle financeiro. | CEO |
| 8 | **Desenvolvimento (Dev)** | P3 — Baixo | Desenvolvimento de novas features e correções não urgentes. | Desenvolvedores |
| 9 | **Administração Interna** | P3 — Baixo | E-mail corporativo, comunicação interna, RH. | CEO |

### 5.2 RTO, RPO e MTD por Processo

| Processo | RTO | RPO | MTD | MBCO |
|----------|-----|-----|-----|------|
| Face ID API — Produção | < 4h | < 15min | 8h | 50% da capacidade normal |
| Banco de Dados Biométrico (RDS) | < 4h | < 15min | 8h | Somente leitura aceitável |
| Armazenamento de Imagens (S3) | < 4h | < 1h | 12h | Acesso somente leitura |
| Pipeline CI/CD | < 8h | < 1h | 24h | Deploy manual aceitável |
| Monitoramento e Alertas | < 2h | < 30min | 4h | Alertas críticos mínimos |
| Suporte ao Cliente | < 4h | N/A | 24h | E-mail funcional |
| Faturamento e Financeiro | < 24h | < 24h | 72h | Emissão manual aceitável |
| Desenvolvimento (Dev) | < 24h | < 4h | 1 semana | N/A |
| Administração Interna | < 24h | N/A | 1 semana | E-mail funcional |

### 5.3 Análise de Impacto por Período de Indisponibilidade

#### 5.3.1 Face ID API — Produção (P0)

| Período | Impacto Financeiro | Impacto Reputacional | Impacto Legal | Impacto Operacional |
|---------|--------------------|---------------------|---------------|---------------------|
| **1 hora** | Baixo — Perda marginal de receita transacional | Baixo — Dentro do SLA tolerável | Nenhum | Baixo — Clientes utilizam cache/retry |
| **4 horas** | Médio — Perda significativa de receita; possível violação de SLA 99,5% | Médio — Clientes reportam falhas; impacto na confiança | Baixo — Possível notificação contratual necessária | Médio — Operações de clientes degradadas |
| **24 horas** | Alto — Perda substancial de receita; penalidades de SLA | Alto — Clientes buscam alternativas; mídia pode notar | Médio — Notificação formal obrigatória a clientes | Alto — Clientes sem serviço de verificação facial |
| **72 horas** | Crítico — Risco de churn de clientes; impacto no fluxo de caixa | Crítico — Dano duradouro à marca; perda de confiança do mercado | Alto — Possível ação judicial de clientes; ANPD pode questionar | Crítico — Clientes ativam planos de contingência próprios |
| **1 semana** | Catastrófico — Viabilidade do negócio em risco | Catastrófico — Reputação irrecuperável a curto prazo | Crítico — Litígios múltiplos; investigação regulatória | Catastrófico — Perda de clientes permanente |

#### 5.3.2 Banco de Dados Biométrico — RDS (P0)

| Período | Impacto Financeiro | Impacto Reputacional | Impacto Legal | Impacto Operacional |
|---------|--------------------|---------------------|---------------|---------------------|
| **1 hora** | Baixo | Baixo | Nenhum | Médio — API degradada |
| **4 horas** | Médio | Médio | Baixo | Alto — API indisponível |
| **24 horas** | Alto | Alto | Médio — Risco LGPD se dados perdidos | Crítico |
| **72 horas** | Crítico | Crítico | Alto — Notificação ANPD obrigatória | Catastrófico |
| **1 semana** | Catastrófico | Catastrófico | Crítico — Sanções LGPD | Catastrófico |

#### 5.3.3 Armazenamento de Imagens — S3 (P0)

| Período | Impacto Financeiro | Impacto Reputacional | Impacto Legal | Impacto Operacional |
|---------|--------------------|---------------------|---------------|---------------------|
| **1 hora** | Baixo | Baixo | Nenhum | Baixo — Processamento em fila |
| **4 horas** | Médio | Baixo | Nenhum | Médio — Fila de processamento crescente |
| **24 horas** | Médio | Médio | Baixo | Alto — Novos cadastros impossíveis |
| **72 horas** | Alto | Alto | Médio | Crítico |
| **1 semana** | Crítico | Crítico | Alto | Catastrófico |

### 5.4 Mapeamento de Dependências

```
┌─────────────────────────────────────────────────────────────────────┐
│                    FACE ID API (Produção)                          │
│                     EKS — us-east-1                                │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────────────────┐  │
│  │ RDS      │  │ S3       │  │ Route 53 │  │ CloudFront / ALB   │  │
│  │ Multi-AZ │  │ Buckets  │  │ DNS      │  │ Load Balancer      │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────────┬───────────┘  │
│       │              │             │                  │              │
│  ┌────▼─────┐  ┌────▼─────┐  ┌────▼─────┐  ┌───────▼──────────┐  │
│  │ KMS      │  │ S3 CRR   │  │ ACM      │  │ WAF              │  │
│  │ Keys     │  │ us-west-2│  │ Certs    │  │ Rules            │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────────┘  │
│                                                                     │
├─────────────────── DEPENDÊNCIAS EXTERNAS ───────────────────────────┤
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │ GitHub   │  │ Docker   │  │ AWS IAM  │  │ CloudWatch /     │  │
│  │ Actions  │  │ Registry │  │ STS      │  │ GuardDuty        │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────────┘  │
│                                                                     │
├───────────────── DEPENDÊNCIAS HUMANAS ──────────────────────────────┤
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────────┐  │
│  │ DevOps   │  │ Junior   │  │ CEO      │  │ Gestor SGSI      │  │
│  │ Lead     │  │ DevOps   │  │          │  │ (Bekaa/Esper)    │  │
│  │ ⚠️ SPOF  │  │ Backup   │  │ Decisor  │  │ Coordenador BCP  │  │
│  └──────────┘  └──────────┘  └──────────┘  └──────────────────┘  │
└─────────────────────────────────────────────────────────────────────┘
```

### 5.5 Matriz de Dependências Críticas

| Componente | Depende de | Impacto se Indisponível | Alternativa |
|------------|-----------|------------------------|-------------|
| Face ID API (EKS) | RDS, S3, Route 53, ALB, KMS | API completamente indisponível | Failover para us-west-2 |
| RDS PostgreSQL | KMS, EBS, rede VPC | Perda de dados transacionais | Multi-AZ failover automático; DR: read replica us-west-2 |
| S3 Buckets | KMS, IAM | Impossível processar novas imagens | S3 CRR para us-west-2 |
| GitHub Actions | GitHub.com, secrets, runners | Impossível fazer deploys | Deploy manual via kubectl + scripts locais |
| Route 53 | AWS global service | Resolução DNS falha | DNS secundário (improvável — SLA 100% AWS) |
| DevOps Lead | Pessoa única | Incapacidade de operar infra crítica | Junior DevOps + runbooks + consultor externo |
| Gestor SGSI | Pessoa única (externo) | Sem coordenação SGSI/BCP | CEO assume temporariamente |
| AWS Account | AWS global | Tudo indisponível | N/A — dependência total |
| KMS Keys | AWS KMS | Dados criptografados inacessíveis | Cross-region key replication |

---

## 6. Cenários de Risco

### 6.1 Visão Geral dos Cenários

| ID | Cenário | Probabilidade | Impacto | Risco | Prioridade |
|----|---------|--------------|---------|-------|-----------|
| CEN-01 | Falha da região AWS us-east-1 | Baixa | Crítico | Alto | P0 |
| CEN-02 | Ransomware / Ataque cibernético | Média | Crítico | Crítico | P0 |
| CEN-03 | Indisponibilidade de pessoa-chave (DevOps Lead SPOF) | Média | Alto | Alto | P1 |
| CEN-04 | Violação de dados / Comprometimento de dados biométricos | Baixa | Crítico | Alto | P0 |
| CEN-05 | Falha de cadeia de suprimentos (GitHub, AWS service degradation) | Média | Médio | Médio | P1 |
| CEN-06 | Falha de banco de dados (corrupção RDS) | Baixa | Crítico | Alto | P0 |
| CEN-07 | Ataque DDoS na API | Média | Médio | Médio | P1 |

### 6.2 Detalhamento dos Cenários

#### CEN-01: Falha da Região AWS us-east-1

- **Descrição**: A região primária da AWS (us-east-1 — N. Virginia) sofre indisponibilidade total ou parcial prolongada (>1 hora).
- **Causa raiz potencial**: Desastre natural, falha de infraestrutura AWS, ataque em larga escala.
- **Ativos afetados**: EKS, RDS, S3, ALB, CloudWatch, CloudTrail, GuardDuty, KMS.
- **Impacto imediato**: Face ID API completamente indisponível. Sem processamento de verificações faciais.
- **Indicadores de detecção**: Alertas CloudWatch (multi-região), AWS Health Dashboard, status.aws.amazon.com, alertas Slack.
- **RTO**: < 4 horas | **RPO**: < 15 minutos

#### CEN-02: Ransomware / Ataque Cibernético

- **Descrição**: Comprometimento de sistemas por ransomware, malware ou ataque direcionado que cifra ou destrói dados e sistemas.
- **Causa raiz potencial**: Phishing, credencial comprometida, vulnerabilidade zero-day, supply chain attack.
- **Ativos afetados**: Potencialmente todos — EKS workloads, RDS, S3, secrets, código-fonte.
- **Impacto imediato**: Serviços degradados ou indisponíveis. Possível perda ou exposição de dados biométricos.
- **Indicadores de detecção**: GuardDuty findings, alertas de acesso anômalo, monitoramento de integridade, alertas AV/EDR.
- **RTO**: < 12 horas (reconstrução) | **RPO**: < 15 minutos (backups não comprometidos)

#### CEN-03: Indisponibilidade de Pessoa-Chave (DevOps Lead — SPOF)

- **Descrição**: O DevOps Lead, único administrador da infraestrutura AWS e Kubernetes, fica indisponível por período prolongado (doença, acidente, desligamento).
- **Causa raiz potencial**: Emergência pessoal, saúde, saída voluntária/involuntária.
- **Ativos afetados**: Capacidade de operar, manter e recuperar toda a infraestrutura de produção.
- **Impacto imediato**: Incapacidade de realizar deploys de emergência, troubleshooting avançado, operações de DR.
- **Indicadores de detecção**: Ausência não comunicada >24h, impossibilidade de contato por múltiplos canais.
- **RTO**: Variável (depende da severidade do incidente concorrente) | **RPO**: N/A

#### CEN-04: Violação de Dados / Comprometimento de Dados Biométricos

- **Descrição**: Acesso não autorizado, exfiltração ou exposição de dados biométricos faciais (classificação RESTRICTED).
- **Causa raiz potencial**: Exploração de vulnerabilidade, insider threat, misconfiguration de S3/RDS, API key comprometida.
- **Ativos afetados**: Dados biométricos (templates faciais), PII de usuários, credenciais de acesso.
- **Impacto imediato**: Obrigação legal de notificação ANPD (≤72h). Possível suspensão de processamento pela ANPD. Dano reputacional severo.
- **Indicadores de detecção**: GuardDuty findings (data exfiltration), CloudTrail anomalias, alertas de volume de dados anormal.
- **RTO**: < 4 horas (contenção) | **RPO**: N/A (foco em contenção, não perda)

#### CEN-05: Falha de Cadeia de Suprimentos (GitHub, AWS Service Degradation)

- **Descrição**: Serviços críticos de terceiros (GitHub, serviços específicos da AWS como EKS control plane, ECR) ficam degradados ou indisponíveis.
- **Causa raiz potencial**: Incidente no fornecedor, ataque a fornecedor, mudança de política.
- **Ativos afetados**: CI/CD pipelines (GitHub Actions), container registry (ECR), Kubernetes control plane (EKS).
- **Impacto imediato**: Impossibilidade de realizar deploys. Em caso de EKS control plane: workloads continuam rodando, mas sem gerenciamento.
- **Indicadores de detecção**: GitHub Status, AWS Health Dashboard, falhas de pipeline, timeout de API calls.
- **RTO**: < 8 horas | **RPO**: N/A (dados não afetados)

#### CEN-06: Falha de Banco de Dados (Corrupção RDS)

- **Descrição**: Corrupção de dados no RDS PostgreSQL ou falha que afete ambas as AZs do Multi-AZ.
- **Causa raiz potencial**: Bug de software, falha de hardware em múltiplas AZs, migração falha, erro humano.
- **Ativos afetados**: Banco de dados de produção, dados transacionais, templates biométricos.
- **Impacto imediato**: API retorna erros, perda potencial de transações recentes.
- **Indicadores de detecção**: CloudWatch RDS metrics, alertas de erro na aplicação, health checks falhando.
- **RTO**: < 4 horas | **RPO**: < 15 minutos (Point-in-Time Recovery)

#### CEN-07: Ataque DDoS na API

- **Descrição**: Ataque distribuído de negação de serviço visando a Face ID API.
- **Causa raiz potencial**: Atacante externo, concorrente, ativismo.
- **Ativos afetados**: ALB, EKS pods, Route 53.
- **Impacto imediato**: Degradação de performance ou indisponibilidade da API para clientes legítimos.
- **Indicadores de detecção**: AWS Shield, WAF metrics, picos anormais de tráfego, aumento de latência.
- **RTO**: < 1 hora (mitigação) | **RPO**: N/A

---

## 7. Estratégias de Recuperação

### 7.1 Estratégias Técnicas

| Cenário | Estratégia Primária | Estratégia Secundária | Infraestrutura Necessária |
|---------|--------------------|-----------------------|--------------------------|
| CEN-01 (Região AWS) | Failover cross-region para us-west-2 | Modo degradado com dados em cache | EKS em us-west-2, RDS read replica promotion, S3 CRR |
| CEN-02 (Ransomware) | Isolamento + rebuild a partir de backups limpos | Rollback para snapshot anterior ao comprometimento | Backups off-region, snapshots RDS, S3 versioning |
| CEN-03 (SPOF) | Runbooks documentados + Junior DevOps opera | Consultor externo de emergência | Knowledge base, credenciais break-glass, runbooks |
| CEN-04 (Data breach) | Contenção imediata + rotação de credenciais | Isolamento de rede + forensics | GuardDuty, CloudTrail, IAM emergency policies |
| CEN-05 (Supply chain) | Deploy manual via scripts locais + kubectl | Freeze de mudanças até restauração do serviço | Scripts de deploy locais, kubeconfig backup |
| CEN-06 (RDS corrupção) | Point-in-Time Recovery (PITR) | Restore de snapshot manual + promoção de read replica | Snapshots automáticos, transaction logs |
| CEN-07 (DDoS) | AWS Shield + WAF rate limiting | Ativação de Shield Advanced + support AWS | AWS Shield, WAF, Route 53 health checks |

### 7.2 Estratégias Organizacionais

#### 7.2.1 Planejamento de Sucessão

| Papel | Titular | Backup Primário | Backup Secundário | Conhecimento Documentado |
|-------|---------|-----------------|--------------------|-----------------------|
| DevOps Lead (Infra Admin) | [Nome DevOps Lead] | Junior DevOps | Consultor externo (contrato de emergência) | Runbooks em `docs/06-implementation-guides/` |
| CEO (Decisor) | [Nome CEO] | Gestor SGSI (Bekaa/Ricardo Esper) | DevOps Lead (decisões técnicas) | Procedimentos documentados neste BCP |
| Gestor SGSI (Coordenador BCP) | Ricardo Esper (Bekaa) | CEO | DevOps Lead | Este documento + SGSI docs |
| Desenvolvimento | Desenvolvedores | DevOps Lead | Contratação emergencial | README + docs técnicos |

#### 7.2.2 Cross-Training (Treinamento Cruzado)

O programa de cross-training visa eliminar SPOFs críticos. Detalhes na [Seção 17](#17-plano-de-mitigação-de-spof).

#### 7.2.3 Knowledge Base

Toda documentação operacional crítica deve estar acessível em:

- **Repositório Git**: `docs/06-implementation-guides/` — runbooks e guias de implementação
- **Secrets em emergência**: AWS Systems Manager Parameter Store + break-glass procedure
- **Contatos de emergência**: Seção 8.3 deste documento (cópia física no escritório)

### 7.3 Estratégias de Comunicação

Detalhadas na [Seção 10 — Plano de Comunicação](#10-plano-de-comunicação).

---

## 8. Equipe de Continuidade de Negócios

### 8.1 Composição da Equipe

| Papel | Responsável | Responsabilidades |
|-------|------------|-------------------|
| **Coordenador BCP** | Gestor SGSI (Bekaa / Ricardo Esper) | Ativar BCP, coordenar resposta, garantir comunicação, conduzir post-mortem |
| **Líder Técnico** | DevOps Lead | Executar procedimentos técnicos de recuperação, operar infraestrutura, escalar problemas |
| **Líder de Comunicação** | CEO | Comunicação externa (clientes, reguladores, mídia), decisões de negócio, autorização de gastos |
| **Backup Operacional** | Junior DevOps | Auxiliar operações técnicas, executar runbooks, operar sistemas auxiliares |
| **Backup Coordenação** | CEO | Assumir coordenação BCP se Gestor SGSI indisponível |
| **Suporte Jurídico** | Assessoria jurídica externa (a designar) | Orientação sobre LGPD, notificações regulatórias, contratos |

### 8.2 Matriz de Escalação

```
Nível 1 (Operacional)         Nível 2 (Tático)           Nível 3 (Estratégico)
┌─────────────────────┐    ┌──────────────────────┐    ┌────────────────────────┐
│ Junior DevOps       │───▶│ DevOps Lead          │───▶│ CEO                    │
│ Detecta e inicia    │    │ Avalia e executa      │    │ Decide ativação BCP    │
│ troubleshooting     │    │ recovery procedures   │    │ Autoriza comunicação   │
│                     │    │                       │    │ Autoriza gastos        │
└─────────────────────┘    │ Escala se:            │    │                        │
                           │ - Impacto >30min      │    │ Gestor SGSI coordena   │
                           │ - Múltiplos sistemas  │    │ a resposta             │
                           │ - Dados comprometidos │    │                        │
                           └──────────────────────┘    └────────────────────────┘
```

| Condição de Escalação | De | Para | Tempo Máximo |
|-----------------------|-----|------|-------------|
| Incidente detectado (qualquer severidade) | Sistema / Operador | Junior DevOps / DevOps Lead | Automático / Imediato |
| Indisponibilidade de serviço P0 > 15min | Junior DevOps | DevOps Lead | 15 minutos |
| Indisponibilidade P0 > 30min OU dados comprometidos | DevOps Lead | CEO + Gestor SGSI | 30 minutos |
| Decisão de ativar BCP | DevOps Lead / Gestor SGSI | CEO (autorização) | 15 minutos |
| Incidente com impacto LGPD (dados pessoais) | Qualquer membro | CEO + Gestor SGSI + Jurídico | Imediato |
| Necessidade de comunicação externa a clientes | Gestor SGSI | CEO (aprovação) | 30 minutos |
| Necessidade de recursos financeiros extraordinários | Qualquer membro | CEO | Conforme necessário |

### 8.3 Informações de Contato de Emergência

> **⚠️ CLASSIFICAÇÃO: CONFIDENCIAL — Preencher com dados reais antes da aprovação.**

| Papel | Nome | Telefone Primário | Telefone Secundário | E-mail Primário | E-mail Secundário |
|-------|------|-------------------|---------------------|-----------------|-------------------|
| CEO | [Nome Completo] | [+55 XX XXXXX-XXXX] | [+55 XX XXXXX-XXXX] | [email@twyn.com.br] | [email pessoal] |
| Gestor SGSI | Ricardo Esper (Bekaa) | [+55 XX XXXXX-XXXX] | [+55 XX XXXXX-XXXX] | [ricardo@bekaa.com.br] | [email secundário] |
| DevOps Lead | [Nome Completo] | [+55 XX XXXXX-XXXX] | [+55 XX XXXXX-XXXX] | [email@twyn.com.br] | [email pessoal] |
| Junior DevOps | [Nome Completo] | [+55 XX XXXXX-XXXX] | [+55 XX XXXXX-XXXX] | [email@twyn.com.br] | [email pessoal] |
| Assessoria Jurídica | [Nome / Escritório] | [+55 XX XXXXX-XXXX] | — | [email@escritório] | — |
| AWS Support | AWS Business Support | Via Console AWS | — | — | — |
| Consultor Externo (Emergência) | [A designar] | [+55 XX XXXXX-XXXX] | — | [email] | — |

### 8.4 Autoridade de Decisão

| Decisão | Autorizado | Backup |
|---------|-----------|--------|
| Ativar BCP | CEO | Gestor SGSI (se CEO indisponível >30min) |
| Executar failover cross-region | DevOps Lead | Junior DevOps (com aprovação CEO) |
| Comunicar clientes sobre incidente | CEO | Gestor SGSI (com template pré-aprovado) |
| Notificar ANPD (data breach) | CEO + Assessoria Jurídica | Gestor SGSI (em extrema urgência) |
| Autorizar gastos emergenciais > R$ 5.000 | CEO | — |
| Declarar retorno à normalidade | CEO + Gestor SGSI + DevOps Lead | — |
| Comunicar mídia | CEO (único porta-voz autorizado) | — |

---

## 9. Critérios e Procedimentos de Ativação

### 9.1 Níveis de Severidade

| Nível | Nome | Descrição | Ação | Quem Decide |
|-------|------|-----------|------|------------|
| **SEV-1** | Observação | Degradação menor detectada. SLA não afetado. | Monitorar. Investigar. Não ativa BCP. | DevOps Lead |
| **SEV-2** | Alerta | Degradação significativa. SLA em risco (<99,5%). Serviço parcialmente afetado. | Acionar equipe técnica. Preparar ativação BCP. Informar Gestor SGSI. | DevOps Lead |
| **SEV-3** | Crise | Indisponibilidade total de processo P0 >30min OU dados comprometidos. SLA violado. | **Ativar BCP**. Acionar equipe completa. Iniciar comunicação. | CEO (mediante recomendação DevOps Lead ou Gestor SGSI) |
| **SEV-4** | Catástrofe | Múltiplos processos P0 indisponíveis >1h OU perda confirmada de dados biométricos OU região AWS indisponível. | **Ativar BCP nível máximo**. Toda equipe mobilizada. DR ativado. Comunicação imediata a clientes e reguladores. | CEO |

### 9.2 Critérios de Ativação Automática

O BCP é **automaticamente ativado** (sem necessidade de aprovação prévia) quando:

1. ✅ Indisponibilidade total da Face ID API por mais de **30 minutos** sem previsão de resolução
2. ✅ Confirmação de **data breach** envolvendo dados biométricos ou PII
3. ✅ Falha da **região primária AWS us-east-1** confirmada pelo AWS Health Dashboard
4. ✅ **Ransomware** confirmado em qualquer sistema de produção
5. ✅ DevOps Lead indisponível E incidente técnico P0 simultâneo

### 9.3 Procedimento de Ativação

```
PASSO 1 — DETECÇÃO E AVALIAÇÃO (0-15min)
├── Incidente detectado (automático ou manual)
├── DevOps Lead / Junior DevOps avalia impacto
├── Classifica severidade (SEV-1 a SEV-4)
└── Se SEV-3 ou SEV-4: prosseguir para Passo 2

PASSO 2 — NOTIFICAÇÃO E AUTORIZAÇÃO (15-30min)
├── DevOps Lead notifica Gestor SGSI e CEO
├── Breve avaliação da situação (5min call)
├── CEO autoriza ativação do BCP
│   (ou ativação automática se critérios da seção 9.2 atendidos)
└── Gestor SGSI registra ativação no log de incidentes

PASSO 3 — MOBILIZAÇÃO DA EQUIPE (30-45min)
├── Gestor SGSI aciona equipe de continuidade
├── Convoca reunião de crise (presencial ou remota)
├── Distribui responsabilidades conforme cenário
└── Inicia procedimento de recuperação específico (Seção 11)

PASSO 4 — COMUNICAÇÃO INICIAL (45-60min)
├── CEO aprova mensagem para clientes (template Seção 10.5)
├── Gestor SGSI envia notificação interna
├── Se data breach: jurídico avalia obrigação ANPD
└── Status page atualizado (se disponível)
```

### 9.4 Cadeia de Notificação

```
┌──────────────────────┐
│ Detecção do Incidente│
└──────────┬───────────┘
           │ Imediato
           ▼
┌──────────────────────┐
│ DevOps Lead avalia   │──── Se indisponível ───▶ Junior DevOps avalia
└──────────┬───────────┘
           │ ≤15min
           ▼
┌──────────────────────┐    ┌──────────────────────┐
│ CEO (decisor)        │◀───│ Gestor SGSI          │
│                      │    │ (coordenador)         │
└──────────┬───────────┘    └──────────┬───────────┘
           │ ≤30min                    │
           ▼                           ▼
┌──────────────────────┐    ┌──────────────────────┐
│ Equipe técnica       │    │ Equipe completa      │
│ (Junior DevOps,      │    │ mobilizada           │
│  Desenvolvedores)    │    │                      │
└──────────────────────┘    └──────────────────────┘
           │ ≤2h
           ▼
┌──────────────────────┐
│ Clientes afetados    │
│ (CEO comunica)       │
└──────────────────────┘
```

---

## 10. Plano de Comunicação

### 10.1 Princípios de Comunicação em Crise

1. **Transparência** — Comunicar fatos conhecidos, não especulações
2. **Tempestividade** — Comunicar rapidamente, mesmo que informações sejam parciais
3. **Consistência** — Uma única voz oficial (CEO para comunicação externa)
4. **Registro** — Toda comunicação deve ser documentada e timestamped
5. **Conformidade** — Respeitar requisitos legais de notificação (LGPD, contratos)

### 10.2 Comunicação Interna

| Público | Canal | Responsável | Timing | Conteúdo |
|---------|-------|------------|--------|----------|
| Equipe BCP | Slack #incidents + telefone | Gestor SGSI | Imediato (≤15min) | Natureza do incidente, severidade, ações em andamento |
| Todos colaboradores TWYN | E-mail corporativo + Slack #geral | CEO | ≤1 hora | Resumo do incidente, impacto, orientações |
| Atualizações durante crise | Slack #incidents | Gestor SGSI | A cada 30min | Status atualizado, ETR (Estimated Time to Recover) |
| Post-incidente | E-mail + reunião | Gestor SGSI | ≤48h após resolução | Post-mortem, lições aprendidas, ações corretivas |

### 10.3 Comunicação Externa

| Público | Canal | Responsável | Timing | Conteúdo |
|---------|-------|------------|--------|----------|
| Clientes B2B afetados | E-mail direto + status page | CEO | ≤2h após confirmação de impacto | Impacto no serviço, ações de recuperação, ETR |
| ANPD (se data breach) | Formulário oficial ANPD | CEO + Jurídico | ≤72h (LGPD Art. 48) | Natureza dos dados, titulares afetados, medidas adotadas |
| Titulares de dados (se data breach) | E-mail individual | CEO + DPO | Prazo razoável (LGPD Art. 48 §1) | Dados afetados, riscos, medidas de proteção recomendadas |
| AWS Support | Console AWS + telefone | DevOps Lead | Imediato (se incidente AWS) | Ticket de suporte com detalhes técnicos |
| Mídia | Comunicado oficial (se necessário) | CEO (único porta-voz) | Quando necessário | Nota oficial pré-aprovada por jurídico |
| Parceiros / Fornecedores | E-mail | CEO / Gestor SGSI | Conforme necessário | Informações relevantes ao parceiro |

### 10.4 Regras de Comunicação com Mídia

- **SOMENTE o CEO** está autorizado a falar com a imprensa
- Nenhum outro colaborador pode emitir declarações públicas sobre incidentes
- Toda comunicação com mídia deve ser previamente revisada pela assessoria jurídica
- Em caso de dúvida, responder: *"Estamos investigando a situação e forneceremos uma atualização em breve."*
- Não especular sobre causas, responsáveis ou extensão do impacto

### 10.5 Templates de Comunicação

#### Template 1 — Notificação Interna (Ativação BCP)

```
ASSUNTO: [URGENTE] Ativação do Plano de Continuidade de Negócios — TWYN

Equipe,

Informamos que o Plano de Continuidade de Negócios (BCP) foi ativado às
[HH:MM] de [DD/MM/AAAA] devido a [descrição breve do incidente].

SITUAÇÃO ATUAL:
- Severidade: [SEV-3 / SEV-4]
- Serviços afetados: [lista de serviços]
- Impacto estimado: [descrição do impacto]

EQUIPE DE CRISE ATIVADA:
- Coordenador BCP: [Nome] (Gestor SGSI)
- Líder Técnico: [Nome] (DevOps Lead)
- Decisor: [Nome] (CEO)

ORIENTAÇÕES:
1. Não realizar deploys ou alterações em produção sem autorização
2. Manter-se disponível para contato via [canal]
3. Direcionar qualquer dúvida para [canal #incidents]
4. NÃO comunicar externamente sobre o incidente

Próxima atualização será enviada em [30/60 minutos].

[Nome] — Gestor SGSI
```

#### Template 2 — Notificação a Clientes (Incidente de Serviço)

```
ASSUNTO: [TWYN] Notificação de Incidente — Serviço Face ID API

Prezado(a) Cliente,

Gostaríamos de informá-lo(a) que identificamos uma interrupção no serviço
Face ID API às [HH:MM] (horário de Brasília) em [DD/MM/AAAA].

IMPACTO:
- Serviço(s) afetado(s): [API de verificação facial / Todos os endpoints]
- Início da interrupção: [HH:MM] [DD/MM/AAAA]
- Status atual: [Em investigação / Em recuperação / Parcialmente restaurado]

AÇÕES EM ANDAMENTO:
Nossa equipe técnica está trabalhando para restaurar os serviços o mais
rapidamente possível. [Detalhes das ações, sem revelar informações sensíveis
de segurança].

PREVISÃO DE RESTAURAÇÃO:
Estimamos a restauração completa para [HH:MM] [DD/MM/AAAA].

Enviaremos uma nova atualização em [1 hora / 2 horas / quando houver mudança
significativa].

Lamentamos qualquer inconveniente causado e agradecemos sua compreensão.

Atenciosamente,
[Nome do CEO]
CEO — TWYN
[email de contato]
```

#### Template 3 — Notificação à ANPD (Violação de Dados Pessoais)

```
COMUNICAÇÃO DE INCIDENTE DE SEGURANÇA — LGPD Art. 48

1. IDENTIFICAÇÃO DO CONTROLADOR
   - Razão Social: TWYN [Razão Social Completa]
   - CNPJ: [XX.XXX.XXX/XXXX-XX]
   - Encarregado (DPO): [Nome] — [email] — [telefone]

2. DESCRIÇÃO DO INCIDENTE
   - Data/hora de identificação: [DD/MM/AAAA às HH:MM]
   - Data/hora estimada da ocorrência: [DD/MM/AAAA às HH:MM]
   - Natureza do incidente: [Acesso não autorizado / Exfiltração / etc.]
   - Descrição: [Descrição detalhada do ocorrido]

3. DADOS PESSOAIS AFETADOS
   - Tipos de dados: [Dados biométricos (templates faciais), nome, CPF, etc.]
   - Categoria dos dados: Dados pessoais sensíveis (Art. 11 LGPD)
   - Volume estimado de titulares afetados: [número]

4. MEDIDAS DE SEGURANÇA EXISTENTES
   - [Criptografia em repouso e trânsito (AES-256, TLS 1.2+)]
   - [Controle de acesso RBAC + MFA]
   - [Monitoramento 24/7 (CloudWatch, GuardDuty)]
   - [Backups automatizados com PITR]

5. MEDIDAS ADOTADAS APÓS O INCIDENTE
   - [Contenção imediata: descrição]
   - [Investigação forense: status]
   - [Notificação a titulares: status]
   - [Medidas corretivas: descrição]

6. RISCOS AOS TITULARES
   - [Avaliação dos riscos aos direitos e liberdades dos titulares]

7. MEDIDAS RECOMENDADAS AOS TITULARES
   - [Orientações de proteção recomendadas]
```

#### Template 4 — Comunicado Final (Resolução)

```
ASSUNTO: [TWYN] Incidente Resolvido — Serviço Face ID API Restaurado

Prezado(a) Cliente,

Informamos que o incidente reportado em [DD/MM/AAAA] foi resolvido.

RESUMO:
- Início do incidente: [HH:MM] [DD/MM/AAAA]
- Resolução: [HH:MM] [DD/MM/AAAA]
- Duração total: [X horas e Y minutos]
- Causa raiz: [Descrição resumida, sem detalhes de segurança]

IMPACTO:
- [Descrição do impacto real verificado]
- [Informação sobre dados, se aplicável]

AÇÕES CORRETIVAS:
Para prevenir recorrência, implementamos:
- [Ação 1]
- [Ação 2]
- [Ação 3]

Os serviços estão operando normalmente. Caso identifique qualquer
anormalidade, entre em contato conosco em [email/telefone].

Agradecemos sua compreensão e paciência.

Atenciosamente,
[Nome do CEO]
CEO — TWYN
```

---

## 11. Procedimentos de Recuperação por Cenário

### 11.1 CEN-01: Falha da Região AWS us-east-1

**Pré-requisitos verificados periodicamente:**
- [ ] S3 Cross-Region Replication ativo para us-west-2
- [ ] RDS read replica em us-west-2 (se ativado)
- [ ] Manifests Kubernetes versionados no Git
- [ ] Terraform/IaC atualizado para us-west-2
- [ ] Route 53 health checks configurados

**Procedimento:**

| Passo | Ação | Responsável | Tempo Estimado | Verificação |
|-------|------|------------|----------------|-------------|
| 1 | Confirmar indisponibilidade de us-east-1 via AWS Health Dashboard e CloudWatch cross-region | DevOps Lead | 15min | Dashboard AWS verificado |
| 2 | Notificar CEO e Gestor SGSI. Solicitar ativação BCP | DevOps Lead | 5min | Confirmação recebida |
| 3 | Abrir ticket AWS Support (Severity: Critical / Business-Critical) | Junior DevOps | 5min | Ticket ID registrado |
| 4 | Verificar integridade dos dados replicados em us-west-2 (S3 CRR, RDS replica) | DevOps Lead | 15min | Checksums validados |
| 5 | Promover RDS read replica em us-west-2 para standalone (se disponível) | DevOps Lead | 30min | RDS endpoint ativo em us-west-2 |
| 6 | Deploy da aplicação no EKS em us-west-2 (usando manifests do Git) | DevOps Lead | 45min | Pods running, health checks OK |
| 7 | Atualizar Route 53 para apontar para ALB em us-west-2 | DevOps Lead | 10min | DNS propagado, API respondendo |
| 8 | Validar operação completa da API em us-west-2 | Junior DevOps | 15min | Testes de integração passam |
| 9 | Comunicar clientes sobre restauração parcial/total | CEO | 15min | E-mail enviado |
| 10 | Monitorar estabilidade em us-west-2 | Junior DevOps | Contínuo | Dashboards sem alertas |
| 11 | Quando us-east-1 restaurado: planejar retorno (Seção 12) | DevOps Lead | — | — |

**Tempo total estimado: 2h30min — 4h**

### 11.2 CEN-02: Ransomware / Ataque Cibernético

**Procedimento:**

| Passo | Ação | Responsável | Tempo Estimado | Verificação |
|-------|------|------------|----------------|-------------|
| 1 | **ISOLAR IMEDIATAMENTE**: Revogar credenciais comprometidas, isolar workloads afetados (network policies, security groups) | DevOps Lead | 15min | Sistemas isolados confirmados |
| 2 | **NÃO PAGAR RESGATE. NÃO NEGOCIAR.** Registrar decisão. | CEO | Imediato | Registrado em log |
| 3 | Notificar CEO, Gestor SGSI. Ativar BCP e IRP (SGSI-IRP-001) | DevOps Lead | 5min | Equipe notificada |
| 4 | Preservar evidências forenses: snapshots de volumes afetados, logs CloudTrail, GuardDuty findings | Junior DevOps | 30min | Evidências preservadas em bucket isolado |
| 5 | Identificar escopo do comprometimento: quais sistemas, quais dados, timeline | DevOps Lead + Gestor SGSI | 1h | Relatório de escopo preliminar |
| 6 | Rotação de TODAS as credenciais: IAM keys, secrets, DB passwords, API tokens | DevOps Lead | 1h | Credenciais antigas invalidadas |
| 7 | Verificar integridade dos backups (confirmar que não estão comprometidos) | DevOps Lead | 30min | Backups validados |
| 8 | Reconstruir ambiente a partir de IaC (Terraform) + restore de backups limpos | DevOps Lead | 2-4h | Ambiente reconstruído |
| 9 | Restaurar dados do último backup limpo (antes do comprometimento) | DevOps Lead | 1-2h | Dados restaurados, validados |
| 10 | Se dados biométricos comprometidos: iniciar procedimento LGPD (Seção 16) | CEO + Jurídico | Paralelo | Notificação ANPD preparada |
| 11 | Validar operação completa, deploy de patches de segurança | DevOps Lead | 1h | Testes de integração passam |
| 12 | Comunicar clientes e reguladores conforme necessário | CEO | 30min | Comunicação enviada |
| 13 | Conduzir investigação forense completa (post-mortem) | Gestor SGSI + Externo | 1-2 semanas | Relatório forense |

**Tempo total estimado (restauração): 6-12h**

### 11.3 CEN-03: Indisponibilidade do DevOps Lead (SPOF)

**Procedimento:**

| Passo | Ação | Responsável | Tempo Estimado | Verificação |
|-------|------|------------|----------------|-------------|
| 1 | Confirmar indisponibilidade (tentativa de contato por múltiplos canais: telefone, WhatsApp, e-mail, Slack) | CEO ou Gestor SGSI | 2h (threshold) | Log de tentativas |
| 2 | Ativar procedimento SPOF. Junior DevOps assume operações conforme runbooks | CEO | 30min | Junior DevOps confirmado |
| 3 | Junior DevOps verifica acesso a todos os sistemas críticos (AWS Console, kubectl, GitHub) | Junior DevOps | 30min | Acessos validados |
| 4 | Se acessos insuficientes: usar procedimento break-glass (credenciais emergenciais em cofre) | Junior DevOps + CEO | 30min | Acessos emergenciais obtidos |
| 5 | Se necessário, acionar consultor externo de emergência (contrato pré-acordado) | CEO | 1-4h | Consultor disponível |
| 6 | Junior DevOps opera sistemas usando runbooks documentados | Junior DevOps | Contínuo | Operações dentro do normal |
| 7 | Comunicar equipe sobre mudança de responsabilidades | CEO | 15min | Equipe informada |
| 8 | Se indisponibilidade prolongada (>1 semana): iniciar recrutamento emergencial | CEO | — | — |

**Nota**: Este cenário pode ocorrer simultaneamente com outro incidente técnico, tornando-o particularmente crítico. A mitigação preventiva (cross-training) é essencial — ver Seção 17.

### 11.4 CEN-04: Violação de Dados / Comprometimento de Dados Biométricos

**Procedimento:**

| Passo | Ação | Responsável | Tempo Estimado | Verificação |
|-------|------|------------|----------------|-------------|
| 1 | **CONTENÇÃO IMEDIATA**: Bloquear acesso do vetor de ataque (revogar credenciais, bloquear IPs, desativar API keys comprometidas) | DevOps Lead | 15min | Vetor bloqueado |
| 2 | Notificar CEO + Gestor SGSI + Assessoria Jurídica. Ativar BCP + IRP | DevOps Lead | 5min | Todos notificados |
| 3 | Preservar evidências: logs, snapshots, network captures | Junior DevOps | 30min | Evidências preservadas |
| 4 | Avaliar escopo: quais dados, quantos titulares, período de exposição | DevOps Lead + Gestor SGSI | 2h | Relatório de escopo |
| 5 | Classificar o incidente: dados biométricos = dados sensíveis LGPD Art. 11 | Gestor SGSI + Jurídico | 30min | Classificação definida |
| 6 | **DECISÃO DE NOTIFICAÇÃO ANPD** (se risco significativo aos titulares) | CEO + Jurídico | 1h | Decisão registrada |
| 7 | Preparar notificação ANPD usando Template 3 (Seção 10.5) | Gestor SGSI + Jurídico | 2h | Notificação pronta |
| 8 | **Enviar notificação ANPD dentro de 72h** da ciência do incidente | CEO | ≤72h | Protocolo ANPD registrado |
| 9 | Notificar titulares afetados (se determinado pelo jurídico) | CEO + DPO | Conforme cronograma | Comunicação enviada |
| 10 | Implementar correções: patching, hardening, rotação de credenciais | DevOps Lead | 1-4h | Correções implementadas |
| 11 | Validar que a vulnerabilidade foi eliminada | DevOps Lead | 1h | Pen test de validação |
| 12 | Conduzir investigação forense completa | Gestor SGSI | 1-4 semanas | Relatório completo |
| 13 | Atualizar risk register e controles baseado nas lições aprendidas | Gestor SGSI | — | SGSI-RISK-002 atualizado |

### 11.5 CEN-05: Falha de Cadeia de Suprimentos

**Procedimento:**

| Passo | Ação | Responsável | Tempo Estimado | Verificação |
|-------|------|------------|----------------|-------------|
| 1 | Identificar serviço afetado (GitHub, ECR, EKS control plane, etc.) | DevOps Lead | 15min | Serviço identificado |
| 2 | Avaliar impacto: workloads em execução continuam? Deploys possíveis? | DevOps Lead | 15min | Avaliação completa |
| 3 | **Se GitHub indisponível**: Usar mirrors locais do código (se mantidos) ou aguardar restauração | DevOps Lead | — | — |
| 4 | **Se EKS control plane indisponível**: Workloads continuam rodando. NÃO tentar escalar ou redeployar. Aguardar. | DevOps Lead | — | Pods monitorados localmente |
| 5 | **Se ECR indisponível**: Usar imagens já em cache nos nós do EKS. Evitar restart de pods. | DevOps Lead | — | Imagens disponíveis |
| 6 | Ativar procedimento de deploy manual se hotfix urgente necessário: | DevOps Lead | 30min-2h | Deploy manual executado |
| | a) Build local da imagem Docker | | | |
| | b) Push para registry alternativo (se disponível) | | | |
| | c) kubectl apply com imagem alternativa | | | |
| 7 | Comunicar equipe sobre limitações temporárias | Gestor SGSI | 15min | Equipe ciente |
| 8 | Freeze de mudanças não críticas até restauração do serviço | DevOps Lead | — | Freeze comunicado |
| 9 | Monitorar status do fornecedor (status pages, suporte) | Junior DevOps | Contínuo | Atualizações registradas |
| 10 | Quando serviço restaurado: validar integridade e retomar operações | DevOps Lead | 30min | Pipeline funcional |

### 11.6 CEN-06: Falha de Banco de Dados (Corrupção RDS)

**Procedimento:**

| Passo | Ação | Responsável | Tempo Estimado | Verificação |
|-------|------|------------|----------------|-------------|
| 1 | Detectar corrupção (erros na aplicação, falha de health check, CloudWatch) | Monitoramento automático / Junior DevOps | 5min | Alerta identificado |
| 2 | Avaliar se Multi-AZ failover automático resolveu (RDS Multi-AZ) | DevOps Lead | 10min | Verificar endpoint RDS |
| 3 | Se Multi-AZ não resolveu: identificar último ponto consistente (CloudWatch, transaction logs) | DevOps Lead | 15min | Timestamp identificado |
| 4 | Iniciar Point-in-Time Recovery (PITR) para timestamp anterior à corrupção | DevOps Lead | 30-60min | Nova instância RDS criada |
| 5 | Validar integridade dos dados na nova instância (queries de verificação) | DevOps Lead | 30min | Dados íntegros verificados |
| 6 | Redirecionar aplicação para nova instância RDS | DevOps Lead | 15min | API usando nova instância |
| 7 | Validar operação completa da API | Junior DevOps | 15min | Testes de integração passam |
| 8 | Comunicar clientes se houve impacto perceptível | CEO | 30min | Comunicação enviada |
| 9 | Investigar causa raiz da corrupção | DevOps Lead | Post-incidente | Root cause identificado |

### 11.7 CEN-07: Ataque DDoS

**Procedimento:**

| Passo | Ação | Responsável | Tempo Estimado | Verificação |
|-------|------|------------|----------------|-------------|
| 1 | Detectar ataque: AWS Shield alerts, CloudWatch (tráfego anormal), WAF metrics | Monitoramento automático | 5min | Alerta identificado |
| 2 | Verificar se AWS Shield Standard está mitigando automaticamente | DevOps Lead | 10min | Métricas verificadas |
| 3 | Ativar regras WAF emergenciais: rate limiting agressivo, geo-blocking se padrão identificado | DevOps Lead | 15min | Regras ativas |
| 4 | Se ataque supera Shield Standard: considerar ativar AWS Shield Advanced (custo envolvido — requer aprovação CEO) | DevOps Lead → CEO | 30min | Decisão registrada |
| 5 | Escalar com AWS Support (caso de Business/Enterprise Support) | Junior DevOps | 15min | Ticket aberto |
| 6 | Se necessário: ativar CloudFront com caching agressivo para reduzir carga no backend | DevOps Lead | 30min | CloudFront ativo |
| 7 | Monitorar eficácia das mitigações | Junior DevOps | Contínuo | Tráfego normalizado |
| 8 | Quando ataque cessar: revisitar regras WAF e normalizar | DevOps Lead | 1h | Regras revisadas |

---

## 12. Retorno à Operação Normal

### 12.1 Critérios para Declarar Retorno à Normalidade

O retorno à operação normal somente é declarado quando **TODOS** os critérios abaixo são atendidos:

1. ✅ Todos os serviços P0 estão operacionais e respondendo normalmente
2. ✅ Métricas de performance dentro dos parâmetros normais (latência, taxa de erro, throughput)
3. ✅ RTO e RPO foram atendidos ou justificativa documentada se excedidos
4. ✅ Dados verificados como íntegros (nenhuma perda ou corrupção não recuperada)
5. ✅ Causa raiz identificada ou investigação em andamento com mitigação temporária implementada
6. ✅ Nenhum indicador de comprometimento ativo (IOCs limpos)
7. ✅ Comunicação de resolução enviada a todos os stakeholders afetados
8. ✅ CEO + Gestor SGSI + DevOps Lead concordam com a declaração

### 12.2 Procedimento de Retorno

| Passo | Ação | Responsável |
|-------|------|------------|
| 1 | Validar todos os critérios da seção 12.1 | Gestor SGSI |
| 2 | Reunião de equipe BCP para confirmar retorno | Todos |
| 3 | Se failover para DR: planejar e executar failback para região primária (us-east-1) | DevOps Lead |
| 4 | Validar failback: testes de integração, performance, dados | DevOps Lead + Junior DevOps |
| 5 | Atualizar Route 53 / DNS para região primária | DevOps Lead |
| 6 | Monitorar estabilidade por mínimo 2 horas após failback | Junior DevOps |
| 7 | Comunicar resolução final a clientes (Template 4, Seção 10.5) | CEO |
| 8 | Desativar BCP formalmente. Registrar no log de incidentes | Gestor SGSI |
| 9 | Agendar post-mortem (≤5 dias úteis após resolução) | Gestor SGSI |
| 10 | Conduzir post-mortem. Documentar lições aprendidas. Atualizar BCP se necessário. | Gestor SGSI + Equipe |

### 12.3 Failback — Retorno à Região Primária (us-east-1)

Se o incidente resultou em failover para us-west-2, o retorno à região primária segue processo controlado:

1. **Verificar estabilidade de us-east-1** (mínimo 2h sem incidentes reportados no AWS Health Dashboard)
2. **Sincronizar dados**: Replicar dados gerados em us-west-2 de volta para us-east-1
3. **Recriar infraestrutura em us-east-1** via IaC (Terraform)
4. **Validar ambiente us-east-1** com testes de integração completos
5. **Migração gradual de tráfego**: Route 53 weighted routing (10% → 50% → 100%)
6. **Monitorar por 4h** após migração completa
7. **Descomissionar recursos temporários em us-west-2** (exceto DR permanente)

---

## 13. Programa de Testes do BCP

### 13.1 Tipos de Teste

| Tipo | Descrição | Participantes | Frequência | Duração |
|------|-----------|--------------|-----------|---------|
| **Tabletop Exercise** | Simulação em mesa: equipe discute resposta a cenário hipotético, sem ação técnica | Equipe BCP completa | Semestral | 2-3 horas |
| **Technical DR Drill** | Teste técnico real: execução de procedimentos de failover, backup restore, recovery | DevOps Lead + Junior DevOps | Anual | 4-8 horas |
| **Communication Test** | Teste da cadeia de notificação e comunicação de crise | Equipe BCP | Anual | 1 hora |
| **Full Simulation** | Simulação completa: cenário realista, sem aviso prévio à equipe operacional, execução técnica + comunicação | Todos | Pré-certificação ISO 27001 | 1 dia |

### 13.2 Cronograma de Testes 2026-2027

| Data | Tipo de Teste | Cenário | Responsável | Status |
|------|--------------|---------|------------|--------|
| **Jul/2026** | Tabletop Exercise | CEN-03 (SPOF DevOps Lead) + CEN-06 (RDS failure simultâneo) | Gestor SGSI | ⏳ Planejado |
| **Ago/2026** | Communication Test | Teste de cadeia de notificação completa | Gestor SGSI | ⏳ Planejado |
| **Set/2026** | Technical DR Drill | CEN-01 (Failover us-east-1 → us-west-2) com RDS promote e EKS redeploy | DevOps Lead | ⏳ Planejado |
| **Out/2026** | Full Simulation | CEN-02 (Ransomware) — simulação pré-certificação | Gestor SGSI | ⏳ Planejado |
| **Jan/2027** | Tabletop Exercise | CEN-04 (Data breach biométrico) + LGPD notification | Gestor SGSI | ⏳ Planejado |
| **Abr/2027** | Technical DR Drill | CEN-06 (RDS PITR) + CEN-07 (DDoS mitigation) | DevOps Lead | ⏳ Planejado |
| **Jul/2027** | Tabletop Exercise | CEN-05 (Supply chain failure) | Gestor SGSI | ⏳ Planejado |
| **Out/2027** | Full Simulation | Cenário combinado: CEN-01 + CEN-03 | Gestor SGSI | ⏳ Planejado |

### 13.3 Critérios de Sucesso dos Testes

| Critério | Descrição | Meta |
|----------|-----------|------|
| RTO atingido | Serviço restaurado dentro do RTO definido | 100% |
| RPO atingido | Perda de dados dentro do RPO definido | 100% |
| Cadeia de notificação | Todos os stakeholders notificados dentro do tempo definido | 100% |
| Runbooks eficazes | Procedimentos executáveis sem ambiguidade | ≥ 90% dos passos sem ajuste |
| Equipe de backup | Junior DevOps capaz de executar procedimentos críticos | Sim |
| Comunicação | Templates de comunicação adequados e utilizados | Sim |

### 13.4 Relatório Pós-Teste

Após cada teste, o Gestor SGSI produz relatório contendo:

1. **Data, tipo e cenário testado**
2. **Participantes**
3. **Cronologia da execução** (timeline detalhado)
4. **Resultados vs. metas** (tabela de critérios de sucesso)
5. **Problemas identificados** (com severidade e responsável)
6. **Lições aprendidas**
7. **Ações corretivas** (com prazo e responsável)
8. **Recomendações de melhoria para o BCP**
9. **Assinatura**: Gestor SGSI + CEO

O relatório é armazenado em `docs/04-evidence/bcp-test-reports/` e revisado na próxima Management Review.

---

## 14. Treinamento e Conscientização

### 14.1 Programa de Treinamento BCP

| Público-Alvo | Conteúdo | Frequência | Formato | Responsável |
|--------------|----------|-----------|---------|------------|
| **Equipe BCP completa** | Este documento completo, procedimentos de ativação, papéis e responsabilidades | Anual + após revisões | Workshop presencial ou remoto (3h) | Gestor SGSI |
| **DevOps Lead + Junior DevOps** | Procedimentos técnicos de recuperação, runbooks, DR drills | Semestral | Hands-on lab (4h) | DevOps Lead |
| **CEO** | Decisões de crise, comunicação externa, autoridade de ativação, LGPD | Anual | Briefing executivo (1h) | Gestor SGSI |
| **Todos os colaboradores** | Awareness: o que é BCP, como reportar incidentes, o que fazer em crise | Anual (parte do treinamento SI geral) | E-learning (30min) | Gestor SGSI |
| **Novos colaboradores** | Introdução ao BCP durante onboarding | Na contratação | Briefing (30min) | Gestor SGSI / RH |

### 14.2 Competências Requeridas

| Papel | Competência | Status Atual | Ação Necessária |
|-------|------------|-------------|-----------------|
| DevOps Lead | AWS DR procedures, EKS operations, RDS management | ✅ Competente | Manter certificação / treinamento contínuo |
| Junior DevOps | AWS básico, kubectl, runbooks de emergência | ⚠️ Em desenvolvimento | Cross-training prioritário (ver Seção 17) |
| CEO | Comunicação de crise, LGPD awareness, decisão sob pressão | ⚠️ Necessita treinamento | Workshop de gestão de crise |
| Gestor SGSI | ISO 27001 BCP, coordenação de incidentes, LGPD | ✅ Competente | Manter atualização |

---

## 15. Manutenção e Revisão do Documento

### 15.1 Frequência de Revisão

Este documento é revisado:

| Gatilho | Frequência | Responsável |
|---------|-----------|------------|
| **Revisão periódica** | Anual (mínimo) | Gestor SGSI |
| **Após ativação do BCP** | Após cada ativação real | Gestor SGSI |
| **Após teste de BCP** | Após cada teste/exercício | Gestor SGSI |
| **Mudanças significativas na infraestrutura** | Quando ocorrerem | DevOps Lead → Gestor SGSI |
| **Mudanças na organização** (contratações, desligamentos, reorganização) | Quando ocorrerem | CEO → Gestor SGSI |
| **Mudanças em legislação** (LGPD, regulamentos ANPD) | Quando publicadas | Gestor SGSI |
| **Novo cenário de risco identificado** | Quando identificado | Gestor SGSI |

### 15.2 Processo de Atualização

1. Gestor SGSI identifica necessidade de revisão
2. Draft da atualização é preparado
3. Revisão técnica por DevOps Lead (procedimentos técnicos)
4. Revisão por CEO (questões de negócio e comunicação)
5. Aprovação formal por CEO
6. Comunicação da atualização a toda equipe BCP
7. Atualização do treinamento se procedimentos mudaram
8. Versão anterior arquivada com data de fim de vigência

### 15.3 Distribuição e Armazenamento

| Localização | Formato | Acesso |
|-------------|---------|--------|
| Repositório Git (`docs/02-policies/`) | Markdown (versionado) | Equipe BCP |
| Cópia impressa no escritório | PDF impresso | CEO (cofre) |
| E-mail para equipe BCP | PDF | Equipe BCP |
| AWS S3 (bucket de documentação) | PDF | DevOps Lead |

---

## 16. Considerações LGPD

### 16.1 Classificação de Dados

A TWYN processa **dados pessoais sensíveis** (Art. 11, LGPD):

| Tipo de Dado | Classificação LGPD | Classificação TWYN | Armazenamento | Proteção |
|-------------|--------------------|--------------------|--------------|----------|
| Templates biométricos faciais | Dado pessoal sensível | RESTRICTED | RDS (criptografado) + S3 (SSE-KMS) | Criptografia AES-256, RBAC, MFA, audit logs |
| Imagens faciais | Dado pessoal sensível | RESTRICTED | S3 (SSE-KMS) | Criptografia, lifecycle policies, CRR |
| Dados cadastrais (nome, CPF) | Dado pessoal | CONFIDENTIAL | RDS (criptografado) | Criptografia, RBAC |
| Logs de auditoria | Dado pessoal (contém IPs, user IDs) | CONFIDENTIAL | CloudWatch / S3 | Criptografia, imutabilidade |

### 16.2 Obrigações de Notificação (LGPD Art. 48)

Em caso de incidente de segurança que possa acarretar **risco ou dano relevante aos titulares**:

| Obrigação | Prazo | Responsável | Referência |
|-----------|-------|------------|-----------|
| Notificação à **ANPD** | ≤ **72 horas** após ciência do incidente | CEO + DPO | LGPD Art. 48 |
| Notificação aos **titulares afetados** | Prazo razoável (definido pela ANPD) | CEO + DPO | LGPD Art. 48, §1 |
| Documentação do incidente | Imediato (durante investigação) | Gestor SGSI | LGPD Art. 48, §1 |

### 16.3 Conteúdo da Notificação à ANPD

A notificação deve conter (mínimo):

1. Descrição da natureza dos dados pessoais afetados
2. Informações sobre os titulares envolvidos
3. Indicação das medidas técnicas e de segurança utilizadas
4. Riscos relacionados ao incidente
5. Motivos da demora (se notificação não foi imediata)
6. Medidas adotadas ou a serem adotadas para reverter ou mitigar

**Template**: Ver Seção 10.5 — Template 3.

### 16.4 Preservação de Dados durante Recuperação

Durante procedimentos de DR/recovery:

- ✅ Dados biométricos devem manter criptografia em todas as etapas
- ✅ Backups devem ser restaurados em ambiente com mesmos controles de segurança
- ✅ Logs de acesso durante a recuperação devem ser mantidos
- ✅ Transferência cross-region deve usar canais criptografados (TLS 1.2+)
- ❌ NUNCA armazenar dados biométricos em ambientes temporários sem criptografia
- ❌ NUNCA desabilitar controles de acesso durante emergência (usar break-glass procedures)

---

## 17. Plano de Mitigação de SPOF

### 17.1 Identificação de SPOFs

| SPOF Identificado | Risco | Impacto | Probabilidade | Severidade |
|-------------------|-------|---------|--------------|-----------|
| **DevOps Lead** — Único administrador de infraestrutura AWS, EKS, RDS | Incapacidade de operar, manter ou recuperar produção | Crítico | Média | **Crítico** |
| **CEO** — Único decisor para ativação BCP e comunicação externa | Atraso em decisões críticas e comunicação | Alto | Baixa | **Alto** |
| **Gestor SGSI (externo)** — Único coordenador SGSI/BCP | Falta de coordenação em incidentes SGSI | Médio | Baixa | **Médio** |
| **AWS Account Owner** — Acesso root limitado a uma pessoa | Impossibilidade de operações root | Médio | Muito Baixa | **Médio** |

### 17.2 Matriz de Cross-Training

| Competência | DevOps Lead (Titular) | Junior DevOps (Backup) | Status | Meta de Conclusão | Evidência |
|-------------|----------------------|----------------------|--------|-------------------|-----------|
| **AWS Console — navegação e operação** | ✅ Expert | ⚠️ Intermediário | Em progresso | Jul/2026 | Certificação AWS ou avaliação interna |
| **kubectl — operações em EKS** | ✅ Expert | ⚠️ Básico | Em progresso | Ago/2026 | Exercício prático documentado |
| **RDS — backup, restore, PITR** | ✅ Expert | ❌ Não treinado | Não iniciado | Set/2026 | DR drill com restore completo |
| **Terraform — apply, plan, state** | ✅ Expert | ❌ Não treinado | Não iniciado | Out/2026 | Deploy de ambiente staging |
| **Route 53 — DNS management** | ✅ Expert | ⚠️ Básico | Em progresso | Jul/2026 | Exercício de failover DNS |
| **IAM — gestão de credenciais** | ✅ Expert | ❌ Não treinado | Não iniciado | Ago/2026 | Rotação de credenciais supervisionada |
| **Incident response — troubleshooting** | ✅ Expert | ⚠️ Básico | Em progresso | Set/2026 | Participação em DR drill |
| **CI/CD — GitHub Actions, deploy** | ✅ Expert | ⚠️ Intermediário | Em progresso | Jul/2026 | Deploy em staging sem supervisão |
| **Monitoramento — CloudWatch, alertas** | ✅ Expert | ⚠️ Intermediário | Em progresso | Jul/2026 | Configuração de alerta novo |
| **Break-glass procedure** | ✅ Conhece | ❌ Não treinado | Não iniciado | Jul/2026 | Teste supervisionado |

### 17.3 Plano de Ação para Mitigação de SPOFs

| # | Ação | Responsável | Prazo | Prioridade | Status |
|---|------|------------|-------|-----------|--------|
| 1 | Documentar todos os runbooks de operações críticas em `docs/06-implementation-guides/` | DevOps Lead | Jun/2026 | P0 — Urgente | ⏳ Em progresso |
| 2 | Treinamento hands-on: Junior DevOps em kubectl e EKS operations | DevOps Lead | Ago/2026 | P0 — Urgente | ⏳ Planejado |
| 3 | Treinamento: Junior DevOps em RDS operations (backup, PITR, promote replica) | DevOps Lead | Set/2026 | P0 — Urgente | ⏳ Planejado |
| 4 | Configurar procedimento break-glass com credenciais emergenciais em cofre | DevOps Lead + CEO | Jul/2026 | P0 — Urgente | ⏳ Planejado |
| 5 | Identificar e pré-contratar consultor externo de emergência para infraestrutura AWS | CEO | Jul/2026 | P1 — Alto | ⏳ Planejado |
| 6 | Treinamento: Junior DevOps em Terraform basics | DevOps Lead | Out/2026 | P1 — Alto | ⏳ Planejado |
| 7 | Treinamento de gestão de crise para CEO | Gestor SGSI | Ago/2026 | P1 — Alto | ⏳ Planejado |
| 8 | Definir backup formal para Gestor SGSI (CEO assume temporariamente) | CEO + Gestor SGSI | Jul/2026 | P2 — Médio | ⏳ Planejado |
| 9 | Configurar acesso AWS root com MFA em dispositivo secundário (CEO) | DevOps Lead + CEO | Jul/2026 | P1 — Alto | ⏳ Planejado |
| 10 | Pair programming mensal: DevOps Lead + Junior DevOps em tarefas de produção | DevOps Lead | Mensal | P1 — Alto | ⏳ Planejado |

### 17.4 Métricas de Progresso SPOF

| Indicador | Meta | Medição |
|-----------|------|---------|
| % de competências com backup treinado | 100% até Out/2026 | Matriz de cross-training (Seção 17.2) |
| Runbooks documentados vs. necessários | 100% até Jul/2026 | Inventário de runbooks |
| DR drills com Junior DevOps como operador | ≥ 1 até Dez/2026 | Relatório de teste BCP |
| Break-glass procedure testado | ≥ 1 até Ago/2026 | Evidência de teste |

---

## 18. Indicadores de Desempenho (KPIs)

### 18.1 KPIs de Continuidade de Negócios

| KPI | Descrição | Meta | Frequência de Medição | Responsável |
|-----|-----------|------|----------------------|------------|
| **RTO real vs. definido** | Tempo efetivo de recuperação em incidentes reais ou testes | ≤ 4h (P0) | Por incidente/teste | Gestor SGSI |
| **RPO real vs. definido** | Perda de dados efetiva em incidentes reais ou testes | ≤ 15min | Por incidente/teste | DevOps Lead |
| **Disponibilidade do serviço** | Uptime da Face ID API | ≥ 99,5% | Mensal | DevOps Lead |
| **Tempo de ativação BCP** | Tempo entre detecção e ativação do BCP | ≤ 30min | Por ativação | Gestor SGSI |
| **Tempo de notificação interna** | Tempo entre detecção e notificação da equipe BCP | ≤ 15min | Por incidente | Gestor SGSI |
| **Tempo de notificação a clientes** | Tempo entre confirmação de impacto e comunicação | ≤ 2h | Por incidente | CEO |
| **Testes BCP realizados vs. planejados** | Aderência ao cronograma de testes | 100% | Semestral | Gestor SGSI |
| **Eficácia dos testes** | % de critérios de sucesso atingidos nos testes | ≥ 90% | Por teste | Gestor SGSI |
| **Progresso cross-training SPOF** | % de competências com backup treinado | 100% até Out/2026 | Trimestral | DevOps Lead |
| **Runbooks documentados** | % de processos críticos com runbook atualizado | 100% | Trimestral | DevOps Lead |
| **Ações pós-teste implementadas** | % de ações corretivas de testes BCP implementadas no prazo | ≥ 90% | Por teste | Gestor SGSI |
| **Notificação LGPD no prazo** | Notificações à ANPD dentro de 72h (se aplicável) | 100% | Por incidente | CEO |

### 18.2 Painel de Acompanhamento

Os KPIs são reportados:

- **Mensalmente**: Disponibilidade do serviço (dashboard automatizado)
- **Trimestralmente**: Progresso SPOF, runbooks, cross-training
- **Semestralmente**: Testes BCP, eficácia
- **Na Management Review** (cláusula 9.3): Todos os KPIs consolidados
- **Por incidente**: RTO, RPO, tempos de notificação (relatório pós-incidente)

---

## 19. Documentos Relacionados

| Doc ID | Título | Descrição |
|--------|--------|-----------|
| SGSI-POLICY-001 | Política de Segurança da Informação | Política mãe do SGSI |
| SGSI-DRP-001 | Plano de Recuperação de Desastres | Procedimentos técnicos detalhados de DR |
| SGSI-IRP-001 | Política de Resposta a Incidentes | Procedimentos de resposta a incidentes de SI |
| SGSI-RISK-002 | Registro de Riscos | Registro e avaliação de riscos do SGSI |
| SGSI-RTP-001 | Plano de Tratamento de Riscos | Plano de tratamento para riscos identificados |
| SGSI-SOA-001 | Declaração de Aplicabilidade | Controles Annex A aplicáveis e justificativas |
| SOP-001 | Procedimento de Onboarding/Offboarding | Procedimento de entrada e saída de colaboradores |
| SOP-005 | Recertificação IAM | Revisão periódica de acessos |
| SGSI-ASSETS-001 | Inventário de Ativos | Inventário de ativos de informação |
| SGSI-BREACH-LOG | Registro de Violações de Dados | Log de incidentes de violação de dados |
| SGSI-TRAINING-LOG | Registro de Treinamentos | Log de treinamentos de SI realizados |
| gap-004-backup-testing.md | Guia de Teste de Backup | Procedimentos de teste de backup e restore |

---

## 20. Histórico de Revisões

| Versão | Data | Autor | Descrição das Alterações | Aprovado por |
|--------|------|-------|-------------------------|-------------|
| 0.1 (Stub) | 26/05/2026 | Ricardo Esper (Bekaa) | Versão inicial stub (39 linhas) | — |
| 1.0 (Draft) | 02/06/2026 | Ricardo Esper (Bekaa) | Reescrita completa: BIA detalhado, 7 cenários de risco, procedimentos de recuperação passo-a-passo, equipe BCP com escalação, critérios de ativação, plano de comunicação com templates, programa de testes 2026-2027, LGPD (notificação ANPD ≤72h), mitigação SPOF com matriz de cross-training, KPIs | **[CEO TWYN]** — Pendente |
| 1.0 | [Pendente] | Ricardo Esper (Bekaa) | Versão aprovada para certificação ISO 27001 | **[CEO TWYN]** |

---

## 21. Aprovação

### Declaração de Aprovação

> **"Eu, [Nome Completo do CEO], como Chief Executive Officer da TWYN, aprovo este Plano de Continuidade de Negócios e me comprometo a alocar os recursos necessários para sua implementação, teste e manutenção contínua, garantindo a resiliência operacional da organização em conformidade com a ISO/IEC 27001:2022."**

---

**CEO TWYN**
**Assinatura**: _______________________________
**Nome**: [Nome Completo]
**Data**: _____ / _____ / 2026

---

**Gestor SGSI**
**Assinatura**: _______________________________
**Nome**: Ricardo Esper
**Data**: _____ / _____ / 2026

---

**DevOps Lead**
**Assinatura**: _______________________________
**Nome**: [Nome Completo]
**Data**: _____ / _____ / 2026

---

## ⚠️ PRÓXIMOS PASSOS CRÍTICOS

1. **[ ]** Preencher todos os placeholders de contato (Seção 8.3)
2. **[ ]** Obter assinatura do CEO
3. **[ ]** Executar primeiro Tabletop Exercise (Jul/2026) — endereçar GAP IA-001
4. **[ ]** Completar documentação de runbooks (DevOps Lead)
5. **[ ]** Iniciar programa de cross-training (Junior DevOps)
6. **[ ]** Configurar procedimento break-glass
7. **[ ]** Identificar e pré-contratar consultor externo de emergência
8. **[ ]** Comunicar BCP a toda equipe TWYN
9. **[ ]** Agendar Management Review para revisão deste documento

---

**FIM DO DOCUMENTO**
