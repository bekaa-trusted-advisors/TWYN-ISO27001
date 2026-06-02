---
document_id: SGSI-POLICY-005
title: "Política de Backup & Recuperação"
version: "1.0"
status: "Draft"
classification: "INTERNAL"
owner: "Gestor SGSI"
approved_by: "CEO (Pendente)"
effective_date: "[Pendente]"
next_review: "2027-06-01"
annex_a_controls: "A.5.29, A.5.30, A.8.13, A.8.14"
related_documents:
  - "SGSI-POLICY-001 — Information Security Policy"
  - "SGSI-DRP-001 — Disaster Recovery Plan"
  - "SGSI-RISK-002 — Risk Register (RISK-006)"
  - "SGSI-GAP-004 — Backup Testing Gap"
---

# Política de Backup & Recuperação

## TWYN Face ID Platform

---

## 1. Propósito

Esta política estabelece os requisitos, diretrizes e procedimentos para **backup, retenção e recuperação** de dados e sistemas da plataforma TWYN Face ID, garantindo:

- **Continuidade operacional** da plataforma de verificação biométrica;
- **Proteção contra perda de dados**, incluindo dados biométricos classificados como RESTRICTED (LGPD Art. 11);
- **Conformidade** com os objetivos de recuperação definidos na Política de Segurança da Informação (SGSI-POLICY-001, Seção 11.1);
- **Atendimento** aos controles ISO 27001:2022 Annex A: A.5.29 (SI durante disrupção), A.5.30 (Prontidão de TIC), A.8.13 (Backup), A.8.14 (Redundância);
- **Conformidade regulatória** com a LGPD (Lei 13.709/2018), especialmente Art. 46 (segurança de dados pessoais sensíveis).

---

## 2. Escopo

Esta política aplica-se a:

- **Todos os ambientes**: Produção (us-east-1), DR (us-west-2), Staging, Desenvolvimento;
- **Todos os serviços AWS**: RDS PostgreSQL, S3 (dados biométricos), EKS, Secrets Manager, KMS, CloudTrail, CloudWatch;
- **Infraestrutura como Código (IaC)**: Terraform state, módulos e configurações;
- **Repositórios de código**: GitHub (manifests Kubernetes, Helm charts, GitOps);
- **Todos os colaboradores** com responsabilidade operacional sobre backups;
- **Fornecedores** que processam ou armazenam dados em nome da TWYN.

**Fora do escopo**:
- Ambientes de sandbox/laboratório pessoal;
- Dados efêmeros de CI/CD pipelines (logs de build, artefatos temporários).

---

## 3. Definições e Terminologia

| Termo | Definição |
|-------|-----------|
| **RPO** (Recovery Point Objective) | Quantidade máxima de dados que pode ser perdida, medida em tempo. |
| **RTO** (Recovery Time Objective) | Tempo máximo para restaurar um serviço ao estado operacional. |
| **PITR** (Point-in-Time Recovery) | Capacidade de restaurar banco de dados para qualquer instante dentro da janela de retenção. |
| **CRR** (Cross-Region Replication) | Replicação automática de objetos S3 entre regiões AWS. |
| **CMK** (Customer Managed Key) | Chave de criptografia gerenciada pelo cliente no AWS KMS. |
| **DR** (Disaster Recovery) | Procedimentos e infraestrutura para recuperação após desastre. |
| **Multi-AZ** | Implantação em múltiplas zonas de disponibilidade AWS. |
| **GitOps** | Padrão operacional onde o Git é a fonte de verdade para infraestrutura e deploys. |

---

## 4. Objetivos de Recuperação (RPO/RTO)

Os seguintes objetivos são estabelecidos em conformidade com a **Política de Segurança da Informação (SGSI-POLICY-001, Seção 11.1)**:

| Métrica | Alvo | Justificativa |
|---------|------|---------------|
| **RPO** (Recovery Point Objective) | **< 15 minutos** | Perda máxima aceitável de transações biométricas; alinhado com PITR do RDS e replicação S3 |
| **RTO** (Recovery Time Objective) | **< 4 horas** | Tempo máximo para restauração completa da plataforma; alinhado com SLA de clientes B2B |
| **Disponibilidade do serviço** | **99,9%** | Uptime anual da plataforma Face ID API |
| **Taxa de sucesso de backup** | **≥ 99,9%** | Percentual de backups completados com sucesso |

> **⚠️ IMPORTANTE**: Estes valores de RPO e RTO são os mesmos definidos na IS Policy (SGSI-POLICY-001, Seção 11.1). Qualquer alteração nestes valores DEVE ser sincronizada entre ambos os documentos e aprovada pelo Gestor SGSI e CEO.

### 4.1 Objetivos por Criticidade

| Classificação do Dado | RPO | RTO | Exemplo |
|------------------------|-----|-----|---------|
| **RESTRICTED** | < 15 minutos | < 2 horas | Dados biométricos (face templates), chaves criptográficas |
| **CONFIDENTIAL** | < 15 minutos | < 4 horas | Credenciais, código-fonte, logs de auditoria |
| **INTERNAL** | < 1 hora | < 8 horas | Documentação técnica, configurações |
| **PUBLIC** | < 24 horas | < 24 horas | Documentação pública de API |

---

## 5. Estratégia de Backup por Serviço

### 5.1 RDS PostgreSQL (Banco de Dados Principal)

O RDS PostgreSQL armazena dados transacionais da plataforma Face ID, incluindo metadados de verificações biométricas, registros de auditoria e dados de clientes.

