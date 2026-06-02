---
document_id: SGSI-POLICY-003
title: Incident Response Policy
version: 1.0
date: 2026-05-26
annex_a_controls: "A.5.24, A.5.25, A.5.26, A.5.27, A.5.28"
---

# Incident Response Policy

## 1. Purpose
Estabelecer procedimentos para detectar, responder, e recuperar de incidentes de segurança da informação.

## 2. Scope
- Todos os incidentes afetando confidencialidade, integridade ou disponibilidade
- Face ID Platform API, AWS infrastructure, dados biométricos
- Aplicável a todos colaboradores e terceiros

## 3. Incident Classification

### Severity Levels
**CRITICAL (P0)**: 
- Data breach de dados biométricos
- Ransomware ativo
- Produção completamente indisponível
- Response time: <15 minutos

**HIGH (P1)**:
- Tentativa de acesso não autorizado a produção
- Malware detectado em sistemas críticos
- Degradação significativa de performance
- Response time: <1 hora

**MEDIUM (P2)**:
- Phishing bem-sucedido (credenciais comprometidas)
- Vulnerabilidade HIGH descoberta
- Response time: <4 horas

**LOW (P3)**:
- Tentativas de login falhadas suspeitas
- Spam/phishing reportado
- Response time: <24 horas

## 4. Incident Response Process

### Phase 1: Detection & Reporting
**Detection Methods**:
- AWS GuardDuty alerts
- CloudWatch anomalies
- User reports (via email: security@twyn.com)
- Audit log reviews

**Reporting**:
- Qualquer colaborador pode reportar suspeita
- Email: security@twyn.com (monitored 24/7)
- Slack: #security-incidents (se disponível)
- Phone: Gestor SGSI (emergências)

### Phase 2: Classification & Escalation
**Incident Manager**: Gestor SGSI (Ricardo Esper)
**Technical Lead**: DevOps Lead

**Escalation Matrix**:
- P0/P1: Notify CEO + DevOps Lead imediatamente
- P2: Notify Gestor SGSI within 1h
- P3: Log ticket, investigate next business day

### Phase 3: Containment
**Immediate Actions** (P0/P1):
1. Isolar sistemas afetados (disable network, terminate EC2)
2. Preservar evidências (snapshots, logs)
3. Revogar credenciais comprometidas
4. Block IPs maliciosos (Security Groups)
5. Ativar Business Continuity Plan se necessário

**Short-term Containment**:
- Aplicar patches de segurança
- Implementar workarounds
- Comunicar stakeholders

### Phase 4: Eradication
- Remover malware/backdoors
- Patch vulnerabilidades exploitadas
- Resetar passwords comprometidos
- Rebuild sistemas se necessário

### Phase 5: Recovery
- Restaurar sistemas de backups validados
- Verificar integridade de dados
- Monitorar por re-infecção (72 horas)
- Validar controles de segurança funcionando

### Phase 6: Post-Incident Review
**Timeline**: Within 48 hours de resolução

**Deliverables**:
1. Incident Report (5W2H: What, When, Where, Who, Why, How, How Much)
2. Root Cause Analysis
3. Lessons Learned
4. Corrective Actions (CARs)
5. Update Runbooks

**Stored in**: `docs/05-evidence/incidents/YYYY-MM-incident-name.md`

## 5. Communication

### Internal
- P0/P1: Immediate notification (CEO, DevOps, Gestor SGSI)
- Status updates every 2 hours during incident
- Post-incident: All-hands summary

### External
**Clients**: 
- Notify if their data affected (within 24h)
- Provide incident summary + remediation

**Regulators (LGPD)**:
- Data breach notification within 72h (ANPD)
- Include: nature of breach, categories affected, consequences, measures taken

**Media**:
- Only CEO or designated spokesperson
- Coordinate with legal team

## 6. Evidence Preservation
- Do NOT delete logs or shut down systems without forensic copy
- Chain of custody documented
- Store evidence for minimum 2 years
- May be needed for legal/insurance claims

## 7. Third-Party Incidents
If incident caused by vendor (AWS, GitHub):
- Report immediately to vendor support
- Document vendor's response
- Assess if SLA breached
- Include in post-incident review

## 8. Training & Drills
- Annual tabletop exercise (simulate P0 incident)
- Quarterly phishing simulations
- New hires: Incident reporting training (Day 1)

## 9. Related Documents
- SGSI-NCR-001: Nonconformity Register
- SGSI-CAR-001: Corrective Action Log
- RISK-009: Incident Response capability gap
- SOP-002: Change Management (emergency changes)

## 10. Approval
- **Owner**: Gestor SGSI
- **Approved By**: CEO (Pendente)
- **Next Review**: 2026-12-31
