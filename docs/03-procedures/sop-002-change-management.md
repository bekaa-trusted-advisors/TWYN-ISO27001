---
document_id: SGSI-SOP-002
title: "Procedimento Operacional Padrão — Gestão de Mudanças"
version: "1.0"
date: 2026-06-02
status: Approved
classification: INTERNAL
owner: Gestor SGSI
approved_by: "CEO (Pendente)"
next_review: 2027-06-02
related_policies:
  - SGSI-POLICY-001
  - SGSI-POLICY-002
annex_a_controls:
  - "A.8.32 — Change management"
  - "A.8.9 — Configuration management"
  - "A.8.25 — Secure development lifecycle"
  - "A.8.27 — Secure system architecture and engineering principles"
  - "A.8.31 — Separation of development, test and production environments"
---

# SOP-002: Gestão de Mudanças

> **Classificação:** INTERNO  
> **Versão:** 1.0 | **Status:** Draft  
> **Proprietário:** Gestor SGSI  
> **Aprovação:** CEO (Pendente)

---

## 1. Objetivo

Estabelecer um procedimento padronizado, rastreável e auditável para gerenciar todas as mudanças em sistemas de informação, infraestrutura e configurações da **TWYN**, assegurando que:

- Mudanças sejam avaliadas quanto ao risco e impacto antes da implementação;
- A integridade, disponibilidade e confidencialidade dos dados biométricos (classificação **RESTRITO**) sejam preservadas;
- Exista rastreabilidade completa para fins de auditoria ISO 27001:2022;
- Procedimentos de rollback estejam definidos e testados;
- A separação de ambientes (Dev → Staging → Production) seja respeitada.

---

## 2. Escopo

Este procedimento aplica-se a **todas as mudanças** nos seguintes ativos:

| Categoria | Exemplos |
|---|---|
| **Infraestrutura AWS** | VPCs, EKS clusters, RDS PostgreSQL, S3 buckets, IAM policies |
| **Infraestrutura como Código** | Módulos Terraform, state files (S3 backend) |
| **Aplicação** | Face ID Platform API, microsserviços, containers |
| **Pipeline CI/CD** | GitHub Actions workflows, ECR repositories |
| **Configurações K8s** | Deployments, Services, ConfigMaps, Secrets, Ingress |
| **Políticas de segurança** | Network policies, Security Groups, WAF rules |
| **Dados biométricos** | Qualquer mudança que altere fluxo de coleta, processamento ou armazenamento |

### 2.1 Exclusões

- Atualizações de documentação que não alteram processos operacionais;
- Mudanças em ambientes de desenvolvimento local (workstations pessoais).

---

## 3. Definições e Termos

| Termo | Definição |
|---|---|
| **Mudança** | Adição, modificação ou remoção de qualquer componente que possa afetar serviços de TI |
| **RFC** | Request for Change — solicitação formal de mudança |
| **CAB** | Change Advisory Board — comitê consultivo de mudanças |
| **CMDB** | Configuration Management Database — inventário de ativos e configurações |
| **Rollback** | Reversão a um estado anterior conhecido e funcional |
| **Dados RESTRITOS** | Dados biométricos faciais conforme classificação SGSI-POLICY-002 |
| **IaC** | Infrastructure as Code (Terraform) |
| **CI/CD** | Continuous Integration / Continuous Delivery (GitHub Actions) |

---

## 4. Classificação de Mudanças

### 4.1 Matriz de Classificação

| Classificação | Risco | Aprovação | Prazo | Exemplos |
|---|---|---|---|---|
| **Standard (Padrão)** | Baixo | Pré-aprovada | Sem restrição | Atualização de dependência sem breaking changes, ajuste de réplicas, scaling de pods |
| **Normal** | Médio/Alto | CAB | Mínimo 48h antes da implantação | Nova feature, alteração de schema DB, mudança em network policies, alteração de pipeline |
| **Emergency (Emergência)** | Crítico | DevOps Lead (pós-aprovação CAB) | Imediato | Hotfix de vulnerabilidade crítica, incidente de segurança, indisponibilidade de produção |

### 4.2 Critérios para Escalonamento Automático para "Normal"

Uma mudança **deve** ser classificada como **Normal** (mínimo) quando:

