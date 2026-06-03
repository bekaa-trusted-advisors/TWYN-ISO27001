---
document_id: SGSI-GLOSSARY-001
title: Glossário - Termos e Definições ISO 27001:2022
version: 1.0
date: 2026-05-26
classification: Public
owner: Gestor SGSI
next_review: 2026-11-26
---

# Glossário - ISO 27001:2022 e Segurança da Informação

## Sobre este Documento

Este glossário define termos-chave usados na documentação do SGSI da TWYN. É um recurso de referência para todos os stakeholders (técnicos e não-técnicos) que interagem com o Sistema de Gestão de Segurança da Informação.

**Audience**: Todos os funcionários, auditores, consultores, e partes interessadas.

---

## A

### Access Control (Controle de Acesso)
Processo de limitar acesso a recursos (sistemas, dados, aplicações) apenas a usuários autorizados. Implementado através de autenticação, autorização, e princípio de least privilege.
- **Exemplo**: DevOps Lead tem acesso admin AWS, mas desenvolvedores apenas read-only em produção.
- **Referência**: Controles A.5.15-5.18

### Accountability (Responsabilização)
Na matriz RACI, é a pessoa que possui autoridade final sobre uma decisão ou atividade. Apenas 1 pessoa pode ser Accountable por atividade.
- **Exemplo**: CEO é Accountable por aprovar Information Security Policy.

### AES-256
Advanced Encryption Standard com chave de 256 bits. Algoritmo de criptografia simétrica considerado seguro para proteger dados sensíveis em repouso (at-rest).
- **Uso**: S3 buckets, RDS databases, EBS volumes na AWS.

### Annex A (Anexo A)
Lista de 93 controles de segurança no ISO 27001:2022, organizados em 4 temas (Organizational, People, Physical, Technological). A organização seleciona quais controles são aplicáveis no Statement of Applicability (SoA).
- **Versão anterior**: ISO 27001:2013 tinha 114 controles em 14 domínios.
- **Novo em 2022**: 11 controles novos (cloud, threat intel, data masking, secure coding).

### ANPD
Autoridade Nacional de Proteção de Dados. Órgão brasileiro responsável por fiscalizar e aplicar a LGPD.
- **Relevância**: Breach de dados pessoais deve ser notificado à ANPD em até 72 horas se houver risco aos titulares.

### Asset (Ativo)
Qualquer coisa de valor para a organização que precisa ser protegida. Pode ser informação (data), infraestrutura (servers), software (applications), ou pessoas (employees with privileged access).
- **Classificação TWYN**: CRITICAL, CONFIDENTIAL, INTERNAL, PUBLIC.
- **Referência**: SGSI-ASSETS-001 (Asset Inventory)

### Asset Owner (Proprietário de Ativo)
Pessoa responsável por um ativo específico, incluindo sua classificação, controles de proteção, e aprovação de acesso.
- **Exemplo**: DevOps Lead é owner do S3 bucket de dados biométricos.

### ATO (Authority to Operate)
Aprovação formal para operar um sistema de informação. Comum em contextos governamentais e compliance como FedRAMP.

### Audit (Auditoria)
Processo sistemático de examinar evidências para verificar se o SGSI está conforme ISO 27001:2022 e está operando eficazmente.
- **Tipos**: Internal audit (conduzida pela organização), External audit (conduzida por auditor certificador).
- **Frequência TWYN**: Auditorias internas trimestrais, auditorias externas anuais.

### Availability (Disponibilidade)
Um dos três pilares da CIA Triad. Garante que sistemas e dados estão acessíveis quando necessário por usuários autorizados.
- **Métrica**: Uptime, RTO (Recovery Time Objective), RPO (Recovery Point Objective).

### AWS (Amazon Web Services)
Provedor de cloud computing usado pela TWYN para hospedar a Face ID Platform API.
- **Account**: 992382542028 (production)
- **Serviços chave**: EKS, RDS, S3, CloudTrail, GuardDuty, Config, IAM, KMS.

### AWS Config
Serviço AWS que monitora e registra configurações de recursos para avaliar compliance com regras (ex: CIS Benchmarks).
- **Status TWYN**: Não implementado - CAR-003 (blocker AWS FTR).

### AWS FTR (Foundational Technical Review)
Revisão técnica da AWS para validar que arquitetura do cliente segue best practices. Necessário para desbloquear Advanced Tier Benefits e AWS Enterprise Support.
- **Blockers TWYN**: 3 issues (backup testing, CIS controls, IAM key rotation).

---

## B

### Backup
Cópia de dados armazenada separadamente do sistema original para permitir restauração em caso de perda, corrupção, ou desastre.
- **TWYN**: Backups diários de RDS (7 dias retention), S3 cross-region replication para us-west-2.
- **Requisito**: Testar restauração trimestralmente (CAR-004).
- **Referência**: Controles A.8.13-8.14

### Baseline
Configuração padrão segura de um sistema ou aplicação. Usado como referência para detectar desvios (drift).
- **Exemplo**: CIS AWS Foundations Benchmark define baseline de segurança para AWS.