| Parâmetro | Configuração |
|-----------|-------------|
| **Implantação** | Multi-AZ (us-east-1) |
| **PITR (Point-in-Time Recovery)** | Habilitado — backup contínuo a cada 5 minutos |
| **Snapshot automático diário** | Habilitado — janela de backup: 03:00–04:00 UTC |
| **Retenção de snapshots automáticos** | 35 dias |
| **Replicação cross-region** | Read Replica em us-west-2 (DR) com promoção automática |
| **Snapshot manual pré-deploy** | Obrigatório antes de migrations e major changes |
| **Criptografia** | AES-256 via AWS KMS (CMK: `alias/twyn-rds-cmk`) |
| **Monitoramento** | CloudWatch Alarms para falhas de snapshot |

**Procedimentos automatizados**:
1. AWS RDS executa snapshots automáticos diários e transaction logs a cada 5 minutos;
2. PITR permite restauração para qualquer segundo dentro dos últimos 35 dias;
3. Read Replica em us-west-2 mantém réplica assíncrona com lag monitorado (alerta se > 60s);
4. Snapshots diários são copiados automaticamente para us-west-2 via AWS Backup.

### 5.2 S3 — Dados Biométricos (RESTRICTED)

O S3 armazena imagens faciais, face templates e dados biométricos classificados como **RESTRICTED** sob LGPD Art. 11.

| Parâmetro | Configuração |
|-----------|-------------|
| **Bucket principal** | `twyn-biometric-data-prod` (us-east-1) |
| **Versionamento** | Habilitado (todas as versões retidas) |
| **CRR (Cross-Region Replication)** | Ativo para `twyn-biometric-data-dr` (us-west-2) |
| **Replication Time Control (RTC)** | Habilitado — SLA de 15 minutos para 99,99% dos objetos |
| **Criptografia** | SSE-KMS com CMK (`alias/twyn-s3-biometric-cmk`) |
| **Object Lock** | COMPLIANCE mode — retenção mínima de 5 anos para dados biométricos |
| **MFA Delete** | Habilitado — exclusão requer MFA do root account |
| **Lifecycle Policies** | Ver Seção 12 (Política de Retenção) |
| **Access Logging** | Habilitado para bucket de logs de acesso dedicado |

**Políticas de ciclo de vida**:
- Versões anteriores (noncurrent) → Glacier Deep Archive após 90 dias;
- Versões anteriores (noncurrent) → Exclusão após 5 anos (respeitando Object Lock);
- Incomplete multipart uploads → Exclusão após 7 dias.

### 5.3 EKS (Kubernetes — Plataforma de Aplicação)

O EKS executa os microsserviços da plataforma Face ID API.

| Componente | Estratégia de Backup |
|------------|---------------------|
| **Manifests Kubernetes** | GitOps — repositório Git como fonte de verdade (GitHub) |
| **Helm Charts** | Versionados no repositório (Helm chart museum ou OCI registry) |
| **Helm Values (por ambiente)** | Versionados em Git (com secrets separados no Secrets Manager) |
| **Persistent Volumes (EBS)** | Snapshots via AWS Backup — diário, retenção 35 dias |
| **etcd** (se EKS self-managed) | N/A — EKS managed control plane (AWS responsável) |
| **ConfigMaps / não sensíveis** | Versionados em Git |
| **Namespaces e RBAC** | Declarativos em Git (Terraform ou manifests) |

**Estratégia de recuperação**:
1. Cluster EKS: Recriado via Terraform (`terraform apply`);
2. Workloads: Reimplantados via GitOps (ArgoCD/Flux) ou `helm install`;
3. Persistent Volumes: Restaurados a partir de EBS snapshots via AWS Backup;
4. DNS/Ingress: Atualizados automaticamente via Terraform/External-DNS.

### 5.4 AWS Secrets Manager

O Secrets Manager armazena credenciais de banco de dados, API keys de terceiros e tokens de integração.

| Parâmetro | Configuração |
|-----------|-------------|
| **Replicação** | Multi-Region replication habilitada (us-east-1 → us-west-2) |
| **Rotação automática** | Habilitada — ciclo de 90 dias para credenciais de banco |
| **Criptografia** | AWS KMS CMK (`alias/twyn-secrets-cmk`) |
| **Versionamento** | Nativo do Secrets Manager (staging labels: AWSCURRENT, AWSPREVIOUS) |
| **Backup adicional** | Valores exportados (criptografados) para S3 vault bucket — trimestral |
| **Auditoria** | CloudTrail logging de todos os acessos a secrets |

**Backup de chaves KMS**:
- Chaves KMS CMK possuem material criptográfico gerenciado pela AWS (não exportável);
- Política de chave (key policy) documentada e versionada em Terraform;
- Alias de chave mapeados para facilitar rotação e DR;
- Em cenário DR, réplicas de secrets usam KMS key da região DR.

### 5.5 Terraform State (Infraestrutura como Código)

O estado do Terraform é a representação atual de toda a infraestrutura AWS da TWYN.

| Parâmetro | Configuração |
|-----------|-------------|
| **Backend** | S3 bucket (`twyn-terraform-state`) com versionamento habilitado |
| **Lock** | DynamoDB table (`twyn-terraform-locks`) |
| **Criptografia** | SSE-KMS com CMK dedicada |
| **Replicação** | CRR para bucket em conta AWS separada (backup account) |
| **Retenção de versões** | Indefinida (todas as versões retidas) |
| **Acesso** | IAM policy restritiva — somente CI/CD pipeline e DevOps Lead |

