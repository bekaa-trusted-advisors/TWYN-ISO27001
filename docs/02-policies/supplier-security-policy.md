---
document_id: SGSI-POLICY-009
title: Política de Segurança em Fornecedores
version: 1.0
date: 2026-06-09
classification: Público
owner: Gestor SGSI
approved_by: CEO (Aprovado)
next_review: Anual
annex_a_controls: "A.5.19, A.5.20, A.5.21, A.5.22, A.5.23"
---

# Política de Segurança em Fornecedores

## 1. Propósito
Esta política estabelece os controles de Segurança da Informação a serem aplicados no relacionamento da TWYN com fornecedores, contratados terceirizados e provedores de nuvem (CSP). O objetivo é mitigar os riscos associados ao acesso de terceiros aos ativos organizacionais, preservando a segurança, a continuidade dos negócios e a adequação à LGPD.

## 2. Escopo
Abrange fornecedores de serviços em nuvem (ex: AWS, GitHub), ferramentas SaaS de produtividade, e prestadores de serviço independentes que possuam acesso lógico a qualquer nível de informação confidencial ou a sistemas críticos da TWYN.

## 3. Avaliação e Seleção de Fornecedores (TPRA - A.5.19)
Devido ao modelo operacional da TWYN e ao uso de plataformas de hiperescala, a metodologia de **Third-Party Risk Assessment (TPRA)** é executada da seguinte maneira:

### 3.1 Provedores de Hiperescala (AWS, GitHub)
- O processo de avaliação consumirá relatórios de auditoria e certificados emitidos publicamente em seus respectivos portais de conformidade (*Trust Centers*).
- O Gestor do SGSI fará o download e a verificação de certificados relevantes (ISO 27001, SOC 2 Type II, CSA STAR) para assegurar o alinhamento de maturidade do fornecedor.

### 3.2 Contratados Menores ou Acesso Crítico
- Para prestadores de serviço locais ou empresas menores com acesso direto ao ambiente da TWYN, deve ser preenchido um Questionário de Segurança de Fornecedor.
- A contratação será condicionada a uma pontuação mínima de risco aceitável.

## 4. Requisitos Contratuais (A.5.20)
Todos os contratos firmados com fornecedores devem conter formalizações que garantam:
- **Acordo de Confidencialidade (NDA):** Assinado antes do compartilhamento de qualquer informação confidencial.
- **Acordo de Processamento de Dados (DPA):** Obrigatório sempre que o fornecedor atuar como sub-operador no tratamento de dados pessoais ou biométricos (requisito da LGPD).
- Cláusulas de obrigação de reporte de incidentes de violação de dados em prazo legal.
- Cláusulas garantindo o "Direito de Auditar" (substituível pela aceitação do SOC 2 / ISO do parceiro).

## 5. Segurança no Uso de Serviços em Nuvem (A.5.23)
A TWYN adota as seguintes práticas frente aos seus provedores (ex: AWS):
- **Modelo de Responsabilidade Compartilhada:** A TWYN reconhece e opera exclusivamente dentro do modelo definido pelo CSP. As configurações "In-Cloud" (ex: IAM, Security Groups, Criptografia KMS) são de inteira responsabilidade técnica da equipe da TWYN.
- O acesso a consoles de nuvem é restrito a indivíduos autorizados e sempre exige Autenticação Multifator (MFA).

## 6. Monitoramento de Fornecedores (A.5.22)
- O Gestor SGSI e o DevOps Lead devem monitorar ativamente a conformidade continuada dos fornecedores de grande porte (acompanhamento de caducidade de certificados e novos riscos).
- Permissões e direitos de acesso concedidos a contas de fornecedores devem ser revistos trimestralmente na Recertificação de Acessos (SOP-005).

## 7. Encerramento de Contrato
Ao finalizar o contrato com qualquer fornecedor ou prestador de serviço:
- Todo acesso lógico fornecido deve ser imediatamente revogado.
- O fornecedor deve confirmar formalmente a exclusão ou devolução de todos os dados e segredos operacionais da TWYN armazenados em seus ambientes.

## 8. Histórico de Revisão
| Data | Versão | Autor | Descrição |
|------|--------|-------|-----------|
| 2026-06-09 | 1.0 | Gestor SGSI | Conversão do cabeçalho para YAML e alinhamento ortográfico (PT-BR). |
