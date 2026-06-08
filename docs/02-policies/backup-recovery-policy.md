---
document_id: SGSI-POLICY-005
title: Backup & Recovery Policy
version: 2.0
date: 2026-06-02
annex_a_controls: "A.8.13"
owner: DevOps Lead
approved_by: CEO (Aprovado - Ata 001)
---

# Política de Backup e Recuperação

## 1. Propósito e Escopo
Esta política visa garantir que a TWYN possua mecanismos e regras estritas para cópias de segurança (backup) e restauração, prevenindo a perda acidental ou maliciosa de dados e garantindo a continuidade do negócio em linha com a ISO 27001 (Anexo A.8.13).
**Escopo:** Sistemas críticos, bancos de dados em nuvem, dados biométricos de clientes e arquivos corporativos de infraestrutura.

## 2. Princípios de Backup
Todos os sistemas hospedando dados classificados como CONFIDENCIAL e RESTRITO devem possuir mecanismos de backup automatizados ativos. O princípio adotado é a automação máxima: não deve haver dependência de trabalho manual para o ciclo de proteção.

### 2.1 Criptografia e Proteção do Backup
- **Em repouso (At Rest):** Todos os snapshots, backups de S3 e instâncias devem ser criptografados obrigatoriamente (AES-256) utilizando AWS KMS Customer Managed Keys.
- **Acesso:** O repositório de backup deve ter acesso estritamente restrito. Nenhum usuário da TWYN tem a capacidade de alterar ou deletar backups retidos que estejam marcados com bloqueio de exclusão (S3 Object Lock / AWS Backup Vault Lock).
- **Isolamento:** Os backups de produção devem preferencialmente residir em local isolado ou logicamente segregado do ambiente de onde são originados, ou utilizar políticas de versionamento no S3.

## 3. Matriz de Backup e Retenção

A TWYN adota a seguinte arquitetura de backup nativa na AWS:

| Categoria / Sistema | Ferramenta / Método | Frequência (Ciclo) | Período de Retenção | RPO |
|---------------------|---------------------|--------------------|---------------------|-----|
| **AWS RDS (PostgreSQL)** (Dados biométricos e logs) | AWS RDS Automated Backups (Snapshots diários) + PITR | Snapshot Diário. Logs a cada 5 min (PITR). | 30 Dias para o Snapshot completo. | 1 Hora |
| **AWS S3 (Imagens/Vetores Brutos)** | S3 Versioning + S3 Cross-Region Replication | Contínuo / Imediato a cada evento de objeto. | 30 Dias (objetos excluídos mantêm versão). | Quase Zero |
| **Infraestrutura como Código** (Terraform State) | S3 (Versionamento habilitado) | Contínuo (a cada apply). | 90 Dias | Quase Zero |
| **Bases Auxiliares/Ambiente Secundário** | Sem backup para ambiente Dev/Staging. | N/A | N/A | N/A |

### 3.1 Point-In-Time Recovery (PITR)
O banco de dados de produção (Face ID Platform) possui a função *Point-in-Time Recovery* ativada. Isso permite que a equipe reverta o banco de dados para qualquer segundo exato até o limite de 30 dias passados, o que é crítico para ataques granulares de ransomware ou corrupção de tabelas.

## 4. Procedimentos de Restauração

O backup só tem valor se puder ser restaurado. Somente o *DevOps Lead* possui a autoridade técnica (IAM Roles) para acionar restaurações sobre a infraestrutura produtiva. Em caso de desastre, a restauração segue as diretrizes do plano de Continuidade (SGSI-POLICY-006 / BCP).

### Passos Gerais de Restauração Segura (RDS):
1. Avaliar a integridade: Isolar o banco comprometido, mantendo-o vivo apenas para fins forenses (se necessário).
2. Via AWS Console ou CLI, instanciar um novo RDS a partir do Snapshot/PITR desejado.
3. Testar localmente a consistência do banco de dados restaurado.
4. Redirecionar o tráfego da API (Connection String) para a nova instância.

## 5. Testes Regulares de Backup (Restore Tests)
A eficácia dos backups deve ser provada por meio de exercícios práticos (A.8.13).

- **Periodicidade:** Testes de Restauração devem ser conduzidos, no mínimo, **semestralmente**.
- **Métrica a Testar:** O teste medirá o RTO real alcançado (tempo que levou para o banco estar disponível) e garantirá que o RPO foi atendido.
- **Relatório de Teste:** Toda simulação gerará um breve laudo reportando o tempo gasto, eventuais gargalos e se o banco subiu corretamente. Este relatório fica sob custódia do Gestor SGSI e arquivado na pasta `docs/05-evidence/dr-tests/`.

## 6. Papéis e Responsabilidades
- **DevOps Lead:** Configurar, monitorar e garantir as rotinas automatizadas no AWS (via Terraform). Responsável direto pela execução dos Restore Tests e execuções técnicas reais.
- **Gestor SGSI:** Auditar se a configuração técnica corresponde às obrigações legais, contratuais (ISO/LGPD) e se os testes semestrais estão em dia e bem-sucedidos.
- **Colaboradores:** Salvar todos os documentos e códigos corporativos nos repositórios oficiais (GitHub, Google Workspace). Máquinas locais (Laptops) não são contempladas por backup corporativo da TWYN.

---
*Política de Backup estabelecida para proteger os ativos críticos, aprovada em conformidade com o SGSI.*