**Proteções adicionais**:
- Bucket policy impede exclusão de objetos (deny `s3:DeleteObject`);
- MFA Delete habilitado;
- Backup diário para conta AWS separada (cross-account replication);
- Módulos Terraform versionados em Git com tags semânticas.

### 5.6 CloudTrail e CloudWatch Logs

Logs de auditoria e operacionais são essenciais para conformidade e investigação de incidentes.

| Tipo de Log | Destino | Retenção |
|-------------|---------|----------|
| **CloudTrail** (API calls) | S3 bucket dedicado (`twyn-cloudtrail-logs`) | 2 anos (730 dias) |
| **CloudTrail** (management events) | CloudWatch Logs | 1 ano (365 dias) |
| **Application Logs** (EKS pods) | CloudWatch Logs → S3 export | 90 dias (CW) + 2 anos (S3) |
| **VPC Flow Logs** | CloudWatch Logs → S3 export | 1 ano (365 dias) |
| **RDS Audit Logs** | CloudWatch Logs | 1 ano (365 dias) |
| **WAF Logs** | S3 bucket dedicado | 1 ano (365 dias) |
| **Audit Logs** (conformidade LGPD) | S3 bucket dedicado (Object Lock) | 7 anos |

**Configurações de proteção**:
- Buckets de log com Object Lock (COMPLIANCE mode);
- CloudTrail Log File Validation habilitado (digest files);
- KMS encryption para todos os buckets de log;
- Lifecycle policy: S3 Standard → S3 Glacier após 180 dias → Deep Archive após 365 dias.

---

## 6. Monitoramento e Alertas de Backup

### 6.1 CloudWatch Alarms

Os seguintes alarmes devem estar configurados e ativos:

| Alarme | Métrica | Threshold | Ação |
|--------|---------|-----------|------|
| **RDS Snapshot Failure** | `RDS:BackupRetentionPeriodCheck` | Qualquer falha | SNS → PagerDuty → DevOps Lead |
| **RDS Replica Lag** | `ReplicaLag` | > 60 segundos | SNS → Slack #ops-alerts |
| **S3 CRR Failure** | `ReplicationLatency` | > 15 minutos | SNS → PagerDuty → DevOps Lead |
| **S3 CRR Pending** | `OperationsPendingReplication` | > 1000 objetos | SNS → Slack #ops-alerts |
| **EBS Snapshot Failure** | AWS Backup job failure | Qualquer falha | SNS → PagerDuty → DevOps Lead |
| **Secrets Manager Rotation** | `RotationFailed` | Qualquer falha | SNS → PagerDuty → DevOps Lead |
| **Terraform State Replication** | S3 replication metrics | Falha de replicação | SNS → DevOps Lead email |

### 6.2 Dashboard de Monitoramento

Um dashboard CloudWatch dedicado (**TWYN-Backup-Dashboard**) deve apresentar:

- Status de todos os backups nas últimas 24h;
- Lag de replicação RDS (gráfico temporal);
- Métricas de replicação S3 CRR;
- Status de jobs do AWS Backup;
- Histórico de rotação de secrets;
- KPIs de backup (taxa de sucesso, compliance).

### 6.3 Relatórios

| Relatório | Frequência | Destinatário | Conteúdo |
|-----------|------------|-------------|----------|
| **Backup Status Report** | Semanal | DevOps Lead, Gestor SGSI | Status de todos os backups, falhas, ações corretivas |
| **Backup Compliance Report** | Mensal | Gestor SGSI, CTO | KPIs, compliance RPO/RTO, gaps identificados |
| **DR Readiness Report** | Trimestral | CEO, CTO, Gestor SGSI | Resultado de testes de restauração, melhorias recomendadas |

---

## 7. Classificação de Backup por Nível de Dados

| Classificação | Tipo de Dado | Estratégia de Backup | Criptografia | Retenção | Teste |
|---------------|-------------|---------------------|-------------|----------|-------|
| **RESTRICTED** | Dados biométricos, face templates, chaves criptográficas | S3 versionamento + CRR + Object Lock; RDS PITR + snapshots cross-region | KMS CMK (AES-256) obrigatório | 5 anos (mínimo) | Trimestral |
| **CONFIDENTIAL** | Código-fonte, credenciais, logs de auditoria, contratos | Git (GitHub) + Secrets Manager replication + CloudTrail S3 | KMS CMK obrigatório | 2–7 anos (conforme tipo) | Trimestral |
| **INTERNAL** | Documentação técnica, configurações, terraform state | Git + S3 versionamento + cross-account | KMS CMK recomendado | 1 ano | Semestral |
| **PUBLIC** | Documentação pública, API docs | Git | Integridade (hash) | 6 meses | Anual |

---

## 8. Procedimentos de Restauração

### 8.1 Restauração RDS PostgreSQL

#### 8.1.1 Point-in-Time Recovery (PITR)

**Quando utilizar**: Corrupção de dados, exclusão acidental, rollback de migration.

**Procedimento**:

1. **Identificar o timestamp** exato anterior ao incidente (via CloudTrail, application logs);
2. **Executar PITR via AWS Console ou CLI**:
   ```bash
   aws rds restore-db-instance-to-point-in-time \
     --source-db-instance-identifier twyn-prod-db \
     --target-db-instance-identifier twyn-prod-db-restored \
     --restore-time "2026-XX-XXTXX:XX:XXZ" \
     --db-instance-class db.r6g.xlarge \
     --multi-az \
     --tags Key=Environment,Value=production
   ```
