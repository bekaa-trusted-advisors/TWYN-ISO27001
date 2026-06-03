---
document_id: SGSI-GAP-004
title: Implementation Guide - GAP-004: Execução do Teste de Disaster Recovery (Restore)
version: 1.1
date: 2026-06-03
---

# GAP-004: Guia de Execução do Teste de Disaster Recovery (DR)

## Propósito
Este documento detalha o roteiro técnico e as obrigações probatórias para a execução do Teste de Disaster Recovery (Restore Test) da TWYN. A execução bem sucedida e documentada deste teste é **mandatória** para a certificação ISO 27001 (Controles A.5.30 e A.8.13).

---

## O Roteiro de Evidência de DR (Restore Test)

### 1. Abra um Ticket formal (GitHub/Linear)
Crie uma tarefa chamada `[SEC] Teste Semestral de Disaster Recovery - Q2 2026`. Isso prova para o auditor que a ação foi planejada e governada, e não um teste aleatório.

### 2. Execute o Teste de Restore em Ambiente Isolado (Sandbox/Dev)
A equipe de DevOps deve realizar as seguintes ações de restauração na AWS:

*   **Banco de Dados (RDS):**
    *   Pegar o snapshot automático mais recente do RDS de produção.
    *   Comando CLI: `aws rds restore-db-instance-from-db-snapshot --db-instance-identifier dr-test-restore --db-snapshot-identifier [ID_DO_SNAPSHOT]`
*   **Aplicações (EKS):**
    *   Fazer o deploy da API (em um namespace temporário ou cluster de teste) apontando as variáveis de ambiente de banco de dados para a instância `dr-test-restore`.
*   **Storage (S3):**
    *   Validar o acesso aos objetos cruciais ou restaurar uma versão anterior de um objeto para atestar a integridade do versionamento.

### 3. Tire os "Prints Comprobatórios" (A Evidência)
O auditor quer ver "a fumaça da arma" (logs ou telas que comprovem 3 coisas: que funcionou, quando ocorreu e quanto tempo demorou). Guarde:
*   Print da tela da AWS ou log do Terraform mostrando o **início** do processo de restore.
*   Print mostrando a nova instância RDS com o status **"Available"** (com o relógio do sistema visível na barra de tarefas).
*   Print de um teste de conectividade (ex: endpoint `/health` ou um `curl` na API) retornando `200 OK`, provando que o sistema subiu e comunicou com o banco.

### 4. Preencha o Laudo (DR Test Report)
Acesse o template de laudo localizado em `docs/05-evidence/dr-test-report-Q2-2026.md`. Nele, você irá consolidar as informações do teste:
*   **RPO Atingido (Recovery Point Objective):** Qual o atraso dos dados em relação à produção (ex: O snapshot era de 1 hora atrás).
*   **RTO Atingido (Recovery Time Objective):** Quanto tempo demorou desde o acionamento do restore até a aplicação responder `200 OK` (O SLA do BCP é <4 horas).
*   Insira os prints e salve o arquivo.

### 5. Destrua o Ambiente de Teste
Após consolidar a evidência e preencher o laudo, **exclua imediatamente** a instância RDS restaurada e o cluster/namespace temporário para evitar custos desnecessários na AWS.
*   Comando CLI: `aws rds delete-db-instance --db-instance-identifier dr-test-restore --skip-final-snapshot`

---

## Critérios de Sucesso (Para fechamento do GAP)
- [ ] Ticket de mudança/planejamento criado.
- [ ] RTO registrado foi inferior a 4 horas.
- [ ] RPO registrado atende às políticas do BCP.
- [ ] O laudo `dr-test-report-Q2-2026.md` está totalmente preenchido com as imagens (prints) comprobatórias anexadas.
