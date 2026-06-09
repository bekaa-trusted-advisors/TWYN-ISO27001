---
document_id: SGSI-POLICY-003
title: Política de Resposta a Incidentes
version: 2.0
date: 2026-06-09
classification: Interno
owner: Gestor SGSI
approved_by: CEO (Aprovado)
next_review: Anual
annex_a_controls: "A.5.24, A.5.25, A.5.26, A.5.27, A.5.28"
---

# Política de Resposta a Incidentes

## Controle de Documento

| Propriedade | Detalhe |
|---|---|
| **ID do Documento** | SGSI-POLICY-003 |
| **Versão** | 2.0 |
| **Data de Aprovação** | 2026-06-09 |
| **Classificação** | Interno |
| **Elaborado por** | Gestor SGSI |
| **Aprovado por** | CEO (Aprovado) |
| **Próxima Revisão** | Anual |


## 1. Propósito
Estabelecer procedimentos para detectar, responder e se recuperar de incidentes de segurança da informação, em conformidade com a ISO 27001 e com os requisitos de notificação de incidentes da Lei Geral de Proteção de Dados Pessoais (LGPD - vazamento de biometria).

## 2. Escopo
Aplica-se a todos os colaboradores, prestadores de serviço e fornecedores que interagem com o ambiente tecnológico da TWYN (AWS, GitHub, sistemas corporativos) e tratam dados da empresa ou de seus clientes.

## 3. Fases da Resposta a Incidentes (A.5.26)

### Fase 1: Preparação
- Manutenção de canais de alerta (CloudWatch, GuardDuty, alertas do GitHub).
- Treinamento anual da equipe técnica sobre identificação de anomalias.
- Realização de simulação de incidentes de segurança pelo menos uma vez por ano.

### Fase 2: Identificação e Relato (A.5.24)
- **Obrigação de relatar**: Qualquer colaborador que suspeitar de um incidente (phishing, acesso não autorizado, credenciais vazadas) deve relatar imediatamente ao Gestor SGSI através do e-mail oficial (security@twyn) ou canal designado no Slack (#security-alerts).
- O Gestor do SGSI fará a triagem inicial e ativará o Comitê de Resposta a Incidentes, caso o impacto seja confirmado.

### Fase 3: Contenção
- **Contenção a Curto Prazo**: Isolar imediatamente o ativo comprometido (ex: desativar credencial IAM vazada, revogar token GitHub, isolar instância EC2 em um Security Group restrito).
- **Contenção a Longo Prazo**: Remoção temporária do serviço do ar se houver risco contínuo à base de dados biométrica (RESTRICTED).

### Fase 4: Erradicação e Avaliação de Vulnerabilidades (A.5.25)
- Eliminar a causa raiz (ex: correção de bug em código, remoção de malware).
- Analisar os logs (CloudTrail, Access Logs) para entender a extensão do dano e se houve exfiltração de dados (vazamento).

### Fase 5: Recuperação
- Restaurar sistemas a partir de backups limpos e testados (conforme SGSI-POLICY-005 - Política de Backup).
- Validar se o sistema está operando de forma normal e segura antes de reabrir os acessos aos usuários finais.

### Fase 6: Lições Aprendidas (Post-Mortem) (A.5.28)
- Um relatório post-mortem deve ser redigido num prazo máximo de 5 dias úteis após a resolução do incidente.
- O relatório deve documentar a causa raiz, tempo de detecção, impacto gerado e medidas para evitar recorrência.

## 4. Gestão de Crise e LGPD (Notificações Legais)
- **Incidente envolvendo Dados Biométricos (LGPD Art. 11)**:
  - Caso haja confirmação de vazamento de dados biométricos, a Autoridade Nacional de Proteção de Dados (ANPD) e os titulares dos dados afetados devem ser comunicados no prazo máximo legal estipulado pela legislação (via DPO).
- Comunicações externas (imprensa e clientes corporativos) devem ser aprovadas exclusivamente pelo CEO.

## 5. Coleta e Preservação de Evidências (A.5.28)
- Antes de reconstruir a máquina/ambiente comprometido, a equipe técnica (DevOps) deve garantir a coleta de logs, snapshot de disco e do estado do sistema.
- As evidências devem ser guardadas de forma segura (armazenamento criptografado no S3) caso seja necessária perícia legal futura.

## 6. Histórico de Revisão
| Data | Versão | Autor | Descrição |
|------|--------|-------|-----------|
| 2026-06-09 | 2.0 | Gestor SGSI | Tradução integral para PT-BR, adequação da estrutura de YAML e refinamento de controles ISO 27001. |
