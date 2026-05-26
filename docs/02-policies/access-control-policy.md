---
document_id: SGSI-POLICY-002
title: Access Control Policy - Política de Controle de Acesso
version: 1.0
date: 2026-05-26
iso_clause: "8.1"
annex_a_controls: "A.5.15, A.5.16, A.5.17, A.5.18"
classification: Internal
owner: Gestor SGSI
approved_by: CEO
next_review: 2026-12-31
---

# Access Control Policy

## 1. Document Control

| Field | Value |
|-------|-------|
| Document ID | SGSI-POLICY-002 |
| Version | 1.0 |
| Status | Draft |
| Classification | Internal |
| Owner | Gestor SGSI (Ricardo Esper) |
| Approved By | CEO (Pendente assinatura) |
| Date Created | 2026-05-26 |
| Next Review | 2026-12-31 (Anual) |
| ISO 27001:2022 Clause | 8.1 (Operational planning and control) |
| Annex A Controls | A.5.15, A.5.16, A.5.17, A.5.18 |

## 2. Purpose

Esta política define os requisitos de controle de acesso para proteger os ativos de informação da TWYN, garantindo que:
- Apenas usuários autorizados acessem recursos
- Princípio de **least privilege** seja aplicado
- Segregação de funções evite conflitos de interesse
- Acesso seja revogado imediatamente após término de vínculo

Aplica-se a:
- ✅ Todos os colaboradores TWYN (permanentes, temporários, estagiários)
- ✅ Consultores e terceiros com acesso a sistemas TWYN
- ✅ Todos os sistemas no escopo ISMS (Face ID Platform API, AWS, GitHub, etc.)

## 3. Policy Statements

### 3.1 Princípio de Least Privilege

**Regra**: Cada usuário recebe APENAS os privilégios mínimos necessários para executar suas funções.

**Implementação**:
- ✅ AWS IAM policies granulares (não usar `AdministratorAccess` sem justificativa)
- ✅ GitHub: membros recebem `Read` por padrão, `Write` apenas se necessário
- ✅ Databases: read-only por padrão para desenvolvedores
- ✅ Produção: acesso restrito ao DevOps Lead (+ Junior DevOps após onboarding)

**Exceções**:
- DevOps Lead: acesso admin AWS (justificado por função)
- Gestor SGSI: visibilidade completa para auditoria
- CEO: owner em repositórios sensíveis

### 3.2 Segregação de Funções (Separation of Duties)

**Regra**: Funções críticas devem requerer aprovação de múltiplas pessoas.

**Exemplos**:
- ✅ Deploy produção: Developer cria PR → DevOps aprova → Pipeline executa
- ✅ Mudanças IAM críticas: DevOps propõe → Gestor SGSI aprova
- ✅ Exclusão de dados: Solicitante → Aprovador → Executor
- ✅ Certificados SSL: Renovação automática + alerta para validação manual

**Proibido**:
- ❌ Mesma pessoa que desenvolve fazer deploy sem revisão
- ❌ Root account AWS usado para operações rotineiras
- ❌ Senhas de produção compartilhadas via Slack/email

### 3.3 Gestão de Identidades (Identity Management)

**Ciclo de Vida de Identidades**:

#### A) Provisioning (Criação de Contas)
**Quando**: Novo colaborador inicia (Day 1)
**Quem**: DevOps Lead (ou HR para ferramentas administrativas)
**Processo**:
1. HR notifica Gestor SGSI + DevOps Lead (SOP-001)
2. DevOps cria contas baseadas em template de função:
   - **Developer**: AWS IAM user (limited), GitHub (Write no repo específico), Slack
   - **DevOps**: AWS IAM user (admin), GitHub (Admin), Slack
   - **Gestor SGSI**: AWS IAM user (read-only amplo), GitHub (Maintain), Slack
3. MFA obrigatório ativado (não permite acesso sem MFA)
4. Credenciais temporárias enviadas via canal seguro
5. Force password change no primeiro login
6. Registrado em Asset Inventory (SGSI-ASSETS-001) e Competence Records (SGSI-COMP-001)

#### B) Access Review (Recertificação)
**Quando**: Trimestral (Q1: Janeiro, Q2: Abril, Q3: Julho, Q4: Outubro)
**Quem**: DevOps Lead executa → Gestor SGSI aprova
**Processo** (SOP-005):
1. Gerar relatório de todos os acessos (AWS IAM, GitHub, etc.)
2. Gestor SGSI revisa:
   - Identifica contas inativas >90 dias
   - Verifica se privilégios ainda são necessários
   - Confirma segregação de funções mantida