### BCP (Business Continuity Plan)
Plano documentado para manter operações críticas de negócio durante e após um incidente ou desastre.
- **Relacionado**: Disaster Recovery (DR) é o componente técnico de TI do BCP.
- **Referência**: Controles A.5.29-5.30

### Biometric Data (Dados Biométricos)
Categoria especial de dados pessoais segundo LGPD (Art. 5º, II). Inclui características físicas únicas como face embeddings, impressões digitais, íris.
- **TWYN**: Face embeddings gerados pela Face ID Platform API.
- **Classificação**: CRITICAL (mais alto nível de proteção).
- **Requisitos**: Encryption at-rest + in-transit, access control rigoroso, audit logging, consent explícito.

### Break-glass
Procedimento de emergência para obter acesso privilegiado em situações críticas (ex: usar AWS root account apenas em emergência).
- **Requisito**: Documentar uso, alertar automaticamente, revisar logs.

---

## C

### CAR (Corrective Action Request)
Ação tomada para eliminar a causa raiz de uma não-conformidade e prevenir recorrência.
- **Estrutura**: Root cause analysis → Corrective actions → Preventive actions → Evidence → Verification.
- **TWYN**: 4 CARs abertos (MFA, key rotation, AWS Config, DR testing).
- **Referência**: SGSI-CAR-001

### CEO (Chief Executive Officer)
Autoridade máxima da organização. No contexto ISO 27001, o CEO DEVE demonstrar comprometimento com o SGSI e assinar a Information Security Policy.
- **Responsabilidades ISO 27001**: Aprovar política de SI, alocar recursos, aceitar riscos CRITICAL, participar de Management Review.

### Certification (Certificação)
Processo formal de auditoria por organismo certificador independente para validar conformidade com ISO 27001:2022.
- **Etapas**: Stage 1 (document review) → Stage 2 (on-site assessment) → Certificado emitido (3 anos) → Surveillance audits (anuais).
- **Target TWYN**: Q3 2026 (setembro).

### CIA Triad (Tríade CIA)
Três princípios fundamentais de segurança da informação:
- **C**onfidentiality (Confidencialidade): Dados acessíveis apenas a autorizados.
- **I**ntegrity (Integridade): Dados precisos e não modificados indevidamente.
- **A**vailability (Disponibilidade): Sistemas e dados acessíveis quando necessário.

### CIS Benchmarks
Center for Internet Security Benchmarks. Conjunto de best practices de hardening para sistemas operacionais, cloud providers, databases, etc.
- **Exemplo**: CIS AWS Foundations Benchmark (controles de IAM, logging, monitoring, networking).
- **TWYN**: 8 controles faltando - CAR-003.

### Classification (Classificação)
Categorização de informação de acordo com seu nível de sensibilidade e impacto se comprometida.
- **TWYN**: CRITICAL (biometric data) > CONFIDENTIAL (PII, code) > INTERNAL (docs) > PUBLIC (marketing).
- **Referência**: Control A.5.12, SGSI-ASSETS-001

### Clause (Cláusula)
Seção da norma ISO 27001:2022. Cláusulas 4-10 são obrigatórias e definem requisitos do SGSI.
- **4**: Context | **5**: Leadership | **6**: Planning | **7**: Support | **8**: Operation | **9**: Performance Evaluation | **10**: Improvement.

### Cloud-only Architecture
Infraestrutura 100% baseada em serviços de cloud (sem hardware físico on-premises).
- **TWYN**: 100% AWS - justifica N/A em 12 controles físicos (Theme 7).

### CloudTrail
Serviço AWS que registra todas as chamadas de API para auditoria e compliance.
- **TWYN**: Habilitado, logs armazenados em S3 com encryption, multi-region.
- **Uso**: Detectar uso não autorizado, investigação de incidentes, compliance.
- **Referência**: Control A.8.16

### Compliance
Conformidade com leis, regulamentos, normas, e políticas internas.
- **TWYN**: ISO 27001:2022, LGPD, AWS FTR, CIS Benchmarks.

### Confidentiality (Confidencialidade)
Propriedade de que informação não é disponibilizada ou divulgada a indivíduos, entidades ou processos não autorizados.
- **Controles**: Encryption, access control, NDAs, DLP (Data Leakage Prevention).

### Conformity (Conformidade)
Em auditoria, indica que um requisito ou controle está implementado conforme especificado e é eficaz.
- **Oposto**: Non-conformity (não-conformidade).

### Consulted (Consultado)
Na matriz RACI, pessoa que fornece input e expertise antes de decisão ou ação ser tomada (comunicação bidirecional).
- **Exemplo**: DPO/Legal é consultado ao definir risk treatment para dados biométricos.

### Control (Controle)
Medida que modifica risco. Pode ser preventiva (evita incidente), detectiva (detecta incidente), ou corretiva (corrige após incidente).
- **ISO 27001:2022**: 93 controles no Annex A.
- **Tipos**: Technical (firewalls, encryption), Administrative (policies, training), Physical (locks, CCTV - N/A para TWYN).

### Corrective Action
Ver **CAR (Corrective Action Request)**.

