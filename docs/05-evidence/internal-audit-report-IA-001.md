---
document_id: SGSI-IA-001
title: "Relatório de Auditoria Interna IA-001 — Sistema de Gestão da Segurança da Informação (SGSI)"
version: "1.0"
status: Final
classification: CONFIDENTIAL
audit_date: "2026-06-02"
auditor: "Gestor SGSI (Auditoria Inicial de Baseline)"
scope: "Cláusulas 4-10 da ISO/IEC 27001:2022 + Controles Selecionados do Anexo A"
owner: Gestor SGSI
approved_by: "CEO (Ata 001)"
approval_date: "2026-06-08"
next_review: "2026-09-30"
related_documents:
  - SGSI-AUDIT-001   # Programa de Auditoria Interna
  - SGSI-NCR-001     # Registro de Não-Conformidades
  - SGSI-CAR-001     # Registro de Ações Corretivas
  - TEMPLATE-AUDIT-002  # Template do Relatório de Auditoria
iso_clause: "9.2"
---

# Relatório de Auditoria Interna — IA-001

## Resumo Executivo

- **Identificador da Auditoria**: IA-001
- **Data da Auditoria**: 02 de junho de 2026
- **Auditor**: Ricardo Esper — Gestor SGSI
- **Escopo**: Cláusulas 4 a 10 da ISO/IEC 27001:2022 e controles selecionados do Anexo A, conforme Declaração de Aplicabilidade (SoA — SGSI-SOA-001)
- **Avaliação Geral**: 🟡 **Necessita Melhorias** (*Needs Improvement*)

> **Nota sobre Independência do Auditor (Cláusula 9.2.2):**
> Esta auditoria inicial (IA-001) foi conduzida pelo Gestor SGSI na qualidade de auditoria de baseline para estabelecer a linha de partida do SGSI antes da certificação. O Gestor SGSI reconhece que esta prática **não atende plenamente** ao requisito de independência da Cláusula 9.2.2, que determina que auditores não devem auditar seu próprio trabalho. Auditorias subsequentes (IA-002 a IA-004) utilizarão auditor independente externo ou consultor da Bekaa Trusted Advisors, conforme previsto no Programa de Auditoria Interna (SGSI-AUDIT-001, Seção 8). Esta NC está registrada como NC-MAJOR-01.

### Resumo dos Achados

| Classificação | Quantidade |
|---|---|
| **Não-Conformidades Maiores (Major NC)** | 5 |
| **Não-Conformidades Menores (Minor NC)** | 5 |
| **Observações / Oportunidades de Melhoria (OBS)** | 5 |
| **Pontos Fortes / Destaques Positivos** | 7 |

### Conclusão Resumida

O SGSI da TWYN possui uma **base documental sólida e abrangente** (aproximadamente 200 KB de documentação estruturada), com políticas, procedimentos operacionais e registros de riscos bem elaborados. A Ata de Reunião recém aprovada resolveu pendências críticas documentais. Contudo, ainda restam não-conformidades técnicas na infraestrutura AWS (bloqueadores do AWS Foundational Technical Review), e necessidade de evidências operacionais de implementação efetiva dos controles. A organização deve priorizar o fechamento das 5 NCs maiores restantes antes de agendar a auditoria de Stage 1 com o organismo certificador.

---

## 1. Objetivos da Auditoria

Esta auditoria interna foi conduzida com os seguintes objetivos:

1. **Verificar conformidade** com os requisitos da norma ISO/IEC 27001:2022 (Cláusulas 4 a 10) aplicáveis ao escopo do SGSI da TWYN;
2. **Avaliar a eficácia** dos controles de segurança da informação implementados, conforme definidos na Declaração de Aplicabilidade (SoA — SGSI-SOA-001);
3. **Identificar lacunas e não-conformidades** que possam comprometer a integridade, confidencialidade e disponibilidade das informações processadas pela plataforma Face ID da TWYN;
4. **Avaliar o alinhamento** entre a documentação do SGSI e as práticas operacionais reais da organização;
5. **Estabelecer uma linha de base** (baseline) para medição de melhoria contínua e preparação para a auditoria de certificação (Stage 1 e Stage 2);
6. **Atender ao requisito** da Cláusula 9.2 da ISO 27001:2022, que exige a condução de auditorias internas em intervalos planejados.

---

## 2. Escopo da Auditoria

### 2.1 Processos Auditados

| Área | Cláusula / Controle | Documentos Avaliados |
|---|---|---|
| Contexto e Escopo do SGSI | Cláusula 4 | SGSI-SCOPE-001 |
| Liderança e Comprometimento | Cláusula 5 | SGSI-POLICY-001 (implícito), SGSI-RACI-001 |
| Planejamento — Gestão de Riscos | Cláusula 6 | SGSI-RISK-001, SGSI-RISK-002, SGSI-RTP-001, SGSI-OBJ-001 |
| Suporte — Competências e Conscientização | Cláusula 7 | SGSI-COMP-001, SGSI-TRAIN-001 |
| Operação — Processos Operacionais | Cláusula 8 | SOPs 001 a 005, Políticas 002 a 007 |
| Avaliação de Desempenho | Cláusula 9 | SGSI-AUDIT-001, SGSI-MREVIEW-001 |
| Melhoria | Cláusula 10 | SGSI-NCR-001, SGSI-CAR-001 |
| Controles Tecnológicos (Anexo A) | A.5, A.6, A.7, A.8 | SoA, Políticas, SOPs |

### 2.2 Localidades

| Localidade | Descrição |
|---|---|
| **AWS us-east-1** | Região primária da infraestrutura (conta 992382542028) |
| **GitHub** | Organização TWYN — repositórios de código e IaC |
| **Ambientes Remotos** | 100% dos colaboradores em regime remoto |

### 2.3 Período Coberto

- **Período da documentação avaliada**: maio a junho de 2026 (desde o início do projeto SGSI)
- **Data da auditoria**: 02 de junho de 2026

### 2.4 Exclusões

Conforme documentado na Cláusula 4 (SGSI-SCOPE-001):
- Instalações físicas (escritório) — empresa 100% remota
- Laptops e dispositivos dos colaboradores (fora do escopo, embora requisitos mínimos sejam definidos no SOP-003)
- Operações administrativas, financeiras e de RH

---

## 3. Metodologia de Auditoria

### 3.1 Abordagem

A auditoria foi conduzida utilizando uma abordagem baseada em:

1. **Revisão documental**: Análise de todos os documentos mandatórios, políticas, procedimentos operacionais, registros de evidências e templates do SGSI;
2. **Verificação técnica**: Avaliação das configurações de segurança na infraestrutura AWS com base nos achados documentados nos registros de risco e ações corretivas;
3. **Análise de lacunas**: Comparação entre os requisitos da ISO/IEC 27001:2022 e o estado atual de implementação do SGSI;
4. **Referência cruzada**: Validação da consistência entre documentos (por exemplo, entre o Registro de Riscos e a Declaração de Aplicabilidade).

### 3.2 Critérios de Auditoria

- ISO/IEC 27001:2022 — Cláusulas 4 a 10
- ISO/IEC 27001:2022 — Anexo A (93 controles, conforme SoA)
- Políticas e procedimentos internos do SGSI da TWYN
- Requisitos da LGPD (Lei 13.709/2018) aplicáveis ao tratamento de dados biométricos
- AWS Well-Architected Framework — Pilar de Segurança
- CIS AWS Foundations Benchmark v3.0

### 3.3 Amostragem

| Item | Amostra |
|---|---|
| Documentos mandatórios | 100% (todos os documentos existentes) |
| Políticas | 100% (6 políticas avaliadas) |
| SOPs | 100% (5 procedimentos avaliados) |
| Registros de evidência | 100% (todos os registros existentes) |
| Controles do Anexo A | Baseado na SoA — controles aplicáveis |

### 3.4 Ferramentas e Referências Utilizadas

- Checklist de auditoria interna (SGSI-AUDIT-CHECKLIST)
- Template de relatório de auditoria (TEMPLATE-AUDIT-002)
- Documentação AWS (IAM, CloudTrail, Config, GuardDuty)
- CIS AWS Foundations Benchmark v3.0

---

## 4. Achados da Auditoria

### 4.1 Não-Conformidades Maiores (Major NC)

---



---

#### NC-MAJOR-03: Chave de Acesso IAM Não Rotacionada > 90 Dias (tmpsaasboost)

- **Cláusula**: Anexo A — A.5.17 (Informações de autenticação), A.5.18 (Direitos de acesso)
- **Descrição**: O usuário IAM `tmpsaasboost` na conta AWS (992382542028) possui chave de acesso ativa não rotacionada há mais de 90 dias, sem proprietário identificado e sem uso legítimo confirmado. Esta é uma "credencial órfã" que representa um vetor de ataque persistente de alto risco. Este achado é classificado como **bloqueador do AWS Foundational Technical Review (FTR)** e viola a política de rotação de chaves de 90 dias definida no SOP-004 (SGSI-SOP-004, Seção 6.2) e o CIS AWS Foundations Benchmark (Controle 1.4).
- **Evidência**: Documentado no Registro de Riscos (SGSI-RISK-002) como RISK-006 (Classificação: HIGH, Score: 9), no Registro de Ações Corretivas (SGSI-CAR-001) como CAR-002, e no SOP-004 Seção 12.1 que reconhece explicitamente esta não-conformidade.
- **Impacto**: Uma credencial órfã com permissões indefinidas pode ser explorada para acesso não autorizado à infraestrutura AWS. Como os dados biométricos da Face ID Platform são classificados como RESTRICTED e protegidos pela LGPD (Art. 11), o comprometimento desta chave pode resultar em violação de dados pessoais sensíveis, com obrigação de notificação à ANPD em 72 horas e possíveis penalidades de até 2% do faturamento.
- **Causa Raiz**: A conta `tmpsaasboost` é um resquício de um proof-of-concept anterior (AWS SaaS Boost) que não foi devidamente descomissionada após o fim do projeto. Falta de processo formal de de-provisioning e ausência de revisão periódica de acessos (recertificação IAM).
- **Ação Corretiva Requerida**: (1) Desativar imediatamente todas as chaves de acesso do usuário `tmpsaasboost`; (2) Monitorar por 14 dias para confirmar ausência de impacto; (3) Remover o usuário IAM completamente (incluindo policies, grupos, MFA); (4) Documentar a remediação no CAR-002; (5) Implementar o processo trimestral de recertificação IAM conforme SOP-005.
- **Prazo**: 08 de junho de 2026 (P0 — FTR BLOCKER)
- **Responsável**: DevOps Lead

---

#### NC-MAJOR-04: AWS Config e GuardDuty Não Habilitados

- **Cláusula**: Anexo A — A.8.16 (Monitoramento de atividades), A.5.7 (Inteligência de ameaças)
- **Descrição**: Os serviços AWS Config e Amazon GuardDuty não estão habilitados na conta AWS da TWYN (992382542028, região us-east-1). O AWS Config é necessário para monitoramento contínuo de conformidade de configurações, e o GuardDuty é essencial para detecção de ameaças em tempo real. Ambos são exigidos pelo CIS AWS Foundations Benchmark e são bloqueadores do AWS FTR.
- **Evidência**: Documentado no Registro de Riscos como RISK-011 (sem monitoramento de conformidade, Score: 6) e RISK-016 (falta de logging centralizado, Score: 6). Registrado no Registro de Ações Corretivas como CAR-003 (Status: OPEN, Prioridade: HIGH). O Status Report de 08/06/2026 confirma esta lacuna como Blocker #4.
- **Impacto**: Sem AWS Config, não há monitoramento automatizado de desvios de configuração de segurança (por exemplo, abertura de Security Groups para 0.0.0.0/0, desativação de criptografia em buckets S3). Sem GuardDuty, a TWYN não possui capacidade de detecção de atividades maliciosas como mineração de criptomoedas, exfiltração de credenciais, ou acesso anômalo de regiões não autorizadas. Isto viola diretamente os controles A.8.16 (Monitoramento de atividades) e A.5.7 (Inteligência de ameaças).
- **Causa Raiz**: Serviços não foram habilitados durante a configuração inicial da infraestrutura AWS. Falta de um baseline de segurança obrigatório para a conta.
- **Ação Corretiva Requerida**: (1) Habilitar AWS Config em todas as regiões suportadas com regras do CIS AWS Foundations Benchmark; (2) Habilitar Amazon GuardDuty com detecção de ameaças para EC2, S3, EKS e IAM; (3) Configurar alertas via SNS para findings de severidade HIGH e CRITICAL; (4) Implementar Conformance Pack do CIS para verificação automatizada; (5) Documentar a implementação e gerar primeiro relatório de conformidade.
- **Prazo**: 15 de junho de 2026 (CAR-003)
- **Responsável**: DevOps Lead

---

#### NC-MAJOR-05: Teste de Restauração de Backups Nunca Realizado