3. **Validar integridade** do banco restaurado:
   - Verificar contagem de registros nas tabelas críticas;
   - Executar queries de validação pré-definidas;
   - Comparar checksums de tabelas biométricas.
4. **Redirecionar aplicação** para o novo endpoint (via Parameter Store ou DNS);
5. **Monitorar** performance e erros por 1 hora após redirecionamento;
6. **Documentar** incidente, tempo de recuperação (RTO alcançado) e lições aprendidas.

**RTO estimado**: 30–90 minutos | **RPO**: até o segundo exato (dentro da janela PITR)

#### 8.1.2 Snapshot Restore

**Quando utilizar**: Falha completa da instância, rebuild de ambiente.

**Procedimento**:

1. **Listar snapshots disponíveis**:
   ```bash
   aws rds describe-db-snapshots \
     --db-instance-identifier twyn-prod-db \
     --query 'DBSnapshots[*].[DBSnapshotIdentifier,SnapshotCreateTime,Status]' \
     --output table
   ```
2. **Restaurar a partir do snapshot selecionado**:
   ```bash
   aws rds restore-db-instance-from-db-snapshot \
     --db-instance-identifier twyn-prod-db-from-snapshot \
     --db-snapshot-identifier rds:twyn-prod-db-YYYY-MM-DD-HH-MM \
     --db-instance-class db.r6g.xlarge \
     --multi-az
   ```
3. **Aplicar security groups e parameter groups** do ambiente de produção;
4. **Validar e redirecionar** (mesmo processo da Seção 8.1.1, passos 3–6).

**RTO estimado**: 1–2 horas | **RPO**: até a hora do último snapshot

#### 8.1.3 Failover Cross-Region (DR)

**Quando utilizar**: Indisponibilidade da região us-east-1 (desastre regional).

**Procedimento**:

1. **Promover Read Replica** em us-west-2 para instância standalone:
   ```bash
   aws rds promote-read-replica \
     --db-instance-identifier twyn-dr-replica \
     --region us-west-2
   ```
2. **Aguardar** promoção completar (status: `available`);
3. **Habilitar Multi-AZ** na nova instância primária;
4. **Atualizar connection strings** no Secrets Manager (us-west-2);
5. **Redirecionar tráfego** via Route 53 health check failover;
6. **Validar** integridade e funcionalidade da aplicação.

**RTO estimado**: 2–4 horas | **RPO**: lag de replicação (tipicamente < 1 minuto)

### 8.2 Restauração S3 (Dados Biométricos)

#### 8.2.1 Restauração por Versionamento

**Quando utilizar**: Exclusão ou sobrescrita acidental de objetos.

**Procedimento**:

1. **Identificar objetos afetados** (via S3 access logs ou application logs);
2. **Listar versões do objeto**:
   ```bash
   aws s3api list-object-versions \
     --bucket twyn-biometric-data-prod \
     --prefix "faces/user-id/template.bin"
   ```
3. **Restaurar versão anterior**:
   ```bash
   aws s3api copy-object \
     --bucket twyn-biometric-data-prod \
     --copy-source "twyn-biometric-data-prod/faces/user-id/template.bin?versionId=VERSION_ID" \
     --key "faces/user-id/template.bin"
   ```
4. **Validar** integridade do objeto restaurado (checksum SHA-256);
5. **Documentar** ação no registro de incidentes.

#### 8.2.2 Failover CRR (DR)

**Quando utilizar**: Indisponibilidade da região us-east-1.

**Procedimento**:

1. **Redirecionar aplicação** para ler do bucket DR (`twyn-biometric-data-dr`, us-west-2);
2. **Atualizar configurações** de aplicação (environment variables ou Parameter Store);
3. **Validar** que CRR manteve consistência (verificar S3 replication metrics);
4. **Após recuperação de us-east-1**: Executar sync reverso se necessário.

### 8.3 Restauração EKS (Aplicação)

#### 8.3.1 Redeploy via GitOps

**Quando utilizar**: Falha de cluster, corrupção de workloads.

**Procedimento**:

1. **Recriar cluster EKS** (se necessário) via Terraform:
   ```bash
   cd infrastructure/terraform/eks
   terraform plan
   terraform apply
   ```
2. **Reinstalar componentes base** (ingress controller, cert-manager, monitoring):
   ```bash
   helm install ingress-nginx ingress-nginx/ingress-nginx -f values-prod.yaml
   helm install cert-manager jetstack/cert-manager -f values-prod.yaml
   ```
3. **Reimplantar workloads** via ArgoCD sync ou Helm:
   ```bash
   helm install twyn-api ./charts/twyn-api -f values-prod.yaml
   ```
4. **Restaurar Persistent Volumes** (se aplicável):
   ```bash
   aws ec2 create-volume --snapshot-id snap-XXXXXXXXXX \
     --availability-zone us-east-1a --volume-type gp3
   ```
5. **Validar** health checks, endpoints de API e métricas;
6. **Atualizar DNS** se necessário (Route 53 / External-DNS).

**RTO estimado**: 2–4 horas (cluster completo) | **RPO**: N/A (stateless, dados em RDS/S3)

#### 8.3.2 Restauração de Persistent Volumes

**Procedimento**:

1. **Identificar EBS snapshots** via AWS Backup:
   ```bash
   aws backup list-recovery-points-by-resource \
     --resource-arn arn:aws:ec2:us-east-1:ACCOUNT:volume/vol-XXXXXXXX
   ```