### CRITICAL (Classificação)
Nível mais alto de classificação de dados na TWYN. Perda ou exposição causa dano irreparável.
- **Exemplos**: Biometric data, encryption keys, AWS root credentials.
- **Controles obrigatórios**: Encryption at-rest + in-transit, MFA, audit logging, DLP, backup off-site.

---

## D

### Data Breach (Violação de Dados)
Incidente de segurança onde dados são acessados, divulgados, ou roubados sem autorização.
- **LGPD**: Notificar ANPD em até 72h se houver risco aos titulares.
- **ISO 27001**: Registrar no incident log, investigar root cause, implementar CAs.

### Data Leakage Prevention (DLP)
Tecnologia e processos para prevenir exfiltração não autorizada de dados sensíveis.
- **Exemplo**: Bloquear commits de credentials em Git, escanear emails para PII.
- **Referência**: Control A.8.12

### Data Masking (Mascaramento de Dados)
Técnica de ofuscar dados sensíveis em ambientes não-produção para proteger privacidade.
- **Exemplo**: Substituir CPFs reais por valores fake em staging.
- **Referência**: Control A.8.11 (novo em 2022)

### DevOps Lead
Papel técnico responsável por infraestrutura AWS, segurança de rede, e implementação de controles técnicos.
- **TWYN**: Owner de 24 ativos (11 CRITICAL) - representa SPOF (RISK-015).

### Disaster Recovery (DR)
Conjunto de políticas, ferramentas e procedimentos para restaurar sistemas críticos após desastre.
- **Métricas**: RTO (Recovery Time Objective), RPO (Recovery Point Objective).
- **TWYN**: RTO <8h, RPO <4h.
- **Referência**: Controles A.5.29-5.30, CAR-004

### DPO (Data Protection Officer)
Encarregado de Proteção de Dados segundo LGPD. Responsável por compliance com lei de privacidade, DPIAs, e comunicação com ANPD.
- **TWYN**: Externo (a contratar).

### Drift
Desvio de uma configuração de sistema em relação ao baseline aprovado.
- **Exemplo**: Security group AWS com regra adicionada manualmente fora do Terraform.
- **Detecção**: AWS Config.

---

## E

### EKS (Elastic Kubernetes Service)
Serviço gerenciado de Kubernetes da AWS. TWYN usa EKS para hospedar Face ID Platform API em containers.
- **Cluster**: twyn-faceid-prod
- **Multi-AZ**: us-east-1a, us-east-1b.

### Encryption at-rest
Criptografia de dados armazenados em disco (storage).
- **TWYN**: AES-256 em S3, RDS, EBS.
- **Referência**: Control A.8.24

### Encryption in-transit
Criptografia de dados em movimento pela rede (durante transmissão).
- **TWYN**: TLS 1.2+ obrigatório para todas as conexões (API, RDS, S3).
- **Referência**: Control A.8.24

### Evidence (Evidência)
Documentos, registros, screenshots, logs, ou outras provas objetivas usadas para demonstrar conformidade em auditoria.
- **Exemplos**: Certificados de training, screenshots de AWS console com MFA enabled, CloudTrail logs, relatórios de vulnerability scan.
- **Armazenamento TWYN**: `docs/05-evidence/`

---

## F

### Face Embeddings
Representação matemática de características faciais únicas. Usado pela Face ID Platform API para reconhecimento facial.
- **Classificação**: CRITICAL (dados biométricos segundo LGPD).
- **Armazenamento**: S3 bucket com encryption AES-256, acesso restrito apenas à aplicação.

### Finding (Achado)
Resultado de auditoria ou assessment. Pode ser conformity, non-conformity (maior/menor), ou observation.

### FTR
Ver **AWS FTR (Foundational Technical Review)**.

---

## G

### Gap Analysis
Processo de comparar estado atual (as-is) com estado desejado (to-be) para identificar gaps (lacunas).
- **TWYN**: Gap analysis identificou 8 gaps principais, resultando em 4 NCRs e 4 CARs.

### Gestor SGSI (ISMS Manager)
Pessoa responsável por coordenar e gerenciar o SGSI. Ponto focal para certificação ISO 27001.
- **Requisitos**: ISO 27001 Lead Implementer certification (40h), experiência em risk management.
- **Status TWYN**: **NÃO CONTRATADO - CRITICAL BLOCKER**.

### GuardDuty
Serviço AWS de threat detection que monitora atividades maliciosas e comportamentos anômalos.
- **TWYN**: Habilitado em us-east-1.
- **Referência**: Control A.5.7 (Threat intelligence)

---

## H

### Hardening
Processo de reduzir superfície de ataque de um sistema removendo serviços desnecessários, aplicando patches, e configurando security controls.
- **Exemplo**: Disable SSH em servidores, usar IMDSv2 no EC2, habilitar MFA.

---

## I

### IAM (Identity and Access Management)
Serviço AWS para gerenciar usuários, grupos, roles, e permissões.
- **Princípios**: Least privilege, MFA, key rotation (90 dias), no root account usage.
- **TWYN Issue**: Access key "tmpsaasboost" >90 dias (CAR-002).