- **Cláusula**: Anexo A — A.8.13 (Backup de informações), A.5.30 (Prontidão de TIC para continuidade de negócios)
- **Descrição**: A Política de Backup e Recuperação (SGSI-POLICY-005, Seção 6.4) e o Plano de Continuidade de Negócios (SGSI-POLICY-006, Seção 7) definem que testes de restauração devem ser realizados trimestralmente. No entanto, não há evidência de que **qualquer** teste de restauração de backup tenha sido conduzido desde a criação da infraestrutura. O RTO (Recovery Time Objective) de 4 horas e o RPO (Recovery Point Objective) de 1 hora definidos na política nunca foram validados.
- **Evidência**: Documentado no Registro de Riscos como RISK-005 (Score: 9 — HIGH). Registrado no Registro de Ações Corretivas como CAR-004 (Status: OPEN, Prioridade: MEDIUM). A Política de Backup (SGSI-POLICY-005, Seção 6.4) define testes trimestrais, mas a tabela de resultados de testes está vazia. O BCP (SGSI-POLICY-006, Seção 7.2.5) reconhece que "nenhum DR drill foi conduzido até o momento".
- **Impacto**: Sem validação dos procedimentos de restauração, a TWYN não pode garantir a recuperação dos dados biométricos, configurações de aplicação ou Terraform state em caso de desastre. Se uma perda de dados ocorrer, o RTO/RPO pode ser significativamente maior do que o previsto, causando indisponibilidade prolongada do serviço Face ID e potencial perda permanente de dados sensíveis.
- **Causa Raiz**: Falta de agendamento formal de testes de DR. O DevOps Lead é o único responsável pela infraestrutura (SPOF — RISK-015), limitando a capacidade de conduzir testes sem impactar operações.
- **Ação Corretiva Requerida**: (1) Agendar e executar o primeiro teste de restauração completo (DR drill) cobrindo: RDS snapshot restore, S3 versioned object recovery, Terraform state restore, EKS cluster rebuild; (2) Documentar os resultados, incluindo tempo real de restauração versus RTO/RPO planejados; (3) Identificar e corrigir quaisquer falhas no processo de restauração; (4) Estabelecer calendário trimestral de testes futuros conforme a política.
- **Prazo**: 22 de junho de 2026 (CAR-004)
- **Responsável**: DevOps Lead + Gestor SGSI

---

#### NC-MAJOR-06: Designação Formal do DPO / Encarregado de Dados Incompleta

- **Cláusula**: Cláusula 5.3 — Papéis, responsabilidades e autoridades organizacionais; LGPD Art. 41
- **Descrição**: A TWYN processa dados biométricos classificados como dados pessoais sensíveis pela LGPD (Art. 11), o que torna a designação de um Encarregado de Dados (DPO) obrigatória conforme Art. 41 da LGPD. A matriz RACI (SGSI-RACI-001) define o papel de "DPO/Encarregado de Dados" com responsabilidade Accountable pelo titular Ricardo Esper, porém este acumula simultaneamente os papéis de Gestor SGSI, DevOps Lead e DPO, sem designação formal publicada ou comunicação à ANPD. O Registro de Competências (SGSI-COMP-001) indica que a certificação DPO (EXIN Privacy & Data Protection ou equivalente) ainda está pendente, com treinamento planejado apenas para Q2 2026.
- **Impacto**: A ausência de designação formal do DPO com comunicação à ANPD e disponibilização do canal de atendimento aos titulares de dados configura não-conformidade com a LGPD. Em uma auditoria de certificação ISO 27001, o auditor verificará o alinhamento com requisitos legais e regulatórios aplicáveis (Cláusula 4.2 — Partes Interessadas). A acumulação de papéis conflitantes (DPO auditando seu próprio trabalho) também configura risco de independência.
- **Causa Raiz**: Equipe enxuta (~10 pessoas) com restrição de orçamento para contratação de DPO dedicado. Acumulação de papéis por necessidade operacional.
- **Ação Corretiva Requerida**: (1) Emitir designação formal do DPO por ato do CEO, publicando o nome e canais de contato; (2) Comunicar a designação à ANPD; (3) Concluir a certificação DPO (EXIN Privacy ou equivalente) no prazo previsto; (4) Avaliar a contratação de DPO dedicado ou terceirizado no médio prazo para mitigar conflito de papéis.
- **Prazo**: 30 de junho de 2026
- **Responsável**: CEO + Gestor SGSI

---

#### NC-MAJOR-07: Independência da Auditoria Interna Não Atendida

- **Cláusula**: 9.2.2 — Auditoria Interna
- **Descrição**: Esta auditoria (IA-001) foi conduzida pelo Gestor SGSI (Ricardo Esper), que é também o autor principal da maioria dos documentos do SGSI, responsável pela implementação dos controles e titular do papel de DevOps Lead. A Cláusula 9.2.2 exige que os auditores sejam selecionados de modo a "assegurar a objetividade e a imparcialidade do processo de auditoria" e que os auditores "não devem auditar seu próprio trabalho".
- **Evidência**: O Programa de Auditoria Interna (SGSI-AUDIT-001, Seção 8) reconhece explicitamente a necessidade de independência e recomenda a contratação de auditor externo independente. No entanto, a presente auditoria IA-001 foi conduzida pelo próprio Gestor SGSI.
- **Impacto**: A falta de independência do auditor pode comprometer a objetividade dos achados e é um item que o organismo certificador verificará durante o Stage 1. Se não for corrigida, esta não-conformidade será identificada novamente pelo auditor externo.
- **Causa Raiz**: Esta é uma auditoria de baseline conduzida antes da contratação de um auditor externo independente. A equipe enxuta da TWYN não possui outro colaborador qualificado para conduzir a auditoria.
- **Ação Corretiva Requerida**: (1) Contratar auditor externo independente ou utilizar consultor da Bekaa Trusted Advisors para as auditorias IA-002 a IA-004; (2) Documentar a justificativa para a exceção na IA-001 como auditoria de baseline, com compromisso de que auditorias subsequentes utilizarão auditor independente; (3) Incluir o requisito de independência do auditor como critério obrigatório no Programa de Auditoria.
- **Prazo**: Antes das auditorias IA-002 a IA-004 (julho/agosto de 2026)
- **Responsável**: Gestor SGSI

---

### 4.2 Não-Conformidades Menores (Minor NC)

---

#### NC-MINOR-01: Programa de Treinamento e Conscientização Não Iniciado