2. **Restaurar volume** a partir do snapshot;
3. **Reattach** ao pod/node correspondente via PersistentVolume reclaim;
4. **Validar** dados restaurados.

### 8.4 Procedimento Completo de Failover DR

**Cenário**: Indisponibilidade total da região us-east-1.

**Tempo máximo para decisão de failover**: 30 minutos após confirmação de indisponibilidade regional.

**Sequência de failover**:

| Passo | Ação | Responsável | Tempo Est. |
|-------|------|-------------|------------|
| 1 | Confirmar indisponibilidade regional (AWS Health Dashboard + monitoramento) | DevOps Lead | 15 min |
| 2 | Notificar Gestor SGSI e CTO — decisão de failover | DevOps Lead | 15 min |
| 3 | Promover RDS Read Replica em us-west-2 | DevOps Lead | 30 min |
| 4 | Atualizar Secrets Manager endpoints (us-west-2) | DevOps Lead | 15 min |
| 5 | Criar/ativar cluster EKS em us-west-2 via Terraform | DevOps Lead | 60 min |
| 6 | Deploy de workloads via Helm/GitOps | Junior DevOps | 30 min |
| 7 | Atualizar Route 53 para apontar para us-west-2 | DevOps Lead | 5 min |
| 8 | Validar S3 CRR bucket como fonte de dados biométricos | Junior DevOps | 15 min |
| 9 | Smoke tests completos (API endpoints, auth, biometrics) | QA + DevOps | 30 min |
| 10 | Comunicar clientes B2B sobre status do serviço | Gestor SGSI | 15 min |
| **Total** | | | **~3,5 horas** |

**Pós-failover**:
- Monitoramento contínuo por 24 horas;
- Documentar incidente e tempos reais de recuperação;
- Planejar failback quando us-east-1 disponível;
- Atualizar runbooks com lições aprendidas.

---

## 9. Cronograma de Testes

> **⚠️ NOTA**: Testes de backup nunca foram realizados (GAP-004, RISK-006). A execução do primeiro ciclo de testes é **prioridade imediata** após aprovação desta política.

### 9.1 Cronograma

| Tipo de Teste | Frequência | Próxima Execução | Responsável |
|---------------|------------|-------------------|-------------|
| **Restore RDS (PITR)** | Trimestral | [Data — dentro de 30 dias da aprovação] | DevOps Lead |
| **Restore RDS (Snapshot)** | Trimestral | [Data — dentro de 30 dias da aprovação] | DevOps Lead |
| **Restore S3 (versionamento)** | Trimestral | [Data — dentro de 30 dias da aprovação] | Junior DevOps |
| **Restore EKS (GitOps redeploy)** | Trimestral | [Data — dentro de 30 dias da aprovação] | DevOps Lead |
| **Restore Secrets Manager** | Semestral | [Data — dentro de 60 dias da aprovação] | DevOps Lead |
| **DR Failover Drill completo** | Anual | [Data — dentro de 90 dias da aprovação] | DevOps Lead + Gestor SGSI |
| **Validação de integridade de backup** | Mensal | Contínuo (automatizado) | Automatizado (CloudWatch) |

### 9.2 Procedimentos de Teste

#### 9.2.1 Teste de Restore RDS

**Objetivo**: Validar que o backup do RDS pode ser restaurado e contém dados íntegros.

**Pré-requisitos**:
- Acesso IAM com permissões `rds:RestoreDBInstanceFromDBSnapshot`;
- VPC e security groups de staging disponíveis;
- Queries de validação pré-definidas.

**Passos**:

1. Selecionar o snapshot mais recente;
2. Restaurar em instância temporária no ambiente de staging:
   ```bash
   aws rds restore-db-instance-from-db-snapshot \
     --db-instance-identifier twyn-restore-test-$(date +%Y%m%d) \
     --db-snapshot-identifier [SNAPSHOT_ID] \
     --db-instance-class db.r6g.large \
     --no-multi-az \
     --vpc-security-group-ids sg-staging
   ```
3. Conectar à instância restaurada e executar validações:
   - Contagem de registros nas tabelas: `users`, `verifications`, `audit_logs`;
   - Verificar integridade referencial (foreign keys);
   - Executar query de verificação de dados biométricos (checksums);
   - Comparar contagens com métricas de produção.
4. Registrar tempo de restauração (RTO real);
5. Registrar ponto de recuperação (RPO real — diferença entre snapshot e dados atuais);
6. **Excluir instância temporária após teste**;
7. Documentar resultados no **Backup Test Log** (SGSI-BACKUP-TEST-LOG).

**Critérios de sucesso**:
- Instância restaurada com sucesso;
- Integridade referencial mantida;
- Dados biométricos íntegros (checksums válidos);
- RTO real ≤ 4 horas;
- RPO real ≤ 15 minutos.

#### 9.2.2 Teste de Restore S3

**Objetivo**: Validar restauração de objetos S3 via versionamento.

**Passos**:

1. Criar objeto de teste no bucket de staging;
2. Sobrescrever objeto (criando nova versão);
3. Restaurar versão anterior via `copy-object` com `versionId`;
4. Validar checksum SHA-256 do objeto restaurado;
5. Documentar resultados.

**Critérios de sucesso**:
- Versão anterior restaurada corretamente;
- Checksum corresponde ao original;
- Metadados preservados.

#### 9.2.3 Teste de Restore EKS

**Objetivo**: Validar capacidade de recriar workloads a partir do Git.

**Passos**:

1. Criar namespace de teste no cluster EKS de staging;
2. Executar deploy completo dos charts Helm do ambiente de produção:
   ```bash
   helm install twyn-api-test ./charts/twyn-api \
     -f values-staging.yaml -n restore-test
   ```
3. Validar que todos os pods estão em estado `Running`;
4. Executar health checks nos endpoints;
5. Validar conectividade com serviços dependentes;
6. Deletar namespace de teste;
7. Documentar resultados e tempo total.

#### 9.2.4 Teste de DR Failover (Anual)

**Objetivo**: Validar capacidade de failover completo para us-west-2.

**Pré-requisitos**:
- Janela de manutenção comunicada a clientes (mínimo 72h de antecedência);
- Runbook DR atualizado;
- Equipe completa disponível (DevOps Lead + Junior DevOps + Gestor SGSI).

**Passos**:

1. Simular indisponibilidade de us-east-1 (desabilitar Route 53 health check);
2. Executar procedimento de failover completo (Seção 8.4);
3. Validar todos os serviços operando em us-west-2;
4. Executar suite de testes de integração contra ambiente DR;
5. Validar dados biométricos acessíveis via S3 CRR bucket;
6. Medir e documentar RTO e RPO reais;
7. Executar failback para us-east-1;
8. Validar retorno à operação normal;
9. Documentar resultados, gaps e melhorias.

**Critérios de sucesso**:
- Failover completo em ≤ 4 horas (RTO);
- Perda de dados ≤ 15 minutos (RPO);
- Todos os endpoints de API operacionais em us-west-2;
- Dados biométricos acessíveis e íntegros;
- Failback bem-sucedido.

---

## 10. Resultados de Testes e Registro

### 10.1 Template de Registro de Teste

Cada teste de restauração deve ser documentado com:

| Campo | Descrição |
|-------|-----------|
| **Data do teste** | Data e hora de início |
| **Tipo de teste** | PITR / Snapshot / S3 / EKS / DR Drill |
| **Executor** | Nome do responsável pela execução |
| **Ambiente** | Staging / DR / Produção (somente DR drill) |
| **Backup utilizado** | Identificador do snapshot/versão utilizado |
| **Tempo de restauração (RTO real)** | HH:MM:SS |
| **Ponto de recuperação (RPO real)** | HH:MM:SS |
| **Resultado** | PASS / FAIL |
| **Problemas encontrados** | Descrição de falhas ou dificuldades |
| **Ações corretivas** | Melhorias identificadas e responsáveis |
| **Evidências** | Screenshots, logs, relatórios anexados |

Registros armazenados em: **SGSI-BACKUP-TEST-LOG**

---

## 11. Política de Retenção

### 11.1 Tabela de Retenção por Tipo de Dado

| Tipo de Dado | Classificação | Retenção Mínima | Storage Tier | Fundamentação |
|-------------|---------------|-----------------|-------------|---------------|
| **Dados biométricos (face templates)** | RESTRICTED | 5 anos | S3 Standard → Glacier (90d) → Deep Archive (365d) | LGPD Art. 16; requisito contratual B2B |
| **Imagens faciais (verificação)** | RESTRICTED | 2 anos | S3 Standard → Glacier (90d) | LGPD Art. 15, proporcionalidade |
| **Snapshots RDS (automáticos)** | CONFIDENTIAL | 35 dias | RDS native | AWS limite máximo para automated snapshots |
| **Snapshots RDS (manuais pré-deploy)** | CONFIDENTIAL | 90 dias | RDS native | Janela de rollback de releases |
| **Logs de auditoria (CloudTrail)** | CONFIDENTIAL | 2 anos (730 dias) | S3 Standard → Glacier (180d) | ISO 27001 A.8.15; compliance |
| **Logs de auditoria (LGPD)** | CONFIDENTIAL | 7 anos | S3 Glacier → Deep Archive (365d) | LGPD Art. 37; prescrição legal |
| **Application logs** | INTERNAL | 90 dias (CW) + 2 anos (S3) | CloudWatch → S3 Standard → Glacier | Troubleshooting + compliance |
| **VPC Flow Logs** | INTERNAL | 1 ano (365 dias) | S3 Standard → Glacier (180d) | Investigação de incidentes |
| **Terraform state** | CONFIDENTIAL | Indefinido (todas as versões) | S3 Standard | Rastreabilidade de infraestrutura |
| **Código-fonte (Git)** | CONFIDENTIAL | Indefinido | GitHub | Histórico de desenvolvimento |
| **Secrets (rotacionados)** | RESTRICTED | 2 versões (current + previous) | Secrets Manager | Rollback de rotação |
| **EBS Snapshots (PV)** | INTERNAL | 35 dias | EBS Snapshot | AWS Backup policy |

### 11.2 Procedimento de Exclusão

A exclusão de dados ao final do período de retenção deve:

1. Ser **autorizada** pelo Gestor SGSI (dados RESTRICTED/CONFIDENTIAL);
2. Ser **documentada** no registro de retenção;
3. Garantir **exclusão segura** (purge de versões S3, incluindo delete markers);
4. Incluir **exclusão em todas as réplicas** (DR, backups, archives);
5. Emitir **certificado de exclusão** para dados biométricos (LGPD Art. 16).

---

## 12. Papéis e Responsabilidades

