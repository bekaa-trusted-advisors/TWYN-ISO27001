---
document_id: SGSI-SOP-005
title: "Procedimento Operacional Padrão — Recertificação de Identidades e Acessos (IAM)"
version: "1.0"
status: Draft
classification: INTERNAL
owner: Gestor SGSI
approved_by: ""
approval_date: ""
effective_date: ""
next_review: ""
related_policies:
  - SGSI-POLICY-002  # Política de Controle de Acesso
related_controls:
  - A.5.15  # Controle de acesso
  - A.5.16  # Gestão de identidades
  - A.5.17  # Informações de autenticação
  - A.5.18  # Direitos de acesso
  - A.8.2   # Acesso privilegiado
  - A.8.3   # Restrição de acesso à informação
---

# SGSI-SOP-005 — Recertificação de Identidades e Acessos (IAM)

## 1. Objetivo

Este Procedimento Operacional Padrão (SOP) estabelece o processo formal e auditável de **recertificação periódica de identidades e acessos** em todos os ambientes tecnológicos da TWYN, incluindo:

- **AWS Account** (ID: `992382542028`)
- **GitHub** (organização TWYN)
- **Kubernetes (EKS)** — RBAC de clusters

O objetivo é garantir que:

1. Todos os acessos estejam alinhados à **matriz RBAC aprovada** e ao princípio do menor privilégio.
2. Contas **órfãs, inativas ou com permissões excessivas** sejam identificadas e remediadas tempestivamente.
3. A conformidade com os controles do **Anexo A da ISO 27001:2022** (A.5.15 a A.5.18, A.8.2, A.8.3) seja evidenciada.
4. Registros de auditoria sejam mantidos para demonstração a auditores internos e externos.

---

## 2. Escopo

| Dimensão           | Cobertura                                                                                     |
| ------------------- | --------------------------------------------------------------------------------------------- |
| **Organização**     | TWYN (~10 colaboradores)                                                                      |
| **Conta AWS**       | `992382542028` — todos os usuários IAM, roles, policies e access keys                         |
| **GitHub**          | Organização TWYN — membros, repositórios, permissões de equipe                                |
| **Kubernetes**      | Clusters EKS — ClusterRoleBindings, RoleBindings, ServiceAccounts                             |
| **Conta Root AWS**  | Verificação de conformidade break-glass (não recertificação regular de uso)                    |
| **Exclusões**       | Contas de serviço gerenciadas automaticamente pelo AWS (e.g., service-linked roles do próprio AWS) |

### 2.1 Papéis RBAC Definidos

| Papel              | Permissões AWS                                   | MFA         | Observações                          |
| ------------------- | ------------------------------------------------ | ----------- | ------------------------------------ |
| CEO                 | Console read-only (`ReadOnlyAccess`)             | Obrigatório | Apenas visualização                  |
| Gestor SGSI         | `SecurityAudit` (read-only)                      | Obrigatório | Responsável por auditorias           |
| DevOps Lead         | `AdministratorAccess`                            | Hardware MFA | Acesso administrativo completo       |
| Junior DevOps       | `PowerUserAccess` (escopo limitado)              | Obrigatório | Sem IAM admin                        |
| Developer           | EKS + ECR + CloudWatch (limitado)                | Obrigatório | Acesso restrito a workloads          |
| External Auditor    | `SecurityAudit` (time-boxed 30 dias)             | Obrigatório | Acesso temporário, renovação manual  |

---

## 3. Definições e Siglas

| Termo / Sigla       | Definição                                                                              |
| -------------------- | -------------------------------------------------------------------------------------- |
| **IAM**              | Identity and Access Management — gerenciamento de identidades e acessos na AWS         |
| **RBAC**             | Role-Based Access Control — controle de acesso baseado em papéis                       |
| **MFA**              | Multi-Factor Authentication — autenticação multifator                                  |
| **SGSI**             | Sistema de Gestão da Segurança da Informação                                           |
| **Break-glass**      | Procedimento de acesso emergencial à conta root                                        |
| **Conta órfã**       | Conta de usuário sem titular ativo identificado (ex.: `tmpsaasboost`)                  |
| **Access Key**       | Par de credenciais programáticas (Access Key ID + Secret Access Key)                   |
| **Recertificação**   | Processo de revalidação formal de que os acessos concedidos permanecem justificados    |

---

## 4. Responsabilidades

| Papel               | Responsabilidade                                                                        |
| -------------------- | --------------------------------------------------------------------------------------- |
| **Gestor SGSI**      | Iniciar, coordenar e aprovar o ciclo de recertificação; manter evidências               |
| **DevOps Lead**      | Executar comandos de coleta, implementar remediações técnicas, co-aprovar relatório      |
| **CEO**              | Aprovar exceções de acesso privilegiado quando escalado                                  |
| **Todos os usuários**| Validar a necessidade contínua de seus próprios acessos quando solicitado                |
| **Auditor Externo**  | Revisar evidências durante auditorias de certificação/recertificação ISO 27001           |