### IaC (Infrastructure as Code)
Prática de gerenciar infraestrutura via código versionado (ex: Terraform, CloudFormation).
- **TWYN**: Terraform usado para provisionar AWS resources.
- **Benefício**: Repeatability, auditability, drift detection.

### Impact
No contexto de risk assessment, magnitude de dano se uma ameaça se materializar.
- **Escala TWYN**: 1 (Very Low) a 5 (Catastrophic).
- **Dimensões**: Financeiro, reputacional, legal, operacional.

### Incident (Incidente)
Evento que compromete confidencialidade, integridade, ou disponibilidade de informação.
- **Classificação TWYN**: CRITICAL (data breach), HIGH (produção down), MEDIUM (controle falhou), LOW (security event).
- **Processo**: Detectar → Classificar → Responder → Investigar → Documentar → Lições aprendidas.
- **Referência**: Controles A.5.24-5.28

### Informed (Informado)
Na matriz RACI, pessoa que recebe updates sobre progresso ou resultados de ação (comunicação unidirecional).
- **Exemplo**: CEO é informado sobre incidentes CRITICAL após resposta inicial.

### Information Security (Segurança da Informação)
Preservação da confidencialidade, integridade e disponibilidade da informação.

### Information Security Policy
Documento top-level que expressa intenção e direção da liderança sobre segurança da informação. DEVE ser assinado pelo CEO.
- **TWYN**: SGSI-POLICY-001 (22.4KB, 26 seções).
- **Status**: **CEO signature pending (obrigatório para certificação)**.

### Integrity (Integridade)
Propriedade de que informação é precisa e completa, e não foi modificada indevidamente.
- **Controles**: Checksums, digital signatures, access control, audit logging.

### Internal Audit (Auditoria Interna)
Auditoria conduzida pela própria organização (ou terceiro contratado) para avaliar SGSI antes de auditoria externa.
- **TWYN**: 4 auditorias agendadas Jul-Ago 2026.
- **Requisito ISO 27001**: Pelo menos 1x por ano cobrindo todo o SGSI.
- **Referência**: Cláusula 9.2, SGSI-AUDIT-001

### ISO 27001:2022
Norma internacional que especifica requisitos para estabelecer, implementar, manter e melhorar continuamente um SGSI.
- **Diferença vs 2013**: 93 controles (vs 114), 4 themes (vs 14 domains), 11 controles novos (cloud, data masking, secure coding, etc.).
- **Transição**: Certificados 2013 expiraram em outubro 2025.

### ISMS (Information Security Management System)
Ver **SGSI**.

---

## J

### Justification (Justificativa)
No SoA, explicação de por que um controle foi selecionado (ou não selecionado, se N/A).
- **Exemplo N/A**: "Control A.7.1 (Physical security perimeter) não aplicável - TWYN opera 100% em AWS cloud sem facilities físicos."

---

## K

### KMS (Key Management Service)
Serviço AWS para criar e gerenciar chaves criptográficas.
- **TWYN**: Usado para encryption at-rest de S3, RDS, EBS.
- **Referência**: Control A.8.24

### KPI (Key Performance Indicator)
Métrica mensurável para avaliar sucesso de objetivos de SI.
- **Exemplos TWYN**: % controles implementados (target 85%), incidentes CRITICAL (target 0), backup success rate (target 100%).

---

## L

### Least Privilege
Princípio de conceder apenas as permissões mínimas necessárias para executar uma tarefa.
- **Exemplo**: Desenvolvedores têm read-only em produção, não admin.

### LGPD (Lei Geral de Proteção de Dados)
Lei brasileira nº 13.709/2018 que regula tratamento de dados pessoais.
- **Categorias especiais**: Dados biométricos (Face ID Platform), dados de saúde, origem racial, etc.
- **Requisitos**: Consent, purpose limitation, data minimization, security, breach notification (<72h).

### Likelihood (Probabilidade)
No risk assessment, chance de uma ameaça se materializar.
- **Escala TWYN**: 1 (Rare) a 5 (Almost Certain).
- **Fatores**: Vulnerabilidades existentes, atratividade do alvo, histórico de incidentes.

### Logging
Registro de eventos de sistemas, aplicações e segurança para auditoria, troubleshooting e incident response.
- **TWYN**: CloudTrail (API calls), application logs (CloudWatch), GuardDuty (threat alerts).
- **Requisito**: Logs imutáveis, retention ≥1 ano, monitoramento em tempo real.
- **Referência**: Control A.8.15-8.16

---

## M

### Major Non-Conformity (Não-conformidade Maior)
Falha sistêmica ou ausência de controle obrigatório que pode comprometer eficácia do SGSI.
- **Impacto em certificação**: Impede emissão de certificado até ser resolvida.
- **TWYN**: 3 MAJORs (MFA root, AWS Config, DR testing).

### Management Review
Reunião trimestral da liderança (CEO obrigatório) para avaliar desempenho do SGSI e tomar decisões estratégicas.
- **Inputs**: Mudanças externas, performance de objetivos, resultados de auditorias, status de CAs, feedback de stakeholders.
- **Outputs**: Decisões, ações, alocação de recursos.
- **Referência**: Cláusula 9.3, SGSI-MREVIEW-001