3. Ajustes executados (remover/reduzir privilégios)
4. Sign-off documentado para auditoria

#### C) De-provisioning (Desativação de Contas)
**Quando**: Colaborador sai (resignação, demissão, término de contrato)
**Quem**: DevOps Lead (executado imediatamente)
**Processo** (SOP-001):
1. Manager notifica HR → HR notifica Gestor SGSI + DevOps
2. **No último dia de trabalho (ou imediatamente se demissão)**:
   - ✅ Desabilitar AWS IAM user (disable console + keys)
   - ✅ Remover de GitHub org
   - ✅ Desabilitar Slack
   - ✅ Revogar VPN (se aplicável)
   - ✅ Desabilitar email (converter para shared mailbox se necessário)
3. **Rotação de segredos** (se colaborador tinha acesso a):
   - Passwords de databases
   - API keys compartilhadas
   - SSH keys de produção
4. Audit logs revisados (últimos 30 dias de atividade)
5. Atualizar Asset Inventory + RACI Matrix

**SLA**: Desativação em **<4 horas** após notificação (target: imediato)

### 3.4 Autenticação (Authentication)

#### A) Senhas
**Requisitos mínimos**:
- ✅ Comprimento: ≥14 caracteres
- ✅ Complexidade: letras (maiúsculas + minúsculas) + números + símbolos
- ✅ Não reutilizar últimas 5 senhas
- ✅ Rotação: Obrigatória a cada **90 dias** (AWS IAM enforced)
- ✅ Sem senhas óbvias: Validado via password strength checker

**Proibições**:
- ❌ Senhas compartilhadas entre usuários
- ❌ Senhas armazenadas em plain text (post-its, emails, docs)
- ❌ Senhas enviadas via Slack/WhatsApp
- ❌ Senhas default de vendor (ex: `admin/admin`)

**Password Managers**:
- ✅ Uso de password managers **obrigatório** (ex: 1Password, Bitwarden, LastPass)
- ✅ Organizacional para segredos compartilhados (ex: AWS Secrets Manager)

#### B) Multi-Factor Authentication (MFA)
**Obrigatoriedade**:
- ✅ AWS root account: **Hardware MFA** (YubiKey recomendado) - **BLOCKER crítico**
- ✅ AWS IAM users: **MFA virtual** (Google Authenticator, Authy) - **OBRIGATÓRIO**
- ✅ GitHub: MFA via app ou SMS - **OBRIGATÓRIO para org members**
- ✅ VPN: MFA via certificado + senha
- ✅ Acesso produção: Requerer re-autenticação com MFA

**Enforcement**:
- AWS IAM policy nega acesso se MFA não configurado
- GitHub org settings: require 2FA for all members
- Onboarding (Day 1): MFA setup **antes** de conceder qualquer acesso

**Exceções**: Nenhuma. MFA é **não-negociável**.

#### C) Session Management
- ✅ Timeout de inatividade: **15 minutos** (AWS Console, aplicações web)
- ✅ Re-autenticação para ações sensíveis: Deleção de recursos, mudanças IAM
- ✅ Logout automático ao fechar browser
- ✅ Não permitir múltiplas sessões simultâneas para usuários admin

### 3.5 Autorização (Authorization)

#### A) Role-Based Access Control (RBAC)
**Funções definidas**:

| Função | AWS IAM | GitHub | Produção DB | Justificativa |
|--------|---------|--------|-------------|---------------|
| **CEO** | Read-only (billing, high-level metrics) | Owner (repos sensíveis) | Nenhum | Oversight, assinatura de políticas |
| **Gestor SGSI** | Read-only amplo (auditoria) | Maintain (todos repos) | Read-only | Auditoria e compliance |
| **DevOps Lead** | Admin (infraestrutura) | Admin (repos infra) | Admin (emergências) | Responsável por infra |
| **Junior DevOps** | PowerUser (sem IAM/billing) | Write (repos infra) | Read-only | Backup do DevOps Lead |
| **Developer** | Limited (deploy via CI/CD) | Write (repos de código) | Read-only | Desenvolvimento |
| **External Auditor** | Read-only (logs, configs) | Read (docs ISO) | Nenhum | Auditoria externa |

**Mapeamento documentado em**: SGSI-RACI-001 (RACI Matrix)

