---
document_id: SGSI-POLICY-004
title: Política de Gestão de Ativos
version: 1.0
date: 2026-06-09
classification: Interno
owner: Gestor SGSI
approved_by: CEO (Aprovado)
next_review: Anual
annex_a_controls: "A.5.9, A.5.10, A.5.11, A.5.12, A.5.13"
---

# Política de Gestão de Ativos

## Controle de Documento

| Propriedade | Detalhe |
|---|---|
| **ID do Documento** | SGSI-POLICY-004 |
| **Versão** | 1.0 |
| **Data de Aprovação** | 2026-06-09 |
| **Classificação** | Interno |
| **Elaborado por** | Gestor SGSI |
| **Aprovado por** | CEO (Aprovado) |
| **Próxima Revisão** | Anual |


## 1. Propósito
Identificar, classificar e proteger os ativos de informação da TWYN de acordo com seu valor de negócio e criticidade para a organização.

## 2. Escopo
Todos os ativos pertencentes ao escopo do SGSI da TWYN:
- **Ativos de Informação**: Dados biométricos, códigos-fonte, documentação do SGSI, credenciais, segredos, chaves de API.
- **Infraestrutura**: Recursos na AWS (EC2, RDS, S3, EKS).
- **Software**: Aplicações, bibliotecas de terceiros, containers.
- **Pessoas**: Colaboradores com conhecimento crítico do negócio.

## 3. Inventário de Ativos
É obrigatório manter o inventário de ativos atualizado.
- **Campos obrigatórios**: ID do Ativo, Nome, Tipo, Proprietário (Owner), Custodiante, Classificação, Localização, Status e Riscos associados.
- **Frequência de Atualização**:
  - *Imediata*: Para novos ativos críticos ou mudanças de proprietário.
  - *Trimestral*: Auditoria geral do inventário.

## 4. Classificação da Informação (A.5.12)

### Níveis de Classificação
1. **PÚBLICO (PUBLIC)**:
   - Informações que podem ser divulgadas externamente sem restrição (ex: site público, manuais abertos).
2. **INTERNO (INTERNAL)**:
   - Documentos internos, e-mails corporativos, processos não-sensíveis.
   - Acesso restrito a colaboradores e contratados da TWYN.
3. **CONFIDENCIAL (CONFIDENTIAL)**:
   - Repositórios de código (Terraform), configurações arquiteturais, senhas e credenciais, dados financeiros.
   - Controle estrito de acesso (menor privilégio).
4. **RESTRITO (RESTRICTED)**:
   - **Dados biométricos (Sensíveis - LGPD Art. 11)**.
   - Acesso exclusivo via VPN para o time de infraestrutura autorizado pelo Gestor do SGSI.
   - Obrigatória criptografia em repouso e em trânsito (AES-256 ou superior).

## 5. Manuseio de Ativos (A.5.10, A.5.13)

### Armazenamento
- **INTERNO**: Google Workspace (Drive), Slack corporativo.
- **CONFIDENCIAL/RESTRITO**: Armazenamento exclusivo em serviços de nuvem controlados (ex: AWS S3 com criptografia KMS ativada, AWS Secrets Manager).

### Transmissão
- Dados **RESTRITOS** não devem ser enviados por e-mail ou Slack em nenhuma circunstância. Devem ser geradas URLs temporárias do S3 (Pre-Signed URLs).
- Proibido o uso de pendrives ou HDs externos para arquivos Confidenciais ou Restritos.

### Descarte e Destruição
- **Dados**: Exclusão segura (remoção de chaves KMS ou substituição criptográfica) quando o período de retenção expirar.
- **Hardware**: O descarte de discos (se houver infraestrutura local, o que não é o caso padrão do SaaS) exige sanitização com ferramenta de wiping.

## 6. Papéis e Responsabilidades

- **Proprietário do Ativo (Owner)**: Define a classificação da informação, aprova acessos e estabelece os períodos de retenção (ex: CEO, CTO).
- **Custodiante**: Implementa os controles técnicos de segurança sobre o ativo (ex: DevOps Lead aplica regras no S3).
- **Usuário**: Utiliza o ativo em conformidade com as regras de manuseio.

## 7. Dispositivos Físicos e Laptops (A.8.1)
- **Criptografia**: Todos os notebooks utilizados pela equipe da TWYN que acessam a AWS devem ter o disco totalmente criptografado (FDE - BitLocker ou FileVault).
- **Bloqueio de Tela**: Configurado para travamento automático após 15 minutos de inatividade.
- **Antivírus**: Solução de endpoint protection sempre atualizada e ativa.
- O uso de dispositivos pessoais (BYOD) para acessar o ambiente de produção da AWS é proibido.

## 8. Ativos em Nuvem (AWS) e Uso de Software
- Todos os recursos criados na nuvem devem utilizar **Tags obrigatórias** (`Environment`, `Owner`, `Classification`).
- A infraestrutura deve ser gerenciada como código (Terraform). Alterações manuais em produção são proibidas sem ticket de mudança.
- Todos os softwares utilizados pelos colaboradores devem ser devidamente licenciados e aprovados pela diretoria.

## 9. Histórico de Revisão
| Data | Versão | Autor | Descrição |
|------|--------|-------|-----------|
| 2026-06-09 | 1.0 | Gestor SGSI | Tradução e adaptação estrutural para certificação (PT-BR). |