- **Cláusula**: 7.2 — Competência; 7.3 — Conscientização; Anexo A — A.6.3
- **Descrição**: O Programa de Treinamento em Segurança (SGSI-TRAIN-001) está abrangente e bem estruturado, com 15 módulos em 4 tracks, porém permanece com status "Draft" e kick-off planejado apenas para 03/06/2026. Nenhum módulo foi ministrado e nenhum registro de conclusão de treinamento existe. O Registro de Competências (SGSI-COMP-001) mostra que 100% dos treinamentos obrigatórios estão com status "Não Iniciado" ou "Planejado".
- **Evidência**: SGSI-TRAIN-001 (status: Approved, approved_by: CEO — Pendente). SGSI-COMP-001 mostra "Training Status: Planned" para todos os colaboradores. Nenhuma evidência de quiz completado, certificado emitido ou phishing simulation conduzida.
- **Impacto**: A falta de treinamento em segurança aumenta o risco de incidentes causados por erro humano (RISK-002: Insider Threat, RISK-014: Phishing). O auditor externo solicitará evidências de treinamento durante o Stage 2.
- **Ação Corretiva Requerida**: (1) Obter aprovação formal do CEO para o programa de treinamento; (2) Iniciar o Track 1 (Universal) imediatamente com todos os colaboradores; (3) Registrar evidências de conclusão (certificados, resultados de quiz) no SGSI-COMP-001.
- **Prazo**: 30 de junho de 2026
- **Responsável**: Gestor SGSI

---

#### NC-MINOR-02: Registro de Não-Conformidades com Campos Placeholder

- **Cláusula**: 10.1 — Não-conformidade e ação corretiva; 7.5.3 — Controle de informação documentada
- **Descrição**: O Registro de Não-Conformidades (SGSI-NCR-001) contém registros com campos incompletos. Especificamente, alguns campos de "Verification Status" e "Verified By" estão vazios, e as datas de verificação estão pendentes para todas as NCRs abertas.
- **Evidência**: SGSI-NCR-001 — NCR-001 a NCR-004 com campos de verificação incompletos. A coluna "Evidence" contém referências a documentos futuros que ainda não existem.
- **Impacto**: Registros incompletos dificultam o acompanhamento da eficácia das ações corretivas e podem ser questionados pelo auditor externo quanto à adequação do processo de melhoria contínua.
- **Ação Corretiva Requerida**: (1) Preencher todos os campos obrigatórios do NCR Register; (2) Vincular cada NCR às evidências correspondentes; (3) Atualizar o status à medida que as ações corretivas forem implementadas.
- **Prazo**: Contínuo — atualização a cada ciclo de revisão
- **Responsável**: Gestor SGSI

---

#### NC-MINOR-03: Plano de Continuidade de Negócios sem Teste de Tabletop Exercise

- **Cláusula**: Anexo A — A.5.30 (Prontidão de TIC para continuidade de negócios)
- **Descrição**: O Plano de Continuidade de Negócios (SGSI-POLICY-006) é detalhado e abrangente, com cenários bem definidos, comunicação de crise e equipe de resposta. Contudo, nenhuma simulação (tabletop exercise) ou teste de ativação do plano foi conduzido. A Seção 7.2.5 do BCP reconhece explicitamente: "Nenhum DR drill foi conduzido até o momento".
- **Evidência**: SGSI-POLICY-006, Seção 7.2.5 e Seção 9. Nenhum registro de simulação encontrado nos arquivos de evidências.
- **Impacto**: Sem testes, a eficácia do BCP é teórica. Em caso de incidente real, a equipe pode não saber como executar os procedimentos documentados, resultando em tempo de resposta excessivo.
- **Ação Corretiva Requerida**: (1) Agendar e conduzir a primeira tabletop exercise com cenário de ransomware ou falha de região AWS; (2) Documentar os resultados e lições aprendidas; (3) Atualizar o BCP com base nas conclusões do exercício.
- **Prazo**: 31 de julho de 2026
- **Responsável**: DevOps Lead + Gestor SGSI

---

#### NC-MINOR-04: Classificação e Inventário de Ativos Sensíveis Incompleto para Código-Fonte

- **Cláusula**: Anexo A — A.5.9 (Inventário de informações e outros ativos associados), A.5.12 (Classificação de informações)
- **Descrição**: O Inventário de Ativos (SGSI-ASSETS-001) é abrangente para infraestrutura AWS e dados, mas a classificação de segurança de alguns repositórios de código-fonte no GitHub não está consistentemente documentada. A Política de Gestão de Ativos (SGSI-POLICY-004) define níveis de classificação (PUBLIC, INTERNAL, CONFIDENTIAL, RESTRICTED), porém os metadados YAML de alguns documentos não incluem o campo `classification`.
- **Evidência**: SGSI-ASSETS-001 lista repositórios GitHub como ativos, mas nem todos possuem classificação de segurança explícita. Alguns documentos do SGSI possuem `classification: INTERNAL` ou `CONFIDENTIAL`, mas outros não possuem o campo.
- **Impacto**: Sem classificação consistente, não é possível aplicar controles proporcionais ao nível de sensibilidade dos ativos, conforme exigido pelo controle A.5.12.
- **Ação Corretiva Requerida**: (1) Revisar o inventário de ativos e completar a classificação de todos os repositórios; (2) Padronizar o campo `classification` em todos os documentos do SGSI; (3) Aplicar controles de acesso proporcionais à classificação.
- **Prazo**: 30 de junho de 2026
- **Responsável**: Gestor SGSI

---

#### NC-MINOR-05: Política de Uso Aceitável (AUP) sem Evidência de Aceite pelos Colaboradores

- **Cláusula**: Anexo A — A.5.10 (Uso aceitável de informações e outros ativos associados)
- **Descrição**: A Política de Uso Aceitável (SGSI-POLICY-007 — AUP) está completa e bem estruturada, com definições claras de responsabilidades, práticas proibidas e consequências. No entanto, não há evidência de que os colaboradores tenham lido e aceito formalmente esta política. A AUP prevê um "Termo de Ciência e Aceite" (Seção 11), mas nenhum termo assinado foi encontrado nos registros de evidências.
- **Evidência**: SGSI-POLICY-007, Seção 11 — template do Termo de Aceite presente, mas sem assinaturas. SGSI-COMP-001 não registra aceite da AUP como item de competência verificado.
- **Impacto**: Sem aceite formal, a TWYN não pode demonstrar que os colaboradores estão cientes de suas responsabilidades de segurança, fragilizando a aplicação de medidas disciplinares em caso de violação.
- **Ação Corretiva Requerida**: (1) Distribuir a AUP a todos os colaboradores; (2) Coletar assinaturas (digitais ou físicas) do Termo de Aceite; (3) Registrar o aceite no SGSI-COMP-001.
- **Prazo**: 30 de junho de 2026
- **Responsável**: Gestor SGSI

---

### 4.3 Não-Conformidades Fechadas/Resolvidas

---

