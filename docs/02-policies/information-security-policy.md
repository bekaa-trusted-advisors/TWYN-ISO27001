---
document_id: SGSI-POLICY-001
title: Política de Segurança da Informação
version: 1.0
date: 2026-06-09
classification: Público
owner: Gestor SGSI
approved_by: CEO (Aprovado - Ata 001)
next_review: Anual
iso_clause: "5.2"
annex_a_controls: "A.5.1"
---

# Política de Segurança da Informação (PSI)

## Controle de Documento

| Propriedade | Detalhe |
|---|---|
| **ID do Documento** | SGSI-POLICY-001 |
| **Versão** | 1.0 |
| **Data de Aprovação** | 2026-06-09 |
| **Classificação** | Público |
| **Elaborado por** | Gestor SGSI |
| **Aprovado por** | CEO (Aprovado - Ata 001) |
| **Próxima Revisão** | Anual |


## 1. Declaração de Comprometimento da Alta Direção
A Alta Direção da **TWYN** reconhece a Segurança da Informação como um pilar fundamental para o negócio, especialmente por tratarmos dados sensíveis (biometria facial) sob o rigor da Lei Geral de Proteção de Dados (LGPD). 

O compromisso da diretoria está no fornecimento dos recursos necessários para o estabelecimento, implementação, manutenção e melhoria contínua do Sistema de Gestão de Segurança da Informação (SGSI), em conformidade com a norma **ISO/IEC 27001:2022**.

## 2. Propósito e Objetivos
Esta Política Mestra estabelece as diretrizes globais para a proteção das informações e dos sistemas da TWYN contra acesso não autorizado, uso indevido, divulgação, interrupção, modificação ou destruição.

Os objetivos de Segurança da Informação da TWYN são (Cláusula 6.2):
- Proteger a confidencialidade e integridade da **Face ID Platform API** e de todos os dados biométricos processados.
- Garantir a alta disponibilidade dos serviços oferecidos aos clientes.
- Atender a todos os requisitos legais (LGPD), regulatórios e contratuais aplicáveis.
- Minimizar o impacto de incidentes de segurança por meio de planos de resposta rápidos e eficazes.

## 3. Escopo
O SGSI abrange os processos de negócio, a infraestrutura em nuvem (AWS) e as pessoas (colaboradores e terceiros) que operam, gerenciam e suportam a **Face ID Platform API**. Estão excluídos do escopo as máquinas pessoais e as redes domésticas, sendo os riscos mitigados através de VPN e controles de endpoint.

## 4. Princípios Fundamentais
A TWYN baseia sua segurança na Tríade CIA:
- **Confidencialidade**: Garantir que as informações sejam acessíveis apenas àqueles autorizados (Least Privilege).
- **Integridade**: Proteger a precisão e a integridade da informação e dos métodos de processamento.
- **Disponibilidade**: Garantir que os usuários autorizados tenham acesso à informação e aos ativos associados quando necessário.

## 5. Estrutura de Políticas do SGSI
Esta Política de Segurança da Informação atua como documento-guia. As diretrizes técnicas e operacionais detalhadas encontram-se nas políticas específicas, que compõem a documentação do SGSI:
- **SGSI-POLICY-002**: Política de Controle de Acesso
- **SGSI-POLICY-003**: Política de Resposta a Incidentes
- **SGSI-POLICY-004**: Política de Gestão de Ativos
- **SGSI-POLICY-005**: Política de Backup e Recuperação
- **SGSI-POLICY-006**: Plano de Continuidade de Negócios (BCP/DR)
- **SGSI-POLICY-007**: Política de Uso Aceitável (AUP)
- E demais políticas correlatas estabelecidas no SGSI.

## 6. Papéis e Responsabilidades (Cláusula 5.3)
- **Alta Direção (CEO)**: Aprovar a PSI, garantir o alinhamento com os objetivos estratégicos e promover a cultura de segurança.
- **Gestor do SGSI**: Implementar, operar, monitorar e relatar o desempenho do SGSI para a Alta Direção.
- **Encarregado de Dados (DPO)**: Garantir a conformidade dos processos com a LGPD no que tange ao tratamento de dados pessoais.
- **Colaboradores e Terceiros**: Ler, compreender e assinar o Termo de Aceite desta e de outras políticas aplicáveis, reportando quaisquer incidentes ou vulnerabilidades identificadas.

## 7. Violações e Sanções
O descumprimento intencional ou por negligência das regras estabelecidas nesta política ou nas políticas subsidiárias será tratado como uma violação de segurança. As sanções aplicáveis podem variar desde advertências até a rescisão do contrato por justa causa e medidas legais, dependendo da gravidade e do impacto para a TWYN e seus clientes.

## 8. Revisão e Melhoria Contínua
Esta Política será revisada anualmente, ou sempre que ocorrerem mudanças significativas no ambiente de negócios, infraestrutura tecnológica ou cenário de ameaças. A TWYN se compromete a buscar ativamente a melhoria contínua do SGSI através de auditorias internas, análise de métricas e lições aprendidas de incidentes.

## 9. Procedimentos Relacionados (SOPs)

Esta política mestre é operacionalizada através dos seguintes procedimentos formais (SOPs):

- **[SGSI-SOP-001](../03-procedures/sop-001-onboarding-offboarding.md)**: Procedimento de Onboarding e Offboarding
- **[SGSI-SOP-002](../03-procedures/sop-002-change-management.md)**: Gestão de Mudanças
- **[SGSI-SOP-003](../03-procedures/sop-003-remote-work.md)**: Trabalho Remoto (Teletrabalho)
- **[SGSI-SOP-004](../03-procedures/sop-004-secrets-management.md)**: Gestão de Segredos e Chaves
- **[SGSI-SOP-005](../03-procedures/sop-005-iam-recertification.md)**: Recertificação Trimestral de Acessos

## 10. Histórico de Revisão
| Data | Versão | Autor | Descrição |
|------|--------|-------|-----------|
| 2026-06-09 | 1.0 | Gestor SGSI | Versão inicial aprovada - Consolidação da Política para conformidade ISO 27001 (PT-BR). |

