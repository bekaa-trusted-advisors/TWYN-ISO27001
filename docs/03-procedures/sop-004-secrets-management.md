---
document_id: SGSI-SOP-004
title: "Procedimento Operacional Padrão — Gestão de Segredos e Rotação de Chaves (90 dias)"
version: "1.0"
status: Approved
classification: CONFIDENTIAL
owner: DevOps Lead
approved_by: "CEO (Ata 001)"
approval_date: "2026-06-08"
effective_date: "2026-06-08"
next_review: ""
related_policies:
  - SGSI-POLICY-001
  - SGSI-POLICY-002
annex_a_controls:
  - "A.5.17 - Authentication information"
  - "A.8.24 - Use of cryptography"
tags:
  - secrets-management
  - key-rotation
  - aws
  - kms
  - iam
  - compliance
---

# SGSI-SOP-004 — Gestão de Segredos e Rotação de Chaves (90 dias)

## 1. Objetivo

Este Procedimento Operacional Padrão (SOP) estabelece as diretrizes, responsabilidades e procedimentos técnicos obrigatórios para a gestão segura de segredos (credenciais, chaves criptográficas, tokens e certificados) na infraestrutura da **TWYN — Face ID Platform API**, hospedada na Amazon Web Services (AWS).

O objetivo principal é garantir que:

- Todos os segredos sejam armazenados de forma criptografada e com acesso controlado.
- Chaves de acesso IAM sejam rotacionadas a cada **90 dias**, sem exceção.
- Chaves criptográficas (KMS CMK) sejam rotacionadas anualmente ou imediatamente em caso de comprometimento.
- Credenciais de banco de dados sejam gerenciadas via AWS Secrets Manager com rotação automática.
- Certificados TLS sejam renovados automaticamente via AWS Certificate Manager (ACM).
- Nenhum segredo seja armazenado em texto plano, código-fonte, variáveis de ambiente não protegidas ou canais de comunicação não autorizados.

Este SOP atende aos requisitos dos controles **A.5.17**, **A.8.24** e **A.8.25** do Anexo A da ISO/IEC 27001:2022, e está alinhado com as políticas **SGSI-POLICY-001** e **SGSI-POLICY-002**.

---

## 2. Escopo

Este procedimento aplica-se a:

| Escopo                     | Descrição                                                                 |
|----------------------------|---------------------------------------------------------------------------|
| **Ambientes**              | Produção (`prod`), Homologação (`staging`), Desenvolvimento (`dev`)       |
| **Sistemas**               | Face ID Platform API, infraestrutura AWS, pipelines CI/CD (GitHub Actions)|
| **Contas AWS**             | Todas as contas da organização TWYN                                       |
| **Pessoal**                | DevOps Lead, Engenheiros de Plataforma, SRE, CISO, Auditores             |
| **Terceiros**              | Prestadores com acesso temporário a recursos AWS (via IAM roles)          |

### 2.1 Fora do Escopo

- Senhas de usuários finais da plataforma (gerenciadas pelo módulo de autenticação da aplicação).
- Chaves PGP/GPG pessoais de colaboradores.
- Credenciais de ferramentas SaaS não integradas à infraestrutura AWS.

---

## 3. Definições e Terminologia

| Termo                  | Definição                                                                                          |
|------------------------|----------------------------------------------------------------------------------------------------|
| **Segredo**            | Qualquer informação de autenticação ou criptografia que deve permanecer confidencial               |
| **IAM Access Key**     | Par de chaves (Access Key ID + Secret Access Key) para autenticação programática na AWS            |
| **CMK**                | Customer Managed Key — chave criptográfica gerenciada pelo cliente no AWS KMS                      |
| **Rotação**            | Processo de substituição de um segredo ativo por um novo, invalidando o anterior                   |
| **Segredo Órfão**      | Credencial ativa associada a entidade inativa, sem proprietário ou sem uso legítimo                |
| **Break-Glass**        | Procedimento de emergência para acesso à conta root AWS                                            |
| **OIDC Federation**    | Federação de identidade via OpenID Connect — elimina necessidade de chaves de longa duração        |
| **ACM**                | AWS Certificate Manager — serviço gerenciado de certificados TLS                                   |

---

## 4. Tipos de Segredos Gerenciados

### 4.1 Inventário de Segredos

| # | Tipo de Segredo                  | Armazenamento             | Rotação            | Responsável         |
|---|----------------------------------|---------------------------|--------------------|--------------------|
| 1 | IAM Access Keys                  | AWS IAM                   | 90 dias            | DevOps Lead        |
| 2 | Credenciais de Banco de Dados    | AWS Secrets Manager       | 90 dias (automática)| DevOps Lead       |
| 3 | API Keys (serviços externos)     | AWS Secrets Manager       | 90 dias            | DevOps Lead        |
| 4 | Certificados TLS                 | AWS ACM                   | Automática (ACM)   | DevOps Lead        |
| 5 | KMS CMK (biometria)              | AWS KMS                   | Anual (automática)  | DevOps Lead / CISO|
| 6 | SSH Keys (acesso a instâncias)   | AWS Systems Manager       | 90 dias            | DevOps Lead        |
| 7 | Tokens de Serviço / OAuth        | AWS Secrets Manager       | 90 dias            | DevOps Lead        |
| 8 | Terraform State Encryption Key   | AWS KMS (S3 SSE)          | Anual              | DevOps Lead        |
| 9 | GitHub Actions OIDC              | Federação (sem chave)     | N/A                | DevOps Lead        |