#### [RESOLVIDO] NC-MAJOR-01: Ausência de Análise Crítica pela Direção (Management Review)
- **Status**: CLOSED
- **Ação Executada**: A primeira ata formal já foi consolidada e aprovada pelo CEO (Ata 001).
- **Evidência**: Confirmação executiva.

---

#### [RESOLVIDO] NC-MAJOR-02: Documentos Mandatórios sem Aprovação Formal da Alta Direção
- **Status**: CLOSED
- **Ação Executada**: A aprovação foi outorgada a todos os documentos (Ata 001).
- **Evidência**: Confirmação executiva.

---

### 4.4 Observações e Oportunidades de Melhoria (OBS)

---

#### OBS-01: Single Point of Failure (SPOF) no Papel de DevOps Lead

- **Descrição**: O DevOps Lead (Ricardo Esper) acumula simultaneamente os papéis de Gestor SGSI, DPO, DevOps Lead e único administrador da infraestrutura AWS. Este cenário configura um Single Point of Failure (SPOF) significativo, documentado no Registro de Riscos como RISK-015 (Score: 12 — CRITICAL).
- **Recomendação**: O tamanho atual da equipe (10 pessoas) inviabiliza a segregação plena exigida pelo controle A.5.3. Recomenda-se a mitigação via controles compensatórios: rastreabilidade absoluta (CloudTrail/logs imutáveis) e obrigatoriedade de aprovação por terceiros nas requisições de mudança (Pull Requests). O risco foi aceito pela diretoria nestas condições.

---

#### OBS-02: Indicadores de Desempenho de Segurança (KPIs) Parcialmente Definidos

- **Descrição**: Os objetivos de segurança da informação (SGSI-OBJ-001) definem KPIs mensuráveis (por exemplo, "100% rotação de chaves ≤90 dias", "Zero incidentes críticos de dados", "<5% click rate em phishing simulations"). No entanto, os valores de baseline ainda não foram coletados e as medições reais ainda não iniciaram, impossibilitando a avaliação de tendências.
- **Recomendação**: (1) Coletar valores de baseline para todos os KPIs no próximo ciclo trimestral; (2) Estabelecer dashboard de monitoramento contínuo; (3) Incluir relatório de KPIs como input obrigatório da Management Review.

---

#### OBS-03: Automação de Controles de Segurança AWS via Infrastructure-as-Code

- **Descrição**: A TWYN utiliza Terraform como ferramenta de Infrastructure-as-Code (IaC), o que é uma excelente prática. No entanto, nem todos os controles de segurança obrigatórios estão definidos em código (por exemplo, habilitação do AWS Config, configuração do GuardDuty, regras de CloudWatch Alarms para eventos do CIS Benchmark). A implementação manual destes controles aumenta o risco de drift de configuração.
- **Recomendação**: (1) Codificar 100% dos controles de segurança obrigatórios em módulos Terraform reutilizáveis; (2) Implementar pipeline de CI/CD com validação de segurança automatizada (tfsec, checkov); (3) Utilizar AWS Config Rules como guardrails permanentes.

---

#### OBS-04: Política de Resposta a Incidentes sem Playbooks Específicos para Dados Biométricos

- **Descrição**: A Política de Resposta a Incidentes (SGSI-POLICY-003) é completa e segue o ciclo NIST (Preparação → Detecção → Contenção → Erradicação → Recuperação → Lições Aprendidas). No entanto, não inclui um playbook específico para o cenário de violação de dados biométricos, que é o ativo mais sensível da TWYN e tem obrigações específicas de notificação sob a LGPD (Art. 48 — comunicação à ANPD e aos titulares em prazo razoável).
- **Recomendação**: (1) Desenvolver playbook específico para violação de dados biométricos com: identificação e isolamento do sistema afetado, avaliação da natureza e volume de dados comprometidos, notificação à ANPD dentro de 72 horas, notificação aos titulares afetados, preservação de evidências forenses; (2) Conduzir tabletop exercise baseada neste cenário.

---

#### OBS-05: Estrutura de Pastas de Evidências Necessita Organização para Auditorias Futuras

- **Descrição**: Os registros de evidências (competência, NCRs, CARs, auditorias) estão organizados em `docs/05-evidence/`, porém a estrutura prevista no Programa de Auditoria (SGSI-AUDIT-001, Seção 9) — `docs/05-evidence/internal-audits/2026/` — ainda não existe como diretório dedicado. Para auditorias futuras, será necessário manter evidências organizadas por ciclo trimestral (por exemplo, `Q1-2026/`, `Q2-2026/`).
- **Recomendação**: (1) Criar a estrutura de diretórios conforme previsto no programa de auditoria; (2) Estabelecer nomenclatura padronizada para arquivos de evidência; (3) Manter índice de evidências para facilitar a localização durante auditorias externas.

---

## 5. Pontos Fortes Identificados

A auditoria identificou os seguintes **destaques positivos** que demonstram maturidade e comprometimento da TWYN com a segurança da informação:

---

### FORÇA-01: Documentação do SGSI Abrangente e Bem Estruturada

A base documental do SGSI é excepcional para uma organização do porte da TWYN (~10 colaboradores). Aproximadamente 200+ KB de documentação técnica de alta qualidade foram produzidos, incluindo:
- 6 políticas detalhadas (Controle de Acesso, Resposta a Incidentes, Gestão de Ativos, Backup e Recuperação, Continuidade de Negócios, Uso Aceitável)
- 5 SOPs operacionais com comandos técnicos executáveis (Onboarding/Offboarding, Change Management, Trabalho Remoto, Gestão de Segredos, Recertificação IAM)
- Registro de Riscos com 18 riscos identificados e classificados com metodologia Likelihood × Impact
- Declaração de Aplicabilidade (SoA) cobrindo todos os 93 controles do Anexo A
- Glossário ISO 27001 com 100+ termos

A documentação segue formato consistente (Markdown com frontmatter YAML), facilitando controle de versão, revisão e manutenção.

---

### FORÇA-02: Gestão de Riscos Robusta e Contextualizada

O processo de gestão de riscos demonstra maturidade significativa:
- **18 riscos** identificados com análise realista e específica para o contexto da TWYN (não genérica)
- **Classificação por criticidade**: 3 CRITICAL, 6 HIGH, 6 MEDIUM, 3 LOW
- **Plano de Tratamento de Riscos (RTP)** com ações concretas, responsáveis e prazos definidos
- **SoA** com justificativa de aplicabilidade/exclusão para cada um dos 93 controles do Anexo A
- Os riscos refletem ameaças reais do ambiente operacional (AWS, dados biométricos, LGPD)

---

### FORÇA-03: SOPs Técnicos com Profundidade e Operacionalidade Exemplares