---

## 5. Frequência e Gatilhos

### 5.1 Ciclo Regular — Trimestral

A recertificação completa é executada **a cada trimestre**, nos seguintes meses:

| Ciclo | Meses de Execução | Prazo para Conclusão |
| ----- | ------------------ | -------------------- |
| Q1    | Janeiro            | Até 31 de Janeiro    |
| Q2    | Abril              | Até 30 de Abril      |
| Q3    | Julho              | Até 31 de Julho      |
| Q4    | Outubro            | Até 31 de Outubro    |

### 5.2 Gatilhos Extraordinários

Além do ciclo trimestral, a recertificação **deve ser iniciada imediatamente** quando:

| Gatilho                                  | SLA de Início       | Responsável        |
| ---------------------------------------- | -------------------- | ------------------ |
| Mudança de função/papel de colaborador   | 24 horas             | Gestor SGSI        |
| Desligamento de colaborador              | **< 4 horas**        | DevOps Lead        |
| Término de projeto com acessos dedicados | 48 horas             | Gestor SGSI        |
| Incidente de segurança envolvendo IAM    | Imediato             | DevOps Lead        |
| Término de contrato de auditor externo   | Dia do término       | Gestor SGSI        |
| Detecção de conta órfã ou anômala        | 24 horas             | DevOps Lead        |

> **SLA Crítico:** Para desligamentos, o de-provisioning completo (AWS + GitHub + Kubernetes) deve ocorrer em **menos de 4 horas** a partir da notificação formal.

---

## 6. Procedimento Detalhado de Recertificação Trimestral

### Pré-requisitos

- Acesso ao AWS CLI configurado com credenciais do perfil `gestor-sgsi` ou `devops-lead`.
- Acesso ao GitHub CLI (`gh`) autenticado na organização TWYN.
- Acesso ao `kubectl` configurado para os clusters EKS.
- Cópia atualizada da **Matriz RBAC Aprovada** (SGSI-POLICY-002, Anexo A).

---

### ETAPA 1 — Gerar Relatório de Credenciais AWS IAM

**Responsável:** DevOps Lead  
**Controles:** A.5.16, A.5.17

Gerar e baixar o relatório de credenciais do IAM para análise completa de todos os usuários.

```bash
# 1.1 — Solicitar geração do relatório de credenciais
aws iam generate-credential-report

# 1.2 — Aguardar conclusão (pode levar alguns segundos)
aws iam generate-credential-report --query 'State' --output text

# 1.3 — Baixar o relatório em formato CSV
aws iam get-credential-report \
  --query 'Content' \
  --output text | base64 --decode > credential-report-$(date +%Y-%m-%d).csv

# 1.4 — Verificar o conteúdo do relatório
head -5 credential-report-$(date +%Y-%m-%d).csv
```

**Saída esperada:** Arquivo CSV com colunas incluindo `user`, `arn`, `user_creation_time`, `password_enabled`, `password_last_used`, `mfa_active`, `access_key_1_active`, `access_key_1_last_rotated`, `access_key_1_last_used_date`, entre outras.

**Evidência:** Arquivo `credential-report-YYYY-MM-DD.csv` salvo no repositório de evidências.

---

### ETAPA 2 — Listar Todos os Usuários, Roles e Permissões IAM

**Responsável:** DevOps Lead  
**Controles:** A.5.15, A.5.18

```bash
# 2.1 — Listar todos os usuários IAM
aws iam list-users \
  --query 'Users[*].[UserName,UserId,CreateDate,PasswordLastUsed]' \
  --output table

# 2.2 — Para CADA usuário, listar grupos e políticas anexadas
for user in $(aws iam list-users --query 'Users[*].UserName' --output text); do
  echo "============================================"
  echo "USUÁRIO: $user"
  echo "--------------------------------------------"
  echo "Grupos:"
  aws iam list-groups-for-user --user-name "$user" \
    --query 'Groups[*].GroupName' --output text
  echo "Políticas anexadas diretamente:"
  aws iam list-attached-user-policies --user-name "$user" \
    --query 'AttachedPolicies[*].PolicyName' --output text
  echo "Políticas inline:"
  aws iam list-user-policies --user-name "$user" \
    --query 'PolicyNames' --output text
  echo "Access Keys:"
  aws iam list-access-keys --user-name "$user" \
    --query 'AccessKeyMetadata[*].[AccessKeyId,Status,CreateDate]' --output table
  echo "MFA Devices:"
  aws iam list-mfa-devices --user-name "$user" \
    --query 'MFADevices[*].SerialNumber' --output text
  echo ""
done

# 2.3 — Listar todas as IAM Roles
aws iam list-roles \
  --query 'Roles[*].[RoleName,Arn,CreateDate]' \
  --output table

# 2.4 — Listar todas as IAM Policies customizadas (não-AWS)
aws iam list-policies --scope Local \
  --query 'Policies[*].[PolicyName,Arn,AttachmentCount,CreateDate]' \
  --output table
```

