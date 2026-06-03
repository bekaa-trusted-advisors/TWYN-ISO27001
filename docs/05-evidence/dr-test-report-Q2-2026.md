---
document_id: SGSI-EVID-DR-Q2-2026
title: Relatório de Teste de Disaster Recovery (Restore) - Q2 2026
date: 2026-06-03
---

# Relatório de Teste de Disaster Recovery - Q2 2026

**Este laudo serve como evidência probatória para atendimento dos Controles A.5.30 e A.8.13 da ISO/IEC 27001:2022.**

## 1. Informações do Teste
- **Data da Execução:** [PREENCHER_AQUI] (ex: 04/06/2026)
- **Responsável pela Execução:** [PREENCHER_AQUI] (Nome do Analista DevOps)
- **Ticket de Referência:** [PREENCHER_AQUI] (Link do Issue no GitHub/Linear)
- **Ambiente Restaurado:** RDS (PostgreSQL) para um cluster temporário (EKS Sandbox).

## 2. Métricas Alcançadas
De acordo com o BCP (Business Continuity Plan), o RTO máximo permitido é de 4 horas.

- **RPO Alcançado (Recovery Point Objective):** [PREENCHER_AQUI] (ex: "Utilizamos o snapshot gerado às 02h00 da manhã. RPO de 12 horas.")
- **Horário de Início do Restore:** [PREENCHER_AQUI]
- **Horário em que a API respondeu 200 OK:** [PREENCHER_AQUI]
- **RTO Atingido (Recovery Time Objective):** [PREENCHER_AQUI] (ex: "Demorou 45 minutos no total. SLA cumprido.")

## 3. Evidências Visuais (Anexos)

*(O analista deve substituir o texto abaixo pelos prints reais do teste)*

**Evidência 1: Acionamento do Restore**
> [!NOTE]
> *Coloque aqui o Print do console da AWS (ou log CLI) mostrando o início da restauração do snapshot.*

**Evidência 2: Banco de Dados Disponível**
> [!NOTE]
> *Coloque aqui o Print do painel do RDS mostrando a instância `dr-test-restore` com o status "Available" e o relógio da máquina visível.*

**Evidência 3: Validação da Aplicação**
> [!NOTE]
> *Coloque aqui o Print do terminal mostrando um `curl` no endpoint `/health` ou equivalente retornando `200 OK`, comprovando conectividade do app com o banco restaurado.*

## 4. Conclusão e Observações
- **O teste foi bem sucedido?** [SIM / NÃO]
- **Observações/Problemas encontrados:** [PREENCHER_AQUI] (Houve lentidão? Algum script falhou?)

---
**Status da Evidência:** Pendente de Execução pelo Time de Infraestrutura.