### 4.2 Classificação de Criticidade

| Criticidade  | Segredos                                                        | Impacto de Comprometimento          |
|-------------|-----------------------------------------------------------------|-------------------------------------|
| **CRÍTICA**  | KMS CMK (`alias/twyn-biometric-key`), credenciais de produção  | Exposição de dados biométricos      |
| **ALTA**     | IAM Access Keys, credenciais de banco de dados                  | Acesso não autorizado a recursos    |
| **MÉDIA**    | API Keys de serviços externos, tokens OAuth                     | Interrupção de integrações          |
| **BAIXA**    | SSH Keys de desenvolvimento, certificados de staging            | Impacto limitado a ambientes dev    |

---

## 5. Responsabilidades

| Papel                  | Responsabilidades                                                                                  |
|------------------------|----------------------------------------------------------------------------------------------------|
| **DevOps Lead**        | Proprietário do processo. Executa rotações, monitora alertas, garante conformidade                 |
| **Engenheiros SRE**    | Executam rotações delegadas. Respondem a alertas de chaves expiradas                               |
| **CISO**               | Aprova exceções. Revisa relatórios de auditoria. Autoriza rotação emergencial de KMS CMK           |
| **Auditores**          | Verificam evidências de rotação. Validam registros no CloudTrail                                   |
| **Desenvolvedores**    | Nunca armazenam segredos em código. Utilizam referências a Secrets Manager                         |

---

## 6. Procedimentos Detalhados

### 6.1 Criação de Novos Segredos no AWS Secrets Manager

#### Pré-requisitos

- Permissão IAM: `secretsmanager:CreateSecret`, `secretsmanager:TagResource`
- Sessão MFA ativa para ambiente de produção

#### Procedimento

**Passo 1 — Criar o segredo com criptografia KMS:**

```bash
aws secretsmanager create-secret \
  --name "twyn/prod/db-credentials" \
  --description "Credenciais do banco de dados PostgreSQL de produção - Face ID Platform" \
  --kms-key-id "alias/twyn-biometric-key" \
  --secret-string '{"username":"twyn_app","password":"GENERATED_SECURE_PASSWORD","host":"twyn-prod.cluster-xxxx.us-east-1.rds.amazonaws.com","port":"5432","dbname":"faceid_prod"}' \
  --tags '[{"Key":"Environment","Value":"prod"},{"Key":"Owner","Value":"devops-lead"},{"Key":"RotationSchedule","Value":"90-days"},{"Key":"ManagedBy","Value":"SGSI-SOP-004"}]' \
  --region us-east-1
```

**Passo 2 — Verificar a criação:**

```bash
aws secretsmanager describe-secret \
  --secret-id "twyn/prod/db-credentials" \
  --region us-east-1
```

**Passo 3 — Registrar no inventário de segredos** (planilha `SGSI-REG-SECRETS` ou ferramenta de CMDB).

> **⚠️ IMPORTANTE:** Nunca utilize `--secret-string` com valores reais diretamente na linha de comando em ambientes compartilhados. Utilize `--secret-string file://secret.json` com arquivo temporário de permissão `600`, deletado imediatamente após uso.

```bash
# Método seguro de criação
umask 077
cat > /tmp/secret.json << 'EOF'
{"username":"twyn_app","password":"$(openssl rand -base64 32)","host":"twyn-prod.cluster-xxxx.us-east-1.rds.amazonaws.com","port":"5432","dbname":"faceid_prod"}
EOF

aws secretsmanager create-secret \
  --name "twyn/prod/db-credentials" \
  --description "Credenciais PostgreSQL produção" \
  --kms-key-id "alias/twyn-biometric-key" \
  --secret-string file:///tmp/secret.json \
  --region us-east-1

# Remover arquivo temporário de forma segura
shred -u /tmp/secret.json
```

---

### 6.2 Rotação de IAM Access Keys (90 dias)

> **Controle ISO 27001:** A.5.17 — Informações de autenticação

#### Ciclo de Rotação

A rotação de IAM Access Keys segue o modelo **create-before-delete** para evitar interrupção de serviço.

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│  1. Criar nova   │───▶│ 2. Atualizar     │───▶│ 3. Validar      │───▶│ 4. Desativar e   │
│     chave        │    │    aplicações    │    │    funcionamento │    │    deletar antiga │
└─────────────────┘    └─────────────────┘    └─────────────────┘    └─────────────────┘
```

#### Procedimento Passo a Passo

**Passo 1 — Identificar chaves que necessitam rotação:**

```bash
# Listar todas as chaves de acesso e suas datas de criação
aws iam list-access-keys --user-name twyn-platform-svc --output table

