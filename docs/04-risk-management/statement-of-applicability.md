---
document_id: SGSI-SOA-001
title: Statement of Applicability (SoA)
version: 2.0
date: 2026-06-02
owner: Gestor SGSI
approved_by: CEO (Aprovado - Ata 001)
---

# Declaração de Aplicabilidade (Statement of Applicability - SoA)

Este documento atende ao requisito da cláusula 6.1.3 (d) da ISO/IEC 27001:2022. Ele contém o relacionamento entre os controles exigidos (baseados na apreciação de riscos da TWYN) e os controles do Anexo A. 

A TWYN é uma provedora B2B de API de Reconhecimento Facial operando 100% remota com infraestrutura na nuvem AWS. Esta configuração dita a exclusão majoritária dos controles físicos corporativos (Anexo A.7), dado que não há escritórios físicos dentro do escopo do SGSI.

## 1. Controles Organizacionais (A.5)

| Ref. | Controle | Aplicável? | Status | Justificativa / Implementação |
|---|---|---|---|---|
| A.5.1 | Políticas para segurança da informação | Sim | Implementado | SGSI-POLICY-001 aprovada pela diretoria. |
| A.5.2 | Funções e responsabilidades da segurança | Sim | Implementado | Matriz RACI estabelecida (SGSI-RACI-001). |
| A.5.3 | Segregação de funções | Sim | Parcial | Regras de RBAC ativas, porém há SPOF em cargos chave (GAP). |
| A.5.4 | Responsabilidades da direção | Sim | Implementado | Revisão da direção executada e orçamento garantido. |
| A.5.5 | Contato com autoridades | Sim | Implementado | Contatos da ANPD mantidos pelo DPO (Pol. de SI Seç 4.6). |
| A.5.6 | Contato com grupos especiais | Sim | Implementado | Gestor SGSI e DevOps participam de fóruns e monitoram CVEs (Pol. de SI Seç 4.6). |
| A.5.7 | Inteligência de ameaças (Threat Intel) | Sim | Parcial | Assinaturas de feeds no GuardDuty e GitHub advisories. |
| A.5.8 | Segurança em gerenciamento de projetos | Sim | Implementado | Integrado no SDLC e Jira/Linear. |
| A.5.9 | Inventário de informações e outros ativos | Sim | Implementado | Ativos AWS listados (SGSI-ASSET-001). |
| A.5.10 | Uso aceitável da informação e ativos | Sim | Implementado | AUP policy estabelecida (SGSI-POLICY-007). |
| A.5.11 | Devolução de ativos | Sim | Implementado | Processo listado no SOP-001 (Offboarding). |
| A.5.12 | Classificação da informação | Sim | Implementado | Público/Interno/Confidencial/Restrito no IS Policy. |
| A.5.13 | Rótulos da informação | Sim | Parcial | Metadados aplicados em arquivos, falta tag em todo S3. |
| A.5.14 | Transferência da informação | Sim | Implementado | APIs usam estritamente TLS 1.3 (Face ID Platform). |
| A.5.15 | Controle de acesso | Sim | Implementado | SGSI-POLICY-002; MFA é padrão ouro. |
| A.5.16 | Gestão de identidade | Sim | Implementado | Contas baseadas no IAM e GitHub (SOP-001). |
| A.5.17 | Informação de autenticação | Sim | Parcial | AWS Secrets Manager (SOP-004). Chave 'tmpsaasboost' não rotacionada. |
| A.5.18 | Direitos de acesso | Sim | Implementado | Recertificação trimestral (SOP-005). |
| A.5.19 | Segurança em relacionamentos com fornecedores | Sim | Implementado | TPRA process, Supplier Security Questionnaire. |
| A.5.20 | Abordagem à segurança em contratos de fornecedores| Sim | Implementado | Cláusulas de DPAs assinadas em NDA. |
| A.5.21 | Gestão da cadeia de suprimento de TI | Sim | Parcial | Análise baseada no GitHub/AWS TPRAs (SGSI-TPRA). |
| A.5.22 | Monitoramento dos serviços de fornecedores | Sim | Parcial | Monitoramento de SLAs de uptime dos hiperescaladores. |
| A.5.23 | Segurança no uso de serviços em nuvem | Sim | Implementado | Modelo Shared Responsibility, uso do AWS Config/Security Hub. |
| A.5.24 | Gestão de incidentes de segurança | Sim | Parcial | Incident Response Policy criado, pendente testes. |
| A.5.25 | Avaliação de eventos de segurança | Sim | Implementado | Classificação de P0 a P4 implementada. |
| A.5.26 | Resposta a incidentes | Sim | Parcial | IRP necessita formalização prática de runbooks. |
| A.5.27 | Aprendizado com incidentes | Sim | Implementado | Requisito de Post-Mortem (CARs gerados após crise). |
| A.5.28 | Coleta de evidências | Sim | Parcial | Não há exclusão de logs em instâncias sob ataque. |
| A.5.29 | Segurança durante interrupções | Sim | Implementado | Descrito no BCP (SGSI-POLICY-006). |
| A.5.30 | Prontidão das TIC para continuidade | Sim | Parcial | BCP elaborado, testes semestrais de restore *nunca realizados* (RISK-009). |
| A.5.31 | Requisitos legais e regulamentares | Sim | Implementado | Conformidade com LGPD Art. 11 (Dados Sensíveis). |
| A.5.32 | Direitos de propriedade intelectual | Sim | Parcial | Políticas de uso de software licenciado apenas. |
| A.5.33 | Proteção de registros organizacionais | Sim | Implementado | Registros vitais em S3 versionado e logs imutáveis. |
| A.5.34 | Privacidade e dados pessoais | Sim | Implementado | Execução do RIPD (SGSI-RIPD-001) para dados biométricos. |
| A.5.35 | Análise crítica independente | Sim | Implementado | Auditorias internas planejadas semestralmente. |
| A.5.36 | Conformidade com políticas de segurança | Sim | Parcial | Auditado em revisões gerenciais anuais. |
| A.5.37 | Procedimentos operacionais documentados | Sim | Implementado | SOPs (001 a 005) criados e mantidos no GitHub. |

