---
document_id: SGSI-PLAN-001
title: Plano de Monitoramento e Medição do SGSI
version: 1.0
status: Approved
classification: INTERNAL
owner: Gestor SGSI
approved_by: CEO
last_review: 2026-06-09
next_review: 2027-06-09
related_policies:
  - SGSI-POLICY-001
---

# Plano de Monitoramento, Medição, Análise e Avaliação do SGSI

## 1. Objetivo
Este documento define a metodologia da TWYN para monitorar, medir, analisar e avaliar o desempenho do Sistema de Gestão de Segurança da Informação (SGSI) e a eficácia de seus controles, em estrita conformidade com a **Cláusula 9.1 da ISO/IEC 27001:2022**.

## 2. Metodologia de Medição

Para garantir que a segurança da informação seja gerenciada proativamente, a TWYN monitora um conjunto definido de Indicadores Chave de Desempenho (KPIs).

O monitoramento segue o fluxo:
1. **Coleta**: O proprietário do controle extrai o dado da ferramenta (ex: AWS Security Hub, GitHub, Plataforma de Treinamento).
2. **Análise**: O Gestor SGSI compila os dados trimestralmente antes da Reunião de Análise Crítica (Management Review).
3. **Avaliação**: A Diretoria (CEO/CTO) avalia se as metas foram atingidas e define Ações Corretivas para métricas abaixo do limite.

## 3. Indicadores Chave de Desempenho (KPIs) Oficiais

Abaixo estão os indicadores oficiais medidos pela TWYN para avaliar o SGSI.

| ID | Métrica (O que medir) | Método (Como medir) | Responsável (Quem) | Frequência (Quando) | Meta de Sucesso |
|---|---|---|---|---|---|
| KPI-01 | **Treinamento de Conscientização** | Extração do relatório da plataforma de Security Awareness. | Gestor SGSI | Mensal | **100%** dos colaboradores ativos. |
| KPI-02 | **Endpoint Security (FDE & AV)** | Relatório do MDM/Inventário comprovando criptografia de disco. | DevOps Lead | Trimestral | **100%** dos equipamentos corporativos. |
| KPI-03 | **Revisão de Acessos IAM** | Execução e assinatura formal da recertificação trimestral (SOP-005). | DevOps Lead | Trimestral | **100%** executado no prazo. |
| KPI-04 | **Conformidade em Nuvem** | Pontuação de compliance no AWS Security Hub (CIS Benchmarks). | Cloud Infra | Semanal | **> 90%** (Nenhuma falha crítica). |
| KPI-05 | **Tempo de Resposta a Incidentes** | MTTR (Mean Time to Resolve) de incidentes críticos P0. | SecOps | Pós-Incidente | MTTR **< 4 horas**. |
| KPI-06 | **Testes de Disaster Recovery** | Execução com sucesso do restore do RDS para ambiente validado. | Cloud Infra | Semestral | RTO **< 4 horas** e RPO **< 24 horas**. |
| KPI-07 | **Gestão de Vulnerabilidades** | Quantidade de vulnerabilidades críticas em produção não patcheadas > 30 dias. | SecOps | Mensal | **Zero (0)**. |

## 4. Avaliação e Melhoria Contínua

Se qualquer KPI não atingir a meta estabelecida por 2 trimestres consecutivos, uma **Não-Conformidade Maior** deve ser levantada no Registro de Não-Conformidades e tratada imediatamente com um plano de ação formal.

## 5. Histórico de Revisão
- 1.0 (09/06/2026): Versão Inicial criada para sanar o GAP da Cláusula 9.1.