# Verificar idade da chave (deve ser < 90 dias)
aws iam list-access-keys --user-name twyn-platform-svc \
  --query 'AccessKeyMetadata[*].[AccessKeyId,CreateDate,Status]' \
  --output table
```

**Passo 2 — Gerar relatório de chaves com mais de 80 dias (alerta preventivo):**

```bash
# Script de verificação de idade de chaves
aws iam generate-credential-report
aws iam get-credential-report \
  --query 'Content' \
  --output text | base64 --decode > /tmp/credential-report.csv

# Filtrar chaves com mais de 80 dias
awk -F',' '{
  if ($9 != "N/A" && $9 != "access_key_1_last_rotated") {
    cmd = "date -d \"" $9 "\" +%s"
    cmd | getline created
    close(cmd)
    now = systime()
    age = (now - created) / 86400
    if (age > 80) print $1, $9, int(age) " dias"
  }
}' /tmp/credential-report.csv
```

**Passo 3 — Criar nova chave de acesso:**

```bash
aws iam create-access-key --user-name twyn-platform-svc \
  --output json > /tmp/new-key.json

# Extrair valores (ambiente seguro apenas)
NEW_ACCESS_KEY=$(jq -r '.AccessKey.AccessKeyId' /tmp/new-key.json)
NEW_SECRET_KEY=$(jq -r '.AccessKey.SecretAccessKey' /tmp/new-key.json)

echo "Nova Access Key ID: $NEW_ACCESS_KEY"
echo "ATENÇÃO: Secret Key exibida apenas uma vez. Armazene de forma segura."
```

**Passo 4 — Atualizar o segredo no Secrets Manager com a nova chave:**

```bash
aws secretsmanager update-secret \
  --secret-id "twyn/prod/iam-keys/twyn-platform-svc" \
  --secret-string "{\"AccessKeyId\":\"$NEW_ACCESS_KEY\",\"SecretAccessKey\":\"$NEW_SECRET_KEY\"}" \
  --region us-east-1
```

**Passo 5 — Aguardar propagação e validar (mínimo 24h em produção):**

```bash
# Testar a nova chave
AWS_ACCESS_KEY_ID=$NEW_ACCESS_KEY \
AWS_SECRET_ACCESS_KEY=$NEW_SECRET_KEY \
aws sts get-caller-identity
```

**Passo 6 — Desativar a chave antiga:**

```bash
aws iam update-access-key \
  --user-name twyn-platform-svc \
  --access-key-id AKIA_OLD_KEY_ID \
  --status Inactive
```

**Passo 7 — Monitorar por 48h e, se não houver impacto, deletar:**

```bash
# Verificar último uso da chave antiga
aws iam get-access-key-last-used --access-key-id AKIA_OLD_KEY_ID

# Deletar chave antiga (somente após confirmação de não uso)
aws iam delete-access-key \
  --user-name twyn-platform-svc \
  --access-key-id AKIA_OLD_KEY_ID
```

**Passo 8 — Limpar arquivos temporários:**

```bash
shred -u /tmp/new-key.json /tmp/credential-report.csv
```

**Passo 9 — Registrar a rotação:**

- Atualizar planilha `SGSI-REG-SECRETS` com nova data de criação
- Criar registro no sistema de tickets: "Rotação IAM Key — twyn-platform-svc — [DATA]"
- Evidência: screenshot do `aws iam list-access-keys` mostrando apenas a nova chave ativa

---

### 6.3 Rotação de Credenciais de Banco de Dados (Secrets Manager Auto-Rotation)

#### Configuração da Rotação Automática

**Passo 1 — Criar a função Lambda de rotação:**

```bash
aws secretsmanager rotate-secret \
  --secret-id "twyn/prod/db-credentials" \
  --rotation-lambda-arn "arn:aws:lambda:us-east-1:ACCOUNT_ID:function:SecretsManagerRDSPostgreSQLRotation" \
  --rotation-rules '{"AutomaticallyAfterDays": 90}' \
  --region us-east-1
```

**Passo 2 — Verificar configuração de rotação:**

```bash
aws secretsmanager describe-secret \
  --secret-id "twyn/prod/db-credentials" \
  --query '{RotationEnabled:RotationEnabled,RotationLambdaARN:RotationLambdaARN,RotationRules:RotationRules,LastRotatedDate:LastRotatedDate}' \
  --region us-east-1
```

**Passo 3 — Forçar rotação manual (se necessário):**

```bash
aws secretsmanager rotate-secret \
  --secret-id "twyn/prod/db-credentials" \
  --region us-east-1
```

**Passo 4 — Monitorar status da rotação:**

```bash
# Verificar versões do segredo (AWSCURRENT = ativa, AWSPENDING = em rotação)
aws secretsmanager list-secret-version-ids \
  --secret-id "twyn/prod/db-credentials" \
  --query 'Versions[*].[VersionId,VersionStages]' \
  --output table \
  --region us-east-1
