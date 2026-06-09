---
document_id: SGSI-MREVIEW-001
title: Ata de Revisão pela Direção (Management Review)
version: 1.0
date: 2026-06-09
iso_clause: "9.3"
classification: Internal
owner: Gestor SGSI
next_review: Trimestral
---

# Ata de Revisão pela Direção (Management Review)

## Detalhes da Reunião
- **Data**: 2026-06-09
- **Trimestre**: Q2 2026
- **Participantes**: Ricardo Esper (CEO, Gestor SGSI, DevOps Lead, DPO)
- **Duração**: 60 minutos
- **Local**: Virtual

## 1. Revisão de Ações Anteriores
| Item de Ação | Responsável | Prazo | Status | Notas |
|-------------|-------|----------|--------|-------|
| Preparação para Auditoria Interna | Gestor SGSI | 26/05/2026 | Concluído | Relatório IA-001 gerado. |

## 2. Mudanças (Internas e Externas)
- **Mudança de Escopo do SGSI**: A engenharia foi formalmente reclassificada como fornecedor interno. O escopo do SGSI agora reflete de maneira estrita a Hospedagem/Operação na AWS.
- **Estruturação de Políticas**: Criação do Adendo de Segurança de Fornecedores (SGSI-POLICY-011) para cobrar compliance do time de Dev.

## 3. Desempenho do SGSI (Cláusula 9.3.2)

### 3.1 Progresso dos Objetivos de Segurança da Informação
| Objetivo | Meta | Status Atual | No Caminho? | Problemas |
|-----------|--------|---------------|-----------|--------|
| Certificação ISO 27001 | Q3 2026 | Documentação Pronta (Fase 1) | Sim | Dependência de ajustes na AWS |
| Zero Incidentes Críticos | Contínuo | 0 incidentes | Sim | Nenhum |

### 3.2 KPIs e Métricas
- **% de controles do Anexo A aplicados**: Alvo 100% dos aplicáveis. Atual: ~85% (Faltando GAPs técnicos na AWS e endpoints).
- **Taxa de conclusão de Treinamentos**: Alvo 100%. Atual: 0% (Issue Aberta).
- **Testes de Restore de Backup**: Alvo 100% testado. Atual: 0% (GAP-004 aberto para execução hoje).

## 4. Feedback de Partes Interessadas
- O escopo reduzido foi bem recebido, mas requer validação rigorosa dos contratos e NDAs do fornecedor interno (Desenvolvimento).

## 5. Resultados da Avaliação de Riscos
- **Risco Reavaliado**: O risco de SPOF (RISK-015) do papel do DevOps Lead foi mitigado e justificado através da aceitação formal do uso de CloudTrail e dupla verificação de PRs como controles compensatórios. Risco Residual aceito pela Direção.

## 6. Status de Ações Corretivas (Principais GAPs)
| ID | Descrição | Status | Notas |
|--------|-------------|--------|-------|
| NC-MAJOR-06 | Nomeação do DPO à ANPD | FECHADO | Feito via carta de designação oficial. |
| GAP-003 | Habilitar AWS Config/CIS Benchmarks | ABERTO | Pendente deploy no Terraform. |
| GAP-004 | Teste de Restore de DR | ABERTO | Crítico para processamento de Biometria. |
| GAP-011 | Criptografia FDE de Endpoints | ABERTO | Pendente evidências (BitLocker/FileVault). |

## 7. Resultados da Auditoria Interna
- **ID da Auditoria**: IA-001
- **Não-Conformidades**: Maior: 6, Menor: 5 (Vários já mitigados após a auditoria).
- **Avaliação Geral**: Necessita Melhoria Técnica (Prontidão da Fase 1 garantida documentalmente, mas requer correção de infraestrutura para Fase 2).

## 8. Necessidade de Mudanças no SGSI
- Nenhuma mudança adicional de escopo é requerida. O modelo atual (Operações AWS) será defendido junto ao auditor externo.

## 9. Decisões Oficiais da Direção (Blockers Resolvidos)
1. **Aprovação de Políticas**: O CEO aprova formalmente todo o conjunto de políticas documentadas na pasta `docs/02-policies/`, alterando o status de todas de "Draft" para "Approved" (Isto resolve o GAP-006 / NC-MAJOR-02).
2. **Aprovação de Riscos**: O CEO aprova formalmente o Risk Treatment Plan (Plano de Tratamento de Riscos) e a Declaração de Aplicabilidade (SoA) em sua versão atual.

## 10. Próximos Passos (Ações Imediatas)
| Decisão/Ação | Responsável | Prazo | Prioridade |
|-----------------|-------|----------|----------|
| Executar código Terraform na AWS (Config/CloudTrail) | DevOps Lead | Hoje | Crítica |
| Tirar prints do BitLocker dos Laptops | DevOps Lead | Hoje | Alta |

---

**Assinaturas Digitais**:
- **CEO**: _[Assinado Digitalmente por Ricardo Esper]_ Data: 2026-06-09
- **Gestor SGSI**: _[Assinado Digitalmente por Ricardo Esper]_ Data: 2026-06-09

**Distribuição**: CEO, Gestor SGSI, DevOps Lead
**Retenção**: 3 anos
