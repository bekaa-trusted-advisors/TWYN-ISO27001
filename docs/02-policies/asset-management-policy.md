---
document_id: SGSI-POLICY-004
title: Asset Management Policy
version: 1.0
date: 2026-05-26
annex_a_controls: "A.5.9, A.5.10, A.5.11, A.5.12"
---

# Asset Management Policy

## 1. Purpose
Identificar, classificar, e proteger ativos de informação conforme seu valor de negócio e criticidade.

## 2. Scope
Todos os ativos no escopo ISMS:
- **Information Assets**: Dados biométricos, código-fonte, documentação ISO, credentials
- **Infrastructure**: AWS resources (EC2, RDS, S3, EKS)
- **Software**: Aplicações, libraries, containers
- **People**: Colaboradores com conhecimento crítico

## 3. Asset Inventory
**Mandatory**: Manter inventory atualizado em SGSI-ASSETS-001

**Campos obrigatórios**:
- Asset ID, Nome, Tipo, Owner, Custodian
- Classification, Location, Status
- Last update, Dependencies, Risks

**Update frequency**:
- Imediatamente: Novos ativos, mudanças de owner
- Mensal: Validação geral
- Trimestral: Deep audit

## 4. Information Classification

### Levels
**PUBLIC**: 
- Informação pública (website, marketing)
- Nenhuma proteção especial

**INTERNAL**: 
- Documentos internos, emails, código não-sensível
- Acesso apenas colaboradores TWYN
- Encryption in transit

**CONFIDENTIAL**:
- Código-fonte Face ID, configurações AWS, credenciais
- Access control (least privilege)
- Encryption at-rest + in-transit
- Audit logging

**RESTRICTED** (categoria especial LGPD):
- **Dados biométricos** (embeddings faciais)
- Strict access control (DevOps + autorização Gestor SGSI)
- Encryption AES-256
- Geographic restrictions (data residency)
- Retention limits (delete após X dias se não mais necessário)
- Pseudonymization quando possível

### Labeling
- Documentos: Header/footer "CONFIDENTIAL - TWYN"
- Emails: Subject prefix [CONFIDENTIAL]
- Files: Metadata tags
- S3 buckets: Tags (Classification: Restricted)

## 5. Asset Handling

### Storage
- **INTERNAL+**: Google Drive corporativo, Slack
- **CONFIDENTIAL**: GitHub (private repos), AWS
- **RESTRICTED**: S3 com KMS encryption, RDS com encryption at-rest

### Transmission
- Email: CONFIDENTIAL ou menos (TLS)
- RESTRICTED: Nunca via email (usar signed S3 URLs temporários)
- USB drives: Proibido para CONFIDENTIAL/RESTRICTED

### Disposal
- **Dados**: Secure delete (overwrite 3x ou AWS KMS key deletion)
- **Hardware**: Wiping certificado ou destruição física
- **Paper**: Shredding
- **Logs de deletion**: Manter evidência

## 6. Asset Ownership

### Roles
**Asset Owner**: 
- Responsável por classificação
- Aprova access requests
- Define retention period
- Exemplo: CEO (business data), CTO (technical assets)

**Asset Custodian**: 
- Implementa proteções técnicas
- Monitora compliance
- Exemplo: DevOps Lead (AWS infra), Gestor SGSI (docs ISO)

**Users**: 
- Seguem handling rules
- Reportam problemas

### RACI
Detalhado em SGSI-RACI-001

## 7. Acceptable Use

### Permitted
- Uso para fins de trabalho TWYN
- Acesso dentro de role permissions
- Personal use razoável (email, occasional browsing)

### Prohibited
- Download de software não autorizado
- Uso de ativos TWYN para negócios pessoais
- Sharing de credenciais
- Acesso não autorizado (mesmo "only looking")
- Bypass de security controls

### BYOD
- Permitido se: Full disk encryption + screen lock + antivirus
- Não armazenar RESTRICTED em devices pessoais
- Wipe remoto habilitado (MDM se necessário)

## 8. Physical Assets

### Laptops
- Encryption obrigatória (BitLocker/FileVault)
- Screen lock após 5 min
- Antivirus atualizado
- Reportar perda/roubo imediatamente (remote wipe)

### Mobile Devices
- MFA setup
- Passcode obrigatório
- Company data em app containerizado (se possível)

### Office Equipment
- Não aplicável (cloud-only, trabalho remoto)

## 9. Lifecycle Management

### Acquisition
- Approval process (requisition → manager → procurement)
- Add to inventory upon arrival
- Onboarding setup (encryption, monitoring)

### Operation
- Regular patching/updates
- Monitoring (CloudWatch, GuardDuty)
- Access reviews (quarterly)

### Decommissioning
- Remove from inventory
- Revoke all access
- Secure disposal
- Document in Asset Inventory (status: Decommissioned)

## 10. Cloud Assets (AWS)

### Tagging Strategy
Obrigatório para todos recursos AWS:
- `Environment`: prod/staging/dev
- `Owner`: email do owner
- `Classification`: public/internal/confidential/restricted
- `CostCenter`: budget allocation
- `ManagedBy`: terraform/manual

### Resource Management
- Use IaC (Terraform) sempre que possível
- No manual changes in prod without change ticket
- Unused resources deleted monthly (cost optimization)

## 11. Software Assets

### Licensing
- Only licensed software
- Track licenses in Asset Inventory
- Audit annually (compliance)

### Open Source
- Approved licenses only (permissive: MIT, Apache 2.0)
- No GPL in proprietary code (contamination risk)
- SBOM (Software Bill of Materials) maintained

### Dependencies
- Automated vulnerability scanning (Dependabot)
- Patch HIGH/CRITICAL within 30 days

## 12. Intellectual Property

### Ownership
- Código desenvolvido por colaboradores TWYN: Propriedade TWYN
- Contratos de trabalho incluem IP assignment clause
- Consultores: Work-for-hire agreements

### Protection
- Non-disclosure agreements (NDAs) para terceiros
- Code não open-sourced sem approval CEO
- Patents/trademarks registrados quando aplicável

## 13. Media Handling

### Removable Media
- USB drives: Encrypted, approved only
- External HDDs: Prohibited para RESTRICTED data
- CDs/DVDs: Not used (legacy)

### Backups
- S3 versioning (logical backups)
- RDS automated snapshots (7 days)
- Cross-region replication (DR)
- Test restoration quarterly (GAP-004)

## 14. Monitoring & Compliance

### Audit
- Trimestral: Asset inventory accuracy
- Anual: Classification review (over/under classified?)
- Ad-hoc: Após incidents

### Metrics
- % assets with classification: Target 100%
- % assets with defined owner: Target 100%
- Assets >1 year without review: Target 0

## 15. Related Documents
- SGSI-ASSETS-001: Asset Inventory (full list)
- SGSI-POLICY-001: Information Security Policy
- SOP-001: Onboarding (asset assignment)
- SOP-004: Secrets Management (credential assets)

## 16. Approval
- **Owner**: Gestor SGSI
- **Approved By**: CEO (Pendente)
- **Next Review**: 2026-12-31
