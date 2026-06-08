# Evidência: Logs de Aprovação de Mudanças (Change Management)

**Controle Anexo A:** A.8.32 (Gestão de Mudanças)
**Referência:** SOP-002 (Gestão de Mudanças)

## O que o Auditor espera ver?
Como o desenvolvimento lógico da aplicação está *fora do escopo* do SGSI, a Operação atua como uma barreira (*gatekeeper*). O auditor vai pedir para ver as evidências de que o código fornecido pelos desenvolvedores foi devidamente testado e formalmente aceito pela Operação antes de entrar no ambiente de produção na AWS.

## Como gerar esta evidência no dia da auditoria?
Não é necessário gerar um PDF ou planilha manual. No dia da auditoria, você deve abrir a tela do GitHub e mostrar:
1. **Pull Requests (PRs) recentes fechadas (Merged):** Mostre que a PR foi aberta pela Engenharia e **aprovada** por um membro da Operação (DevOps Lead / Gestor SGSI).
2. **Checks Automatizados (CI/CD):** Dentro da mesma PR, mostre que os "checks" (ações do GitHub Actions) estão com um *tick* verde (✅), comprovando que ferramentas de SAST/DAST/SCA (como Trivy ou Snyk) rodaram e não encontraram vulnerabilidades críticas.
3. **Logs de Deploy:** Mostre o log final do GitHub Actions realizando o deploy no cluster EKS ou atualizando a infraestrutura via Terraform.

> **Importante:** Se o auditor encontrar uma PR que foi mesclada ("merged") diretamente na branch principal sem revisão (bypass) ou com falhas nos testes de segurança, isso gerará uma Não Conformidade Maior.