```

> **Nota:** A aplicação Face ID Platform API deve utilizar o SDK AWS para buscar credenciais em runtime, **nunca** armazenar credenciais de banco em variáveis de ambiente estáticas ou arquivos de configuração.

---

### 6.4 Rotação de KMS Customer Managed Key (CMK)

> **Controle ISO 27001:** A.8.24 — Uso de criptografia

A CMK `alias/twyn-biometric-key` é utilizada para criptografia de dados biométricos e é classificada como **CRITICIDADE MÁXIMA**.

#### 6.4.1 Rotação Automática Anual

**Passo 1 — Habilitar rotação automática anual:**

```bash
aws kms enable-key-rotation \
  --key-id "alias/twyn-biometric-key" \
  --region us-east-1
```

**Passo 2 — Verificar que a rotação está habilitada:**

```bash
aws kms get-key-rotation-status \
  --key-id "alias/twyn-biometric-key" \
  --region us-east-1
```

Saída esperada:
```json
{
    "KeyRotationEnabled": true
}
```

> **Nota:** A rotação automática do KMS gera novo material criptográfico anualmente. O material antigo é preservado para descriptografia de dados existentes. Não há interrupção de serviço.

#### 6.4.2 Rotação Manual de Emergência (Comprometimento)

Em caso de comprometimento suspeito ou confirmado da CMK:

**Passo 1 — Criar nova CMK imediatamente:**

```bash
aws kms create-key \
  --description "TWYN Biometric Data Encryption Key - Replacement $(date +%Y%m%d)" \
  --key-usage ENCRYPT_DECRYPT \
  --key-spec SYMMETRIC_DEFAULT \
  --tags '[{"TagKey":"Environment","TagValue":"prod"},{"TagKey":"Purpose","TagValue":"biometric-encryption"},{"TagKey":"Owner","TagValue":"devops-lead"},{"TagKey":"EmergencyRotation","TagValue":"true"},{"TagKey":"IncidentRef","TagValue":"INC-XXXX"}]' \
  --region us-east-1
```

**Passo 2 — Atualizar o alias para a nova chave:**

```bash
aws kms update-alias \
  --alias-name "alias/twyn-biometric-key" \
  --target-key-id "NEW_KEY_ID" \
  --region us-east-1
```

**Passo 3 — Re-criptografar dados biométricos existentes com a nova chave:**

> **⚠️ ATENÇÃO:** Este passo requer planejamento de janela de manutenção e aprovação do CISO.

```bash
# Exemplo conceitual — implementação real via script dedicado
aws kms re-encrypt \
  --source-key-id "OLD_KEY_ID" \
  --destination-key-id "alias/twyn-biometric-key" \
  --ciphertext-blob fileb://encrypted-data.bin \
  --region us-east-1
```

**Passo 4 — Desabilitar a chave comprometida (NÃO deletar imediatamente):**

```bash
aws kms disable-key \
  --key-id "OLD_KEY_ID" \
  --region us-east-1
```

**Passo 5 — Agendar deleção da chave antiga (mínimo 30 dias de espera):**

```bash
aws kms schedule-key-deletion \
  --key-id "OLD_KEY_ID" \
  --pending-window-in-days 30 \
  --region us-east-1
```

---

### 6.5 Renovação de Certificados TLS (AWS ACM)

#### Certificados Gerenciados pelo ACM (Renovação Automática)

```bash
# Listar certificados e status de renovação
aws acm list-certificates \
  --certificate-statuses ISSUED \
  --query 'CertificateSummaryList[*].[DomainName,CertificateArn,Status]' \
  --output table \
  --region us-east-1

# Verificar detalhes e data de expiração
aws acm describe-certificate \
  --certificate-arn "arn:aws:acm:us-east-1:ACCOUNT_ID:certificate/CERT_ID" \
  --query '{DomainName:Certificate.DomainName,NotAfter:Certificate.NotAfter,RenewalSummary:Certificate.RenewalSummary}' \
  --region us-east-1
```

> **Nota:** Certificados emitidos pelo ACM para domínios validados por DNS são renovados automaticamente. Monitorar o status `PENDING_VALIDATION` via CloudWatch Alarm.

#### Certificados Importados (Renovação Manual)

```bash
# Renovar certificado importado
aws acm import-certificate \
  --certificate-arn "arn:aws:acm:us-east-1:ACCOUNT_ID:certificate/CERT_ID" \
  --certificate fileb://new-cert.pem \
  --private-key fileb://new-private-key.pem \
  --certificate-chain fileb://new-chain.pem \
  --region us-east-1
```

---

### 6.6 Rotação de SSH Keys

```bash
# Gerar novo par de chaves
ssh-keygen -t ed25519 -C "twyn-devops-$(date +%Y%m%d)" -f /tmp/twyn-key-new

# Armazenar chave privada no Secrets Manager
aws secretsmanager update-secret \
  --secret-id "twyn/prod/ssh-keys/devops" \
  --secret-string file:///tmp/twyn-key-new \
  --region us-east-1

# Atualizar chave pública nas instâncias via SSM
aws ssm send-command \
  --document-name "AWS-RunShellScript" \
  --targets '[{"Key":"tag:Environment","Values":["prod"]}]' \
  --parameters '{"commands":["echo \"$(cat /tmp/twyn-key-new.pub)\" >> /home/devops/.ssh/authorized_keys"]}' \
  --region us-east-1

