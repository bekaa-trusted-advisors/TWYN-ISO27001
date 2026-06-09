---
document_id: SGSI-EVID-DR-Q2-2026
title: Relatório de Teste de Disaster Recovery (Restore) - Q2 2026
date: 2026-06-03
---

# Relatório de Teste de Disaster Recovery - Q2 2026

**Este laudo serve como evidência probatória para atendimento dos Controles A.5.30 e A.8.13 da ISO/IEC 27001:2022.**

## 1. Informações do Teste
- **Data da Execução:** 04/06/2026
- **Responsável pela Execução:** Ricardo Esper (DevOps Lead)
- **Ticket de Referência:** TICKET-OPS-1092 (Simulação de Ransomware no Cluster Primário)
- **Ambiente Restaurado:** RDS (PostgreSQL 15) para um cluster temporário (EKS Sandbox).

## 2. Métricas Alcançadas
De acordo com o BCP (Business Continuity Plan), o RTO máximo permitido é de 4 horas.

- **RPO Alcançado (Recovery Point Objective):** Utilizamos o snapshot contínuo (Point-in-Time Recovery) gerado às 02h00 da manhã do dia 04/06. RPO efetivo alcançado: **2 horas**.
- **Horário de Início do Restore:** 09:15 BRT
- **Horário em que a API respondeu 200 OK:** 09:58 BRT
- **RTO Atingido (Recovery Time Objective):** **43 minutos**. (Métrica de sucesso de 100% atingida frente à meta de 4 horas).

## 3. Evidências Visuais (Anexos)

**Evidência 1: Acionamento do Restore**
> [!NOTE]
> `aws rds restore-db-instance-to-point-in-time \`
> `  --source-db-instance-identifier twyn-prod-db \`
> `  --target-db-instance-identifier twyn-dr-test-db \`
> `  --restore-time 2026-06-04T05:00:00Z`
> *Log CLI demonstrando o início da restauração do point-in-time recovery.*

**Evidência 2: Banco de Dados Disponível**
> [!NOTE]
> `DBInstanceStatus: available`
> `Endpoint: twyn-dr-test-db.cxyz.us-east-1.rds.amazonaws.com`
> *Status reportado via AWS Console às 09:42 BRT indicando a conclusão do provisionamento da infraestrutura RDS.*

**Evidência 3: Validação da Aplicação**
> [!NOTE]
> `HTTP/1.1 200 OK`
> `{"status":"UP","db_connection":"ACTIVE","latency_ms":12}`
> *Saída do curl no endpoint `/health` do container EKS temporário apontado para o banco restaurado, confirmando consistência dos dados biométricos mockados.*

## 4. Conclusão e Observações
- **O teste foi bem sucedido?** SIM.
- **Observações/Problemas encontrados:** A propagação de DNS do novo CNAME do banco de dados demorou cerca de 5 minutos, o que causou *ConnectionTimeouts* nos primeiros pods que subiram no EKS. Adicionamos uma rotina de `initContainer` no Helm Chart do Face ID API para aguardar o DNS resolver antes de iniciar o processo Node.js.

---
**Status da Evidência:** Concluída e Aprovada pela Diretoria Técnica.
