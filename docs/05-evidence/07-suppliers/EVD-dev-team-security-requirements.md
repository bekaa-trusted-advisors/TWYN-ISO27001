# Evidência: Requisitos de Segurança para a Equipe de Engenharia (Fornecedor Interno)

**Controles Anexo A:** A.5.19, A.5.21 (Segurança na cadeia de suprimentos)
**Referência:** Política de Segurança de Fornecedores

## O que o Auditor espera ver?
Como definimos que o Desenvolvimento de Software (SDLC) está fora do escopo do nosso SGSI, a equipe de engenharia passa a ser tratada, do ponto de vista da governança, como um "fornecedor" que entrega o software para ser hospedado pela Operação. O auditor vai querer ver evidências de que impomos regras de segurança a esse fornecedor.

## Como gerar esta evidência no dia da auditoria?
Você deve apresentar este documento (ou o SLA documentado no Jira/Confluence) que estipula o seguinte acordo de nível de serviço de segurança:

1. **Requisito de Entrega:** O fornecedor (Engenharia TWYN) só pode entregar artefatos de código através de Pull Requests no GitHub. Nenhuma entrega direta no servidor é permitida.
2. **Requisito de Qualidade de Segurança:** O código entregue não pode conter vulnerabilidades de nível *CRÍTICO* ou *ALTO* segundo as ferramentas de varredura (Trivy/Snyk) configuradas no repositório.
3. **Requisito de Resolução:** Caso uma vulnerabilidade seja detectada no ambiente de produção (via GuardDuty ou Pentest), o fornecedor (Engenharia) tem um SLA de 4 horas para entregar um *hotfix* de emergência.

A evidência prática de que a TWYN cobra isso do "fornecedor" são as regras de proteção de branch (*Branch Protection Rules*) no GitHub, que impedem o *merge* se os requisitos acima não forem atendidos. Mostre a tela de configurações do GitHub ao auditor.