### MFA (Multi-Factor Authentication)
Autenticação que requer 2 ou mais fatores: algo que você sabe (password), algo que você tem (token), algo que você é (biometria).
- **TWYN Requirement**: MFA obrigatório para acesso a dados CRITICAL e AWS root account.
- **Issue**: CAR-001 - Root account sem MFA.

### Minor Non-Conformity (Não-conformidade Menor)
Falha isolada que não compromete SGSI como um todo.
- **Impacto em certificação**: Não bloqueia certificação, mas deve ser corrigida em prazo (tipicamente 90 dias).
- **TWYN**: 1 MINOR (IAM key >90 dias).

### Mitigate (Mitigar)
Opção de risk treatment que reduz likelihood ou impact de um risco através de controles.
- **Exemplo**: Implementar MFA reduz likelihood de account compromise.

### Monitoring (Monitoramento)
Observação contínua de sistemas, redes e logs para detectar anomalias e incidentes.
- **TWYN**: GuardDuty (threats), CloudWatch (metrics), Security Hub (findings).
- **Referência**: Control A.8.16

### MTTD (Mean Time to Detect)
Tempo médio para detectar um incidente de segurança.
- **Target TWYN**: <15 minutos (via GuardDuty alerting).

### MTTR (Mean Time to Respond)
Tempo médio para responder a um incidente (conter, remediar).
- **Target TWYN**: <4 horas para incidentes CRITICAL.

---

## N

### N/A (Not Applicable)
No SoA, indica que um controle não é aplicável ao escopo do SGSI.
- **Requisito**: Justificativa documentada obrigatória.
- **TWYN**: 12 controles físicos (Theme 7) marcados N/A - arquitetura 100% cloud.

### NCR (Nonconformity Report)
Ver **Non-Conformity**.

### NDA (Non-Disclosure Agreement)
Acordo de confidencialidade assinado por funcionários, contratados, ou parceiros para proteger informação confidencial.

### Non-Conformity (Não-conformidade)
Não atendimento de requisito da norma ISO 27001 ou do SGSI implementado.
- **Tipos**: Major (sistêmica/grave), Minor (isolada/leve).
- **TWYN**: 4 NCRs identificados no gap analysis.
- **Referência**: Cláusula 10.1, SGSI-NCR-001

---

## O

### Objective (Objetivo)
Meta mensurável de segurança da informação alinhada com política de SI e requisitos de negócio.
- **TWYN 2026**: 6 objetivos (ISO cert, AWS FTR, zero incidents, 100% training, reduce SPOF, RPO/RTO).
- **Requisito ISO 27001**: Cláusula 6.2.
- **Referência**: SGSI-OBJ-001

### Observation (Observação)
Em auditoria, oportunidade de melhoria que NÃO é uma não-conformidade.
- **Exemplo**: "Processo de key rotation está funcionando, mas poderia ser automatizado para maior eficiência."

### Offboarding
Processo de remoção de acesso e retorno de ativos quando funcionário deixa a organização.
- **TWYN Checklist**: D-7 (notificar), D-Day 16:00 (revogar acessos), D+1 (verificar), D+7 (audit logs).
- **Referência**: Control A.6.5-6.6, SOP-001

### Onboarding
Processo de provisionar acessos e treinar novos funcionários.
- **TWYN Requirement**: Completar Security Awareness Training em 30 dias.
- **Referência**: Control A.6.1-6.2, SOP-001

### OWASP Top 10
Lista das 10 vulnerabilidades de aplicações web mais críticas segundo Open Web Application Security Project.
- **2021 Top 3**: Broken Access Control, Cryptographic Failures, Injection.
- **TWYN**: Dev Team deve completar OWASP training até Q3 2026.
- **Referência**: Control A.8.28 (Secure coding)

---

## P

### Penetration Testing (Pentest)
Simulação de ataque cibernético para identificar vulnerabilidades exploráveis.
- **TWYN**: Recomendado anualmente (€5k).
- **Referência**: Control A.8.29

### Performance Evaluation (Avaliação de Desempenho)
Cláusula 9 da ISO 27001. Inclui monitoring, internal audit, e management review.

### Phishing
Ataque de engenharia social onde atacante se passa por entidade confiável para roubar credenciais ou instalar malware.
- **TWYN Mitigation**: Security Awareness Training trimestral + phishing simulation mensal.
- **Target**: <5% fail rate em simulações.

### PII (Personally Identifiable Information)
Informação que pode identificar um indivíduo (nome, email, CPF, telefone, IP).
- **TWYN**: Customer PII classificado CONFIDENTIAL.
- **LGPD**: Chamado "dados pessoais".

### Policy (Política)
Documento formal que define intenção, princípios e regras da organização.
- **Hierarquia**: Policy (estratégico) → Procedure/SOP (tático) → Work instruction (operacional).
- **TWYN**: Information Security Policy (SGSI-POLICY-001) é top-level.

### Preventive Control (Controle Preventivo)
Controle que previne incidente de ocorrer.
- **Exemplos**: Firewall, MFA, encryption, access control, security training.

