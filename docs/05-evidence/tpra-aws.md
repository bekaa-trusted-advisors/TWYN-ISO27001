---
document_id: SGSI-TPRA-AWS
title: Third-Party Risk Assessment - Amazon Web Services (AWS)
version: 1.0
date: 2026-06-02
classification: INTERNAL
owner: Gestor SGSI
annex_a_controls: "A.5.19, A.5.21, A.5.22, A.5.23"
---

# Avaliação de Risco de Terceiros (TPRA) - AWS

## 1. Informações do Fornecedor
- **Nome do Fornecedor:** Amazon Web Services (AWS)
- **Serviço Prestado:** Hospedagem de infraestrutura em nuvem (EKS, RDS, S3, KMS, etc.)
- **Criticidade para o Negócio:** Crítico (Nível 1) - Hospeda o ambiente de produção, banco de dados e dados biométricos sensíveis da TWYN.

## 2. Metodologia de Avaliação
Como provedor de nuvem de hiperescala (Hyperscaler), a AWS não responde a questionários manuais de segurança. A conformidade é atestada através do modelo de responsabilidade compartilhada e da verificação de certificações públicas e relatórios de auditoria independentes.

## 3. Certificações e Relatórios de Conformidade Verificados
- **ISO/IEC 27001:2022:** Verificado.
- **ISO/IEC 27017:2015** (Segurança em Nuvem): Verificado.
- **ISO/IEC 27018:2019** (Privacidade em Nuvem): Verificado.
- **SOC 2 Type II:** Verificado.
- **Método de Obtenção:** Relatórios acessados e validados via portal [AWS Artifact](https://aws.amazon.com/artifact/) diretamente do console da conta da TWYN.

## 4. Análise de Risco de Segurança e Privacidade
- **Segurança Física:** Gerenciada pela AWS. Data centers possuem controles de acesso restritos e certificações militares/governamentais.
- **Segurança Lógica:** A AWS fornece ferramentas (KMS, IAM, VPC, Security Groups) que permitem à TWYN implementar segurança forte, incluindo criptografia at-rest e in-transit. O risco recai sobre a configuração correta da TWYN (Responsabilidade Compartilhada).
- **Tratamento de Dados Pessoais:** A AWS atua como sub-operadora de dados, provendo a infraestrutura. Os dados são armazenados na região `us-east-1` (EUA), requerendo mecanismos legais de transferência internacional previstos na LGPD.

## 5. Medidas Compensatórias (Responsabilidade TWYN)
Para utilizar a AWS de forma segura, a TWYN implementa as seguintes medidas mitigadoras:
1. MFA obrigatório para todos os acessos IAM.
2. Criptografia AES-256 habilitada em todos os buckets S3 e bases RDS usando chaves KMS gerenciadas pela TWYN (Customer Managed Keys).
3. Acesso à infraestrutura de produção isolado em redes privadas sem exposição pública direta, protegido via WAF e Load Balancers.

## 6. Conclusão e Parecer
O nível de segurança e maturidade da AWS excede os requisitos internos da TWYN. Os relatórios de auditoria de terceiros confirmam a eficácia dos controles do provedor.

- **Status da Avaliação:** **APROVADO**
- **Data da Avaliação:** 02/06/2026
- **Avaliador:** Ricardo Esper (Gestor SGSI / DPO)
- **Data da Próxima Revisão:** 02/06/2027