# Remover chaves temporárias
shred -u /tmp/twyn-key-new /tmp/twyn-key-new.pub
```

---

## 7. Calendário de Rotação (90 Dias)

### 7.1 Ciclos de Rotação — Ano 2026

| Ciclo | Período              | Deadline de Rotação | Alerta (10 dias antes) | Status   |
|-------|----------------------|---------------------|------------------------|----------|
| Q1    | 01/Jan — 31/Mar      | 31/Mar/2026         | 21/Mar/2026            | Pendente |
| Q2    | 01/Abr — 30/Jun      | 29/Jun/2026         | 19/Jun/2026            | Pendente |
| Q3    | 01/Jul — 30/Set      | 28/Set/2026         | 18/Set/2026            | Pendente |
| Q4    | 01/Out — 31/Dez      | 29/Dez/2026         | 19/Dez/2026            | Pendente |

### 7.2 Checklist de Rotação Trimestral

- [ ] IAM Access Keys de todos os usuários de serviço rotacionadas
- [ ] Credenciais de banco de dados rotacionadas (verificar auto-rotation)
- [ ] API Keys de serviços externos rotacionadas
- [ ] SSH Keys rotacionadas
- [ ] Tokens OAuth/JWT de serviço renovados
- [ ] Relatório de credenciais (`credential-report`) gerado e revisado
- [ ] Credenciais órfãs identificadas e removidas
- [ ] Evidências de rotação arquivadas em `SGSI-REG-SECRETS`
- [ ] Registro de não-conformidades (se aplicável) criado

### 7.3 Automação de Alertas

```bash
# AWS Config Rule — Detectar chaves com mais de 90 dias
aws configservice put-config-rule \
  --config-rule '{
    "ConfigRuleName": "iam-access-key-rotation-90-days",
    "Source": {
      "Owner": "AWS",
      "SourceIdentifier": "ACCESS_KEYS_ROTATED"
    },
    "InputParameters": "{\"maxAccessKeyAge\":\"90\"}",
    "MaximumExecutionFrequency": "TwentyFour_Hours"
  }' \
  --region us-east-1
```

---

## 8. Procedimento de Rotação Emergencial (Credencial Comprometida)

### 8.1 Critérios de Ativação

Este procedimento é ativado quando:

1. Uma credencial é encontrada exposta em repositório público (ex.: GitHub, Pastebin)
2. Atividade suspeita detectada no CloudTrail associada a uma chave específica
3. Notificação de comprometimento por AWS Abuse, parceiro ou equipe interna
4. Detecção de uso de credencial a partir de IP ou região não autorizada
5. Notificação da AWS sobre chave exposta (AWS Health Event)

### 8.2 Procedimento de Resposta Imediata

**Tempo máximo de resposta: 1 hora após detecção.**

**Passo 1 — DESATIVAR a credencial comprometida imediatamente:**

```bash
# Para IAM Access Key
aws iam update-access-key \
  --user-name USUARIO_AFETADO \
  --access-key-id AKIA_COMPROMETIDA \
  --status Inactive

# Para segredo no Secrets Manager
aws secretsmanager update-secret \
  --secret-id "twyn/prod/SEGREDO_COMPROMETIDO" \
  --secret-string '{"status":"REVOKED","reason":"COMPROMISED","incident":"INC-XXXX"}' \
  --region us-east-1
```

**Passo 2 — Revogar sessões ativas:**

```bash
# Revogar todas as sessões do usuário IAM
aws iam put-user-policy \
  --user-name USUARIO_AFETADO \
  --policy-name "RevokeOlderSessions" \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [{
      "Effect": "Deny",
      "Action": "*",
      "Resource": "*",
      "Condition": {
        "DateLessThan": {"aws:TokenIssueTime": "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'"}
      }
    }]
  }'
```

**Passo 3 — Investigar uso não autorizado via CloudTrail:**

```bash
aws cloudtrail lookup-events \
  --lookup-attributes AttributeKey=AccessKeyId,AttributeValue=AKIA_COMPROMETIDA \
  --start-time "$(date -u -d '7 days ago' +%Y-%m-%dT%H:%M:%SZ)" \
  --end-time "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --query 'Events[*].[EventTime,EventName,SourceIPAddress,Resources[0].ResourceName]' \
  --output table \
  --region us-east-1
```

**Passo 4 — Gerar e distribuir nova credencial** (seguir procedimentos da Seção 6.2).

**Passo 5 — Registrar incidente:**

- Abrir ticket de incidente de segurança: `INC-XXXX`
- Classificação: **Incidente de Segurança da Informação**
- Notificar: CISO, DevOps Lead, Gestor de Riscos
- Prazo para relatório pós-incidente: **72 horas**

**Passo 6 — Deletar a credencial comprometida (após investigação):**

```bash
aws iam delete-access-key \
  --user-name USUARIO_AFETADO \
  --access-key-id AKIA_COMPROMETIDA