#### B) AWS IAM Best Practices
- ✅ **No root account usage**: Root só para setup inicial + MFA + guardado em cofre
- ✅ **IAM users para humanos**: Cada pessoa tem IAM user próprio (não shared)
- ✅ **IAM roles para serviços**: EC2, Lambda, EKS usam roles (não access keys)
- ✅ **Inline policies proibidas**: Usar managed policies ou customer managed
- ✅ **Conditional access**: IP whitelisting para acesso produção (se viável)
- ✅ **CloudTrail enabled**: Audit log de todas as ações IAM

#### C) GitHub Access Control
- ✅ **Org-level**: Require 2FA, restrict repo creation
- ✅ **Repo-level**: Branch protection rules (main branch requer PR approval)
- ✅ **Team-based**: Criar teams (DevOps, Developers) e atribuir permissões
- ✅ **Outside collaborators**: Restricted access, revisão trimestral

### 3.6 Acesso Remoto

**Requisitos para trabalho remoto** (Control A.6.7):
- ✅ VPN obrigatória para acessar recursos internos (se aplicável)
- ✅ Laptop com full disk encryption (BitLocker, FileVault)
- ✅ Screen lock após 5 minutos de inatividade
- ✅ Antivirus atualizado
- ✅ Firewall habilitado
- ✅ Não usar WiFi público sem VPN
- ✅ Separação casa/trabalho: não usar laptop pessoal para trabalho

**Detalhes em**: SOP-003 (Remote Work Security)

### 3.7 Acesso Privilegiado

**Contas privilegiadas** (admin AWS, root DB, etc.):
- ✅ Uso monitorado via CloudTrail + alertas
- ✅ Justificativa obrigatória (ticket de mudança)
- ✅ Sessões gravadas (session manager)
- ✅ Revisão mensal de uso de privilégios elevados
- ✅ Break-glass procedures documentadas (emergências)

**Root Account AWS**:
- ✅ MFA hardware obrigatório (GAP-001)
- ✅ Senha guardada em cofre físico (CEO office)
- ✅ Uso apenas para operações que REQUEREM root (billing, account closure)
- ✅ Alerta imediato se root faz login (SNS → email Gestor SGSI)

### 3.8 Acesso de Terceiros

**Consultores / Vendors**:
- ✅ Princípio de least privilege
- ✅ Contas temporárias (expiram após projeto)
- ✅ MFA obrigatória
- ✅ NDA assinado antes de conceder acesso
- ✅ Audit trail revisado após término de contrato
- ✅ Acesso revogado imediatamente ao final do contrato

**Exemplo**: Auditor ISO 27001 recebe acesso read-only a repos de documentação + logs AWS (via temporary credentials)

### 3.9 Access Keys e Tokens

**AWS Access Keys**:
- ✅ Rotação **obrigatória a cada 90 dias** (GAP-002 - tmpsaasboost key >90 dias)
- ✅ Não hardcoded em código (usar AWS Secrets Manager ou environment variables)
- ✅ Keys inativas >90 dias são desabilitadas automaticamente (AWS Config rule)
- ✅ Keys nunca commitadas em Git (pre-commit hook detecta)

**GitHub Personal Access Tokens (PATs)**:
- ✅ Expiration obrigatório (máximo 90 dias)
- ✅ Fine-grained tokens preferidos (não classic)
- ✅ Escopo mínimo necessário
- ✅ Revogação imediata se comprometido

**API Keys**:
- ✅ Armazenadas em AWS Secrets Manager (não em .env files)
- ✅ Rotação automática quando possível
- ✅ Rate limiting e IP whitelisting quando disponível

**Detalhes em**: SOP-004 (Secrets Management)

## 4. Exceptions

**Processo de Exceção**:
1. Solicitante preenche formulário de exceção (justificativa de negócio)
2. Gestor SGSI + DevOps Lead avaliam risco
3. CEO aprova (se risco MEDIUM ou HIGH)
4. Exceção válida por **máximo 90 dias** (revisão obrigatória)
5. Compensating controls implementados (ex: monitoramento adicional)
6. Documentado em registro de exceções

**Exemplos de exceções legítimas**:
- Consultor externo precisa acesso admin temporário (projeto de migração crítica)
- Demo para cliente requer relaxamento temporário de IP whitelist
- Incident response requer bypass de segregação de funções (emergência)

**Nunca permitido mesmo com exceção**:
- ❌ Desabilitar MFA
- ❌ Compartilhar credenciais entre usuários
- ❌ Root account sem MFA

## 5. Monitoring and Compliance