Os 5 SOPs (Procedimentos Operacionais Padrão) são notáveis por sua profundidade técnica:
- **SOP-001** (Onboarding/Offboarding): Processo de provisionamento e desprovisionamento com SLA de 4 horas, comandos AWS CLI completos, checklists detalhados
- **SOP-004** (Gestão de Segredos): Procedimento de rotação de chaves IAM em 90 dias, rotação de KMS CMK, renovação de certificados TLS, com comandos técnicos passo-a-passo e procedimento de emergência para credenciais comprometidas
- **SOP-005** (Recertificação IAM): Processo trimestral de recertificação cobrindo AWS, GitHub e Kubernetes, com KPIs mensuráveis e templates de relatório

Esta profundidade técnica facilita a execução consistente dos processos, mesmo por colaboradores diferentes.

---

### FORÇA-04: Matriz RACI Detalhada e Alinhada com a ISO 27001

A matriz RACI (SGSI-RACI-001) é excepcionalmente detalhada, cobrindo:
- Todas as 10 cláusulas mandatórias da ISO 27001:2022
- Papéis claramente definidos (CEO, Gestor SGSI, DevOps Lead, Developers, DPO)
- Atribuição de Responsável (R), Aprovador (A), Consultado (C) e Informado (I) para cada processo
- Integração com requisitos LGPD para o papel de DPO

---

### FORÇA-05: Reconhecimento Proativo de Lacunas e Auto-Correção

A TWYN demonstra maturidade ao reconhecer proativamente suas lacunas:
- O Status Report de 08/06/2026 identifica honestamente 5 problemas críticos (repositório na conta errada, issues não criados, documentos incompletos, README vazio, sem GitHub Projects)
- Os SOPs incluem seções explícitas reconhecendo não-conformidades conhecidas (por exemplo, SOP-004 Seção 12.1 sobre a conta `tmpsaasboost`)
- O Registro de Ações Corretivas (CAR-001 a CAR-004) documenta proativamente as ações necessárias antes mesmo desta auditoria
- Esta transparência é um indicador positivo de cultura de melhoria contínua (Cláusula 10)

---

### FORÇA-06: Alinhamento com LGPD para Dados Biométricos

A documentação demonstra preocupação consistente com a proteção de dados biométricos conforme a LGPD:
- O escopo do SGSI (Cláusula 4) reconhece dados biométricos como "ativos de informação de maior criticidade"
- O SOP-003 (Trabalho Remoto) define regras específicas e restritivas para dados biométricos (proibição de armazenamento local, proibição de captura de tela, processamento exclusivo em ambientes AWS)
- O SOP-004 (Gestão de Segredos) classifica a CMK de criptografia biométrica como "CRITICIDADE MÁXIMA"
- A Política de Controle de Acesso define acesso baseado em "need-to-know" com restrições adicionais para dados RESTRICTED

---

### FORÇA-07: Uso de GitHub e Infrastructure-as-Code (IaC) para Governança

A utilização de GitHub como repositório do SGSI e Terraform como ferramenta de IaC proporciona:
- **Controle de versão** de toda a documentação (histórico de alterações rastreável)
- **Revisão por pares** via Pull Requests (change management integrado ao fluxo de desenvolvimento)
- **Automação** de deployments via GitHub Actions com OIDC Federation (eliminando chaves de longa duração)
- **Rastreabilidade** de mudanças na infraestrutura via Terraform plan/apply
- Estas práticas estão alinhadas com os controles A.8.25 (Ciclo de vida de desenvolvimento seguro) e A.8.32 (Gestão de mudanças)

---

## 6. Recomendações Priorizadas

### 6.1 Curto Prazo (0-30 dias) — Ações Críticas para Certificação

| # | Ação | Referência | Responsável | Prazo |
|---|---|---|---|---|
| 1 | Obter aprovação formal (assinatura do CEO) na Política de Segurança da Informação e nos objetivos de segurança | NC-MAJOR-02 | CEO | 10/06/2026 |
| 2 | Desativar e remover credenciais da conta IAM `tmpsaasboost` | NC-MAJOR-03, CAR-002 | DevOps Lead | 08/06/2026 |
| 3 | Habilitar AWS Config e GuardDuty com regras CIS | NC-MAJOR-04, CAR-003 | DevOps Lead | 15/06/2026 |
| 4 | Aprovar formalmente todos os documentos do SGSI (atualizar status de Draft para Approved) | NC-MAJOR-02 | Gestor SGSI + CEO | 15/06/2026 |
| 5 | Agendar e conduzir a primeira Management Review | NC-MAJOR-01 | CEO + Gestor SGSI | 30/06/2026 |
| 6 | Designar formalmente o DPO com comunicação à ANPD | NC-MAJOR-06 | CEO | Concluído |
| 7 | Iniciar Track 1 do programa de treinamento (Universal — todos os colaboradores) | NC-MINOR-01 | Gestor SGSI | 30/06/2026 |
| 8 | Coletar aceite formal da AUP de todos os colaboradores | NC-MINOR-05 | Gestor SGSI | 30/06/2026 |

### 6.2 Médio Prazo (30-90 dias) — Consolidação do SGSI

| # | Ação | Referência | Responsável | Prazo |
|---|---|---|---|---|
| 9 | Conduzir primeiro teste de restauração de backup (DR drill) | NC-MAJOR-05, CAR-004 | DevOps Lead | 22/06/2026 |
| 10 | Contratar auditor externo independente para IA-002 a IA-004 | NC-MAJOR-07 | Gestor SGSI | 15/07/2026 |
| 11 | Conduzir primeira tabletop exercise do BCP | NC-MINOR-03 | Gestor SGSI | 31/07/2026 |
| 12 | Completar classificação de segurança de todos os ativos | NC-MINOR-04 | Gestor SGSI | 30/06/2026 |
| 13 | Completar Track 2 e Track 3 do programa de treinamento | NC-MINOR-01 | Gestor SGSI | 31/08/2026 |
| 14 | Desenvolver playbook de resposta a incidentes para dados biométricos | OBS-04 | Gestor SGSI | 31/07/2026 |
| 15 | Coletar valores de baseline para todos os KPIs de segurança | OBS-02 | Gestor SGSI | 31/07/2026 |

### 6.3 Longo Prazo (90+ dias) — Maturidade e Melhoria Contínua

