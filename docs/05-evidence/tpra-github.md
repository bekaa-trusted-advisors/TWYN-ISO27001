---
document_id: SGSI-TPRA-GITHUB
title: Third-Party Risk Assessment - GitHub
version: 1.0
date: 2026-06-02
classification: INTERNAL
owner: Gestor SGSI
annex_a_controls: "A.5.19, A.5.21, A.5.22, A.5.23"
---

# Avaliação de Risco de Terceiros (TPRA) - GitHub

## 1. Informações do Fornecedor
- **Nome do Fornecedor:** GitHub, Inc. (Microsoft Corporation)
- **Serviço Prestado:** Hospedagem de código-fonte (Source Code Management) e pipelines de CI/CD (GitHub Actions).
- **Criticidade para o Negócio:** Crítico (Nível 1) - Armazena a propriedade intelectual (código-fonte), configurações de infraestrutura (Terraform) e fluxos de automação para implantação da plataforma Face ID.

## 2. Metodologia de Avaliação
O GitHub, sendo um provedor de hiperescala, não preenche questionários manuais de segurança de terceiros. A avaliação e aprovação de conformidade são baseadas na análise de seus relatórios independentes e certificações globais, disponibilizados através do portal corporativo do GitHub e Microsoft Trust Center.

## 3. Certificações e Relatórios de Conformidade Verificados
- **ISO/IEC 27001:2022:** Verificado.
- **ISO/IEC 27018:** Verificado.
- **SOC 1 e SOC 2 Type II:** Verificado.
- **Método de Obtenção:** Documentos obtidos através do [GitHub Security/Compliance Trust Center](https://github.com/security) por administradores autorizados.

## 4. Análise de Risco de Segurança e Privacidade
- **Confidencialidade do Código:** Todo o código-fonte proprietário da TWYN está hospedado na nuvem do GitHub. O risco principal reside no vazamento do código-fonte ou segredos vazados no código (hardcoded secrets).
- **Cadeia de Suprimentos (Supply Chain):** Comprometimento do GitHub Actions pode levar à implantação de código malicioso no ambiente AWS (supply chain attack).
- **Proteção de Dados:** O GitHub armazena majoritariamente dados corporativos e código. Dados pessoais (biometria) **NÃO** devem transitar ou ser armazenados no GitHub. 

## 5. Medidas Compensatórias (Responsabilidade TWYN)
Para mitigar os riscos no uso da plataforma, a TWYN implementa e gerencia os seguintes controles:
1. **Autenticação e Acesso:** MFA obrigatório para todas as contas de desenvolvedores (SOP-001).
2. **Segredos:** É estritamente proibido fazer commit de segredos (senhas, chaves) no código. Utiliza-se OIDC (OpenID Connect) para que o GitHub Actions acesse a AWS sem armazenar chaves de longa duração.
3. **Revisão de Código:** Todas as alterações enviadas para produção requerem revisão por pares (Pull Requests) e verificações automáticas (SOP-002).

## 6. Conclusão e Parecer
O GitHub apresenta um ecossistema de segurança altamente maduro e testado. Os relatórios de conformidade evidenciam a eficácia dos seus controles organizacionais e técnicos.

- **Status da Avaliação:** **APROVADO**
- **Data da Avaliação:** 02/06/2026
- **Avaliador:** Ricardo Esper (Gestor SGSI / DPO)
- **Data da Próxima Revisão:** 02/06/2027
