# 🔒 TWYN SGSI - ISO 27001:2022

Sistema de Gestão de Segurança da Informação (SGSI) para certificação ISO/IEC 27001:2022 da **TWYN Face ID Platform**.

**Status**: 🟡 **Documentação 100% Completa | Implementação em Progresso**

---

## 📊 Status do Projeto

| Categoria | Meta | Atual | Status |
|-----------|------|-------|--------|
| **Documentação Obrigatória** | 14 docs | 14/14 (100%) | ✅ |
| **Controles Anexo A** | 85% impl | 70% (31% full + 39% partial) | 🟡 |
| **Riscos Identificados** | 100% | 18 riscos mapeados | ✅ |
| **CARs Abertos** | 0 | 4 (CRITICAL/HIGH) | 🔴 |
| **Gestor SGSI** | Designado | Ricardo Esper | ✅ |
| **Target Certificação** | Q3 2026 | Set/2026 | 🟢 |

---

## 🎯 Informações do Projeto

**Organização**: TWYN  
**Produto**: Face ID Platform API  
**Escopo SGSI**: AWS Account 992382542028, dados biométricos, infraestrutura cloud  
**Norma**: ISO/IEC 27001:2022  
**Gestor SGSI**: Ricardo Esper (resper@bekaa.eu)  
**Consultor**: Bekaa Trusted Advisors  

---

## 📁 Estrutura de Documentos

```
twyn-sgsi-iso27001/
├── README.md                           # Este arquivo
├── GLOSSARY.md                         # 100+ termos ISO 27001
├── STATUS-REPORT-2026-05-26.md        # Status report executivo
├── GITHUB-MIGRATION-GUIDE.md          # Guia de migração (se necessário)
│
├── docs/
│   ├── 01-mandatory-clauses/          # Cláusulas obrigatórias
│   │   ├── clause-4-context-isms-scope.md         # SGSI-SCOPE-001
│   │   ├── information-security-objectives.md     # SGSI-OBJ-001
│   │   └── raci-matrix.md                         # SGSI-RACI-001
│   │
│   ├── 02-policies/                   # Políticas top-level
│   │   └── information-security-policy.md         # SGSI-POLICY-001 ⚠️ CEO signature
│   │
│   ├── 04-risk-management/            # Gestão de riscos
│   │   ├── risk-assessment-methodology.md         # SGSI-RISK-001
│   │   ├── risk-register.md                       # SGSI-RISK-002
│   │   ├── risk-treatment-plan.md                 # SGSI-RTP-001
│   │   └── statement-of-applicability.md          # SGSI-SOA-001
│   │
│   └── 05-evidence/                   # Evidências e registros
│       ├── asset-inventory.md                     # SGSI-ASSETS-001
│       ├── competence-records.md                  # SGSI-COMP-001
│       ├── internal-audit-programme.md            # SGSI-AUDIT-001
│       ├── management-review-template.md          # SGSI-MREVIEW-001
│       ├── nonconformity-register.md              # SGSI-NCR-001
│       └── corrective-action-log.md               # SGSI-CAR-001
```

---

## 🔴 Blockers Críticos

### 1. CEO Não Assinou Information Security Policy
**Doc**: `docs/02-policies/information-security-policy.md`  
**Impacto**: Blocker ABSOLUTO para certificação ISO 27001  
**Ação**: Imprimir, coletar assinatura, armazenar versão assinada  
**Prazo**: URGENTE  

### 2. 4 CARs (Corrective Actions) Abertos

| CAR | Descrição | Prioridade | Prazo | Owner |
|-----|-----------|------------|-------|-------|
| **CAR-001** | Habilitar MFA na AWS root account | 🔴 CRITICAL | 05/06/2026 | DevOps Lead |
| **CAR-002** | Rotacionar IAM key tmpsaasboost (>90 dias) | 🟡 HIGH | 08/06/2026 | DevOps Lead |
| **CAR-003** | Implementar AWS Config + 8 CIS controls | 🔴 CRITICAL | 08/06/2026 | DevOps Lead |
| **CAR-004** | Testar restauração de backups (DR testing) | 🟡 HIGH | 05/06/2026 | DevOps Lead |

