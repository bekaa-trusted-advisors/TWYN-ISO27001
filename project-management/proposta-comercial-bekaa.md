# Proposta Técnica e Comercial
**Consultoria para Implantação e Preparação para Certificação ISO/IEC 27001:2022**

**Cliente:** TWYN  
**Consultoria:** Bekaa Trusted Advisors  
**Modelo:** Fast Track (6 meses) – Cloud & DevOps Focus  
**Data:** 02/02/2026

*Esta é uma proposta formal estruturada para a TWYN, baseada no modelo comercial e metodológico da Bekaa Trusted Advisors e adaptada tecnicamente para o cenário de nuvem AWS e DevOps.*

---

## Sumário Executivo
O objetivo deste projeto é estruturar e preparar o Sistema de Gestão de Segurança da Informação (SGSI) da TWYN para prontidão à auditoria de certificação ISO/IEC 27001:2022. A abordagem será pragmática e orientada a evidências objetivas, alinhada à operação em nuvem da TWYN.

### Diferenciais da Abordagem:
- **Foco em Automação Cloud:** Utilização das ferramentas nativas da AWS (como AWS Artifact e CloudTrail) para reduzir a carga administrativa e gerar evidências de auditoria de forma contínua.
- **Metodologia Fast Track:** Ciclo de 6 meses focado em eficiência, garantindo que a organização esteja pronta para as auditorias Stage 1 e Stage 2.
- **Escopo Estratégico:** Delimitação precisa das fronteiras para focar na operação e infraestrutura, otimizando o esforço de certificação.

---

## Escopo do SGSI
O escopo foi desenhado para cobrir a operação crítica dos serviços na nuvem, estabelecendo uma fronteira clara no pipeline de entrega para isolar o desenvolvimento de software proprietário da auditoria de infraestrutura.

> *"SGSI aplicado à operação e sustentação dos serviços de API hospedados em ambiente de nuvem AWS, abrangendo a gestão de infraestrutura como código (IaC), orquestração de containers/funções, segurança de rede lógica, gestão de segredos e monitoramento de eventos, limitando-se ao ambiente produtivo e pipelines de entrega."*

### Ativos e Fronteiras:
- **Infraestrutura:** API Gateway, Computação (Lambda/ECS), Networking (VPC) e Gestão de Segredos.
- **Fronteira Lógica:** O escopo de auditoria inicia-se a partir da entrada no pipeline (CI/CD), onde ferramentas de segurança automatizada validam o código antes do deploy no ambiente produtivo.

---

## Metodologia de Trabalho
A consultoria atua como orientadora estratégica, transferindo *know-how* para que a TWYN mantenha a autonomia sobre o seu SGSI.

### A. Gestão de Riscos e SoA
- **Gestão de Riscos (ISO 27005):** Identificação de riscos técnicos específicos do ambiente AWS e riscos de negócio, com definição de plano de tratamento e aceite formal pela liderança.
- **Declaração de Aplicabilidade (SoA):** Análise dos 93 controles do Anexo A da ISO 27001:2022.
  - *Nota sobre Desenvolvimento:* Os controles de desenvolvimento seguro (A.8.25 a A.8.30) serão avaliados sob a ótica de segurança do pipeline e Infrastructure as Code (IaC), conforme a estratégia de escopo definida.

### B. Preparação Orientada a Evidências
A metodologia utiliza o conceito de *Evidence Pack*, uma matriz que vincula cada controle aplicável a uma evidência técnica objetiva. No caso da TWYN, o foco será extrair essas evidências diretamente de logs e configurações da AWS para garantir rastreabilidade e auditabilidade sem burocracia excessiva.

---

## Entregas do Projeto
1. **Documentação Completa:** Documentação completa do SGSI (políticas, procedimentos, matriz de riscos, SoA).
2. **Relatórios de Análise:** Relatórios de análise (Gap Analysis, Security Assessment, Evidence Pack).
3. **Auditoria e Transferência:** Auditoria interna simulada e transferência de conhecimento.

---

## Cronograma: Fast Track (6 Meses)
O projeto segue um fluxo estruturado com governança quinzenal para garantir o cumprimento dos prazos.

- **Fase 1 – Diagnóstico (Mês 1)**
  - Kick-off e entendimento detalhado do ambiente AWS.
  - Relatório de Gap Analysis inicial.
- **Fase 2 – Riscos e SoA (Mês 2)**
  - Elaboração da Matriz de Riscos e definição do plano de tratamento.
  - Aprovação da Declaração de Aplicabilidade (SoA).
- **Fase 3 – Implementação (Meses 3 e 4)**
  - Definição e escrita de políticas e procedimentos.
  - Coleta e organização das evidências técnicas (configurações AWS, logs, relatórios).
- **Fase 4 – Auditoria e Prontidão (Meses 5 e 6)**
  - Realização da Auditoria Interna Simulada.
  - Plano de Ação Corretiva (CAPA) e Análise Crítica pela Direção.
  - Preparação final para a auditoria externa.

---

## Riscos e Premissas do Projeto

### Premissas fundamentais para o sucesso do projeto:
- **Disponibilidade:** 20h/mês da equipe técnica TWYN e 8h/mês da liderança.
- **Infraestrutura AWS operacional:** com CloudTrail, IAM e VPC já configurados.
- Custos adicionais (deslocamento, hospedagem, licenças) são de responsabilidade do cliente.

### Riscos Identificados
- **Atraso na Disponibilidade:** Mitigação - Governança quinzenal com acompanhamento de marcos e alertas antecipados.
- **Mudanças de Escopo:** Mitigação - Escopo aprovado no kick-off. Alterações requerem aditivo contratual.

---

## Limites e Responsabilidades
Para garantir a transparência e o sucesso da parceria:

### Responsabilidades da Consultoria (Bekaa)
- Fornecer metodologia, templates e orientação especializada.
- Conduzir a auditoria interna simulada e apoiar na interpretação da norma.

### Responsabilidades do Cliente (TWYN)
- **Execução Técnica:** Configuração de serviços (ex: IAM, CloudTrail, Security Groups) e aplicação de correções na infraestrutura AWS. A consultoria não possui acesso administrativo ao ambiente do cliente.
- **Tomada de Decisão:** Aprovação de políticas, aceitação de riscos e contratação do organismo certificador independente (custos de auditoria externa não inclusos).

---

## Investimento Estimado
Considerando o escopo de atuação remota e a complexidade do ambiente:

- **Investimento Total:** R$ 47.655,00.

**Condições de pagamento:**
- **Entrada (no aceite):** R$ 7.942,50
- **Saldo:** 5 parcelas mensais de R$ 7.942,50

### Composição do Investimento
O valor proposto reflete a complexidade técnica do ambiente cloud-native e a expertise especializada necessária para certificação ISO 27001 em infraestrutura AWS:
- **120 horas** de consultoria especializada distribuídas em 6 meses, incluindo documentação completa do SGSI, análises de segurança, auditoria interna simulada e governança quinzenal.
- *Não inclusos:* Certificação externa pelo organismo certificador (R$ 15-25k), licenças de software, despesas com deslocamento/hospedagem.

---
**Obrigado**  
*Bekaa Trusted Advisors*  
Preparando a TWYN para a excelência em Segurança da Informação.