### Privileged Access (Acesso Privilegiado)
Acesso com permissões elevadas (admin, root, sudoers) que permite modificar sistemas críticos.
- **TWYN**: AWS root account, IAM admin, RDS master user.
- **Requisitos**: MFA obrigatório, audit logging, least privilege, recertification trimestral.

---

## Q

### Quarterly (Trimestral)
Frequência de atividades no SGSI: Management Review, IAM recertification, security awareness training refresh, backup DR testing.

---

## R

### RACI Matrix
Framework para definir roles e responsabilidades:
- **R**esponsible (Responsável): Executa a tarefa.
- **A**ccountable (Autoridade): Aprova e responde pelos resultados (apenas 1).
- **C**onsulted (Consultado): Fornece input antes de decisão.
- **I**nformed (Informado): Recebe update após decisão.
- **Referência**: SGSI-RACI-001

### Ransomware
Malware que criptografa dados da vítima e exige pagamento (ransom) para descriptografar.
- **TWYN**: RISK-007 (score 20 - CRITICAL).
- **Mitigação**: Backups off-site imutáveis, endpoint protection, security awareness, GuardDuty.

### RDS (Relational Database Service)
Serviço AWS de banco de dados relacional gerenciado.
- **TWYN**: PostgreSQL Multi-AZ em us-east-1 (twyn-prod-db).
- **Proteção**: Encryption at-rest (KMS), encryption in-transit (TLS 1.2+), backups diários, VPC isolation.

### Residual Risk (Risco Residual)
Risco remanescente após implementação de controles.
- **Exemplo**: RISK-001 score inicial 25 → após encryption + access control → residual score 10.

### Responsible (Responsável)
Na matriz RACI, pessoa(s) que executam a tarefa ou implementam o controle.

### Risk (Risco)
Efeito da incerteza nos objetivos. Em SI, tipicamente calculado como Likelihood × Impact.
- **TWYN**: 18 riscos identificados (3 CRITICAL, 6 HIGH, 7 MEDIUM, 2 LOW).
- **Referência**: SGSI-RISK-002

### Risk Acceptance (Aceitação de Risco)
Decisão consciente de aceitar um risco sem implementar controles adicionais.
- **Requisito**: Aprovação formal do risk owner (CEO para riscos CRITICAL).

### Risk Assessment (Avaliação de Risco)
Processo de identificar, analisar e avaliar riscos.
- **TWYN Methodology**: Qualitativa, Likelihood (1-5) × Impact (1-5) = Risk Score (1-25).
- **Frequência**: Trimestral ou quando mudanças significativas.
- **Referência**: Cláusula 6.1.2, SGSI-RISK-001

### Risk Register (Registro de Riscos)
Documento que lista todos os riscos identificados com suas características (threat, vulnerability, likelihood, impact, score, treatment, owner, controls).
- **Referência**: SGSI-RISK-002

### Risk Treatment (Tratamento de Risco)
Ação para modificar risco. Opções: Mitigate, Accept, Avoid, Transfer.
- **Referência**: Cláusula 6.1.3, SGSI-RTP-001

### Root Account
Conta com privilégios ilimitados em um sistema. Em AWS, é a conta criada ao abrir account.
- **Best Practice**: Nunca usar para operações do dia-a-dia, habilitar MFA, monitorar uso.
- **TWYN Issue**: CAR-001 - MFA não habilitado.

### RPO (Recovery Point Objective)
Quantidade máxima de dados que pode ser perdida (medida em tempo).
- **TWYN Target**: <4 horas (backups frequentes).

### RTO (Recovery Time Objective)
Tempo máximo aceitável para restaurar sistemas após desastre.
- **TWYN Target**: <8 horas.

---

## S

### S3 (Simple Storage Service)
Serviço AWS de object storage.
- **TWYN Buckets**: twyn-biometric-data (CRITICAL), twyn-backups-dr, twyn-cloudtrail-logs.
- **Proteção**: Encryption (AES-256), block public access, versioning, cross-region replication, bucket policies.

### SAST (Static Application Security Testing)
Análise de código-fonte para identificar vulnerabilidades sem executar aplicação.
- **Exemplo**: Detectar SQL injection, XSS, hardcoded credentials.

### Scope (Escopo)
Definição de limites do SGSI - quais processos, sistemas, localizações, e pessoas estão incluídos.
- **TWYN**: Face ID Platform API, AWS Account 992382542028, dados biométricos.
- **Referência**: Cláusula 4.3, SGSI-SCOPE-001

### Secure Coding
Práticas de desenvolvimento que previnem vulnerabilidades de segurança.
- **Princípios**: Input validation, output encoding, parameterized queries, error handling, least privilege.
- **Referência**: Control A.8.28 (novo em 2022)

### Security Awareness Training
Treinamento para educar funcionários sobre ameaças e boas práticas de segurança.
- **TWYN**: Trimestral, todos os funcionários, plataforma online.
- **Tópicos**: Phishing, password hygiene, clear desk, incident reporting, LGPD basics.
- **Referência**: Control A.6.3

### Security Hub
Serviço AWS que agrega findings de GuardDuty, Config, e outros serviços de segurança.
- **TWYN**: Parcialmente implementado.

