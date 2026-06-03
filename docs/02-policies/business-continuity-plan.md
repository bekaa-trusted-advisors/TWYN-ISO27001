---
document_id: SGSI-POLICY-006
title: Business Continuity & Disaster Recovery Plan
version: 2.0
date: 2026-06-02
annex_a_controls: "A.5.29, A.5.30, A.8.14"
owner: Gestor SGSI
approved_by: CEO (Aprovado - Ata 001)
---

# Plano de Continuidade de Negócios e Disaster Recovery (BCP/DR)

## 1. Objetivo e Escopo
O objetivo deste documento é estabelecer os procedimentos, funções e responsabilidades para garantir que a TWYN continue a operar suas funções críticas e consiga recuperar a "Face ID Platform API" em níveis aceitáveis dentro dos prazos definidos após um desastre, crise ou incidente grave.

O escopo abrange:
- Infraestrutura em nuvem hospedada na AWS.
- Dados de clientes e biometria armazenados.
- Serviços prestados via API REST.
- Equipe de operações (DevOps) e gestão.

## 2. Governança e Declaração de Política
A continuidade de negócios e prontidão da TIC (A.5.29, A.5.30) são essenciais para a resiliência da TWYN. A alta direção compromete-se a fornecer os recursos necessários para garantir que a arquitetura AWS possua alta disponibilidade (High Availability) nativa e capacidade de recuperação de desastres (DR) testada.

## 3. Business Impact Analysis (BIA)
A Análise de Impacto nos Negócios identifica as funções críticas da TWYN e os limites de tempo de inatividade e perda de dados toleráveis.

### 3.1 Sistemas Críticos Identificados
1. **Face ID Platform API** (Serviço principal de validação biométrica).
2. **AWS RDS PostgreSQL** (Banco de dados de transações e logs).
3. **AWS S3 Buckets** (Armazenamento de artefatos/vetores).
4. **AWS KMS** (Chaves de criptografia).

### 3.2 Definição de RTO e RPO
- **RTO (Recovery Time Objective):** Tempo máximo tolerável de inatividade.
  - *Definido para a API:* **4 Horas**. O sistema deve voltar a operar em até 4 horas após a declaração do desastre.
- **RPO (Recovery Point Objective):** Perda máxima tolerável de dados.
  - *Definido para o Banco de Dados:* **1 Hora**. Isso significa que, no pior cenário, perdemos no máximo 1 hora de transações de validação biométrica.

## 4. Cenários de Desastre e Estratégias de Mitigação

### Cenário 1: Queda completa de uma Availability Zone (AZ) na AWS
- **Probabilidade:** Baixa a Média.
- **Impacto:** Degradação temporária.
- **Estratégia (Mitigação Nativa):** A arquitetura da TWYN roda nativamente com o Amazon EKS em *Multi-AZ* e o RDS também configurado como *Multi-AZ*. A transição (failover) deve ocorrer automaticamente sem intervenção manual. O impacto real será apenas latência e tempo de failover DNS (geralmente < 5 minutos).
- **Procedimento DR:** A equipe apenas monitora via CloudWatch e verifica a restauração do *health check*.

### Cenário 2: Perda de Dados (Ransomware ou Corrupção Acidental de Banco de Dados)
- **Probabilidade:** Baixa.
- **Impacto:** Crítico (Violação de Integridade).
- **Estratégia:** Restauração a partir do Snapshot automatizado da AWS ou Point-In-Time-Recovery (PITR).
- **Procedimento DR:** 
  1. O DevOps Lead isola o banco de dados comprometido (Snapshot forense).
  2. Executa a restauração PITR usando o RDS Console/CLI para o momento imediatamente anterior ao incidente.
  3. Redireciona a string de conexão no Kubernetes (via AWS Secrets Manager) para o novo banco de dados.
  4. SLA de execução: < 4 Horas.

### Cenário 3: Queda Completa da Região AWS (us-east-1)
- **Probabilidade:** Muito Baixa.
- **Impacto:** Crítico (Downtime Total).
- **Estratégia:** Pilot Light / Backup & Restore em região secundária (`us-east-2`).
- **Procedimento DR:**
  1. O Comitê de Crise (CEO + Gestor SGSI + DevOps Lead) decreta estado de desastre.
  2. DevOps aciona o pipeline de Infraestrutura como Código (Terraform) na região `us-east-2`.
  3. O último Snapshot inter-regional (Cross-Region Snapshot) do RDS é restaurado.
  4. O Roteamento DNS (Route53) é atualizado para os novos Ingress Controllers.

### Cenário 4: Indisponibilidade Prolongada do Time Técnico
- **Probabilidade:** Baixa.
- **Impacto:** Alto (Impossibilidade de reagir a incidentes).
- **Estratégia:** Documentação abrangente e eliminação de SPOFs (Single Points of Failure) operacionais. Todo o provisionamento de infraestrutura é mantido como código no GitHub. A credencial de root "Break Glass" no cofre físico permite recuperação de acesso emergencial pelo CEO.

## 5. Equipe e Comitê de Continuidade (DRT - Disaster Recovery Team)
| Papel | Nome / Função | Responsabilidades Durante Crise | Contato de Emergência |
|-------|---------------|----------------------------------|------------------------|
| **Comandante de Crise** | Enes / CEO | Aprova failovers, comunica clientes e mídia. Toma decisões finais. | Celular cadastrado no AD |
| **Coordenador de DR** | DevOps Lead | Executa as tarefas técnicas de restauração de banco, roteamento e IaC. | Celular e Slack / PagerDuty |
| **Avaliador de Impacto / Compliance** | Ricardo / Gestor SGSI | Garante que a restauração obedece às exigências de privacidade (KMS/LGPD) e reporta incidentes à ANPD. | Email / Telefone |

## 6. Procedimento Geral de Declaração de Desastre
1. **Ativação:** Qualquer alerta de P0 durando mais de 30 minutos ininterruptos aciona a análise técnica para BCP.
2. **Declaração:** Apenas o CEO e o Gestor SGSI (em consenso) podem declarar formalmente um desastre para executar um *Cross-Region Failover*.
3. **Comunicação:** O Comitê notifica os clientes (SLA de notificação: < 2h a partir do evento).
4. **Recuperação:** O Coordenador de DR (DevOps Lead) atua conforme Seção 4.
5. **Retorno à Normalidade (Failback):** Quando a infraestrutura principal (ou região original) voltar, planeja-se uma janela de manutenção para retornar o tráfego em estado seguro.

## 7. Exercícios e Testes de BCP
O plano de continuidade de negócios da TIC (A.5.30) não é eficaz se não for testado.
- **Tabletop Exercise (Simulação de Mesa):** Ocorre anualmente com o Comitê (CEO, Gestor, DevOps) para validar fluxos de comunicação.
- **Teste de Restauração de Backup (Restore Test):** Ocorre semestralmente. A equipe DevOps deverá subir o banco de dados a partir do PITR em um ambiente isolado (Staging) para validar a integridade e cronometrar o RTO real.
- As atas dos testes ficam arquivadas na pasta `docs/05-evidence/dr-tests/`.

## 8. Manutenção do Plano
Este plano deve ser atualizado pelo menos uma vez por ano, ou quando houver mudanças arquiteturais significativas (ex: migração de nuvem, refatoração severa de banco de dados).

---
*Revisado e Aprovado nos termos do Sistema de Gestão de Segurança da Informação da TWYN.*
