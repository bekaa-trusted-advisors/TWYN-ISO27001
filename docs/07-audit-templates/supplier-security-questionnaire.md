---
document_id: SGSI-TMPL-001
title: Supplier Security Questionnaire
version: 1.0
date: 2026-06-02
classification: INTERNAL
owner: Gestor SGSI
annex_a_controls: "A.5.19, A.5.20, A.5.21, A.5.22"
---

# Questionário de Segurança para Fornecedores (Supplier Security Questionnaire)

Este questionário deve ser preenchido por todos os fornecedores críticos, prestadores de serviços em nuvem ou empresas que terão acesso aos sistemas ou dados (especialmente biometria) da TWYN. 
A avaliação das respostas ditará a aprovação do fornecedor ou a necessidade de cláusulas contratuais adicionais de mitigação de riscos.

> **Nota sobre Hyperscalers (ex: AWS, GitHub, Google):** Grandes provedores não respondem questionários manuais. Para estes casos, a TWYN deve consumir suas certificações públicas e relatórios de auditoria (ex: via AWS Artifact para SOC 2 Type II, ISO 27001, etc). O preenchimento manual do questionário é dispensado, e o Gestor SGSI deve preencher apenas a seção "8. Uso Interno TWYN" com base na análise documental das certificações baixadas.

## 1. Informações da Empresa
- **Razão Social do Fornecedor:** 
- **CNPJ / ID Fiscal:** 
- **Nome do Responsável pela Segurança (CISO/DPO):** 
- **E-mail de Contato (Segurança):** 
- **Serviço/Produto fornecido à TWYN:** 

## 2. Certificações e Conformidade
| ID | Pergunta | Sim/Não | Detalhes / Comentários / Evidências |
|----|----------|---------|-------------------------------------|
| 2.1 | A empresa possui certificação ISO 27001 válida? | [ ] | (Se sim, anexar certificado) |
| 2.2 | A empresa possui relatórios SOC 2 Type II recentes? | [ ] | (Se sim, anexar sumário) |
| 2.3 | A empresa está em conformidade com a LGPD e possui DPO nomeado? | [ ] | |

## 3. Gestão de Segurança da Informação
| ID | Pergunta | Sim/Não | Detalhes / Comentários / Evidências |
|----|----------|---------|-------------------------------------|
| 3.1 | Existe uma Política de Segurança da Informação formalmente aprovada? | [ ] | |
| 3.2 | O fornecedor realiza treinamentos periódicos de conscientização em segurança para seus colaboradores? | [ ] | |
| 3.3 | Colaboradores com acesso a sistemas sensíveis passam por verificação de antecedentes (background check)? | [ ] | |

## 4. Controles Técnicos e Controle de Acesso
| ID | Pergunta | Sim/Não | Detalhes / Comentários / Evidências |
|----|----------|---------|-------------------------------------|
| 4.1 | O uso de Autenticação Multifator (MFA) é obrigatório para acessos corporativos e de produção? | [ ] | |
| 4.2 | Existe um processo documentado de Onboarding/Offboarding com revogação imediata de acessos? | [ ] | |
| 4.3 | Dados confidenciais são criptografados em trânsito (TLS 1.2+) e em repouso (AES-256)? | [ ] | |
| 4.4 | O fornecedor executa varreduras de vulnerabilidades e testes de invasão (Pentest) pelo menos anualmente? | [ ] | |

## 5. Resposta a Incidentes e Continuidade
| ID | Pergunta | Sim/Não | Detalhes / Comentários / Evidências |
|----|----------|---------|-------------------------------------|
| 5.1 | Existe um Plano de Resposta a Incidentes estabelecido e testado anualmente? | [ ] | |
| 5.2 | Em caso de incidente de segurança envolvendo dados da TWYN, vocês se comprometem a notificar-nos em até 24 horas? | [ ] | |
| 5.3 | Existe um Plano de Continuidade de Negócios (BCP) e Disaster Recovery (DR) formal? | [ ] | |

## 6. Privacidade e Tratamento de Dados Pessoais
| ID | Pergunta | Sim/Não | Detalhes / Comentários / Evidências |
|----|----------|---------|-------------------------------------|
| 6.1 | O fornecedor compartilha dados da TWYN com subprocessadores adicionais (quarteirização)? | [ ] | (Se sim, listar subprocessadores) |
| 6.2 | Dados serão processados ou armazenados fora do Brasil? | [ ] | (Se sim, especificar jurisdições) |
| 6.3 | O fornecedor possui processo para destruição segura/apagamento de dados ao término do contrato? | [ ] | |

---

## 7. Declaração do Fornecedor
Declaro que as informações prestadas neste questionário são verdadeiras e refletem a postura atual de segurança da informação da empresa.

**Assinatura do Responsável:** ___________________________
**Data:** ____/____/________

---

## 8. Uso Interno TWYN (Avaliação de Risco)
- **Avaliador (Gestor SGSI):** 
- **Data da Avaliação:** 
- **Parecer:** [  ] APROVADO | [  ] APROVADO COM RESSALVAS | [  ] REJEITADO
- **Nível de Risco Atribuído:** [Baixo / Médio / Alto / Crítico]
- **Observações/Cláusulas Adicionais Exigidas:** 