### 5.1 Audit Logging
**Eventos logados** (Control A.8.15):
- ✅ Login/logout (sucesso e falhas)
- ✅ Mudanças de permissões IAM
- ✅ Acesso a dados sensíveis (S3 biométricos)
- ✅ Tentativas de acesso negado
- ✅ Elevação de privilégios

**Logs armazenados**:
- AWS CloudTrail: 1 ano
- AWS Config: 7 anos (compliance)
- Application logs: 90 dias

**Revisão de logs**:
- Mensal: Gestor SGSI revisa acessos anômalos
- Trimestral: Revisão completa de access patterns
- Imediata: Alertas em tempo real para eventos críticos (root login, failed MFA)

### 5.2 Automated Enforcement
- ✅ AWS Config rules: Enforce MFA, detect non-compliant IAM policies
- ✅ GitHub branch protection: Force code review
- ✅ Pre-commit hooks: Detect secrets in código
- ✅ AWS GuardDuty: Detect compromised credentials

### 5.3 Compliance Checks
**Trimestral** (SOP-005 - IAM Recertification):
- [ ] Audit all IAM users (active/inactive)
- [ ] Review permissions (over-privileged?)
- [ ] Validate MFA enabled (100%)
- [ ] Check access keys age (<90 days)
- [ ] Confirm segregation of duties

**Anual** (Internal Audit - SGSI-AUDIT-001):
- [ ] Test access controls (penetration testing)
- [ ] Review all exceptions granted
- [ ] Validate offboarding complete (ex-employees)
- [ ] Assess effectiveness of RBAC model

## 6. Roles and Responsibilities

| Role | Responsibility |
|------|----------------|
| **CEO** | Aprovar política, aprovar exceções HIGH risk |
| **Gestor SGSI** | Ownership da política, auditoria de compliance, aprovar exceções MEDIUM |
| **DevOps Lead** | Implementação técnica, provisioning/de-provisioning, access reviews |
| **HR** | Notificar onboarding/offboarding, background checks |
| **All Users** | Proteger credenciais, reportar incidentes, seguir política |

**RACI detalhado em**: SGSI-RACI-001

## 7. Related Documents

- **SGSI-POLICY-001**: Information Security Policy (policy framework)
- **SGSI-RACI-001**: RACI Matrix (roles & responsibilities)
- **SGSI-ASSETS-001**: Asset Inventory (contas IAM, grupos, roles)
- **SOP-001**: Onboarding/Offboarding (provisioning/de-provisioning)
- **SOP-004**: Secrets Management (gestão de keys/tokens)
- **SOP-005**: IAM Recertification (access review trimestral)
- **GAP-001**: MFA Root Account (implementação)
- **GAP-002**: IAM Key Rotation (implementação)

## 8. Non-Compliance

**Consequências**:
- **Menor**: Warning verbal + re-training
- **Moderada**: Warning escrito + revisão de acesso
- **Grave**: Suspensão de acesso + processo disciplinar
- **Crítica**: Demissão por justa causa (ex: compartilhar credenciais intencionalmente)

**Exemplos de violações**:
- 🟡 Menor: Esquecer de fazer logout (uma vez)
- 🟠 Moderada: Compartilhar senha com colega (mesmo time)
- 🔴 Grave: Usar root account sem justificativa
- ⚫ Crítica: Exfiltrar dados usando credenciais roubadas

## 9. Review and Updates

- **Frequency**: Anual (ou quando mudanças significativas em tecnologia/riscos)
- **Owner**: Gestor SGSI
- **Approver**: CEO
- **Next Review**: 2026-12-31

**Triggers para revisão ad-hoc**:
- Incidente de segurança relacionado a access control
- Mudanças em regulamentações (LGPD, ISO 27001)
- Novos sistemas/tecnologias adotadas (ex: migração cloud)
- Audit findings requerem ajustes na política

## 10. Approval

| Field | Value |
|-------|-------|
| **Prepared By** | Security Consultant (Bekaa) |
| **Reviewed By** | Gestor SGSI (Ricardo Esper) - Pendente |
| **Approved By** | CEO - Pendente assinatura |
| **Approval Date** | Pendente |
| **Effective Date** | Após aprovação CEO |
| **Distribution** | Todos os colaboradores (via email + onboarding) |

---

## 11. Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-05-26 | Security Consultant | Versão inicial - Access Control Policy detalhada cobrindo identity management, authentication, authorization, privileged access, remote access, monitoring e compliance |

---

**⚠️ AÇÃO OBRIGATÓRIA**: Esta política requer aprovação formal do CEO e deve ser comunicada a todos os colaboradores. Não-conformidade pode resultar em ação disciplinar.