## 2. Controles de Pessoas (A.6)

| Ref. | Controle | Aplicável? | Status | Justificativa / Implementação |
|---|---|---|---|---|
| A.6.1 | Triagem de antecedentes (Background checks) | Sim | Parcial | Realizado para posições técnicas de alto nível no Onboarding. |
| A.6.2 | Termos e condições de contratação | Sim | Implementado | Acordos de confidencialidade (NDA) obrigatórios. |
| A.6.3 | Conscientização, educação e treinamento | Sim | Parcial | Programa de treinamento (TRAINING-PROGRAM) documentado. |
| A.6.4 | Processo disciplinar | Sim | Implementado | Listado na IS Policy (cláusula de sanções). |
| A.6.5 | Responsabilidades após término | Sim | Implementado | NDAs permanecem vigentes e acessos removidos (SOP-001). |
| A.6.6 | Acordos de confidencialidade | Sim | Implementado | Contratos exigem confidencialidade com penalidades explícitas. |
| A.6.7 | Trabalho remoto (Teletrabalho) | Sim | Implementado | TWYN é 100% remota; regras definidas em SOP-003. |
| A.6.8 | Notificação de eventos de segurança | Sim | Implementado | Fomentada cultura 'no-blame'; email security@twyn estabelecido. |

## 3. Controles Físicos (A.7)
*Nota: A TWYN é uma empresa 100% remota e todos os dados produtivos residem na infraestrutura da nuvem AWS. Devido ao escopo (delimitado ao Face ID Platform API e processos remotos), grande parte da segurança física tradicional de datacenters é terceirizada para a AWS, e não há "perímetro físico corporativo" sob controle da TWYN.*

| Ref. | Controle | Aplicável? | Status | Justificativa / Implementação |
|---|---|---|---|---|
| A.7.1 | Perímetros de segurança física | **Não** | N/A | TWYN não possui escritório físico. DC é AWS. |
| A.7.2 | Controle de entrada física | **Não** | N/A | Excluído pelo escopo remoto. AWS provê os controles no DC. |
| A.7.3 | Proteção de escritórios, salas | **Não** | N/A | Excluído pelo escopo remoto. |
| A.7.4 | Monitoramento de segurança física | **Não** | N/A | Excluído pelo escopo remoto. |
| A.7.5 | Proteção contra ameaças externas e ambientais | **Não** | N/A | Excluído pelo escopo remoto. |
| A.7.6 | Trabalho em áreas seguras | **Não** | N/A | Excluído pelo escopo remoto. (A.6.7 cobre o teletrabalho de forma lógica). |
| A.7.7 | Mesas e telas limpas (Clear desk) | Sim | Parcial | Orientado para o home-office (SOP-003). |
| A.7.8 | Localização e proteção de equipamentos | **Não** | N/A | Apenas laptops; sem servidores físicos ou roteadores da empresa. |
| A.7.9 | Segurança de equipamentos fora das instalações | Sim | Parcial | Laptops utilizados home-office devem usar FDE (Full Disk Encryption). |
| A.7.10| Mídias de armazenamento (Storage media) | **Não** | N/A | Uso de pendrives ou HD externos proibido ou irrelevante (100% cloud). |
| A.7.11| Utilidades (Fornecimento de energia, AC) | **Não** | N/A | Excluído pelo escopo. DC gerenciado pela AWS. |
| A.7.12| Segurança no cabeamento | **Não** | N/A | Excluído pelo escopo remoto. |
| A.7.13| Manutenção de equipamentos | **Não** | N/A | Excluído. Manutenção de servidores é da AWS. Laptops são trocados. |
| A.7.14| Descarte e reutilização de equipamentos | Sim | Parcial | Se houver reciclagem de laptop da empresa, o disco é apagado via wipe. |

## 4. Controles Tecnológicos (A.8)