- [ ] Altera fluxo de dados biométricos (classificação RESTRITO)
- [ ] Modifica políticas IAM ou Security Groups
- [ ] Altera schema do RDS PostgreSQL em produção
- [ ] Introduz nova dependência externa ou serviço de terceiros
- [ ] Modifica configurações de rede entre VPCs
- [ ] Altera mecanismos de autenticação/autorização
- [ ] Modifica pipeline CI/CD (GitHub Actions workflows)
- [ ] Altera configurações de criptografia (at-rest ou in-transit)

---

## 5. Papéis e Responsabilidades

### 5.1 Matriz RACI

| Atividade | Change Requester | Change Approver (DevOps Lead) | CAB | Emergency Approver | Gestor SGSI |
|---|---|---|---|---|---|
| Abrir RFC (GitHub Issue) | **R** | I | I | — | I |
| Avaliar impacto e risco | R | **A** | C | — | C |
| Classificar mudança | R | **A** | C | — | I |
| Aprovar mudança Standard | — | **A/R** | — | — | — |
| Aprovar mudança Normal | — | R | **A** | — | C |
| Aprovar mudança Emergency | — | — | — | **A/R** | I |
| Implementar mudança | **R** | A | — | — | — |
| Verificar/validar | R | **A** | — | — | I |
| Fechar RFC | **R** | A | — | — | I |

> **R** = Responsável | **A** = Aprovador | **C** = Consultado | **I** = Informado

### 5.2 Detalhamento dos Papéis

| Papel | Responsável | Descrição |
|---|---|---|
| **Change Requester** | Qualquer colaborador TWYN | Solicita a mudança preenchendo template no GitHub Issues |
| **Change Approver** | DevOps Lead | Avalia risco, aprova mudanças Standard, coordena implementação |
| **CAB** | DevOps Lead + Gestor SGSI | Avalia e aprova mudanças Normal; analisa pós-implementação de emergências |
| **Emergency Approver** | DevOps Lead | Aprova mudanças de emergência; CAB revisa em até 48h após a implementação |
| **Gestor SGSI** | Gestor do Sistema de Gestão | Garante conformidade ISO 27001, revisa impactos em dados RESTRITOS |

---

## 6. Processo de Gestão de Mudanças

### 6.1 Visão Geral do Fluxo

```
┌─────────────┐    ┌──────────────┐    ┌──────────────┐    ┌────────────────┐
│  1. Request  │───▶│ 2. Avaliação │───▶│ 3. Aprovação │───▶│ 4. Implantação │
│  (RFC)       │    │  de Impacto  │    │              │    │                │
└─────────────┘    └──────────────┘    └──────────────┘    └───────┬────────┘
                                                                   │
                   ┌──────────────┐    ┌──────────────┐            │
                   │ 6. Fechamento│◀───│5. Verificação│◀───────────┘
                   │              │    │              │
                   └──────────────┘    └──────────────┘
```

### 6.2 Etapa 1 — Solicitação (Request)

**Responsável:** Change Requester

| # | Ação | Detalhamento |
|---|---|---|
| 1.1 | Abrir GitHub Issue | Utilizar o template `[RFC] Change Request` no repositório `TWYN-ISO27001` |
| 1.2 | Preencher campos obrigatórios | Descrição, justificativa, classificação proposta, sistemas afetados, plano de rollback |
| 1.3 | Adicionar label | `change:standard`, `change:normal` ou `change:emergency` |
| 1.4 | Atribuir ao Change Approver | Assign ao DevOps Lead para triagem |
| 1.5 | Vincular ao projeto/milestone | Se aplicável, vincular à Sprint ou Release correspondente |

**Evidência:** GitHub Issue criado com template preenchido.

### 6.3 Etapa 2 — Avaliação de Impacto

**Responsável:** Change Approver (DevOps Lead), com suporte do Gestor SGSI para dados RESTRITOS

