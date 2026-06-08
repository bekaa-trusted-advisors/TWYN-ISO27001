---
**Document Control**
| Campo | Valor |
|-------|-------|
| **Document ID** | SGSI-POLICY-009 |
| **Version** | 1.0 |
| **Author** | BEKAA Consultoria — Ricardo Esper |
| **Approved By** | **[CEO TWYN]** ⚠️ ASSINATURA OBRIGATÓRIA |
| **Approval Date** | [Pendente] |
| **Effective Date** | [Pendente] |
| **Próxima Revisão** | Anual após aprovação |
| **ISO 27001:2022 Mapping** | **A.5.19**, **A.5.20**, **A.5.21**, **A.5.22**, **A.5.23** |
| **Classification** | **PUBLIC** |
---

# Política de Segurança em Fornecedores
## Supplier Security Policy — TWYN

---

## 1. Propósito

Esta política estabelece os controles de Segurança da Informação a serem aplicados no relacionamento da TWYN com fornecedores, contratados terceirizados e provedores de nuvem. O objetivo é mitigar os riscos associados ao acesso de terceiros aos ativos organizacionais, preservando a segurança, continuidade e adequação à LGPD.

---

## 2. Escopo

Esta política abrange fornecedores de serviços em nuvem (ex: AWS, GitHub, Vercel), ferramentas SaaS de produtividade e contratados independentes (PJ/Freelancers) que possuam acesso lógico a qualquer nível de informação confidencial ou sistemas críticos da TWYN.

---

## 3. Avaliação e Seleção de Fornecedores (TPRA)

Devido ao modelo operacional da TWYN e ao uso de plataformas de hiper-escala e serviços SaaS globalmente reconhecidos, a metodologia de **Third-Party Risk Assessment (TPRA)** é executada da seguinte maneira:

### 3.1 Fornecedores de Grande Porte / Hiperescaladores
Para provedores mundiais como AWS, GitHub, Google, Vercel, entre outros:
- O processo de avaliação consumirá relatórios de auditoria e certificados emitidos publicamente em seus respectivos portais de conformidade (*Trust Centers*).
- O Gestor SGSI da TWYN fará o download e a verificação de certificados relevantes (ISO 27001, SOC 2 Type II, CSA STAR) para assegurar o alinhamento de maturidade do fornecedor.
- O resultado dessa avaliação deve ser condensado em um relatório simplificado de aceitação do fornecedor, anexado como evidência.

### 3.2 Contratados Menores ou Acesso Crítico
Para prestadores de serviço locais ou empresas menores com acesso direto ao ambiente da TWYN:
- Deve ser preenchido um Questionário de Segurança do Fornecedor.
- A contratação será condicionada a uma pontuação mínima de risco aceitável.

---

## 4. Requisitos Contratuais

Todos os contratos firmados com fornecedores devem conter formalizações que garantam:
- **Acordos de Confidencialidade (NDA):** Assinados antes do compartilhamento de qualquer informação da TWYN.
- **Acordo de Processamento de Dados (DPA):** Obrigatório sempre que o fornecedor atuar como sub-operador no tratamento de dados pessoais ou biométricos (requisito LGPD).
- Cláusulas de obrigação de reporte de violações de dados em tempo hábil.
- Cláusulas garantindo o "Direito de Auditar" (mesmo que substituído pela aceitação do SOC 2 / ISO do parceiro).

---

## 5. Segurança no Uso de Serviços em Nuvem (Cloud Security)

Conforme controle A.5.23, a TWYN adota as seguintes práticas frente aos seus provedores (ex: AWS):
- **Modelo de Responsabilidade Compartilhada:** A TWYN reconhece e opera exclusivamente dentro do modelo definido pelo CSP (Cloud Service Provider).
- As configurações de segurança no nível "In-Cloud" (IAM, SecGroups, Criptografia) são de responsabilidade integral da equipe da TWYN.
- O acesso a consoles de nuvem é restrito a indivíduos autorizados e sempre exige Autenticação Multifator (MFA).

---

## 6. Monitoramento de Fornecedores

- O Gestor SGSI e o DevOps Lead devem monitorar ativamente a conformidade continuada dos fornecedores de grande porte (acompanhamento de caducidade de certificados ISO/SOC).
- As permissões e direitos de acesso concedidos a contas de fornecedores e integrações OIDC devem ser revistas trimestralmente na Recertificação de Acessos (SOP-005).

---

## 7. Encerramento de Contrato

Ao finalizar o contrato com qualquer fornecedor:
- Todo acesso lógico fornecido deve ser imediatamente revogado.
- O fornecedor deve confirmar a exclusão de todos os dados e segredos operacionais da TWYN armazenados em seus ambientes.