**Evidência:** Saídas salvas em `iam-users-audit-YYYY-MM-DD.txt`.

---

### ETAPA 3 — Comparar com a Matriz RBAC Aprovada

**Responsável:** Gestor SGSI + DevOps Lead  
**Controles:** A.5.15, A.8.3

1. Abrir a **Matriz RBAC Aprovada** (documento SGSI-POLICY-002, Anexo A).
2. Para cada usuário listado na Etapa 2, verificar:
   - O usuário **consta na matriz RBAC** como ativo?
   - O **papel atribuído** (CEO, DevOps Lead, etc.) corresponde ao registrado na matriz?
   - As **permissões efetivas** (grupos, policies) são **exatamente** as definidas para o papel?
   - Não há **policies adicionais** fora do escopo do papel?
3. Documentar em tabela:

| Usuário IAM      | Papel Esperado  | Papel Efetivo   | Conforme? | Observação               |
| ----------------- | --------------- | --------------- | --------- | ------------------------ |
| `joao.silva`      | DevOps Lead     | DevOps Lead     | ✅ Sim    |                          |
| `tmpsaasboost`    | —               | —               | ❌ Não    | Conta órfã — sem titular |

---

### ETAPA 4 — Identificar Anomalias

**Responsável:** Gestor SGSI + DevOps Lead  
**Controles:** A.5.16, A.5.18, A.8.2

#### 4.1 — Contas Órfãs (sem titular ativo)

```bash
# Identificar usuários que não estão na lista de colaboradores ativos
# Comparar saída da Etapa 2 com a lista de RH/matriz RBAC
# CONHECIDO: tmpsaasboost — conta órfã identificada para remoção
```

#### 4.2 — Usuários Inativos (> 90 dias sem login)

```bash
# Filtrar usuários com password_last_used > 90 dias ou nunca utilizado
aws iam get-credential-report \
  --query 'Content' \
  --output text | base64 --decode | \
  awk -F',' 'NR>1 {
    if ($5 == "true" && ($6 == "no_information" || $6 == "N/A"))
      print "NUNCA FEZ LOGIN: "$1;
  }'

# Verificar último uso de access keys
for user in $(aws iam list-users --query 'Users[*].UserName' --output text); do
  aws iam get-access-key-last-used \
    --access-key-id $(aws iam list-access-keys --user-name "$user" \
      --query 'AccessKeyMetadata[0].AccessKeyId' --output text 2>/dev/null) \
    2>/dev/null | \
    jq -r --arg u "$user" '"\($u): último uso em \(.AccessKeyLastUsed.LastUsedDate // "NUNCA")"'
done
```

#### 4.3 — Access Keys com mais de 90 dias sem rotação

```bash
# Identificar access keys criadas há mais de 90 dias
THRESHOLD=$(date -d "-90 days" +%Y-%m-%dT%H:%M:%S 2>/dev/null || date -v-90d +%Y-%m-%dT%H:%M:%S)

for user in $(aws iam list-users --query 'Users[*].UserName' --output text); do
  aws iam list-access-keys --user-name "$user" \
    --query "AccessKeyMetadata[?CreateDate<='$THRESHOLD'].[UserName,AccessKeyId,CreateDate,Status]" \
    --output table
done
```

#### 4.4 — Usuários sem MFA ativado

```bash
# CRÍTICO: MFA é obrigatório para TODOS os usuários, sem exceção
for user in $(aws iam list-users --query 'Users[*].UserName' --output text); do
  MFA_COUNT=$(aws iam list-mfa-devices --user-name "$user" \
    --query 'length(MFADevices)' --output text)
  if [ "$MFA_COUNT" -eq "0" ]; then
    echo "⚠️  ALERTA CRÍTICO: Usuário SEM MFA: $user"
  fi
done
```

#### 4.5 — Permissões Excessivas (policies fora do papel)

```bash
# Verificar se algum usuário possui AdministratorAccess sem ser DevOps Lead
for user in $(aws iam list-users --query 'Users[*].UserName' --output text); do
  POLICIES=$(aws iam list-attached-user-policies --user-name "$user" \
    --query 'AttachedPolicies[*].PolicyName' --output text)
  if echo "$POLICIES" | grep -q "AdministratorAccess"; then
    echo "🔴 ADMIN ACCESS: $user — Verificar se é DevOps Lead autorizado"
  fi
done
```

