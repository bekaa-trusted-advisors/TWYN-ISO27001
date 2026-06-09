---
document_id: SGSI-POLICY-011
title: Adendo de Segurança para Fornecedores (Supplier Security Addendum)
version: 1.0
status: Draft
classification: INTERNAL
owner: Gestor SGSI
approved_by: CEO (Pendente)
related_policies:
  - SGSI-POLICY-001 (Política de SI)
  - SGSI-POLICY-002 (Controle de Acesso)
annex_a_controls:
  - A.5.19
  - A.5.21
  - A.5.22
  - A.8.25
---

# Adendo de Segurança para Fornecedores (Supplier Security Addendum)

## 1. Propósito e Escopo

Este Adendo de Segurança define os requisitos obrigatórios de Segurança da Informação e Privacidade de Dados que devem ser cumpridos por todos os fornecedores da TWYN, com foco especial nas **Equipes de Engenharia e Desenvolvimento de Software (Tratadas como Fornecedores Internos do SGSI)**.

O escopo operacional do SGSI da TWYN foca na infraestrutura de hospedagem SaaS (AWS). Portanto, qualquer software, código-fonte ou integração fornecida pela equipe de engenharia é tratada como um produto de terceiros e deve aderir a este adendo antes de ser implantado em produção.

## 2. Requisitos de Conformidade Legal e Contratual

### 2.1 Acordo de Confidencialidade (NDA)
Todos os engenheiros, desenvolvedores e terceiros envolvidos no desenvolvimento do software devem assinar um Acordo de Confidencialidade (NDA) irrevogável antes de obter qualquer nível de acesso aos ambientes da TWYN ou documentações de arquitetura.

### 2.2 Conformidade com a LGPD
O fornecedor reconhece que a plataforma processa **Dados Biométricos** (Dados Pessoais Sensíveis, conforme Art. 11 da LGPD). O fornecedor está expressamente proibido de:
- Extrair, copiar ou espelhar dados de produção para ambientes de desenvolvimento ou teste.
- Inserir rotinas no código que enviem telemetria ou dados do usuário para endpoints não autorizados.
- Usar dados reais (produção) para depuração local. Apenas dados sintéticos/anonimizados são permitidos.

## 3. Requisitos de Desenvolvimento Seguro (Ciclo de Vida)

Para que o código desenvolvido seja aceito e implantado pela equipe de Operações (Escopo do SGSI), o fornecedor deve garantir que o processo de desenvolvimento atende aos seguintes requisitos (cobrindo o controle A.8.25):

### 3.1 Análise de Código e Vulnerabilidades (SAST/SCA)
1. O fornecedor deve implementar ferramentas de *Static Application Security Testing* (SAST) em sua pipeline de integração contínua (CI).
2. Nenhuma *Pull Request* (PR) pode ser mesclada na ramificação principal (`main`/`master`) se contiver vulnerabilidades de nível **CRÍTICO** ou **ALTO**.
3. O fornecedor deve realizar *Software Composition Analysis* (SCA) para garantir que nenhuma dependência de terceiros contenha vulnerabilidades conhecidas (CVEs).

### 3.2 Padrões de Codificação
O fornecedor deve aderir às práticas de codificação segura (ex: OWASP Top 10), garantindo proteção contra:
- Injeção de SQL (uso de ORMs seguros ou consultas parametrizadas).
- *Cross-Site Scripting* (XSS) e *Cross-Site Request Forgery* (CSRF).
- *Broken Authentication* e *Insecure Direct Object References* (IDOR).

### 3.3 Gestão de Segredos no Código
É **terminantemente proibido** o *hardcoding* de senhas, chaves de API, tokens JWT ou strings de conexão de banco de dados no código-fonte. O fornecedor deve preparar a aplicação para receber segredos exclusivamente via variáveis de ambiente injetadas em tempo de execução pela plataforma de Operações.

## 4. Service Level Agreement (SLA) para Correção de Vulnerabilidades

Caso a equipe de Operações da TWYN detecte vulnerabilidades na plataforma operante (via testes de penetração, relatórios de bug bounty ou scanners do AWS GuardDuty), o fornecedor deverá fornecer um *patch* de correção nos seguintes prazos máximos:

| Severidade (CVSS v3) | Prazo Máximo para Correção (Patch) |
|----------------------|------------------------------------|
| **Crítico (9.0 - 10.0)** | 24 Horas |
| **Alto (7.0 - 8.9)**     | 7 Dias Corridos |
| **Médio (4.0 - 6.9)**    | 30 Dias Corridos |
| **Baixo (0.1 - 3.9)**    | Próximo Ciclo de Release Planejado |

## 5. Direito a Auditoria e Revisão de Serviços

A equipe de Operações da TWYN, como mantenedora do SGSI, reserva-se o direito de:
1. Requisitar relatórios mensais dos resultados das ferramentas SAST/SCA da equipe de engenharia.
2. Contratar testes de penetração independentes sobre o código fornecido, sem aviso prévio ao fornecedor.
3. Rejeitar ou reverter implantações (*deployments*) caso considere que a versão candidata ameaça a integridade ou confidencialidade do ambiente SaaS.

## 6. Controle de Acesso e Responsabilidades na AWS

O fornecedor (Desenvolvimento) não possui acesso de administrador ao ambiente de Produção AWS (Controle A.5.15). 
- O acesso a logs e métricas de produção será provido via ferramentas de observabilidade restritas, filtrando dados PII ou senhas.
- O *deploy* em produção será automatizado (via GitHub Actions com OIDC) ou conduzido exclusivamente pela equipe de Operações.

## 7. Histórico de Revisão

| Data | Versão | Autor | Descrição das Alterações |
|------|---------|-------|---------------------------|
| 2026-06-09 | 1.0 | Gestor SGSI | Criação inicial (Alinhamento com controles A.5.19, A.5.21 e A.5.22). |