| Ref. | Controle | Aplicável? | Status | Justificativa / Implementação |
|---|---|---|---|---|
| A.8.1 | Dispositivos de endpoint (User devices) | Sim | Parcial | MDM e Endpoint Security recomendado no SOP-003. |
| A.8.2 | Direitos de acesso a informações | Sim | Implementado | RBAC definido para Banco e API na AWS. |
| A.8.3 | Restrição de acesso a informações | Sim | Implementado | Somente portas essenciais (HTTPS) expostas publicamente. |
| A.8.4 | Acesso ao código-fonte | Sim | Implementado | GitHub restrito via repositórios privados e role-based access. |
| A.8.5 | Autenticação segura | Sim | Implementado | MFA mandatório e políticas de senhas rigorosas. |
| A.8.6 | Gerenciamento de capacidade | Sim | Implementado | Autoscaling e métricas no CloudWatch monitoram capacidades. |
| A.8.7 | Proteção contra malware | Sim | Parcial | Container scanning (Trivy) ativado nas pipelines CI/CD. |
| A.8.8 | Gestão de vulnerabilidades técnicas | Sim | Parcial | Processo de correção de CVEs integrado nos sprints de infra. |
| A.8.9 | Gerenciamento de configuração | Sim | Parcial | IaC via Terraform, mas AWS Config NÃO HABILITADO (RISK-002). |
| A.8.10| Eliminação de informações (Deletion) | Sim | Implementado | Regras de Lifecycle de S3 e scripts de sanitização de vetores. |
| A.8.11| Mascaramento de dados | Sim | Implementado | Logs são limpos de PII; banco de dados de dev mascarado. |
| A.8.12| Prevenção contra vazamento (DLP) | Sim | Não Imp. | Ferramentas tradicionais de DLP ainda ausentes nos endpoints. |
| A.8.13| Backup da informação | Sim | Parcial | Política de Backup (005), RDS e S3 ativos. Restores nunca testados. |
| A.8.14| Redundância de instalações | Sim | Implementado | Arquitetura Cloud-Native hospedada em Multi-AZ. |
| A.8.15| Geração de registros de log (Logging) | Sim | Implementado | Centralizado no CloudWatch; AWS CloudTrail ativo. |
| A.8.16| Monitoramento de atividades | Sim | Parcial | GuardDuty NÃO habilitado e Security Hub incompleto (RISK-005). |
| A.8.17| Sincronização de relógios | Sim | Implementado | NTP padronizado gerido nativamente pela infraestrutura AWS. |
| A.8.18| Uso de programas utilitários privilegiados | Sim | Parcial | Uso restrito via sessões documentadas no Change Management. |
| A.8.19| Instalação de software em prod | Sim | Implementado | Deployências feitas exclusivamente pelo GitHub Actions. |
| A.8.20| Redes seguras | Sim | Implementado | Separação em VPCs lógicas, Sub-redes públicas/privadas. |
| A.8.21| Segurança de serviços de rede | Sim | Implementado | WAF, AWS Shield, Security Groups rígidos operando por whitelist. |
| A.8.22| Segregação de redes | Sim | Implementado | Ambientes Dev, Staging e Prod rodam em VPCs isoladas. |
| A.8.23| Filtragem para web (Web filtering) | **Não** | N/A | TWYN não filtra navegação corporativa por ser 100% remoto BYOD. |
| A.8.24| Uso de criptografia | Sim | Implementado | Criptografia AWS KMS AES-256 in-rest e TLS 1.3 in-transit. |
| A.8.25| Ciclo de vida de dev. seguro (SDLC) | Sim | Implementado | Processo CI/CD engloba code-review e scan. (SOP-002). |
| A.8.26| Requisitos de segurança em aplicações | Sim | Implementado | Thread modeling incluído antes de mudanças arquiteturais. |
| A.8.27| Princípios de arquitetura segura | Sim | Implementado | Baseado em Well-Architected Framework (AWS). |
| A.8.28| Codificação segura (Secure coding) | Sim | Implementado | Práticas como validação de inputs e evitar OWASP Top 10. |
| A.8.29| Teste de segurança no desenvolvimento | Sim | Parcial | Depende das integrações atuais de GitHub Actions (Snyk/Trivy). |
| A.8.30| Engenharia terceirizada (Outsourced dev) | **Não** | N/A | A TWYN utiliza equipe interna para o desenvolvimento da API. |
| A.8.31| Separação dos ambientes (Dev/Test/Prod)| Sim | Implementado | Isolamento lógico via contas/VPCs distintas (SOP-002). |
| A.8.32| Gerenciamento de mudanças (Change Mgmt)| Sim | Implementado | Alterações seguem o fluxo de Pull Request (SOP-002). |
| A.8.33| Dados de teste | Sim | Implementado | Estritamente proibido usar dados biométricos reais em DEV. |
| A.8.34| Auditoria em sistemas da informação | Sim | Parcial | Processo manual, necessita evolução com a IA-001. |

---
*Declaração de Aplicabilidade elaborada e aprovada para atender ao requisito 6.1.3 da norma ISO 27001.*
