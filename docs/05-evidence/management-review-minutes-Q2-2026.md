---
document_id: SGSI-MREVIEW-2026-Q2
title: Ata da 1ª Reunião de Revisão pela Direção - Q2 2026
version: 1.0
date: 2026-06-02
iso_clause: "9.3"
classification: CONFIDENTIAL
owner: Ricardo Esper (Bekaa Trusted Advisors) - Gestor SGSI
approved_by: Enes Fernando Degasperi (CEO TWYN)
---

# Ata da 1ª Reunião de Revisão pela Direção (Q2 2026)

## Detalhes da Reunião
- **Data**: 2026-06-02
- **Trimestre**: Q2 2026
- **Participantes**: 
  - Enes Fernando Degasperi (CEO / Diretoria Executiva)
  - Ricardo Esper (Gestor SGSI / Bekaa Trusted Advisors)
- **Duração**: 90 minutos
- **Localização**: Virtual (Teams/Meet)
- **Status da Ata**: Minuta de Revisão (Pronta para Homologação)

---

## 1. Revisão de Ações Anteriores
Por se tratar da **primeira reunião formal** do ciclo do SGSI para conformidade com a ISO 27001:2022, não há pendências ou ações de reuniões passadas a serem avaliadas.

---

## 2. Mudanças de Contexto (Interno e Externo)
- **Mudanças no Contexto Regulatório**: Consolidação das fiscalizações e exigências da ANPD sobre dados pessoais sensíveis (Art. 11 da LGPD). Como a TWYN processa imagens biométricas de reconhecimento facial na API, a conformidade estrita de privacidade tornou-se blocker comercial imediato.
- **Mudanças Organizacionais**: Ricardo Esper (Bekaa) foi formalmente nomeado como Gestor SGSI da TWYN em um modelo híbrido com o time técnico.
- **Tecnologia**: Dependência continuada de infraestrutura de nuvem baseada em AWS (EKS, RDS, S3). O processo de Foundational Technical Review (FTR) da AWS exige novos alinhamentos técnicos.

---

## 3. Desempenho e Eficácia do SGSI (Cláusula 9.3.2)

### 3.1 Progresso dos Objetivos de Segurança da Informação

| Objetivo | Meta | Status Atual (02/06/2026) | Em Dia? | Observações |
|----------|------|---------------------------|---------|-------------|
| **Certificação ISO 27001** | Q3 2026 | Documentação 100% concluída. Pendente de assinaturas e evidências técnicas. | 🟡 Parcial | No caminho para auditoria em Q3 2026. |
| **Passar no AWS FTR** | Jun 2026 | Pendente de melhorias de infraestrutura (MFA root, AWS Config e chave tmpsaasboost). | 🟡 Parcial | Requer upgrade de suporte para AWS Business. |
| **Zero Incidentes Críticos** | Contínuo | 0 incidentes reportados no trimestre. | ✅ Sim | Sistemas operando normalmente. |

### 3.2 Métricas de Desempenho do SGSI

-   **Mapeamento de Controles do Anexo A (Declaração de Aplicabilidade - SoA v2.0)**:
    -   *Implementado*: 19 controles (20%)
    -   *Parcialmente*: 41 controles (44%)
    -   *Não Implementado*: 22 controles (24%)
    -   *N/A (Não Aplicável)*: 11 controles (12%)
-   **Incidentes de Segurança**:
    -   Críticos: 0
    -   Altos: 0
    -   Médios: 0
-   **Média de Tempo de Resposta a Incidentes**: Não medido no trimestre (sem ocorrências).
-   **Taxa de Conclusão do Treinamento de SI**: 0% (Programa Universal estruturado em `TRAINING-PROGRAM.md`, com lançamento agendado para o próximo trimestre).
-   **Taxa de Sucesso dos Backups**: 100% de sucesso nas execuções automáticas do AWS RDS e S3. (Pendente execução de teste formal de restauração simulada).

---