#### 4.6 — Verificar Conta Root

```bash
# Verificar status da conta root (deve ter MFA hardware e NÃO deve ter access keys)
aws iam get-credential-report \
  --query 'Content' \
  --output text | base64 --decode | \
  head -2 | tail -1 | \
  awk -F',' '{
    print "Root - MFA ativo: "$8;
    print "Root - Access Key 1 ativa: "$9;
    print "Root - Access Key 2 ativa: "$14;
  }'

# ESPERADO: MFA ativo = true, Access Keys = false
# Root deve ser break-glass APENAS, com hardware MFA guardado em cofre físico
```

**Evidência:** Relatório de anomalias salvo em `anomalias-iam-YYYY-MM-DD.md`.

---

### ETAPA 5 — Revisar Membros e Permissões do GitHub

**Responsável:** DevOps Lead  
**Controles:** A.5.15, A.5.18

```bash
# 5.1 — Listar todos os membros da organização GitHub
gh api orgs/TWYN/members --paginate \
  --jq '.[] | [.login, .site_admin] | @tsv'

# 5.2 — Listar colaboradores externos (outside collaborators)
gh api orgs/TWYN/outside_collaborators --paginate \
  --jq '.[] | [.login] | @tsv'

# 5.3 — Para cada repositório, listar permissões de equipe
for repo in $(gh repo list TWYN --json name --jq '.[].name'); do
  echo "============================================"
  echo "REPOSITÓRIO: $repo"
  gh api "repos/TWYN/$repo/teams" --jq '.[] | [.name, .permission] | @tsv' 2>/dev/null
  echo "Colaboradores diretos:"
  gh api "repos/TWYN/$repo/collaborators" \
    --jq '.[] | [.login, .role_name] | @tsv' 2>/dev/null
  echo ""
done

# 5.4 — Verificar convites pendentes
gh api orgs/TWYN/invitations --jq '.[] | [.login, .role, .created_at] | @tsv' 2>/dev/null

# 5.5 — Comparar com lista de colaboradores ativos
# Membros do GitHub que NÃO constam na matriz RBAC devem ser removidos
```

**Ação:** Comparar a lista de membros do GitHub com a lista de colaboradores ativos da TWYN. Membros que não forem colaboradores ativos devem ser removidos imediatamente.

**Evidência:** Saídas salvas em `github-audit-YYYY-MM-DD.txt`.

---

### ETAPA 6 — Revisar RBAC do Kubernetes (EKS)

**Responsável:** DevOps Lead  
**Controles:** A.5.15, A.8.2, A.8.3

```bash
# 6.1 — Listar todos os ClusterRoleBindings
kubectl get clusterrolebindings -o wide

# 6.2 — Detalhar ClusterRoleBindings que concedem cluster-admin
kubectl get clusterrolebindings -o json | \
  jq -r '.items[] | select(.roleRef.name == "cluster-admin") |
    "CRB: \(.metadata.name) -> Subjects: \([.subjects[]? | "\(.kind):\(.name)"] | join(", "))"'

# 6.3 — Listar todos os RoleBindings em todos os namespaces
kubectl get rolebindings --all-namespaces -o wide

# 6.4 — Listar ServiceAccounts com tokens ativos
kubectl get serviceaccounts --all-namespaces \
  -o custom-columns=NAMESPACE:.metadata.namespace,NAME:.metadata.name,SECRETS:.secrets[*].name

# 6.5 — Verificar aws-auth ConfigMap (mapeamento IAM -> K8s)
kubectl get configmap aws-auth -n kube-system -o yaml

# 6.6 — Identificar bindings para usuários/grupos que não são mais ativos
# Comparar subjects dos bindings com a matriz RBAC
```

**Ação:** Verificar que:
- Apenas o DevOps Lead possui `cluster-admin`.
- Developers possuem acesso limitado aos namespaces de workload.
- Não há ServiceAccounts com tokens órfãos.
- O ConfigMap `aws-auth` reflete apenas os usuários/roles ativos.

**Evidência:** Saídas salvas em `k8s-rbac-audit-YYYY-MM-DD.txt`.

---

### ETAPA 7 — Documentar Resultados no Relatório de Recertificação

**Responsável:** Gestor SGSI  
**Controles:** A.5.15, A.5.16

Consolidar todas as informações coletadas nas Etapas 1–6 em um **Relatório de Recertificação** formal, seguindo o template abaixo:

```
RELATÓRIO DE RECERTIFICAÇÃO IAM — Qn/AAAA
===========================================

Data da recertificação: DD/MM/AAAA
Executado por: [Nome do DevOps Lead]
Revisado por: [Nome do Gestor SGSI]

1. RESUMO EXECUTIVO
   - Total de usuários IAM: XX
   - Total de usuários ativos: XX
   - Anomalias identificadas: XX
   - Remediações necessárias: XX

2. CONTAS AWS IAM
   [Tabela com todos os usuários e status de conformidade]

3. GITHUB
   [Lista de membros e conformidade]

4. KUBERNETES
   [ClusterRoleBindings e RoleBindings auditados]

5. ANOMALIAS E NÃO-CONFORMIDADES
   [Detalhamento de cada anomalia com classificação de risco]

6. PLANO DE REMEDIAÇÃO
   [Ações corretivas, responsáveis e prazos]

7. SIGN-OFF
   [Assinaturas — ver Etapa 9]
```

**Evidência:** Relatório completo salvo em `recertificacao-iam-Qn-AAAA.md`.

---

### ETAPA 8 — Remediação

**Responsável:** DevOps Lead (execução) + Gestor SGSI (aprovação)  
**Controles:** A.5.18, A.8.2

#### 8.1 — Remover Contas Órfãs

```bash
# Exemplo: Remover conta órfã tmpsaasboost
# 8.1.1 — Listar e remover access keys
aws iam list-access-keys --user-name tmpsaasboost \
  --query 'AccessKeyMetadata[*].AccessKeyId' --output text | \
  xargs -I {} aws iam delete-access-key --user-name tmpsaasboost --access-key-id {}

# 8.1.2 — Remover login profile (console access)
aws iam delete-login-profile --user-name tmpsaasboost 2>/dev/null

# 8.1.3 — Desanexar todas as policies
for policy_arn in $(aws iam list-attached-user-policies --user-name tmpsaasboost \
  --query 'AttachedPolicies[*].PolicyArn' --output text); do
  aws iam detach-user-policy --user-name tmpsaasboost --policy-arn "$policy_arn"
done

# 8.1.4 — Remover de todos os grupos
for group in $(aws iam list-groups-for-user --user-name tmpsaasboost \
  --query 'Groups[*].GroupName' --output text); do
  aws iam remove-user-from-group --user-name tmpsaasboost --group-name "$group"
done

# 8.1.5 — Deletar políticas inline
for policy in $(aws iam list-user-policies --user-name tmpsaasboost \
  --query 'PolicyNames' --output text); do
  aws iam delete-user-policy --user-name tmpsaasboost --policy-name "$policy"
done

# 8.1.6 — Remover MFA devices
for mfa in $(aws iam list-mfa-devices --user-name tmpsaasboost \
  --query 'MFADevices[*].SerialNumber' --output text); do
  aws iam deactivate-mfa-device --user-name tmpsaasboost --serial-number "$mfa"
  aws iam delete-virtual-mfa-device --serial-number "$mfa" 2>/dev/null
done

# 8.1.7 — Deletar o usuário
aws iam delete-user --user-name tmpsaasboost

echo "✅ Conta órfã tmpsaasboost removida com sucesso"
```

#### 8.2 — Reduzir Permissões Excessivas

```bash
# Exemplo: Remover AdministratorAccess de usuário que não é DevOps Lead
aws iam detach-user-policy \
  --user-name <USUARIO> \
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess

# Anexar a policy correta conforme o papel do usuário
aws iam attach-user-policy \
  --user-name <USUARIO> \
  --policy-arn arn:aws:iam::aws:policy/<POLICY_CORRETA>
```

#### 8.3 — Rotacionar Access Keys com mais de 90 dias

```bash
# 8.3.1 — Criar nova access key
aws iam create-access-key --user-name <USUARIO>

# 8.3.2 — Comunicar o usuário para atualizar suas configurações

# 8.3.3 — Após confirmação do usuário, desativar a key antiga
aws iam update-access-key \
  --user-name <USUARIO> \
  --access-key-id <KEY_ANTIGA> \
  --status Inactive

# 8.3.4 — Após período de observação (7 dias), deletar a key antiga
aws iam delete-access-key \
  --user-name <USUARIO> \
  --access-key-id <KEY_ANTIGA>
```

#### 8.4 — Habilitar MFA para Usuários sem MFA

```bash
# Notificar o usuário e acompanhar a ativação
# Se após 24 horas o MFA não for ativado, desativar o console access:
aws iam delete-login-profile --user-name <USUARIO>
# E notificar o Gestor SGSI para ação administrativa
```

#### 8.5 — Remover Acesso de Auditor Expirado

```bash
# Verificar se o acesso do auditor externo excedeu 30 dias
# Se sim, remover completamente seguindo o procedimento da Seção 8.1
```

#### 8.6 — Remediação GitHub

