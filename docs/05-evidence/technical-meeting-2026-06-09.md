---
document_id: SGSI-TECH-MEETING-001
title: Ata da Reunião Técnica (AWS & Infraestrutura)
version: 1.0
date: 2026-06-09
classification: Internal
owner: DevOps Lead
---

# Ata da Reunião Técnica: Resolução de GAPs Críticos (AWS)

## Detalhes da Reunião
- **Data**: 2026-06-09
- **Participantes**: Ricardo Esper (DevOps Lead / Arquiteto Cloud)
- **Foco da Reunião**: Planejamento de execução técnica para fechamento dos GAPs (Fase 2 da ISO 27001).

## 1. Pauta e Escopo Técnico
Esta reunião teve como objetivo definir o roteiro exato de modificações na infraestrutura AWS (via Terraform) e nos endpoints para garantir a eficácia dos controles do Anexo A exigidos no *Statement of Applicability* (SoA).

## 2. Decisões Arquiteturais e Plano de Ação

### Ação Técnica 1: Mitigação de SPOF via Logs Imutáveis (GAP-009)
Para justificar a falta de Segregação de Funções (A.5.3), os logs não podem ser apagáveis.
- **Decisão**: O bucket S3 que armazena os logs do AWS CloudTrail será reconfigurado via Terraform.
- **Implementação Técnica**: Habilitar `Object Lock` no S3 em modo *Compliance* (mínimo de 365 dias). 

### Ação Técnica 2: Auditoria Contínua da AWS (GAP-003)
Precisamos provar o controle de Monitoramento e Configuração (A.8.9, A.8.16).
- **Decisão**: Habilitar o AWS Config com regras baseadas no *CIS AWS Foundations Benchmark*.
- **Implementação Técnica**: Escrever o módulo Terraform para o AWS Config, focando nas regras de IAM, RDS (criptografia) e S3 (acesso público restrito).

### Ação Técnica 3: Teste de Disaster Recovery e Restore (GAP-004)
Um banco de dados biométrico não pode ter seu backup presumido como funcional (A.8.13, A.5.30).
- **Decisão**: Realizar um teste real de *point-in-time recovery* (PITR) no banco PostgreSQL de Produção.
- **Implementação Técnica**: Acessar o console AWS, executar o restore para uma nova instância de teste, validar a integridade dos dados e tirar *screenshots* documentais. Destruir a instância de teste logo em seguida.

### Ação Técnica 4: Blindagem dos Endpoints de Operação (GAP-011)
Não podemos acessar a AWS a partir de computadores inseguros (A.8.1).
- **Decisão**: Todos os notebooks usados para acesso root/Admin na AWS devem estar encriptados.
- **Implementação Técnica**: Gerar evidências (capturas de tela) demonstrando o BitLocker ativado no Windows ou FileVault no macOS.

## 3. Cronograma de Deploy (Hands-on)
| Tarefa Técnica | Ferramenta | Responsável | Prazo |
|----------------|------------|-------------|-------|
| 1. Código Terraform S3 Object Lock | Terraform | DevOps Lead | Hoje |
| 2. Código Terraform AWS Config | Terraform | DevOps Lead | Hoje |
| 3. Teste Restore RDS | Console AWS | DevOps Lead | Hoje |
| 4. Evidência BitLocker | Windows OS | DevOps Lead | Hoje |

---

**Aprovação Técnica**:
- **DevOps Lead**: _[Assinado Digitalmente por Ricardo Esper]_ Data: 2026-06-09
