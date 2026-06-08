# Evidência: Recertificação de Acessos IAM e GitHub

**Controle Anexo A:** A.5.18 (Direitos de acesso)
**Referência:** SOP-005 (IAM Recertification)

## O que o Auditor espera ver?
Como a TWYN baseia sua operação integralmente na nuvem (AWS e GitHub), o auditor precisa de provas contundentes de que "contas fantasmas" (ex-funcionários ou contas de serviço legadas) não mantêm acesso aos ambientes críticos. Ele vai pedir o registro da última revisão trimestral de acessos.

## Como gerar esta evidência?
A evidência deve ser um registro temporal imutável, como uma issue no Linear/GitHub fechada trimestralmente ou uma planilha/documento assinado pelo Gestor do SGSI.

O registro deve conter:
1. **Data da Revisão:** Quando ocorreu a checagem.
2. **Plataformas Inspecionadas:** AWS IAM, AWS EKS (RBAC), GitHub (Organização), Banco de Dados.
3. **Descobertas:** Ex: "Foi identificada a conta legada `tmpsaasboost` na AWS".
4. **Ação Corretiva:** Ex: "Acesso revogado em [Data]".
5. **Responsável:** Nome e aprovação do revisor.

Para auditoria de Estágio 1, basta mostrar a primeira issue documentando a auditoria de acessos inicial do SGSI. No Estágio 2, o auditor vai pedir as revisões do último ano inteiro.