| Papel | Responsabilidades |
|-------|-------------------|
| **CEO** | Aprovar esta política e alocar recursos necessários para implementação |
| **CTO** | Supervisionar arquitetura técnica de backup e DR; aprovar mudanças na estratégia |
| **Gestor SGSI** | Owner desta política; garantir conformidade; revisar resultados de testes; reportar na Management Review |
| **DevOps Lead** (operador primário) | Configurar e manter backups; executar restaurações; conduzir testes trimestrais; monitorar alertas; manter runbooks atualizados |
| **Junior DevOps** (operador backup) | Assistir em restaurações; executar testes sob supervisão; assumir responsabilidades em ausência do DevOps Lead |
| **DPO** (Data Protection Officer) | Validar conformidade LGPD dos procedimentos de backup de dados biométricos |
| **Equipe de Desenvolvimento** | Garantir que aplicações sejam compatíveis com procedimentos de restore; manter migrations e rollback scripts |
| **Auditoria Interna** | Verificar conformidade com esta política; revisar registros de teste |

### 12.1 Matriz RACI

| Atividade | CEO | CTO | Gestor SGSI | DevOps Lead | Jr DevOps | DPO |
|-----------|-----|-----|-------------|-------------|-----------|-----|
| Aprovar política | **A** | C | **R** | I | I | C |
| Configurar backups | I | **A** | C | **R** | C | I |
| Monitorar alertas | I | I | I | **R** | **R** | I |
| Executar restauração | I | **A** | I | **R** | C | I |
| Testar restauração (trimestral) | I | I | **A** | **R** | C | I |
| DR Drill (anual) | I | **A** | **R** | **R** | C | I |
| Revisar resultados | I | C | **R** | C | I | C |
| Reportar compliance | I | I | **R** | C | I | C |

*R = Responsável, A = Aprovador, C = Consultado, I = Informado*

---

## 13. Requisitos de Criptografia

### 13.1 Princípio

**Todos os backups DEVEM ser criptografados em repouso e em trânsito**, sem exceção.

### 13.2 Configuração de Criptografia por Serviço

| Serviço | Criptografia em Repouso | Criptografia em Trânsito | Chave |
|---------|------------------------|-------------------------|-------|
| **RDS Snapshots** | AES-256 (KMS) | TLS 1.2+ (automático AWS) | `alias/twyn-rds-cmk` |
| **S3 Buckets (biometria)** | SSE-KMS (AES-256) | TLS 1.2+ (bucket policy enforce) | `alias/twyn-s3-biometric-cmk` |
| **S3 Buckets (logs)** | SSE-KMS (AES-256) | TLS 1.2+ | `alias/twyn-logs-cmk` |
| **S3 Buckets (terraform)** | SSE-KMS (AES-256) | TLS 1.2+ | `alias/twyn-terraform-cmk` |
| **EBS Snapshots** | AES-256 (KMS) | N/A (snapshot at rest) | `alias/twyn-ebs-cmk` |
| **Secrets Manager** | AES-256 (KMS) | TLS 1.2+ (automático AWS) | `alias/twyn-secrets-cmk` |
| **CloudTrail Logs** | SSE-KMS (AES-256) | TLS 1.2+ | `alias/twyn-cloudtrail-cmk` |

### 13.3 Políticas de Chave KMS

- Todas as CMKs são gerenciadas via **Terraform** (key policies versionadas);
- Key rotation automática habilitada (anual);
- Acesso às chaves restrito via IAM policies (least privilege);
- Auditoria de uso de chaves via CloudTrail;
- CMKs da região DR (us-west-2) são chaves separadas (não réplicas);
- **Proibido** uso de SSE-S3 (chave gerenciada pela AWS) para dados RESTRICTED ou CONFIDENTIAL.

---

## 14. Conformidade Regulatória

### 14.1 LGPD (Lei 13.709/2018)

| Artigo LGPD | Requisito | Implementação nesta Política |
|-------------|-----------|------------------------------|
| **Art. 11** | Tratamento de dados pessoais sensíveis (biométricos) exige medidas de segurança reforçadas | Backups de dados biométricos com criptografia CMK, Object Lock, MFA Delete, CRR (Seção 5.2) |
| **Art. 15–16** | Eliminação de dados pessoais ao término do tratamento | Política de retenção com exclusão segura e certificado (Seção 11.2) |
| **Art. 37** | Manutenção de registro das operações de tratamento | Logs de auditoria retidos por 7 anos (Seção 5.6) |
| **Art. 46** | Medidas de segurança para proteção de dados pessoais | Criptografia obrigatória, controle de acesso, monitoramento de backups (Seções 13, 6) |
| **Art. 48** | Comunicação de incidentes à ANPD | Procedimentos de restauração documentados para minimizar impacto (Seção 8) |

### 14.2 ISO 27001:2022 — Controles Annex A

| Controle | Título | Implementação nesta Política |
|----------|--------|------------------------------|
| **A.5.29** | Segurança da informação durante disrupção | Procedimentos de restauração e DR failover (Seção 8) |
| **A.5.30** | Prontidão de TIC para continuidade de negócios | Estratégia de backup multi-região, testes periódicos (Seções 5, 9) |
| **A.8.13** | Backup de informações | Estratégia completa por serviço, monitoramento, retenção (Seções 5, 6, 11) |
| **A.8.14** | Redundância de instalações de processamento de informações | Multi-AZ, cross-region replication, DR (Seções 5.1, 5.2, 8.4) |

---

## 15. Indicadores de Performance (KPIs)

