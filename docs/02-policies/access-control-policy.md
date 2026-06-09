---
document_id: SGSI-POLICY-002
title: Política de Controle de Acesso
version: 1.0
date: 2026-06-09
classification: Interno
owner: Gestor SGSI
approved_by: CEO (Aprovado)
next_review: Anual
annex_a_controls: "A.5.15, A.5.16, A.5.17, A.5.18, A.8.2, A.8.3"
---

# Política de Controle de Acesso

## 1. Propósito
Garantir que o acesso à informação e aos recursos de processamento da TWYN seja autorizado, controlado e restrito às necessidades de negócio, protegendo contra acessos não autorizados.

## 2. Princípios de Acesso
- **Menor Privilégio (Least Privilege)**: Os usuários recebem apenas os acessos estritamente necessários para executar suas funções.
- **Necessidade de Conhecer (Need-to-Know)**: O acesso à informação confidencial ou restrita requer justificativa de negócio.
- **Separação de Funções (Segregation of Duties)**: Sempre que possível, as funções críticas (ex: desenvolvimento vs. aprovação de deploy) devem ser separadas.

## 3. Diretrizes de Autenticação e Senhas (A.5.17)
- **MFA (Múltiplos Fatores de Autenticação)**: Obrigatório para TODOS os acessos a sistemas corporativos, nuvem (AWS) e repositórios (GitHub).
- **Padrão de Senhas**: Mínimo de 14 caracteres, complexidade habilitada (maiúsculas, minúsculas, números e símbolos).
- **Rotação de Senhas e Chaves**:
  - Senhas de usuários e chaves de acesso (Access Keys AWS / GitHub PATs): rotação a cada 90 dias.
- **Proibição**: É estritamente proibido o compartilhamento de contas e senhas entre usuários.

## 4. Gestão do Ciclo de Vida do Acesso (A.5.16)
### 4.1. Concessão de Acesso (Onboarding)
- Todo acesso deve ser formalmente solicitado e aprovado pelo gestor responsável ou Gestor SGSI (vide SGSI-SOP-001).
- A criação de usuários na AWS e no GitHub deve seguir o provisionamento via IAM Roles e Grupos de Segurança documentados.

### 4.2. Revogação de Acesso (Offboarding)
- Acessos de colaboradores desligados voluntariamente devem ser revogados no último dia de trabalho.
- Desligamentos involuntários exigem o bloqueio imediato das contas corporativas e revogação de acessos na nuvem em no máximo 4 horas.

### 4.3. Revisão de Acessos (A.5.18)
- Os direitos de acesso devem ser revisados pelo Gestor SGSI e pelo DevOps Lead, no mínimo, a cada 3 meses.
- Identificações de acessos ociosos por mais de 90 dias implicam no bloqueio automático da conta.

## 5. Acesso Privilegiado e Administrativo (A.8.2)
- O acesso de administrador (Root / Superusuário) só pode ser concedido a indivíduos explicitamente autorizados pela diretoria.
- **Conta AWS Root**: A conta Root não deve ser usada para atividades do dia a dia. Seu acesso é protegido por Hardware Token (MFA físico) guardado em cofre, utilizando procedimento *break-glass* apenas em emergências críticas.
- Uso de acessos privilegiados deve ser monitorado e logado (ex: AWS CloudTrail).

## 6. Acesso a Redes e Trabalho Remoto (A.8.3, A.6.7)
- O acesso a recursos críticos internos e ambientes RESTITOS (dados biométricos) requer conexão segura (VPN homologada).
- Terminais remotos e laptops da empresa devem possuir criptografia de disco, tela com bloqueio automático (15 min) e proteção antimalware.

## 7. Controle de Acesso para Fornecedores e Terceiros
- Acesso de parceiros e fornecedores a ambientes da TWYN deve ser temporário, limitado por escopo de contrato e monitorado.
- Requer NDA e Adendo de Segurança (SGSI-POLICY-011) devidamente assinados.

## 8. Monitoramento e Auditoria
- As atividades de logon e falhas de autenticação são registradas centralizadamente (CloudTrail/Log Management) e armazenadas de forma segura.
- Violações aos controles de acesso podem gerar sanções disciplinares, incluindo justa causa.

## 9. Histórico de Revisão
| Data | Versão | Autor | Descrição |
|------|--------|-------|-----------|
| 2026-06-09 | 1.0 | Gestor SGSI | Tradução, síntese e padronização para o escopo da auditoria ISO 27001 (PT-BR). |


## 8. Procedimentos Relacionados (SOPs)

O controle de acesso descrito nesta política é aplicado na prática pelos seguintes procedimentos:

- **[SGSI-SOP-001](../03-procedures/sop-001-onboarding-offboarding.md)**: Procedimento de Onboarding e Offboarding (Provisionamento)
- **[SGSI-SOP-004](../03-procedures/sop-004-secrets-management.md)**: Gestão de Segredos e Chaves (Acesso Programático)
- **[SGSI-SOP-005](../03-procedures/sop-005-iam-recertification.md)**: Recertificação Trimestral de Acessos (Auditoria de Privilégios)