| # | Ação | Detalhamento |
|---|---|---|
| 2.1 | Verificar classificação proposta | Validar se a classificação (Standard/Normal/Emergency) está correta conforme §4.2 |
| 2.2 | Avaliar impacto técnico | Sistemas afetados, dependências, janela de manutenção necessária |
| 2.3 | Avaliar impacto em dados biométricos | Se a mudança afeta fluxo de dados RESTRITOS → **escalar obrigatoriamente para Normal** |
| 2.4 | Avaliar risco de segurança | Verificar se há impacto em controles ISO 27001 (Anexo A) |
| 2.5 | Validar plano de rollback | Confirmar que o plano de reversão é viável e documentado |
| 2.6 | Verificar resultados de scanning | Confirmar que Trivy/Snyk não reportam vulnerabilidades críticas |
| 2.7 | Documentar avaliação na Issue | Registrar análise como comentário na GitHub Issue |

**Matriz de Risco para Avaliação:**

| Probabilidade ↓ / Impacto → | Baixo | Médio | Alto | Crítico |
|---|---|---|---|---|
| **Improvável** | Aceitar | Aceitar | Monitorar | Mitigar |
| **Possível** | Aceitar | Monitorar | Mitigar | Mitigar |
| **Provável** | Monitorar | Mitigar | Escalar CAB | Escalar CAB |
| **Quase Certo** | Monitorar | Escalar CAB | Escalar CAB | **Recusar** |

### 6.4 Etapa 3 — Aprovação

**Fluxo de aprovação por classificação:**

```
                    ┌─────────────────┐
                    │ Classificação?  │
                    └────────┬────────┘
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────────┐
        │ Standard │  │  Normal  │  │  Emergency   │
        └─────┬────┘  └─────┬────┘  └──────┬───────┘
              ▼              ▼              ▼
        ┌──────────┐  ┌──────────┐  ┌──────────────┐
        │ Auto-    │  │   CAB    │  │ DevOps Lead  │
        │ aprovada │  │  Review  │  │  aprova      │
        │ DevOps   │  │ (48h)    │  │  imediato    │
        │ Lead     │  └─────┬────┘  └──────┬───────┘
        └─────┬────┘        ▼              ▼
              │        ┌──────────┐  ┌──────────────┐
              │        │Aprovado/ │  │ CAB revisa   │
              │        │Rejeitado │  │ em até 48h   │
              │        └─────┬────┘  │ pós-implant. │
              │              │       └──────┬───────┘
              ▼              ▼              ▼
        ┌─────────────────────────────────────────┐
        │          Etapa 4: Implantação           │
        └─────────────────────────────────────────┘
```

#### 6.4.1 Aprovação Standard

| # | Ação | Detalhamento |
|---|---|---|
| 3.1a | DevOps Lead valida classificação | Confirma que a mudança é de baixo risco e pré-aprovada |
| 3.2a | Aprovar via GitHub | Aprovar PR com comentário `[STANDARD-APPROVED]` |
| 3.3a | Registrar na Issue | Adicionar label `approved:standard` |

#### 6.4.2 Aprovação Normal (CAB)

| # | Ação | Detalhamento |
|---|---|---|
| 3.1b | Agendar revisão CAB | DevOps Lead + Gestor SGSI revisam em reunião ou assíncrono (Slack/GitHub) |
| 3.2b | Avaliar documentação | Verificar completude do RFC: impacto, rollback, testes, janela |
| 3.3b | Decisão formal | Aprovar, solicitar ajustes, ou rejeitar — documentado na Issue |
| 3.4b | Aprovar via GitHub | CAB members aprovam PR com comentário `[CAB-APPROVED]` |
| 3.5b | Registrar na Issue | Adicionar label `approved:normal` e registrar ata resumida |

#### 6.4.3 Aprovação Emergency

| # | Ação | Detalhamento |
|---|---|---|
| 3.1c | DevOps Lead avalia urgência | Confirma que a situação justifica bypass do processo Normal |
| 3.2c | Aprovar imediatamente | Aprovar PR com comentário `[EMERGENCY-APPROVED]` + justificativa |
| 3.3c | Notificar Gestor SGSI | Enviar notificação imediata (Slack/e-mail) |
| 3.4c | Abrir RFC retroativo | Criar GitHub Issue com template em até **4 horas** |
| 3.5c | CAB revisa em até 48h | CAB analisa a mudança e documenta lições aprendidas |

### 6.5 Etapa 4 — Implantação

**Responsável:** Change Requester (implementação), DevOps Lead (supervisão)