```

---

## 9. Práticas Proibidas

As seguintes práticas são **estritamente proibidas** e constituem **não-conformidade** com o SGSI:

| #  | Prática Proibida                                                           | Risco                                              | Controle ISO 27001 |
|----|---------------------------------------------------------------------------|---------------------------------------------------|--------------------|
| 1  | Armazenar segredos hardcoded no código-fonte                              | Exposição em repositórios, logs e artefatos        | A.5.17             |
| 2  | Incluir arquivos `.env` com segredos em repositórios Git                   | Exposição via histórico Git, forks e clones        | A.5.17             |
| 3  | Transmitir segredos em texto plano via Slack, Teams, e-mail ou chat       | Interceptação, logs de comunicação retidos          | A.5.17             |
| 4  | Compartilhar credenciais entre múltiplos usuários ou serviços             | Impossibilidade de rastreamento e auditoria         | A.5.17             |
| 5  | Utilizar a conta root da AWS para operações rotineiras                    | Risco máximo de comprometimento total               | A.8.24             |
| 6  | Criar IAM Access Keys para a conta root                                   | Vetor de ataque persistente de máximo impacto       | A.8.24             |
| 7  | Manter chaves de acesso sem rotação além de 90 dias                       | Não-conformidade ISO 27001, aumento de janela de ataque | A.5.17        |
| 8  | Armazenar chaves privadas em locais sem criptografia                      | Exposição de material criptográfico                 | A.8.24             |
| 9  | Utilizar credenciais de longa duração em pipelines CI/CD                   | Risco de exfiltração via logs de build              | A.5.17, A.8.25     |
| 10 | Desabilitar logs do CloudTrail para operações de KMS ou IAM               | Perda de trilha de auditoria                        | A.8.24             |

### 9.1 GitHub Actions — Uso Obrigatório de OIDC Federation

O pipeline de CI/CD da TWYN utiliza **GitHub Actions com OIDC Federation**, eliminando a necessidade de chaves de longa duração:

```yaml
# Exemplo de configuração no workflow GitHub Actions
permissions:
  id-token: write
  contents: read

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Configure AWS Credentials via OIDC
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: arn:aws:iam::ACCOUNT_ID:role/GitHubActionsDeployRole
          role-session-name: github-actions-deploy
          aws-region: us-east-1
```

> **É PROIBIDO** criar IAM Access Keys para uso em GitHub Actions. Qualquer exceção deve ser documentada como Risco Aceito com aprovação do CISO.

---

## 10. Monitoramento e Alertas

### 10.1 Regras AWS Config

| Regra                              | Descrição                                      | Frequência    |
|------------------------------------|-------------------------------------------------|---------------|
| `ACCESS_KEYS_ROTATED`             | Detecta chaves IAM com mais de 90 dias          | Diária (24h)  |
| `IAM_USER_MFA_ENABLED`            | Verifica MFA habilitado para usuários IAM       | Diária (24h)  |
| `IAM_ROOT_ACCESS_KEY_CHECK`       | Verifica ausência de chaves na conta root       | Diária (24h)  |
| `CMK_BACKING_KEY_ROTATION_ENABLED`| Verifica rotação automática de CMKs habilitada  | Diária (24h)  |

### 10.2 Alarmes CloudWatch

```bash
# Alarme para uso da conta root
aws cloudwatch put-metric-alarm \
  --alarm-name "twyn-root-account-usage" \
  --alarm-description "Alerta: uso da conta root detectado" \
  --metric-name "RootAccountUsage" \
  --namespace "CloudTrailMetrics" \
  --statistic Sum \
  --period 300 \
  --threshold 1 \
  --comparison-operator GreaterThanOrEqualToThreshold \
  --evaluation-periods 1 \
  --alarm-actions "arn:aws:sns:us-east-1:ACCOUNT_ID:twyn-security-alerts" \
  --treat-missing-data notBreaching \
  --region us-east-1
```

### 10.3 CloudTrail — Eventos Monitorados

| Evento                          | Significado                                | Ação Requerida                    |
|---------------------------------|--------------------------------------------|-----------------------------------|
| `CreateAccessKey`               | Nova chave IAM criada                      | Verificar se é rotação planejada  |
| `DeleteAccessKey`               | Chave IAM deletada                         | Verificar se é parte de rotação   |
| `PutSecretValue`                | Segredo atualizado no Secrets Manager      | Verificar se é rotação planejada  |
| `DisableKey` (KMS)              | CMK desabilitada                           | Investigar imediatamente          |
| `ScheduleKeyDeletion` (KMS)     | CMK agendada para deleção                  | Aprovação do CISO obrigatória     |
| `ConsoleLogin` (root)           | Login na conta root                        | Verificar procedimento break-glass|

### 10.4 Filtros de Métrica do CloudTrail

```bash
# Filtro para detecção de criação/deleção de chaves IAM
aws logs put-metric-filter \
  --log-group-name "CloudTrail/ManagementEvents" \
  --filter-name "IAMKeyChanges" \
  --filter-pattern '{ ($.eventName = CreateAccessKey) || ($.eventName = UpdateAccessKey) || ($.eventName = DeleteAccessKey) }' \
  --metric-transformations '[{
    "metricName": "IAMKeyChangeCount",
    "metricNamespace": "TwynSecurityMetrics",
    "metricValue": "1",
    "defaultValue": 0
  }]' \
  --region us-east-1