**Detalhes**: Ver `docs/05-evidence/corrective-action-log.md`

---

## 📋 14 Documentos Obrigatórios ISO 27001:2022

| # | Doc ID | Nome | ISO Clause | Status | Tamanho |
|---|--------|------|------------|--------|---------|
| 1 | SGSI-SCOPE-001 | ISMS Scope Definition | 4.3 | ✅ | 8.4 KB |
| 2 | SGSI-POLICY-001 | Information Security Policy | 5.2 | ✅ 🔴 CEO sig | 22.4 KB |
| 3 | SGSI-RISK-001 | Risk Assessment Methodology | 6.1.2 | ✅ | 19.3 KB |
| 4 | SGSI-RISK-002 | Risk Register (18 risks) | 6.1.2 | ✅ | 29.5 KB |
| 5 | SGSI-RTP-001 | Risk Treatment Plan | 6.1.3 | ✅ | 12.4 KB |
| 6 | SGSI-SOA-001 | Statement of Applicability | 6.1.3d | ✅ | 21.1 KB |
| 7 | SGSI-OBJ-001 | Information Security Objectives | 6.2 | ✅ | 14.6 KB |
| 8 | SGSI-COMP-001 | Competence Records | 7.2 | ✅ | 11.4 KB |
| 9 | SGSI-RACI-001 | RACI Matrix | 5.3, 7.2 | ✅ | 20.8 KB |
| 10 | SGSI-ASSETS-001 | Asset Inventory (49 assets) | 8.1 | ✅ | 26.4 KB |
| 11 | SGSI-AUDIT-001 | Internal Audit Programme | 9.2 | ✅ | 3.6 KB |
| 12 | SGSI-MREVIEW-001 | Management Review Template | 9.3 | ✅ | 3.0 KB |
| 13 | SGSI-NCR-001 | Nonconformity Register (4 NCRs) | 10.1 | ✅ | 2.0 KB |
| 14 | SGSI-CAR-001 | Corrective Action Log (4 CARs) | 10.2 | ✅ | 5.5 KB |

**Total**: 200 KB de documentação técnica

---

## 📊 Annex A Controls - Statement of Applicability

**93 controles ISO 27001:2022**:

| Theme | Total | Implemented | Partial | Not Impl | N/A |
|-------|-------|-------------|---------|----------|-----|
| **5. Organizational** | 37 | 32% | 49% | 14% | 5% |
| **6. People** | 8 | 25% | 50% | 25% | 0% |
| **7. Physical** | 14 | 7% | 0% | 21% | 71% |
| **8. Technological** | 34 | 41% | 35% | 24% | 0% |
| **TOTAL** | **93** | **31%** | **39%** | **17%** | **13%** |

**Nota**: 70% implementados ou parciais. Meta: 85% até Jul/2026.

---

## 🎯 18 Riscos Identificados

### Riscos CRITICAL (Score 20-25)
- **RISK-001**: S3 bucket misconfiguration (biometric data breach) - Score: **25**
- **RISK-003**: AWS root account compromise - Score: **20**
- **RISK-007**: Ransomware attack - Score: **20**

### Riscos HIGH (Score 12-19) - Incluem AWS FTR Blockers
- **RISK-006**: tmpsaasboost IAM key >90 dias (AWS FTR blocker) - Score: **12**
- **RISK-011**: 8 CIS controls faltando (AWS FTR blocker) - Score: **15**
- **RISK-016**: CloudTrail logs não validados - Score: **12**
- E mais 3 riscos HIGH

### Riscos MEDIUM/LOW
- 7 riscos MEDIUM (score 6-11)
- 2 riscos LOW (score <5)

**Detalhes**: Ver `docs/04-risk-management/risk-register.md`

---

## 🗓️ Timeline & Milestones