```bash
# Remover membro que não é mais colaborador ativo
gh api -X DELETE "orgs/TWYN/members/<USERNAME>"

# Ajustar permissões de repositório
gh api -X PUT "orgs/TWYN/teams/<TEAM>/repos/TWYN/<REPO>" \
  -f permission="pull"  # Ajustar conforme papel
```

#### 8.7 — Remediação Kubernetes

```bash
# Remover ClusterRoleBinding indevido
kubectl delete clusterrolebinding <NOME_DO_BINDING>

# Remover RoleBinding de namespace específico
kubectl delete rolebinding <NOME_DO_BINDING> -n <NAMESPACE>

# Atualizar aws-auth ConfigMap se necessário
kubectl edit configmap aws-auth -n kube-system
```

**Evidência:** Log de todas as ações de remediação com timestamps salvo em `remediacao-iam-Qn-AAAA.log`.

---

### ETAPA 9 — Sign-off Formal

**Responsável:** Gestor SGSI + DevOps Lead  
**Controles:** A.5.15

O relatório de recertificação deve ser formalmente aprovado por ambos:

| Campo                     | Valor                                    |
| ------------------------- | ---------------------------------------- |
| **Gestor SGSI**           |                                          |
| Nome:                     | _________________________________________ |
| Data:                     | ___/___/______                           |
| Assinatura:               | _________________________________________ |
| Resultado:                | ☐ Aprovado ☐ Aprovado com ressalvas ☐ Reprovado |
|                           |                                          |
| **DevOps Lead**           |                                          |
| Nome:                     | _________________________________________ |
| Data:                     | ___/___/______                           |
| Assinatura:               | _________________________________________ |
| Resultado:                | ☐ Aprovado ☐ Aprovado com ressalvas ☐ Reprovado |

> **Nota:** Se o resultado for "Aprovado com ressalvas", as ressalvas devem ser documentadas com prazo de resolução e acompanhadas no próximo ciclo.

> **Nota:** Se o resultado for "Reprovado", a recertificação deve ser refeita em até 5 dias úteis.

---

## 7. Checklist de Recertificação

O checklist abaixo deve ser preenchido pelo Gestor SGSI a cada ciclo trimestral:

| #  | Item de Verificação                                                        | Sim | Não | N/A | Observação |
| -- | -------------------------------------------------------------------------- | --- | --- | --- | ---------- |
| 1  | Relatório de credenciais AWS gerado e analisado                            | ☐   | ☐   | ☐   |            |
| 2  | Todos os usuários IAM listados e permissões documentadas                   | ☐   | ☐   | ☐   |            |
| 3  | Comparação com a matriz RBAC aprovada realizada                            | ☐   | ☐   | ☐   |            |
| 4  | Nenhuma conta órfã presente (ou remediação documentada)                    | ☐   | ☐   | ☐   |            |
| 5  | Nenhum usuário inativo > 90 dias (ou remediação documentada)               | ☐   | ☐   | ☐   |            |
| 6  | Todas as access keys rotacionadas (idade < 90 dias)                        | ☐   | ☐   | ☐   |            |
| 7  | MFA ativado para 100% dos usuários IAM                                     | ☐   | ☐   | ☐   |            |
| 8  | Conta root: sem access keys, com hardware MFA, sem uso regular             | ☐   | ☐   | ☐   |            |
| 9  | Nenhuma permissão excessiva identificada (ou remediação documentada)        | ☐   | ☐   | ☐   |            |
| 10 | Membros do GitHub verificados contra lista de colaboradores ativos          | ☐   | ☐   | ☐   |            |
| 11 | Colaboradores externos do GitHub verificados (convites pendentes inclusos)  | ☐   | ☐   | ☐   |            |
| 12 | ClusterRoleBindings do Kubernetes auditados                                | ☐   | ☐   | ☐   |            |
| 13 | RoleBindings de namespaces do Kubernetes auditados                         | ☐   | ☐   | ☐   |            |
| 14 | ConfigMap aws-auth verificado contra usuários ativos                        | ☐   | ☐   | ☐   |            |
| 15 | Acessos de auditores externos dentro do prazo de 30 dias                   | ☐   | ☐   | ☐   |            |
| 16 | Relatório de recertificação documentado                                    | ☐   | ☐   | ☐   |            |
| 17 | Todas as remediações executadas e registradas                              | ☐   | ☐   | ☐   |            |
| 18 | Sign-off obtido do Gestor SGSI e DevOps Lead                              | ☐   | ☐   | ☐   |            |

---

## 8. Procedimento de Escalação e Exceções

### 8.1 Acesso Temporário Elevado

Em situações operacionais que exijam acesso temporário acima do previsto no papel RBAC:

1. O solicitante registra um **pedido formal** contendo: justificativa, escopo de acesso, duração estimada.
2. O **Gestor SGSI** avalia o pedido e, se de acordo, encaminha para aprovação.
3. Se o acesso solicitado for de nível **AdministratorAccess** ou equivalente:
   - Aprovação adicional do **CEO** é obrigatória.
4. O **DevOps Lead** implementa o acesso com:
   - **Tag de expiração** na policy ou no usuário (chave: `ExpirationDate`, valor: `YYYY-MM-DD`).
   - **CloudTrail** com alerta configurado para as ações do usuário durante o período.
5. Ao término do período, o acesso é **revogado automaticamente** (se possível via SCP/policy condition) ou **manualmente pelo DevOps Lead**.
6. O registro da exceção é incluído no **próximo relatório de recertificação**.

```bash
# Exemplo: Criar policy temporária com condição de data
cat > /tmp/temp-access-policy.json << 'EOF'
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["ec2:*"],
      "Resource": "*",
      "Condition": {
        "DateLessThan": {
          "aws:CurrentTime": "2026-06-30T23:59:59Z"
        }
      }
    }
  ]
}
EOF

aws iam put-user-policy \
  --user-name <USUARIO> \
  --policy-name TempAccess-EC2-Exp20260630 \
  --policy-document file:///tmp/temp-access-policy.json
```

### 8.2 Cadeia de Escalação

| Nível | Aprovador      | Escopo                                                  |
| ----- | -------------- | ------------------------------------------------------- |
| 1     | Gestor SGSI    | Exceções de acesso dentro do escopo do papel RBAC        |
| 2     | DevOps Lead    | Exceções técnicas (acesso temporário a recursos)         |
| 3     | CEO            | Acesso administrativo total ou exceções fora da política |

---

## 9. Procedimento de De-Provisioning (Desligamento)

Para garantir o SLA de **< 4 horas**, o seguinte procedimento deve ser executado:

| # | Ação                                              | Responsável   | SLA        |
| - | ------------------------------------------------- | ------------- | ---------- |
| 1 | Receber notificação formal de desligamento         | Gestor SGSI   | Imediato   |
| 2 | Desativar console access (delete-login-profile)    | DevOps Lead   | 30 minutos |
| 3 | Desativar todas as access keys                     | DevOps Lead   | 30 minutos |
| 4 | Remover de todos os grupos IAM                     | DevOps Lead   | 1 hora     |
| 5 | Remover do GitHub (organização + repos)             | DevOps Lead   | 1 hora     |
| 6 | Remover do Kubernetes (bindings + aws-auth)         | DevOps Lead   | 2 horas    |
| 7 | Deletar o usuário IAM                              | DevOps Lead   | 3 horas    |
| 8 | Documentar e confirmar de-provisioning completo     | Gestor SGSI   | 4 horas    |

```bash
# Script consolidado de de-provisioning
USER_TO_REMOVE="<USUARIO>"

# Passo 1: Desativar console
aws iam delete-login-profile --user-name "$USER_TO_REMOVE" 2>/dev/null

# Passo 2: Desativar access keys
for key in $(aws iam list-access-keys --user-name "$USER_TO_REMOVE" \
  --query 'AccessKeyMetadata[*].AccessKeyId' --output text); do
  aws iam update-access-key --user-name "$USER_TO_REMOVE" \
    --access-key-id "$key" --status Inactive
done

# Passo 3: Remover de grupos
for group in $(aws iam list-groups-for-user --user-name "$USER_TO_REMOVE" \
  --query 'Groups[*].GroupName' --output text); do
  aws iam remove-user-from-group --user-name "$USER_TO_REMOVE" --group-name "$group"
done

# Passo 4: Desanexar policies
for policy in $(aws iam list-attached-user-policies --user-name "$USER_TO_REMOVE" \
  --query 'AttachedPolicies[*].PolicyArn' --output text); do
  aws iam detach-user-policy --user-name "$USER_TO_REMOVE" --policy-arn "$policy"
done

# Passo 5: Remover MFA
for mfa in $(aws iam list-mfa-devices --user-name "$USER_TO_REMOVE" \
  --query 'MFADevices[*].SerialNumber' --output text); do
  aws iam deactivate-mfa-device --user-name "$USER_TO_REMOVE" --serial-number "$mfa"
done

# Passo 6: Deletar usuário
aws iam delete-user --user-name "$USER_TO_REMOVE"

# Passo 7: Remover do GitHub
gh api -X DELETE "orgs/TWYN/members/$USER_TO_REMOVE"

echo "✅ De-provisioning completo para: $USER_TO_REMOVE"
echo "⏰ Horário de conclusão: $(date)"
```

---

## 10. Registros e Evidências

Todos os artefatos gerados durante a recertificação devem ser armazenados e retidos conforme abaixo:

| Artefato                                | Formato     | Local de Armazenamento                          | Retenção  |
| --------------------------------------- | ----------- | ------------------------------------------------ | --------- |
| Relatório de credenciais AWS (CSV)       | CSV         | `evidencias/iam/Qn-AAAA/credential-report.csv`  | 3 anos    |
| Listagem de usuários e permissões        | TXT/JSON    | `evidencias/iam/Qn-AAAA/iam-users-audit.txt`    | 3 anos    |
| Comparação com matriz RBAC              | MD          | `evidencias/iam/Qn-AAAA/rbac-comparison.md`     | 3 anos    |
| Relatório de anomalias                   | MD          | `evidencias/iam/Qn-AAAA/anomalias-iam.md`       | 3 anos    |
| Auditoria GitHub                         | TXT         | `evidencias/iam/Qn-AAAA/github-audit.txt`       | 3 anos    |
| Auditoria Kubernetes RBAC                | TXT         | `evidencias/iam/Qn-AAAA/k8s-rbac-audit.txt`     | 3 anos    |
| Relatório de recertificação (consolidado)| MD          | `evidencias/iam/Qn-AAAA/recertificacao-iam.md`  | 3 anos    |
| Log de remediações                       | LOG         | `evidencias/iam/Qn-AAAA/remediacao-iam.log`     | 3 anos    |
| Sign-off aprovado                        | PDF/MD      | `evidencias/iam/Qn-AAAA/sign-off.pdf`           | 3 anos    |
| Exceções aprovadas                       | MD          | `evidencias/iam/Qn-AAAA/excecoes.md`            | 3 anos    |

> **Importante:** Toda evidência deve conter data, hora e identificação do responsável pela coleta. Capturas de tela complementares são recomendadas para outputs críticos.

---

## 11. Indicadores de Desempenho (KPIs)

Os seguintes KPIs devem ser monitorados e reportados a cada ciclo de recertificação:

| KPI                                        | Meta           | Fórmula                                                          |
| ------------------------------------------ | -------------- | ---------------------------------------------------------------- |
| **Taxa de conclusão da recertificação**     | 100%           | (Recertificações concluídas no prazo / Total planejadas) × 100   |
| **Contas órfãs identificadas**              | 0              | Contagem absoluta de contas sem titular ativo                    |
| **Usuários sem MFA**                        | 0              | Contagem absoluta de usuários IAM sem MFA ativado                |
| **Access keys > 90 dias sem rotação**       | 0              | Contagem de access keys com data de criação > 90 dias            |
| **Usuários inativos > 90 dias**             | 0              | Contagem de usuários com último acesso > 90 dias                 |
| **Permissões excessivas identificadas**     | 0              | Contagem de usuários com policies acima do papel RBAC            |
| **Tempo médio de remediação**               | < 48 horas     | Soma dos tempos de remediação / Número de remediações            |
| **Tempo de de-provisioning**                | < 4 horas      | Tempo entre notificação de desligamento e remoção completa       |
| **Conformidade com matriz RBAC**            | 100%           | (Usuários conformes / Total de usuários) × 100                   |
| **Exceções ativas**                         | Minimizar      | Contagem de exceções de acesso temporário vigentes               |

### 11.1 Dashboard de KPIs

Os KPIs devem ser consolidados em uma tabela no relatório de recertificação:

| KPI                                  | Q1    | Q2    | Q3    | Q4    | Tendência |
| ------------------------------------- | ----- | ----- | ----- | ----- | --------- |
| Taxa de conclusão                     |       |       |       |       |           |
| Contas órfãs                          |       |       |       |       |           |
| Usuários sem MFA                      |       |       |       |       |           |
| Access keys > 90 dias                 |       |       |       |       |           |
| Tempo médio de remediação (horas)     |       |       |       |       |           |

---

## 12. Referências

| Documento                          | Identificador       |
| ---------------------------------- | -------------------- |
| Política de Controle de Acesso      | SGSI-POLICY-002     |
| ISO 27001:2022 — Anexo A           | A.5.15 a A.5.18, A.8.2, A.8.3 |
| AWS IAM Best Practices             | [AWS Documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) |
| CIS AWS Foundations Benchmark      | v3.0                |

---

## 13. Histórico de Revisões

| Versão | Data       | Autor           | Descrição da Alteração                                           |
| ------ | ---------- | --------------- | ---------------------------------------------------------------- |
| 1.0    | 02/06/2026 | Gestor SGSI     | Criação inicial do procedimento de recertificação IAM            |
|        |            |                 |                                                                  |
|        |            |                 |                                                                  |

---

> **Classificação:** INTERNAL  
> **Proprietário:** Gestor SGSI  
> **Próxima revisão:** Conforme definido após aprovação  
> **Controles ISO 27001:2022:** A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.3