```

---

## 11. Trilha de Auditoria

### 11.1 Requisitos de Registro

Toda operação envolvendo segredos **DEVE** gerar registros auditáveis:

| Informação Obrigatória     | Fonte                          | Retenção        |
|---------------------------|--------------------------------|-----------------|
| Quem executou a operação  | CloudTrail (`userIdentity`)    | 365 dias mínimo |
| O que foi feito            | CloudTrail (`eventName`)       | 365 dias mínimo |
| Quando foi feito           | CloudTrail (`eventTime`)       | 365 dias mínimo |
| De onde foi feito          | CloudTrail (`sourceIPAddress`) | 365 dias mínimo |
| Resultado da operação      | CloudTrail (`responseElements`)| 365 dias mínimo |

### 11.2 Verificação de Auditoria

```bash
# Verificar integridade dos logs do CloudTrail
aws cloudtrail validate-logs \
  --trail-arn "arn:aws:cloudtrail:us-east-1:ACCOUNT_ID:trail/twyn-management-trail" \
  --start-time "$(date -u -d '30 days ago' +%Y-%m-%dT%H:%M:%SZ)" \
  --end-time "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  --region us-east-1
```

---

## 12. Limpeza de Credenciais Órfãs

### 12.1 Contexto

> **Não-conformidade conhecida:** O usuário IAM `tmpsaasboost` possui chave de acesso não rotacionada, sem proprietário identificado e sem uso legítimo confirmado. Este item está registrado como **CAR-002** (Ação Corretiva) e **RISK-009** (Registro de Riscos).

### 12.2 Procedimento de Identificação de Credenciais Órfãs

**Passo 1 — Gerar relatório de credenciais:**

```bash
aws iam generate-credential-report
sleep 10
aws iam get-credential-report \
  --query 'Content' \
  --output text | base64 --decode > /tmp/credential-report.csv
```

**Passo 2 — Identificar usuários sem uso recente (>90 dias):**

```bash
# Listar usuários IAM com último acesso
aws iam list-users --query 'Users[*].[UserName,CreateDate,PasswordLastUsed]' --output table

# Verificar último uso de chaves de acesso de todos os usuários
for user in $(aws iam list-users --query 'Users[*].UserName' --output text); do
  echo "=== $user ==="
  aws iam list-access-keys --user-name "$user" \
    --query 'AccessKeyMetadata[*].[AccessKeyId,CreateDate,Status]' --output table
  for key in $(aws iam list-access-keys --user-name "$user" \
    --query 'AccessKeyMetadata[*].AccessKeyId' --output text); do
    aws iam get-access-key-last-used --access-key-id "$key" \
      --query '{LastUsed:AccessKeyLastUsed.LastUsedDate,Service:AccessKeyLastUsed.ServiceName}' \
      --output table
  done
done
```

**Passo 3 — Procedimento de remediação para `tmpsaasboost` (CAR-002):**

```bash
# 1. Desativar chaves de acesso
aws iam list-access-keys --user-name tmpsaasboost \
  --query 'AccessKeyMetadata[*].AccessKeyId' --output text | \
  xargs -I{} aws iam update-access-key --user-name tmpsaasboost --access-key-id {} --status Inactive

# 2. Monitorar por 14 dias para confirmar ausência de impacto

# 3. Após confirmação, deletar chaves
aws iam list-access-keys --user-name tmpsaasboost \
  --query 'AccessKeyMetadata[*].AccessKeyId' --output text | \
  xargs -I{} aws iam delete-access-key --user-name tmpsaasboost --access-key-id {}

# 4. Remover políticas inline e attached
aws iam list-user-policies --user-name tmpsaasboost --query 'PolicyNames' --output text | \
  xargs -I{} aws iam delete-user-policy --user-name tmpsaasboost --policy-name {}

aws iam list-attached-user-policies --user-name tmpsaasboost \
  --query 'AttachedPolicies[*].PolicyArn' --output text | \
  xargs -I{} aws iam detach-user-policy --user-name tmpsaasboost --policy-arn {}

# 5. Deletar o usuário IAM
aws iam delete-user --user-name tmpsaasboost