| # | Ação | Detalhamento |
|---|---|---|
| 4.1 | Criar branch feature | `git checkout -b feature/RFC-XXX-descricao` a partir de `main` |
| 4.2 | Implementar mudança | Código, Terraform, K8s manifests conforme especificado no RFC |
| 4.3 | Executar testes locais | Testes unitários, linting, validação Terraform (`terraform validate`) |
| 4.4 | Abrir Pull Request | PR para `main` referenciando a Issue RFC (`Closes #XXX`) |
| 4.5 | Pipeline CI automática | GitHub Actions executa: build → testes → Trivy scan → Snyk scan |
| 4.6 | Code Review obrigatório | Mínimo **1 reviewer** (DevOps Lead ou par designado) |
| 4.7 | Deploy em Staging | Merge em branch staging → deploy automático no EKS staging (VPC separada) |
| 4.8 | Testes em Staging | Testes de integração, smoke tests, verificação de scanning |
| 4.9 | Aprovação para Production | Reviewer aprova e merge em `main` |
| 4.10 | Deploy em Production | GitHub Actions → push para ECR → rolling update no EKS production |

**Checklist pré-deploy Production:**

- [ ] PR aprovado por no mínimo 1 reviewer
- [ ] Pipeline CI verde (build + testes + scans)
- [ ] Trivy/Snyk: zero vulnerabilidades críticas ou altas não mitigadas
- [ ] Testes em Staging concluídos com sucesso
- [ ] Plano de rollback documentado e validado
- [ ] Janela de manutenção comunicada (se aplicável)
- [ ] Backup/snapshot RDS recente (para mudanças de schema)
- [ ] Monitoramento configurado para alertas pós-deploy

### 6.6 Etapa 5 — Verificação

**Responsável:** Change Requester + DevOps Lead

| # | Ação | Detalhamento | Tempo |
|---|---|---|---|
| 5.1 | Health check da aplicação | Verificar endpoints `/health` e `/ready` | Imediato |
| 5.2 | Verificar métricas EKS | CPU, memória, pods running, restarts | 5 min |
| 5.3 | Smoke tests | Executar suite de testes de fumaça em produção | 10 min |
| 5.4 | Verificar logs | Checar CloudWatch/Kubernetes logs para erros | 15 min |
| 5.5 | Monitorar alertas | Observar dashboards de monitoramento | 30 min |
| 5.6 | Validar rollback | Confirmar que o mecanismo de rollback está funcional | 15 min |
| 5.7 | Teste de funcionalidade | Validar que a funcionalidade alterada opera conforme esperado | 30 min |

**Critérios de Sucesso:**

- [ ] Todos os pods em estado `Running`
- [ ] Zero erros 5xx nos primeiros 30 minutos
- [ ] Latência p95 dentro do SLO (< 500ms para API Face ID)
- [ ] Sem alertas de segurança disparados
- [ ] Funcionalidade conforme especificado no RFC

### 6.7 Etapa 6 — Fechamento

**Responsável:** Change Requester

| # | Ação | Detalhamento |
|---|---|---|
| 6.1 | Atualizar inventário de ativos | Registrar mudanças no CMDB/inventário de configuração |
| 6.2 | Documentar resultado | Registrar na GitHub Issue: sucesso, observações, métricas |
| 6.3 | Atualizar documentação | Atualizar READMEs, runbooks ou diagramas afetados |
| 6.4 | Fechar Issue | Adicionar label `status:completed` e fechar a Issue |
| 6.5 | Comunicar stakeholders | Notificar equipe sobre a conclusão da mudança |
| 6.6 | Arquivar evidências | Garantir que logs de CI/CD, PRs e aprovações estejam preservados |

---

## 7. Procedimento de Mudança de Emergência (Hotfix)

### 7.1 Critérios para Ativação

Uma mudança de emergência é ativada **apenas** quando:

1. Existe vulnerabilidade de segurança sendo explorada ativamente;
2. O serviço de produção está indisponível ou severamente degradado;
3. Há risco iminente de vazamento de dados biométricos (RESTRITOS);
4. Há violação regulatória que requer correção imediata.

### 7.2 Fluxo de Emergência