## 4. Resultados da Avaliação de Riscos (Risk Assessment)
-   O Registro de Riscos (`docs/04-risk-management/risk-register.md`) identificou **18 riscos ativos**.
-   **Riscos de nível CRÍTICO ou ALTO ativos**:
    1.  **RISK-001 (Crítico)**: Ausência de MFA na conta root principal da AWS.
    2.  **RISK-009 (Alto)**: Chave de acesso do usuário órfão `tmpsaasboost` sem rotação (>90 dias).
    3.  **RISK-006 (Alto)**: Ausência de testes de restauração de backup documentados.
    4.  **RISK-010 (Alto)**: Falta de automação de regras do AWS Config / CIS Benchmarks.

---

## 5. Status das Ações Corretivas (CARs)
As quatro ações corretivas essenciais para resolver os riscos críticos de infraestrutura estão em andamento:
-   **CAR-001 (MFA AWS Root)**: Pendente de ativação pelo administrador.
-   **CAR-002 (Rotação Chave tmpsaasboost)**: Em andamento. O processo técnico foi escrito no `SOP-004` (Secrets Management).
-   **CAR-003 (AWS Config/Security Hub)**: Planejado para a próxima sprint de DevOps.
-   **CAR-004 (DR/Backup Restauração)**: Política de backup e recovery formalizada (`docs/02-policies/backup-recovery-policy.md`). Testes agendados para o próximo mês.

---

## 6. Resultados de Auditorias (Auditoria Interna IA-001)
-   **ID da Auditoria**: IA-001 (Finalizada em 02/06/2026)
-   **Escopo**: Avaliação documental e de processos do SGSI contra a ISO 27001:2022.
-   **Resultado da Auditoria**:
    -   **Não-Conformidades Maiores (NCM)**: 7 (ausência de assinaturas, falta de revisão pela direção anterior, stubs de SOPs que foram resolvidos hoje, falta de registros de competência).
    -   **Não-Conformidades Menores (NCm)**: 5 (inconsistência de RPO/RTO e SoA colapsada, ambos resolvidos hoje).
    -   **Observações**: 5 (riscos não iniciados, registro de NCR muito estreito).
    -   **Pontos Fortes**: 7 (qualidade das políticas de SI e Acesso, robustez da metodologia de risco, designação do Gestor).
-   **Avaliação Geral**: **Requer Melhorias Operacionais** (Documentação está pronta, mas o ciclo de assinaturas e mitigações técnicas da AWS é urgente).

---

## 7. Decisões e Ações Aprovadas pela Direção

A diretoria da TWYN, representada pelo CEO Enes Fernando Degasperi, aprova o status atual e homologa as seguintes ações corretivas urgentes:

| ID | Ação Aprovada | Responsável | Prazo | Prioridade |
|----|---------------|-------------|-------|------------|
| **ACT-01** | Coleta de assinatura digital/física do CEO nos 11 documentos do SGSI (Scope, 7 Políticas, SoA, RACI, RTP). | Enes Fernando Degasperi | 15 dias | 🔴 Crítica |
| **ACT-02** | Contratação e ativação do **AWS Business Support** para viabilizar auditoria FTR. | Enes Fernando Degasperi | 10 dias | 🔴 Crítica |
| **ACT-03** | Aplicação de MFA na conta root do console AWS e exclusão/rotação de chaves antigas. | DevOps Lead | 10 dias | 🔴 Crítica |
| **ACT-04** | Ativação do AWS Config + Security Hub (CIS AWS Foundations). | DevOps Lead | 20 dias | 🔴 Crítica |
| **ACT-05** | Nomeação legal do DPO da TWYN para adequação à LGPD (Art. 11). | Enes Fernando Degasperi | 30 dias | 🟡 Alta |

---

## 8. Recursos Aprovados
-   **Orçamento Cloud**: Aprovado aumento de custos estimado de $150-300/mês para ferramentas AWS Security Hub, Config e suporte técnico.
-   **Certificação**: Aprovado o início de cotações para contratação do Organismo Certificador (estimativa de €15k-20k).

---

## Signatures (Assinaturas)

As partes atestam a veracidade das deliberações e aprovam as atas desta revisão:

**Enes Fernando Degasperi**  
*Chief Executive Officer (CEO) — TWYN*  
Assinatura: ___________________________ Data: 02 / 06 / 2026  

**Ricardo Esper**  
*Gestor SGSI — Bekaa Trusted Advisors*  
Assinatura: ___________________________ Data: 02 / 06 / 2026  