| # | Ação | Referência | Responsável | Prazo |
|---|---|---|---|---|
| 16 | Formalizar controles compensatórios para A.5.3 (SPOF mitigado via IaC/CloudTrail) | OBS-01 | CEO | Concluído |
| 17 | Codificar 100% dos controles de segurança AWS em Terraform | OBS-03 | DevOps Lead | Q4 2026 |
| 18 | Implementar pentesting anual da plataforma Face ID | SoA — A.8.8 | Gestor SGSI | Q3 2026 |
| 19 | Organizar estrutura de evidências por trimestre | OBS-05 | Gestor SGSI | Contínuo |
| 20 | Estabelecer processo de melhoria contínua com revisões trimestrais | Cláusula 10 | Gestor SGSI | Contínuo |

---

## 7. Conclusão

### 7.1 Avaliação Geral

O SGSI da TWYN encontra-se em um estágio de **implementação intermediária** com uma base documental excepcionalmente forte, mas com lacunas operacionais significativas que impedem a prontidão imediata para a certificação ISO 27001:2022.

**Pontos positivos predominantes:**
- A documentação é abrangente, técnica e específica ao contexto da TWYN
- A gestão de riscos é robusta com 18 riscos realistas e tratamento definido
- Os SOPs são operacionais e executáveis, com comandos técnicos detalhados
- Há consciência proativa das lacunas e cultura emergente de melhoria contínua

**Áreas críticas que requerem atenção imediata:**
- Aprovação formal dos documentos pela Alta Direção (bloqueador absoluto)
- Realização da primeira Management Review
- Remediação de vulnerabilidades técnicas na AWS (tmpsaasboost, Config, GuardDuty)
- Validação de backups e continuidade de negócios
- Designação formal do DPO
- Garantia de independência nas auditorias subsequentes

### 7.2 Prontidão para Certificação

| Critério | Status | Avaliação |
|---|---|---|
| Documentação mandatória | 🟡 | Completa em conteúdo, mas sem aprovação formal |
| Gestão de riscos | ✅ | Robusta e contextualizada |
| Controles do Anexo A | 🟡 | ~70% implementados (31% total + 39% parcial) |
| Evidências operacionais | ❌ | Insuficientes (sem Management Review, sem treinamentos, sem testes de DR) |
| Conformidade técnica AWS | ❌ | 4 CARs críticos em aberto |
| Melhoria contínua | 🟡 | Processo definido, mas sem ciclo completo executado |

### 7.3 Estimativa de Prontidão

Com a implementação das ações corretivas de curto prazo (0-30 dias), a TWYN poderá estar pronta para o **Stage 1** (revisão documental) no final de julho de 2026. O **Stage 2** (auditoria de certificação) poderá ser agendado para agosto/setembro de 2026, condicionado à:
1. Fechamento das 5 NCs maiores restantes
2. Conclusão de pelo menos um ciclo completo de Management Review
3. Evidência de pelo menos um teste de restauração de backup
4. Evidência de treinamento concluído para 100% dos colaboradores
5. Auditorias IA-002 a IA-004 conduzidas por auditor independente

---

## 8. Acompanhamento (Follow-Up)

### 8.1 NCRs Criados

As seguintes não-conformidades devem ser registradas no Registro de Não-Conformidades (SGSI-NCR-001):

| NCR ID | Tipo | Referência | Status |
|---|---|---|---|
| NCR-005 | Major | NC-MAJOR-01 — Management Review | CLOSED |
| NCR-006 | Major | NC-MAJOR-02 — Aprovação de Documentos | CLOSED |
| NCR-007 | Major | NC-MAJOR-03 — tmpsaasboost (referência existente: NCR-002/CAR-002) | OPEN |
| NCR-008 | Major | NC-MAJOR-04 — AWS Config/GuardDuty (referência existente: CAR-003) | OPEN |
| NCR-009 | Major | NC-MAJOR-05 — DR Testing (referência existente: CAR-004) | OPEN |
| NCR-010 | Major | NC-MAJOR-06 — Designação DPO | CLOSED |
| NCR-011 | Major | NC-MAJOR-07 — Independência do Auditor | OPEN |
| NCR-012 | Minor | NC-MINOR-01 — Treinamento | OPEN |
| NCR-013 | Minor | NC-MINOR-02 — Registros NCR | OPEN |
| NCR-014 | Minor | NC-MINOR-03 — BCP Testing | OPEN |
| NCR-015 | Minor | NC-MINOR-04 — Classificação de Ativos | OPEN |
| NCR-016 | Minor | NC-MINOR-05 — Aceite AUP | OPEN |

### 8.2 CARs Associados

| CAR ID | Referência NC | Status | Prioridade |
|---|---|---|---|
| CAR-002 | NC-MAJOR-03 (tmpsaasboost) | OPEN | CRITICAL |
| CAR-003 | NC-MAJOR-04 (AWS Config/GuardDuty) | OPEN | HIGH |
| CAR-004 | NC-MAJOR-05 (DR Testing) | OPEN | MEDIUM |
| CAR-005 (novo) | NC-MAJOR-01 (Management Review) | CLOSED | CRITICAL |
| CAR-006 (novo) | NC-MAJOR-02 (Aprovação de Documentos) | CLOSED | CRITICAL |
| CAR-007 (novo) | NC-MAJOR-06 (Designação DPO) | CLOSED | HIGH |

### 8.3 Próximas Auditorias

| Auditoria | Escopo | Auditor | Data Planejada |
|---|---|---|---|
| **IA-002** | Cláusula 6 (Gestão de Riscos) + Anexo A Tema 5 | Auditor Externo / Bekaa | Julho 2026 |
| **IA-003** | Cláusulas 7-8 (Suporte, Operação) + Anexo A Temas 6, 8 | Auditor Externo / Bekaa | Agosto 2026 |
| **IA-004** | Cláusulas 9-10 (Avaliação, Melhoria) | Auditor Externo / Bekaa | Agosto 2026 |

---

## Apêndices

### Apêndice A: Documentos do SGSI Avaliados