| KPI | Meta | Medição | Frequência | Responsável |
|-----|------|---------|------------|-------------|
| **Taxa de sucesso de backup** | ≥ 99,9% | (Backups bem-sucedidos / Total de backups programados) × 100 | Mensal | DevOps Lead |
| **Taxa de sucesso de teste de restore** | 100% | (Testes bem-sucedidos / Total de testes executados) × 100 | Trimestral | Gestor SGSI |
| **Compliance RPO** | 100% | % de backups que atendem RPO < 15 min | Mensal | DevOps Lead |
| **Compliance RTO** | 100% | % de restaurações que atendem RTO < 4h | Trimestral (em testes) | DevOps Lead |
| **Tempo médio de restauração** | < 2 horas | Média de RTO real nos testes trimestrais | Trimestral | DevOps Lead |
| **Frequência de testes de restore** | 4× / ano | Número de testes executados por ano | Anual | Gestor SGSI |
| **DR Drill executado** | 1× / ano | Drill anual completado com sucesso | Anual | Gestor SGSI |
| **Cobertura de monitoramento** | 100% | % de serviços com alarmes de backup configurados | Mensal | DevOps Lead |
| **Tempo de detecção de falha de backup** | < 15 minutos | Tempo entre falha e alerta disparado | Contínuo | Automatizado |

### 15.1 Reporting

- KPIs reportados **mensalmente** no Backup Compliance Report;
- Resultados consolidados apresentados na **Management Review** (ISO 27001, Cláusula 9.3);
- Desvios dos KPIs geram **ações corretivas** registradas no SGSI-CAPA-LOG;
- Dashboard de KPIs disponível no CloudWatch (**TWYN-Backup-KPIs**).

---

## 16. Exceções e Escalação

### 16.1 Processo de Exceção

Exceções a esta política devem seguir o processo formal:

1. **Solicitação escrita** (ticket ou email) com justificativa técnica e de negócio;
2. **Análise de risco** documentada pelo solicitante;
3. **Aprovação** pelo Gestor SGSI **e** CTO;
4. **Registro** no SGSI-EXCEPTIONS-LOG com:
   - Descrição da exceção;
   - Justificativa;
   - Riscos residuais aceitos;
   - Controles compensatórios implementados;
   - Data de expiração (máximo 12 meses);
   - Responsável pela revisão.
5. **Revisão** a cada 6 meses ou na renovação.

### 16.2 Exceções Proibidas

As seguintes exceções **NUNCA** são concedidas:

- Desabilitar criptografia de backups de dados RESTRICTED;
- Desabilitar Object Lock em buckets de dados biométricos;
- Reduzir retenção de backups abaixo dos mínimos regulatórios (LGPD);
- Eliminar monitoramento de falhas de backup;
- Pular testes trimestrais de restauração por mais de um ciclo consecutivo.

### 16.3 Escalação

| Nível | Gatilho | Escalado Para | Tempo |
|-------|---------|---------------|-------|
| **1** | Falha de backup individual | DevOps Lead | Imediato (alarme automático) |
| **2** | Falha recorrente (≥ 2 em 24h) ou falha em dados RESTRICTED | DevOps Lead + Gestor SGSI | < 1 hora |
| **3** | Falha sistêmica ou incapacidade de restauração | CTO + Gestor SGSI | < 2 horas |
| **4** | Perda de dados confirmada ou impacto em clientes | CEO + CTO + Gestor SGSI + DPO | Imediato |

---

## 17. Documentos Relacionados

| Doc ID | Título | Relação |
|--------|--------|---------|
| SGSI-POLICY-001 | Política de Segurança da Informação | Define RPO/RTO (Seção 11.1) — esta política DEVE estar alinhada |
| SGSI-DRP-001 | Disaster Recovery Plan | Procedimentos detalhados de DR referenciados na Seção 8.4 |
| SGSI-RISK-002 | Risk Register | RISK-006: Ausência de testes de backup |
| SGSI-GAP-004 | Gap Analysis — Backup Testing | Identifica que testes de backup nunca foram realizados |
| SGSI-SOA-001 | Statement of Applicability | Controles A.5.29, A.5.30, A.8.13, A.8.14 |
| SOP-002 | Change Management Procedure | Snapshots manuais pré-deploy |
| SGSI-IRP-001 | Incident Response Policy | Integração com procedimentos de restauração |
| SGSI-BACKUP-TEST-LOG | Registro de Testes de Backup | Resultados de testes trimestrais e DR drills |
| SGSI-CAPA-LOG | Registro de Ações Corretivas | Ações decorrentes de falhas em backup/restore |

---

## 18. Histórico de Revisões

| Versão | Data | Autor | Alterações | Aprovado Por |
|--------|------|-------|------------|-------------|
| 0.1 (Stub) | 26/05/2026 | Ricardo Esper (BEKAA) | Versão inicial (stub — 37 linhas) | — |
| 1.0 (Draft) | 02/06/2026 | Ricardo Esper (BEKAA) | Reescrita completa: estratégia por serviço, procedimentos de restauração, testes, retenção, KPIs, compliance LGPD, criptografia, DR failover. Alinhamento RPO/RTO com SGSI-POLICY-001. | **CEO (Pendente)** |

---

## 19. Assinaturas de Aprovação

**Owner — Gestor SGSI**
**Assinatura**: _______________________________
**Nome**: Enes Fernando Degasperi
**Data**: _____ / _____ / 2026

---

**Aprovador — CEO TWYN**
**Assinatura**: _______________________________
**Nome**: Enes Fernando Degasperi
**Data**: _____ / _____ / 2026

---

**Revisão Técnica — CTO**
**Assinatura**: _______________________________
**Nome**: Enes Fernando Degasperi
**Data**: _____ / _____ / 2026

---

**END OF DOCUMENT — SGSI-POLICY-005 v1.0**