```
┌─────────────┐    ┌───────────────┐    ┌─────────────┐    ┌──────────────┐
│  Incidente  │───▶│ DevOps Lead   │───▶│   Hotfix     │───▶│   Deploy     │
│  Detectado  │    │ Aprova        │    │   Branch     │    │   Direto     │
└─────────────┘    └───────────────┘    └─────────────┘    └──────┬───────┘
                                                                   │
┌──────────────┐    ┌───────────────┐    ┌─────────────┐           │
│  RFC         │◀───│  CAB Review   │◀───│ Verificação │◀──────────┘
│  Retroativo  │    │  (até 48h)    │    │ Pós-deploy  │
└──────────────┘    └───────────────┘    └─────────────┘
```

| # | Ação | Responsável | SLA |
|---|---|---|---|
| 7.1 | Confirmar criticidade do incidente | DevOps Lead | 15 min |
| 7.2 | Aprovar mudança de emergência | DevOps Lead (Emergency Approver) | 15 min |
| 7.3 | Criar branch `hotfix/EMERGENCY-XXX` | Implementador | Imediato |
| 7.4 | Implementar correção | Implementador | Variável |
| 7.5 | PR com scan mínimo obrigatório | Implementador | — |
| 7.6 | Deploy direto em Production | DevOps Lead | — |
| 7.7 | Verificação pós-deploy | DevOps Lead + Implementador | 30 min |
| 7.8 | Notificar Gestor SGSI | DevOps Lead | 1 hora |
| 7.9 | Abrir RFC retroativo (GitHub Issue) | Implementador | 4 horas |
| 7.10 | CAB revisa mudança de emergência | CAB | 48 horas |

> **⚠️ IMPORTANTE:** Mesmo em emergências, o scan de container via Trivy/Snyk **deve** ser executado. Apenas o processo de aprovação CAB é abreviado.

---

## 8. Procedimento de Rollback

### 8.1 Critérios para Ativação de Rollback

O rollback **deve** ser iniciado quando:

- [ ] Erros 5xx > 1% do tráfego por mais de 5 minutos;
- [ ] Health check falha em 2+ pods consecutivamente;
- [ ] Alerta de segurança crítico disparado pós-deploy;
- [ ] Funcionalidade core da API Face ID comprometida;
- [ ] Latência p95 excede 2x o SLO por mais de 10 minutos;
- [ ] Evidência de impacto em dados biométricos.

### 8.2 Procedimentos de Rollback por Tipo

#### 8.2.1 Rollback de Aplicação (EKS)

| # | Ação | Comando/Detalhamento |
|---|---|---|
| R.1 | Identificar deployment afetado | `kubectl get deployments -n production` |
| R.2 | Executar rollback | `kubectl rollout undo deployment/<nome> -n production` |
| R.3 | Verificar rollback | `kubectl rollout status deployment/<nome> -n production` |
| R.4 | Confirmar versão anterior | `kubectl describe deployment/<nome> -n production` |
| R.5 | Executar smoke tests | Suite de testes pós-rollback |

#### 8.2.2 Rollback de Infraestrutura (Terraform)

| # | Ação | Comando/Detalhamento |
|---|---|---|
| R.6 | Identificar state anterior | Verificar versões no S3 backend (versionamento habilitado) |
| R.7 | Reverter commit Terraform | `git revert <commit-hash>` no repositório IaC |
| R.8 | Planejar reversão | `terraform plan` para verificar mudanças de reversão |
| R.9 | Aplicar reversão | `terraform apply` após revisão do plan |
| R.10 | Verificar estado | `terraform state list` + verificação manual dos recursos |

#### 8.2.3 Rollback de Schema de Banco (RDS)

| # | Ação | Detalhamento |
|---|---|---|
| R.11 | Avaliar tipo de mudança | DDL (schema) vs DML (dados) |
| R.12 | Para DDL: executar migration down | Executar script de reversão de migração |
| R.13 | Para casos críticos: restaurar snapshot | Restaurar snapshot RDS pré-mudança |
| R.14 | Validar integridade | Verificar consistência de dados pós-rollback |
| R.15 | Documentar dados afetados | Registrar intervalo de dados impactado |

### 8.3 Pós-Rollback

| # | Ação |
|---|---|
| PR.1 | Registrar rollback na GitHub Issue original |
| PR.2 | Documentar causa raiz da falha |
| PR.3 | Atualizar classificação de risco da mudança |
| PR.4 | Agendar revisão CAB para análise de falha |
| PR.5 | Criar novo RFC para re-implementação corrigida |