# 6. Registrar fechamento de CAR-002 e mitigação de RISK-009
```

### 12.3 Verificação Periódica (Mensal)

Uma verificação mensal de credenciais órfãs deve ser realizada pelo DevOps Lead:

1. Gerar `credential-report` atualizado
2. Comparar com inventário `SGSI-REG-SECRETS`
3. Identificar discrepâncias (credenciais não inventariadas)
4. Desativar credenciais suspeitas
5. Documentar resultados no registro de verificação mensal

---

## 13. Conta Root — Procedimento Break-Glass

### 13.1 Proteção da Conta Root

| Controle                          | Status         | Detalhes                                    |
|-----------------------------------|----------------|---------------------------------------------|
| MFA de Hardware                   | ✅ Implementado | YubiKey 5 NFC                                |
| Armazenamento Físico              | ✅ Implementado | Cofre físico com acesso controlado           |
| Chaves de Acesso (Access Keys)    | ✅ Nenhuma      | Proibido criar chaves para root              |
| Uso                               | ✅ Break-Glass  | Somente para operações que requerem root     |

### 13.2 Procedimento de Acesso

1. Obter aprovação do CISO e de pelo menos mais um membro da diretoria
2. Registrar solicitação formal com justificativa
3. Retirar o YubiKey do cofre físico (dois responsáveis presentes)
4. Realizar a operação necessária
5. Registrar todas as ações executadas
6. Devolver o YubiKey ao cofre
7. Revisar CloudTrail para o período de uso
8. Documentar no registro de incidentes/operações extraordinárias

---

## 14. Terraform State — Proteção de Segredos

O estado do Terraform é armazenado em **S3 com criptografia SSE-KMS**:

```hcl
# backend.tf
terraform {
  backend "s3" {
    bucket         = "twyn-terraform-state"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    kms_key_id     = "alias/twyn-terraform-state-key"
    dynamodb_table = "twyn-terraform-lock"
  }
}
```

> **⚠️ IMPORTANTE:** O arquivo `terraform.tfstate` pode conter segredos em texto plano. O acesso ao bucket S3 deve ser restrito via policy de bucket e IAM. O versionamento do S3 deve estar habilitado para recuperação em caso de corrupção.

---

## 15. Registros e Evidências

### 15.1 Documentos Gerados por Este SOP

| Registro                          | ID do Registro      | Frequência      | Responsável    | Armazenamento              |
|-----------------------------------|---------------------|-----------------|----------------|----------------------------|
| Inventário de Segredos            | SGSI-REG-SECRETS    | Contínuo        | DevOps Lead    | Planilha controlada / CMDB |
| Relatório de Rotação Trimestral   | SGSI-REP-ROT-QX     | Trimestral      | DevOps Lead    | Repositório de evidências  |
| Credential Report AWS             | AWS-CRED-RPT        | Mensal          | DevOps Lead    | S3 bucket de auditoria     |
| Registro de Incidente de Segurança| INC-XXXX            | Conforme demanda| CISO           | Sistema de tickets         |
| Relatório de Limpeza de Órfãos    | SGSI-REP-ORPHAN     | Mensal          | DevOps Lead    | Repositório de evidências  |
| Evidência de Rotação de Chaves    | SGSI-EVD-ROT-XXXX   | Por rotação     | DevOps Lead    | S3 bucket de auditoria     |
| Log de Acesso Root (Break-Glass)  | SGSI-LOG-ROOT       | Conforme demanda| CISO           | Cofre digital + físico     |

### 15.2 Retenção

| Tipo de Registro          | Período de Retenção | Base Legal / Normativa       |
|--------------------------|---------------------|------------------------------|
| CloudTrail Logs          | Mínimo 365 dias     | ISO 27001, A.8.24            |
| Credential Reports       | Mínimo 365 dias     | ISO 27001, A.5.17            |
| Evidências de Rotação    | Mínimo 3 anos       | Ciclo de certificação ISO    |
| Registros de Incidentes  | Mínimo 5 anos       | Requisitos legais (LGPD)     |

---

## 16. Exceções

Qualquer exceção a este SOP deve ser:

1. Solicitada formalmente por escrito
2. Avaliada pelo DevOps Lead
3. Aprovada pelo CISO
4. Registrada como **Risco Aceito** no Registro de Riscos (`SGSI-REG-RISK`)
5. Revisada a cada **90 dias** para verificar se a exceção ainda é necessária
6. Limitada a um período máximo de **180 dias** antes de reavaliação obrigatória

---

## 17. Referências

| Documento                                    | Código            |
|----------------------------------------------|-------------------|
| Política de Segurança da Informação          | SGSI-POLICY-001   |
| Política de Controle de Acesso               | SGSI-POLICY-002   |
| Registro de Riscos                           | SGSI-REG-RISK     |
| Ação Corretiva — Credencial Órfã             | CAR-002           |
| Risco — IAM User `tmpsaasboost`              | RISK-009          |
| ISO/IEC 27001:2022                           | Cláusulas 4-10    |
| ISO/IEC 27001:2022 Anexo A                   | A.5.17, A.8.24, A.8.25 |
| AWS Well-Architected Framework — Security    | Pilar de Segurança|
| CIS AWS Foundations Benchmark                | v3.0              |

---

## 18. Histórico de Revisões

| Versão | Data       | Autor         | Descrição da Alteração                                            |
|--------|------------|---------------|-------------------------------------------------------------------|
| 1.0    | 2026-06-02 | DevOps Lead   | Versão inicial do SOP. Cobre gestão de segredos, rotação de 90 dias para IAM keys, auto-rotação de credenciais de banco via Secrets Manager, rotação anual de KMS CMK, renovação de certificados TLS via ACM, procedimento emergencial, limpeza de credenciais órfãs (CAR-002/RISK-009), e requisitos de auditoria. |

---

> **Classificação:** CONFIDENCIAL  
> **Proprietário:** DevOps Lead  
> **Próxima Revisão:** A definir após aprovação  
> **Documento controlado — Cópias não controladas não garantem atualização.**
