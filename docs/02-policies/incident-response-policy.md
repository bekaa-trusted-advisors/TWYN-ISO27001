---
document_id: SGSI-POLICY-003
title: Incident Response Policy
version: 2.0
date: 2026-06-02
annex_a_controls: "A.5.24, A.5.25, A.5.26, A.5.27, A.5.28"
owner: Gestor SGSI
approved_by: CEO (Pendente)
---

# Incident Response Policy

## 1. Purpose
Estabelecer procedimentos para detectar, responder, e recuperar de incidentes de segurança da informação, em conformidade com a ISO 27001 e os requisitos de notificação de incidentes da Lei Geral de Proteção de Dados Pessoais (LGPD).

## 2. Scope
- Todos os incidentes afetando a confidencialidade, integridade ou disponibilidade da informação.
- Plataforma Face ID (Face ID Platform API), infraestrutura AWS e dados biométricos.
- Aplicável a todos os colaboradores, contratados e terceiros da TWYN.

## 3. Incident Classification (Severity Levels)

**CRITICAL (P0)**:
- Vazamento confirmado de dados biométricos (Data Breach).
- Infecção ativa por Ransomware.
- Indisponibilidade total do ambiente de produção.
- **Tempo de Resposta (SLA):** < 15 minutos

**HIGH (P1)**:
- Acesso não autorizado confirmado ao ambiente de produção ou banco de dados.
- Malware detectado em sistemas críticos (ex: containers EKS, instâncias EC2).
- Degradação severa de performance impactando múltiplos clientes.
- **Tempo de Resposta (SLA):** < 1 hora

**MEDIUM (P2)**:
- Campanha de phishing bem-sucedida (credenciais de colaboradores comprometidas).
- Vulnerabilidade HIGH/CRITICAL descoberta em produção sem exploit ativo.
- **Tempo de Resposta (SLA):** < 4 horas

**LOW (P3)**:
- Tentativas de login falhadas (brute force) bloqueadas.
- Alertas de anomalia isolada no GuardDuty / WAF.
- **Tempo de Resposta (SLA):** < 24 horas

**INFORMATIONAL (P4)**:
- Scans de rede passivos bloqueados pelo firewall.
- E-mails de phishing reportados e não clicados.
- **Tempo de Resposta (SLA):** Revisão semanal

## 4. Processo de Resposta a Incidentes

### Fase 1: Detecção & Reporte
**Fontes de Detecção**:
- Alertas automatizados (AWS GuardDuty, AWS Security Hub, CloudWatch).
- Notificações de usuários ou clientes (email: security@twyn.com).
- Revisão contínua de logs e relatórios de auditoria.

**Reporte Interno**:
- Qualquer colaborador que suspeitar de um incidente deve contatar imediatamente o email `security@twyn.com` ou utilizar o canal do Slack `#security-incidents`.
- Emergências (P0/P1) devem ser escaladas por telefone para o Gestor SGSI e DevOps Lead.

### Fase 2: Classificação & Escalada
**Gerente do Incidente (Incident Commander):** Gestor SGSI (Ricardo Esper)
**Líder Técnico:** DevOps Lead

**Fluxo de Escalada**:
1. **Triagem Inicial:** O DevOps Lead analisa o alerta e classifica a severidade (P0 a P4).
2. **Notificação P0/P1:** O CEO e o Gestor SGSI são acionados em até 15 minutos via telefone. Um "War Room" (sala de crise virtual) é estabelecido.
3. **Notificação P2:** O Gestor SGSI é notificado via Slack/Email para acompanhamento.
4. **Notificação P3/P4:** O ticket é registrado no sistema para investigação em horário comercial.

### Fase 3: Contenção
**Ações Imediatas (P0/P1):**
1. Isolar sistemas afetados (desconectar EC2 da rede via Security Groups, desligar containers K8s comprometidos).
2. Preservar evidências (capturar snapshots de disco/RDS antes de qualquer reinicialização).
3. Revogar imediatamente credenciais suspeitas (IAM, banco de dados, VPN).
4. Bloquear IPs maliciosos no AWS WAF.
5. Invocar o Plano de Continuidade de Negócios (BCP) se a contenção resultar em downtime prolongado.

### Fase 4: Erradicação
- Identificar e remover a causa raiz (malware, backdoor, credencial exposta).
- Aplicar patches de segurança para vulnerabilidades exploradas.
- Resetar e forçar a rotação de todas as senhas/chaves associadas ao vetor de ataque.
- Reconstruir a infraestrutura afetada a partir de imagens imutáveis limpas (IaC via Terraform).

### Fase 5: Recuperação
- Restaurar dados a partir do último backup validado.
- Iniciar os serviços de forma gradual, monitorando logs de perto por 72 horas para garantir que não há reinfecção.
- Validar a eficácia dos novos controles de segurança implementados.

### Fase 6: Revisão Pós-Incidente (Post-Mortem)
- **Prazo:** Em até 48 horas após a contenção final.
- **Entregáveis:** Relatório Post-Mortem contendo causa raiz, cronograma dos eventos, lições aprendidas e Ações Corretivas (CARs).
- **Armazenamento:** `docs/05-evidence/incidents/YYYY-MM-incident-name.md`

## 5. Plano de Comunicação e Notificação à ANPD

### Comunicação Interna
- **P0/P1:** Updates a cada 2 horas para o Board (CEO, Gestor SGSI). Reunião All-hands pós-incidente.

### Comunicação com Clientes
- Notificar clientes afetados em até 24 horas se houver comprometimento de disponibilidade ou confidencialidade dos seus dados.

### Notificação à Autoridade Nacional de Proteção de Dados (ANPD)
Se o incidente envolver vazamento ou acesso não autorizado a dados pessoais (biometria) que possa acarretar risco ou dano relevante aos titulares:
1. **Prazo:** O DPO (Gestor SGSI) deve notificar a ANPD em até **2 dias úteis** contados da ciência do incidente (conforme diretrizes da ANPD).
2. **Template de Notificação:**
   - Natureza dos dados pessoais afetados (biometria facial).
   - Informações sobre os titulares envolvidos.
   - Indicação das medidas técnicas e de segurança utilizadas para proteção.
   - Riscos relacionados ao incidente.
   - Medidas que foram ou serão adotadas para reverter ou mitigar os efeitos.

### Comunicação com a Mídia
- Somente o CEO ou porta-voz designado (em coordenação com o departamento jurídico) está autorizado a falar publicamente sobre o incidente.

## 6. Preservação de Evidências
- Nunca desligar máquinas virtuais ou excluir logs sem antes realizar uma cópia forense.
- Manter a cadeia de custódia documentada (quem acessou a evidência e quando).
- Evidências de incidentes P0/P1 devem ser retidas por no mínimo 5 anos.

## 7. Exercícios e Testes (Drills)
- Exercícios de mesa (Tabletop) anuais simulando incidentes P0 (ex: ataque de ransomware e vazamento de banco de dados).
- Campanhas de phishing simulado trimestrais para todos os colaboradores.

## 8. Aprovação
- **Proprietário:** Gestor SGSI
- **Aprovado Por:** CEO (Pendente)
- **Próxima Revisão:** 2026-12-31
