# Guia de Coleta de Evidências (ISO 27001)

Este diretório (`docs/05-evidence/`) é o cofre central de comprovação do SGSI da TWYN. É aqui que os rastros auditáveis que provam a **implementação** (e não apenas a intenção) dos controles devem ser armazenados.

## Estrutura de Pastas de Evidências

Para manter o repositório organizado e facilitar a vida do auditor durante as verificações da Fase 1 e Fase 2, as evidências físicas (PDFs, screenshots, relatórios exportados) devem ser salvas nas seguintes pastas:

### `01-management/`
**O que vai aqui:** Evidências de Liderança e Gestão.
- Atas de reunião assinadas (Management Review).
- Termos de nomeação (Gestor SGSI, DPO).
- Comunicações da alta diretoria sobre a importância do SGSI (prints de Slack/Email).

### `02-risk-audit/`
**O que vai aqui:** Evidências de Avaliação.
- Relatórios fechados de auditoria interna.
- Aceites formais de risco assinados pela diretoria.
- Relatórios de Pentest (versão executiva/sanitizada, sem expor as falhas abertas publicamente).

### `03-hr-training/`
**O que vai aqui:** Evidências de RH (Controles A.6).
- Termos de Confidencialidade (NDA) assinados.
- Certificados de conclusão de treinamentos de Segurança (OWASP, AWS, LGPD).
- Checklists de Onboarding e Offboarding preenchidos e assinados.

### `04-access-crypto/`
**O que vai aqui:** Evidências de Controle de Acesso (Controles A.5).
- Relatórios (prints ou CSVs) das revisões trimestrais de acesso ao IAM e GitHub.
- Logs exportados provando a rotação de chaves KMS ou IAM Access Keys.

### `05-operations-threat-intel/`
**O que vai aqui:** Evidências Operacionais e Contato com Grupos/Autoridades (A.5.5, A.5.6).
- Prints de e-mails confirmando a inscrição em *Security Bulletins* (AWS, GitHub).
- Comprovantes de filiação à OWASP ou Cloud Security Alliance.
- Evidências de tickets criados a partir de inteligência de ameaças externa.
- Resultados de scans de vulnerabilidade (Trivy/Snyk).

### `06-incident-dr/`
**O que vai aqui:** Evidências de Resiliência.
- Relatórios Post-Mortem de incidentes de segurança (se houverem).
- Relatórios e atas de execução de testes de Disaster Recovery (DR Drills).
- Protocolos de notificação da ANPD em caso de Data Breach.

### `07-suppliers/`
**O que vai aqui:** Evidências de Fornecedores (Controles A.5.19 a A.5.23).
- DPAs (Data Processing Agreements) e BAAs assinados.
- Relatórios do tipo TPRA (Third-Party Risk Assessment) concluídos.
- Relatórios SOC 2 Type II dos fornecedores (arquivados localmente ou os links oficiais de compliance).

## Regras de Armazenamento no GitHub

1. **Nunca** faça o upload de segredos reais (senhas, chaves privadas, tokens). Use o *Secrets Manager*.
2. **Sanitize (Tarje) Dados Pessoais:** Se o print contém CPFs ou dados biométricos reais, cubra-os antes do upload (LGPD).
3. **Formatos Preferidos:** Use preferencialmente `.pdf` (documentos), `.png` ou `.jpg` (prints), e `.csv` (exportações de log).
4. **Nomenclatura:** Nomeie os arquivos com clareza cronológica (ex: `2026-06-08-aws-iam-review.pdf`).