---

## 9. Template de Solicitação de Mudança (RFC)

O template abaixo deve ser utilizado ao abrir uma GitHub Issue para RFC:

### Template: `[RFC] Change Request`

```markdown
## Solicitação de Mudança (RFC)

| Campo | Valor |
|---|---|
| **RFC ID** | RFC-YYYY-NNN (preenchido automaticamente) |
| **Solicitante** | @username |
| **Data da solicitação** | YYYY-MM-DD |
| **Classificação** | [ ] Standard / [ ] Normal / [ ] Emergency |
| **Prioridade** | [ ] Baixa / [ ] Média / [ ] Alta / [ ] Crítica |
| **Sistemas afetados** | (ex: Face ID API, EKS, RDS, Terraform) |
| **Ambiente** | [ ] Dev / [ ] Staging / [ ] Production |

### Descrição da Mudança
<!-- Descreva a mudança proposta em detalhes -->

### Justificativa
<!-- Por que esta mudança é necessária? -->

### Impacto em Dados Biométricos (RESTRITOS)
- [ ] Esta mudança NÃO afeta fluxo de dados biométricos
- [ ] Esta mudança AFETA fluxo de dados biométricos — detalhes:
  <!-- Descreva o impacto em dados RESTRITOS -->

### Análise de Risco

| Aspecto | Avaliação |
|---|---|
| **Probabilidade de falha** | Baixa / Média / Alta |
| **Impacto em caso de falha** | Baixo / Médio / Alto / Crítico |
| **Impacto em confidencialidade** | Sim / Não — detalhes: |
| **Impacto em disponibilidade** | Sim / Não — detalhes: |
| **Impacto em integridade** | Sim / Não — detalhes: |

### Plano de Implementação
1. <!-- Passo 1 -->
2. <!-- Passo 2 -->
3. <!-- ... -->

### Plano de Rollback
<!-- Descreva como reverter esta mudança -->

### Plano de Teste
- [ ] Testes unitários
- [ ] Testes de integração
- [ ] Smoke tests em staging
- [ ] Verificação de scanning (Trivy/Snyk)

### Janela de Manutenção
- **Data/hora proposta:** YYYY-MM-DD HH:MM (UTC-3)
- **Duração estimada:** X minutos/horas
- **Downtime esperado:** Sim / Não

### Checklist de Aprovação
- [ ] RFC preenchido completamente
- [ ] Plano de rollback documentado
- [ ] Impacto em dados RESTRITOS avaliado
- [ ] Scans de segurança executados
- [ ] Testes em staging concluídos

### Controles ISO 27001 Relacionados
<!-- Liste os controles do Anexo A afetados -->
```

---

## 10. Registros e Evidências

### 10.1 Registros Obrigatórios

Todos os registros abaixo **devem** ser mantidos para fins de auditoria ISO 27001:

| Registro | Localização | Retenção | Responsável |
|---|---|---|---|
| RFC (GitHub Issue) | GitHub Issues — repo `TWYN-ISO27001` | Mínimo 3 anos | Change Requester |
| Aprovação (comentários/labels) | GitHub Issues + PR reviews | Mínimo 3 anos | Change Approver / CAB |
| Pull Request + Code Review | GitHub Pull Requests | Mínimo 3 anos | Change Requester |
| Pipeline CI/CD (logs) | GitHub Actions run logs | Mínimo 1 ano | Automático |
| Resultados de scanning | Trivy/Snyk reports nos CI logs | Mínimo 1 ano | Automático |
| Logs de deploy | CloudWatch + EKS audit logs | Mínimo 1 ano | Automático |
| Evidência de rollback | GitHub Issue + kubectl logs | Mínimo 3 anos | DevOps Lead |
| Ata de CAB (Normal changes) | Comentário na GitHub Issue | Mínimo 3 anos | Gestor SGSI |
| Post-mortem (emergências) | Documento vinculado à Issue | Mínimo 3 anos | CAB |

### 10.2 Rastreabilidade

A rastreabilidade completa é garantida pela cadeia:

```
GitHub Issue (RFC) ──▶ Branch ──▶ Pull Request ──▶ CI Pipeline ──▶ Deploy ──▶ Verificação ──▶ Issue Fechada
      │                                │                  │                         │
      └── Labels + Comentários         └── Code Review     └── Scan Results          └── Metrics
```

---

## 11. Indicadores de Desempenho (KPIs)

### 11.1 Métricas Obrigatórias

| KPI | Métrica | Meta | Frequência |
|---|---|---|---|
| **Taxa de sucesso de mudanças** | (Mudanças bem-sucedidas / Total) × 100 | ≥ 95% | Mensal |
| **% de mudanças de emergência** | (Emergências / Total) × 100 | ≤ 10% | Mensal |
| **Taxa de rollback** | (Rollbacks / Total de deploys) × 100 | ≤ 5% | Mensal |
| **Lead time médio** | Tempo entre RFC e deploy em produção | ≤ 5 dias (Normal) | Mensal |
| **Tempo médio de emergência** | Tempo entre detecção e deploy do hotfix | ≤ 4 horas | Por evento |
| **Conformidade do processo** | RFCs com todos os campos preenchidos | 100% | Trimestral |
| **Cobertura de scanning** | Deploys com Trivy/Snyk executados | 100% | Mensal |

### 11.2 Relatório Mensal

O DevOps Lead deve gerar relatório mensal contendo:

1. Total de mudanças por classificação (Standard/Normal/Emergency);
2. Taxa de sucesso e rollbacks;
3. Mudanças que afetaram dados RESTRITOS;
4. Vulnerabilidades detectadas nos scans;
5. Tempo médio de aprovação por tipo;
6. Lições aprendidas de incidentes;
7. Tendências e recomendações.

**Entrega:** Até o 5º dia útil do mês seguinte ao Gestor SGSI.

---

## 12. Integração com Controles ISO 27001:2022

| Controle Anexo A | Como Este SOP Atende |
|---|---|
| **A.8.32 — Change management** | Processo completo de gestão de mudanças com classificação, aprovação e rastreabilidade |
| **A.8.9 — Configuration management** | Atualização de CMDB/inventário na etapa de fechamento; IaC versionado em Git |
| **A.8.25 — Secure development lifecycle** | Scanning obrigatório (Trivy/Snyk), code review, testes em staging antes de produção |
| **A.8.27 — Secure system architecture** | Avaliação de impacto em segurança, revisão de network policies e IAM |
| **A.8.31 — Separation of environments** | Fluxo obrigatório Dev → Staging → Production em VPCs separadas |

---

## 13. Documentos Relacionados

| Documento | ID | Relação |
|---|---|---|
| Política de Segurança da Informação | SGSI-POLICY-001 | Política-mãe |
| Política de Classificação de Dados | SGSI-POLICY-002 | Classificação de dados RESTRITOS |
| SOP de Gestão de Incidentes | SGSI-SOP-XXX | Vinculado a mudanças de emergência |
| Inventário de Ativos | SGSI-ASSET-001 | Atualizado no fechamento de mudanças |
| Registro de Riscos | SGSI-RISK-001 | Referência para avaliação de impacto |

---

## 14. Treinamento e Conscientização

| Público | Conteúdo | Frequência |
|---|---|---|
| Todos os colaboradores | Visão geral do processo, como abrir RFC | Onboarding + anual |
| DevOps Team | Processo completo, rollback, emergências | Semestral |
| CAB Members | Critérios de avaliação, aprovação, conformidade | Semestral |

---

## 15. Exceções

Exceções a este procedimento **devem**:

1. Ser formalmente solicitadas ao Gestor SGSI;
2. Incluir justificativa documentada;
3. Definir controles compensatórios;
4. Ter prazo de validade definido (máximo 90 dias);
5. Ser registradas no registro de exceções do SGSI.

---

## 16. Histórico de Revisões

| Versão | Data | Autor | Descrição da Mudança |
|---|---|---|---|
| 1.0 | 2026-06-02 | Gestor SGSI | Versão inicial — criação do procedimento completo |
| — | — | — | *Próxima revisão programada: 2027-06-02* |

---

**Fim do Documento**

> **SGSI-SOP-002 v1.0** | Classificação: INTERNO | TWYN — Sistema de Gestão de Segurança da Informação
