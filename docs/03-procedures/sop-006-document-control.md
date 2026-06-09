---
document_id: SGSI-SOP-006
title: Controle de Informação Documentada
version: 1.0
status: Approved
classification: INTERNAL
owner: Gestor SGSI
approved_by: CEO
last_review: 2026-06-09
next_review: 2027-06-09
related_policies:
  - SGSI-POLICY-001
annex_a_controls:
  - A.5.1
  - A.5.37
---

# Procedimento de Controle de Informação Documentada (SOP-006)

## 1. Objetivo e Escopo
Este documento estabelece o procedimento padronizado para criação, atualização, aprovação e retenção de todas as políticas, procedimentos e registros do Sistema de Gestão de Segurança da Informação (SGSI) da TWYN.
O escopo abrange todos os documentos oficiais que apoiam a certificação ISO 27001, residentes no repositório `TWYN-ISO27001`.

**Atendimento à Cláusula ISO 27001:** 7.5 (Informação Documentada).

## 2. Responsabilidades
- **Gestor SGSI**: Responsável pela curadoria do repositório, validação das tags e metadados, e coordenação das revisões anuais.
- **Autores (Qualquer Colaborador)**: Criação inicial de minutas e submissão via Pull Request (PR).
- **Aprovadores (CEO ou Diretoria)**: Aprovação formal de Políticas Mestre.
- **Aprovadores Técnicos (DevOps Lead)**: Aprovação de SOPs operacionais.

## 3. Padrão de Identificação (Nomenclatura e Metadados)
Todo documento oficial DEVE possuir um bloco `YAML frontmatter` no início do arquivo `.md`, garantindo legibilidade tanto humana quanto pelo *Governance Dashboard*.

O bloco obrigatório deve conter:
- `document_id`: Identificador único (ex: SGSI-POLICY-001, SGSI-SOP-002).
- `title`: Título legível.
- `version`: Versão atual (ex: 1.0, 1.1).
- `status`: Draft, In Review, Approved, ou Obsolete.
- `classification`: PÚBLICO, INTERNO, CONFIDENCIAL, ou RESTRITO.
- `owner`: Cargo responsável por manter o documento atualizado.
- `approved_by`: Cargo que tem a autoridade final para aprovar.
- `last_review` e `next_review`: Datas no formato YYYY-MM-DD.

## 4. Ciclo de Vida do Documento

### 4.1. Criação
1. O autor clona o repositório ou cria uma *branch* nova no GitHub.
2. O arquivo Markdown é criado seguindo a hierarquia de pastas (`/docs/02-policies`, `/docs/03-procedures`, etc).
3. O metadado `status` nasce como `Draft`.

### 4.2. Revisão e Aprovação (Docs as Code)
A TWYN adota o modelo "Docs as Code". A aprovação é rastreada nativamente através de Pull Requests.
1. O autor abre um Pull Request para a branch `main`.
2. O `approved_by` designado (ou Gestor SGSI) revisa o documento no GitHub.
3. Se aprovado, o revisor altera o metadado para `status: Approved` em um commit de revisão e realiza o `Merge` na branch `main`.
4. O *Merge Commit* serve como assinatura e carimbo temporal incontestável da aprovação (Audit Trail).

### 4.3. Atualização e Versionamento
- **Minor Changes (Erros de digitação, hiperlinks)**: Bump da versão menor (ex: 1.0 para 1.1).
- **Major Changes (Mudanças de regras de negócio, novos controles)**: Bump da versão maior (ex: 1.1 para 2.0) e exige novo Pull Request com aprovação da Diretoria.

### 4.4. Retenção e Descarte (Obsolescência)
- Registros vitais e Logs do SGSI (ex: Atas de MR, Relatórios de Auditoria, Registros de Treinamento) são retidos no Git por **no mínimo 3 anos**.
- Documentos obsoletos têm o seu `status` alterado para `Obsolete` e são movidos para uma subpasta `/archive`.
- Sendo baseados em Git, todo o histórico criptográfico de alterações é mantido indefinidamente contra adulterações.

## 5. Registros (Evidências)
O histórico de Commits da branch `main` no repositório GitHub atua como o log oficial de auditoria para o controle de versões. Não é necessário manter planilhas paralelas de controle de versão.