### Segregation of Duties
Princípio de dividir responsabilidades críticas entre múltiplas pessoas para prevenir fraude ou erro.
- **Exemplo**: Pessoa que cria usuário IAM não deve ser a mesma que aprova permissões.

### SGSI (Sistema de Gestão de Segurança da Informação)
Conjunto de políticas, procedimentos, processos e controles para gerenciar sistematicamente riscos de segurança da informação.
- **Equivalente em inglês**: ISMS (Information Security Management System).
- **Norma**: ISO/IEC 27001:2022.

### Single Point of Failure (SPOF)
Componente cuja falha causa falha total do sistema.
- **TWYN**: DevOps Lead é SPOF humano (RISK-015) - owner de 11 ativos CRITICAL.
- **Mitigação**: Contratar backup DevOps, documentar runbooks, cross-training.

### SoA (Statement of Applicability)
Documento OBRIGATÓRIO que lista todos os 93 controles Anexo A, indicando quais são aplicáveis (com justificativa) e quais não são (com justificativa de exclusão).
- **TWYN**: 70% implementados ou parciais, 17% não implementados, 13% N/A.
- **Referência**: Cláusula 6.1.3d, SGSI-SOA-001

### SOP (Standard Operating Procedure)
Procedimento operacional padrão - documento tático que descreve passo-a-passo como executar uma atividade.
- **TWYN Planned**: SOP-001 (Onboarding/Offboarding), SOP-002 (Change Mgmt), SOP-003 (Remote Work), SOP-004 (Secrets), SOP-005 (IAM Recertification).

### SPOF
Ver **Single Point of Failure**.

### SQL Injection
Vulnerabilidade onde atacante injeta comandos SQL maliciosos via input de aplicação.
- **Mitigação**: Parameterized queries, input validation, WAF.
- **OWASP Top 10**: #3 Injection.

### Stage 1 Audit
Primeira fase de auditoria de certificação ISO 27001. Foco em document review (políticas, procedimentos, SoA, risk register).
- **TWYN Target**: Julho 2026.

### Stage 2 Audit
Segunda fase de auditoria de certificação. Foco em on-site assessment, entrevistas, verificação de evidências técnicas, eficácia de controles.
- **TWYN Target**: Agosto 2026.

### Stakeholder (Parte Interessada)
Pessoa ou organização que pode afetar, ser afetada por, ou perceber-se afetada por uma decisão ou atividade do SGSI.
- **TWYN**: Clientes, funcionários, AWS, auditores, ANPD, acionistas.

### Surveillance Audit
Auditoria anual de manutenção após certificação inicial para verificar que SGSI continua conforme.
- **Ciclo**: Ano 1: Certificação | Anos 2-3: Surveillance | Ano 4: Recertification.

---

## T

### Terraform
Ferramenta de Infrastructure as Code (IaC) para provisionar e gerenciar recursos cloud.
- **TWYN**: Usado para AWS resources.

### Threat (Ameaça)
Causa potencial de um incidente indesejado que pode resultar em dano.
- **Exemplos**: Hackers, malware, erro humano, desastre natural, insider threat.

### Threat Intelligence
Informação sobre ameaças emergentes, vulnerabilidades, e indicadores de compromisso.
- **TWYN**: GuardDuty fornece threat intel automaticamente.
- **Referência**: Control A.5.7 (novo em 2022)

### TLS (Transport Layer Security)
Protocolo criptográfico para comunicação segura pela rede.
- **TWYN**: TLS 1.2+ obrigatório (TLS 1.0 e 1.1 deprecados).

### Training
Ver **Security Awareness Training**.

### Transfer (Transferir)
Opção de risk treatment onde risco é compartilhado com terceiro (ex: seguro cyber, outsourcing).

### Treatment (Tratamento)
Ver **Risk Treatment**.

### Trust Services Criteria (TSC)
Framework usado em SOC 2 audits (não diretamente relevante para ISO 27001, mas mencionado para referência).
- **5 Critérios**: Security, Availability, Confidentiality, Processing Integrity, Privacy.

---

## U

### Uptime
Porcentagem de tempo que sistema está disponível e operacional.
- **Exemplo**: 99.9% uptime = ~8.7 horas de downtime por ano.

---

## V

### Vulnerability (Vulnerabilidade)
Fraqueza em um ativo ou controle que pode ser explorada por ameaça.
- **Exemplos**: Software sem patch, password fraca, S3 bucket mal configurado, falta de MFA.

### Vulnerability Management
Processo contínuo de identificar, avaliar, remediar e reportar vulnerabilidades.
- **Ferramentas**: Vulnerability scanners, SAST/DAST, penetration testing.
- **Referência**: Control A.8.8, A.8.29

---

## W

### WAF (Web Application Firewall)
Firewall que filtra tráfego HTTP/HTTPS para proteger aplicações web de ataques (SQLi, XSS, etc.).

---

## X

### XSS (Cross-Site Scripting)
Vulnerabilidade onde atacante injeta scripts maliciosos em páginas web vistas por outros usuários.
- **Mitigação**: Output encoding, Content Security Policy (CSP), WAF.
- **OWASP Top 10**: Parte de #3 Injection.