### ✅ Concluído (Maio 2026)
- [x] Gap analysis completo
- [x] 14 documentos obrigatórios criados (100%)
- [x] 18 riscos identificados e mapeados
- [x] 4 NCRs e 4 CARs documentados
- [x] Glossário ISO 27001 (100+ termos)
- [x] Ricardo Esper designado como Gestor SGSI

### 🔴 Urgente (Jun 2026)
- [ ] CEO assinar Information Security Policy
- [ ] Implementar CAR-001, CAR-002, CAR-003, CAR-004 (15-20h DevOps)
- [ ] Resolver AWS FTR blockers
- [ ] Contratar auditor de certificação ISO 27001

### 🟡 Importante (Jul-Ago 2026)
- [ ] 4 auditorias internas (IA-001 a IA-004)
- [ ] Stage 1 audit (document review)
- [ ] Stage 2 audit (on-site assessment)
- [ ] Implementar 5 SOPs operacionais
- [ ] Security Awareness training (100% equipe)

### 🟢 Certificação (Set 2026)
- [ ] Certificado ISO 27001:2022 emitido
- [ ] 🎉 Celebrar!

---

## 💰 Investimento Estimado

| Item | Valor | Status | Timing |
|------|-------|--------|--------|
| Auditor certificação ISO 27001 | €15k-20k | Orçamento pendente | Q2 2026 |
| AWS Config + Security Hub | €50-200/mês | Aprovado | Imediato |
| Training platform | €500/ano | Orçamento pendente | Q2 2026 |
| Pentesting anual | €5k | Planejado | Q3 2026 |
| Junior DevOps (mitigar SPOF) | €40k-50k/ano | Planejado | Q3 2026 |
| **TOTAL Ano 1** | **€60-75k** | | |

---

## 🚀 Como Usar Este Repositório

### Para o Gestor SGSI (Ricardo)
1. Revisar todos os documentos em `docs/`
2. Coletar assinatura do CEO em `SGSI-POLICY-001`
3. Acompanhar implementação dos 4 CARs (DevOps)
4. Agendar auditorias internas (Jul/Ago 2026)
5. Contratar auditor de certificação

### Para o DevOps Lead
1. Ver `docs/05-evidence/corrective-action-log.md` para CARs
2. Prioridade: CAR-001 (MFA) e CAR-003 (AWS Config)
3. Deadline: 08/06/2026 (AWS FTR blockers)

### Para o CEO
1. Assinar `docs/02-policies/information-security-policy.md`
2. Aprovar orçamento (€60-75k)
3. Participar de Management Reviews (trimestrais)

### Para Auditores
1. Ver `docs/04-risk-management/statement-of-applicability.md` (SoA)
2. Ver `docs/05-evidence/` para registros de auditoria
3. Consultar `GLOSSARY.md` para termos específicos TWYN

---

## 📞 Contatos

**Gestor SGSI**: Ricardo Esper  
📧 resper@bekaa.eu  
🏢 Bekaa Trusted Advisors  

**Consultor ISO 27001**: Bekaa Trusted Advisors  
🌐 https://bekaa.eu  

---

## 📚 Recursos Adicionais

- **ISO 27001:2022 Standard**: https://www.iso.org/standard/27001
- **LGPD (Lei Geral de Proteção de Dados)**: Lei nº 13.709/2018
- **CIS AWS Foundations Benchmark**: https://www.cisecurity.org/benchmark/amazon_web_services
- **AWS Security Best Practices**: https://docs.aws.amazon.com/security/

---

## 🔒 Classificação

**Documento**: Public  
**Repositório**: Public (documentação ISO 27001 pode ser pública)  
**Dados Sensíveis**: Não incluídos (biometric data, credentials, etc. estão fora deste repo)

---

## 📜 Licença e Propriedade

© 2026 TWYN. Todos os direitos reservados.  
Documentação ISO 27001:2022 preparada por Bekaa Trusted Advisors.

Este repositório contém documentação de compliance. Não contém código-fonte, dados sensíveis, ou propriedade intelectual confidencial.

---

**Última atualização**: 2026-05-26  
**Próxima revisão**: Management Review Q2 2026 (Junho)
