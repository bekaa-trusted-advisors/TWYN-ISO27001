---
document_id: SGSI-POLICY-010
title: Política de Retenção e Descarte Seguro de Dados
version: 1.0
date: 2026-06-09
classification: Público
owner: Gestor SGSI
approved_by: CEO (Aprovado)
next_review: Anual
annex_a_controls: "A.8.10, A.8.12, A.8.14"
---

# Política de Retenção e Descarte Seguro de Dados

## Controle de Documento

| Propriedade | Detalhe |
|---|---|
| **ID do Documento** | SGSI-POLICY-010 |
| **Versão** | 1.0 |
| **Data de Aprovação** | 2026-06-09 |
| **Classificação** | Público |
| **Elaborado por** | Gestor SGSI |
| **Aprovado por** | CEO (Aprovado) |
| **Próxima Revisão** | Anual |


## 1. Propósito
Assegurar que os dados armazenados e processados pela TWYN, especialmente informações biométricas classificadas como RESTRITO (altamente sensíveis), não sejam retidos por mais tempo do que o estritamente necessário para o propósito da coleta, e que o seu descarte seja executado de forma irreversível e segura, em conformidade com a **Lei Geral de Proteção de Dados Pessoais (LGPD)** e ISO 27001.

## 2. Escopo
Aplica-se a todos os ativos físicos e lógicos, instâncias em nuvem (S3, RDS), backups, logs e estações de trabalho de colaboradores que armazenem dados corporativos ou de clientes da TWYN.

## 3. Prazos de Retenção de Dados (A.8.12)
Os dados sob a tutela da TWYN devem seguir a seguinte tabela de retenção padrão:

| Tipo de Dado | Classificação | Prazo de Retenção | Justificativa |
|---|---|---|---|
| Vetores Biométricos | RESTRITO | Imediato ou Término de Contrato | Uso restrito da API Face ID. Dados são descartados via exclusão de conta pelo cliente (LGPD Art. 16). |
| Logs de Aplicação / Auditoria | CONFIDENCIAL | 1 a 5 anos | Compliance forense e segurança operacional. |
| Dados Cadastrais B2B | INTERNO | 5 anos pós-distrato | Obrigação legal / Exercício regular de direitos (Art. 7, LGPD). |
| Documentos do SGSI | PÚBLICO / INTERNO | Mínimo 3 anos | Conformidade ISO 27001 e auditorias de certificação. |

## 4. Descarte de Informações Digitais (A.8.10)

### 4.1 Ambiente em Nuvem (AWS)
- A exclusão de informações contidas em bancos de dados (ex: RDS PostgreSQL) deve seguir procedimentos de *soft-delete* seguido de limpeza periódica e irreversível (*hard-delete*).
- **Trituração Criptográfica (Crypto-Shredding):** Para garantir o expurgo irreversível de dados sensíveis armazenados na nuvem (AWS), a TWYN prioriza a deleção das chaves de criptografia (KMS Customer Managed Keys) que encriptaram os respectivos volumes (S3 e RDS).

### 4.2 Dispositivos Pessoais e de Trabalho
- Nenhum dado corporativo confidencial, em especial dados biométricos, deve residir permanentemente no armazenamento local (discos C: ou /home) das máquinas.
- Ao término do contrato do colaborador, a máquina deve passar por formatação completa (zero-fill ou destruição de chave FDE).

## 5. Destruição de Mídia Física (A.8.10)
A TWYN é uma empresa nativa em nuvem e não armazena dados de clientes em papel ou mídias removíveis (pen drives). Caso haja impressão de documentos de negócios confidenciais, estes devem ser destruídos utilizando fragmentadoras de papel corte em cruz antes do descarte.

## 6. Conformidade e Revisão
O não cumprimento desta política configura uma quebra grave de conformidade com a LGPD e pode expor a empresa a sanções. A área técnica e o Gestor do SGSI auditarão periodicamente os recursos na nuvem (S3, RDS) para atestar a exclusão adequada de dados expirados.

## 7. Histórico de Revisão
| Data | Versão | Autor | Descrição |
|------|--------|-------|-----------|
| 2026-06-09 | 1.0 | Gestor SGSI | Conversão de cabeçalho para YAML e ajustes ortográficos e de estilo (PT-BR). |