---

## Z

### Zero Trust
Modelo de segurança onde nenhum usuário ou sistema é confiável por padrão - todos devem ser verificados continuamente.
- **Princípios**: Verify explicitly, least privilege access, assume breach.

---

## Siglas e Acrônimos Comuns

| Sigla | Significado | Tradução/Descrição |
|-------|-------------|-------------------|
| **AES** | Advanced Encryption Standard | Algoritmo de criptografia |
| **ALB** | Application Load Balancer | Load balancer AWS camada 7 |
| **ANPD** | Autoridade Nacional de Proteção de Dados | Órgão fiscalizador LGPD (Brasil) |
| **API** | Application Programming Interface | Interface de programação |
| **ATO** | Authority to Operate | Autorização para operar (governo) |
| **AWS** | Amazon Web Services | Provedor cloud |
| **BCP** | Business Continuity Plan | Plano de continuidade de negócio |
| **CAR** | Corrective Action Request | Pedido de ação corretiva |
| **CEO** | Chief Executive Officer | Diretor executivo |
| **CIA** | Confidentiality, Integrity, Availability | Tríade de SI |
| **CIS** | Center for Internet Security | Organização de benchmarks |
| **CPF** | Cadastro de Pessoas Físicas | Identificação brasileira |
| **DAST** | Dynamic Application Security Testing | Teste de segurança dinâmico |
| **DLP** | Data Leakage Prevention | Prevenção de vazamento |
| **DNS** | Domain Name System | Sistema de nomes de domínio |
| **DPO** | Data Protection Officer | Encarregado de proteção de dados |
| **DR** | Disaster Recovery | Recuperação de desastre |
| **EBS** | Elastic Block Store | Storage AWS |
| **ECR** | Elastic Container Registry | Registro Docker AWS |
| **EKS** | Elastic Kubernetes Service | Kubernetes gerenciado AWS |
| **FTR** | Foundational Technical Review | Revisão técnica AWS |
| **GDPR** | General Data Protection Regulation | Lei europeia de privacidade |
| **IAM** | Identity and Access Management | Gestão de identidades AWS |
| **IaC** | Infrastructure as Code | Infraestrutura como código |
| **ISMS** | Information Security Management System | SGSI em inglês |
| **KMS** | Key Management Service | Serviço de chaves AWS |
| **KPI** | Key Performance Indicator | Indicador de desempenho |
| **LGPD** | Lei Geral de Proteção de Dados | Lei brasileira 13.709/2018 |
| **MFA** | Multi-Factor Authentication | Autenticação multifator |
| **MTTD** | Mean Time to Detect | Tempo médio para detectar |
| **MTTR** | Mean Time to Respond | Tempo médio para responder |
| **N/A** | Not Applicable | Não aplicável |
| **NDA** | Non-Disclosure Agreement | Acordo de confidencialidade |
| **NCR** | Nonconformity Report | Relatório de não-conformidade |
| **OWASP** | Open Web Application Security Project | Projeto de segurança web |
| **PII** | Personally Identifiable Information | Informação pessoal identificável |
| **RDS** | Relational Database Service | Banco dados AWS |
| **RPO** | Recovery Point Objective | Objetivo de ponto de recuperação |
| **RTO** | Recovery Time Objective | Objetivo de tempo de recuperação |
| **S3** | Simple Storage Service | Object storage AWS |
| **SAST** | Static Application Security Testing | Teste de segurança estático |
| **SGSI** | Sistema de Gestão de Segurança da Informação | ISMS em português |
| **SLA** | Service Level Agreement | Acordo de nível de serviço |
| **SNS** | Simple Notification Service | Notificações AWS |
| **SoA** | Statement of Applicability | Declaração de aplicabilidade |
| **SOP** | Standard Operating Procedure | Procedimento operacional |
| **SPOF** | Single Point of Failure | Ponto único de falha |
| **SQL** | Structured Query Language | Linguagem de banco de dados |
| **TLS** | Transport Layer Security | Segurança de transporte |
| **TSC** | Trust Services Criteria | Critérios SOC 2 |
| **VPC** | Virtual Private Cloud | Rede isolada AWS |
| **WAF** | Web Application Firewall | Firewall de aplicação web |
| **XSS** | Cross-Site Scripting | Injeção de script web |

---

## Document Control

| Field | Value |
|-------|-------|
| **Version** | 1.0 |
| **Last Updated** | 2026-05-26 |
| **Owner** | Gestor SGSI |
| **Next Review** | 2026-11-26 (Semestral) |
| **Classification** | Public (pode ser compartilhado com stakeholders externos) |

---

**Como usar este glossário**:
- Use Ctrl+F ou Cmd+F para buscar termos específicos
- Termos estão organizados alfabeticamente
- Cada termo inclui definição, exemplos práticos (quando aplicável), e referências a documentos SGSI
- Para dúvidas não cobertas, contatar Gestor SGSI

**Contribuições**: Se você identificar termos faltando ou definições que precisam ser clarificadas, envie feedback ao Gestor SGSI.