| # | Document ID | Título | Localização | Status |
|---|---|---|---|---|
| 1 | SGSI-SCOPE-001 | Contexto da Organização e Escopo do SGSI | `docs/01-mandatory-clauses/` | Draft |
| 2 | SGSI-OBJ-001 | Objetivos de Segurança da Informação | `docs/01-mandatory-clauses/` | Draft |
| 3 | SGSI-RACI-001 | Matriz RACI | `docs/01-mandatory-clauses/` | Draft |
| 4 | SGSI-POLICY-002 | Política de Controle de Acesso | `docs/02-policies/` | Draft |
| 5 | SGSI-POLICY-003 | Plano de Resposta a Incidentes | `docs/02-policies/` | Draft |
| 6 | SGSI-POLICY-004 | Política de Gestão de Ativos | `docs/02-policies/` | Draft |
| 7 | SGSI-POLICY-005 | Política de Backup e Recuperação | `docs/02-policies/` | Draft |
| 8 | SGSI-POLICY-006 | Plano de Continuidade de Negócios | `docs/02-policies/` | Draft |
| 9 | SGSI-POLICY-007 | Política de Uso Aceitável (AUP) | `docs/02-policies/` | Draft |
| 10 | SGSI-SOP-001 | Onboarding e Offboarding de Colaboradores | `docs/03-procedures/` | Draft |
| 11 | SGSI-SOP-002 | Gestão de Mudanças | `docs/03-procedures/` | Draft |
| 12 | SGSI-SOP-003 | Segurança no Trabalho Remoto | `docs/03-procedures/` | Draft |
| 13 | SGSI-SOP-004 | Gestão de Segredos e Rotação de Chaves | `docs/03-procedures/` | Draft |
| 14 | SGSI-SOP-005 | Recertificação de Identidades e Acessos | `docs/03-procedures/` | Draft |
| 15 | SGSI-RISK-001 | Metodologia de Avaliação de Riscos | `docs/04-risk-management/` | Draft |
| 16 | SGSI-RISK-002 | Registro de Riscos | `docs/04-risk-management/` | Draft |
| 17 | SGSI-RTP-001 | Plano de Tratamento de Riscos | `docs/04-risk-management/` | Draft |
| 18 | SGSI-SOA-001 | Declaração de Aplicabilidade | `docs/04-risk-management/` | Draft |
| 19 | SGSI-COMP-001 | Registros de Competência | `docs/05-evidence/` | Draft |
| 20 | SGSI-CAR-001 | Registro de Ações Corretivas | `docs/05-evidence/` | Draft |
| 21 | SGSI-NCR-001 | Registro de Não-Conformidades | `docs/05-evidence/` | Draft |
| 22 | SGSI-MREVIEW-001 | Template de Management Review | `docs/05-evidence/` | Draft |
| 23 | SGSI-AUDIT-001 | Programa de Auditoria Interna | `docs/05-evidence/` | Draft |
| 24 | SGSI-TRAIN-001 | Programa de Treinamento em Segurança | Raiz | Draft |

### Apêndice B: Mapeamento de Achados por Cláusula ISO 27001:2022

| Cláusula | Achado | Classificação |
|---|---|---|
| 4.1, 4.2, 4.3 | Escopo bem definido, partes interessadas identificadas | ✅ Conforme |
| 5.1 | Sem evidência de comprometimento da liderança (Management Review pendente) | ❌ NC-MAJOR-01 |
| 5.2 | Política sem aprovação formal | ❌ NC-MAJOR-02 |
| 5.3 | Papéis definidos (RACI) e DPO nomeado formalmente | ✅ Conforme |
| 6.1 | Gestão de riscos robusta e contextualizada | ✅ Conforme |
| 6.2 | Objetivos de segurança definidos e mensuráveis | ✅ Conforme |
| 7.1 | Recursos alocados. SPOF inicial (OBS-01) justificado via controles compensatórios e aprovado pela diretoria. | ✅ Conforme |
| 7.2, 7.3 | Treinamento planejado mas não executado | 🟡 NC-MINOR-01 |
| 7.5 | Documentação abrangente, mas sem aprovação formal | ❌ NC-MAJOR-02 |
| 8.1 | Processos operacionais definidos (SOPs) | ✅ Conforme |
| 8.2 | Avaliação de riscos realizada | ✅ Conforme |
| 8.3 | Plano de tratamento de riscos definido | ✅ Conforme |
| 9.1 | KPIs definidos, mas sem medição executada | 🟡 OBS-02 |
| 9.2 | Auditoria realizada, mas sem independência | ❌ NC-MAJOR-07 |
| 9.3 | Management Review não realizada | ❌ NC-MAJOR-01 |
| 10.1, 10.2 | Processo de NCR/CAR definido, registros parcialmente incompletos | 🟡 NC-MINOR-02 |

### Apêndice C: Mapeamento de Achados por Controle do Anexo A

| Controle | Descrição | Achado | Classificação |
|---|---|---|---|
| A.5.7 | Inteligência de ameaças | GuardDuty não habilitado | ❌ NC-MAJOR-04 |
| A.5.9 | Inventário de ativos | Classificação parcialmente incompleta | 🟡 NC-MINOR-04 |
| A.5.10 | Uso aceitável | AUP sem aceite formal | 🟡 NC-MINOR-05 |
| A.5.12 | Classificação de informações | Política definida, aplicação parcial | 🟡 NC-MINOR-04 |
| A.5.15-5.18 | Controle de acesso / Identidades | SOPs excelentes, conta órfã existente | ❌ NC-MAJOR-03 |
| A.5.17 | Informações de autenticação | Chave >90 dias sem rotação | ❌ NC-MAJOR-03 |
| A.5.30 | Prontidão TIC para continuidade | BCP sem teste, DR não validado | ❌ NC-MAJOR-05 / NC-MINOR-03 |
| A.6.3 | Conscientização em segurança | Treinamento não iniciado | 🟡 NC-MINOR-01 |
| A.6.7 | Trabalho remoto | SOP-003 abrangente e detalhado | ✅ Conforme |
| A.8.1 | Dispositivos endpoint | Requisitos definidos no SOP-003 | ✅ Conforme |
| A.8.13 | Backup | Política definida, teste não realizado | ❌ NC-MAJOR-05 |
| A.8.16 | Monitoramento de atividades | AWS Config não habilitado | ❌ NC-MAJOR-04 |
| A.8.24 | Uso de criptografia | KMS CMK configurada, política definida | ✅ Conforme |
| A.8.25 | Ciclo de vida de dev seguro | Controle excluído (N/A) do escopo (foco estrito em Operação SaaS) | ➖ N/A |

---

## Assinaturas

| Campo | Valor |
|---|---|
| **Relatório Preparado Por** | |
| Nome: | Ricardo Esper — Gestor SGSI |
| Data: | 08/06/2026 |
| Assinatura: | _________________________________________ |
| | |
| **Revisado Por (Gestor SGSI)** | |
| Nome: | _________________________________________ |
| Data: | ___/___/______ |
| Assinatura: | _________________________________________ |
| | |
| **Ciência da Auditoria (Auditado)** | |
| Nome: | _________________________________________ |
| Data: | ___/___/______ |
| Assinatura: | _________________________________________ |

---

**Classificação**: CONFIDENTIAL
**Documento**: SGSI-IA-001
**Próxima Revisão**: Após implementação das ações corretivas e antes do Stage 1

*Este documento é propriedade da TWYN e seu conteúdo é classificado como CONFIDENTIAL. A distribuição não autorizada é proibida.*
