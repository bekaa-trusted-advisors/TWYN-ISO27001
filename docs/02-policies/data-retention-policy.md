---
**Document Control**
| Campo | Valor |
|-------|-------|
| **Document ID** | SGSI-POLICY-010 |
| **Version** | 1.0 |
| **Author** | BEKAA Consultoria — Ricardo Esper |
| **Approved By** | **CEO (Ata 001)** |
| **Approval Date** | 2026-06-08 |
| **Effective Date** | 2026-06-08 |
| **Próxima Revisão** | Anual após aprovação |
| **ISO 27001:2022 Mapping** | **A.8.10**, **A.8.12**, **A.8.14** |
| **Classification** | **PUBLIC** |
---

# Política de Retenção e Descarte Seguro de Dados
## Data Retention and Disposal Policy — TWYN

---

## 1. Propósito

Assegurar que os dados armazenados e processados pela TWYN, especialmente informações biométricas classificadas como *RESTRICTED* (Altamente Sensíveis), não sejam retidos por mais tempo do que o estritamente necessário para o propósito da coleta, e que o seu descarte seja executado de forma irreversível e segura, em estrita conformidade com a **Lei Geral de Proteção de Dados Pessoais (LGPD)** e ISO 27001.

---

## 2. Escopo

Aplica-se a todos os ativos físicos e lógicos, instâncias em nuvem (S3, RDS), backups, logs e estações de trabalho de colaboradores que armazenem dados corporativos ou de clientes da TWYN.

---

## 3. Prazos de Retenção de Dados (Data Retention)

Os dados sob a tutela da TWYN devem seguir a seguinte tabela de retenção padrão:

| Tipo de Dado | Classificação | Prazo de Retenção | Justificativa |
|---|---|---|---|
| Vetores Biométricos | RESTRICTED | Imediato ou Término de Contrato | Uso restrito da API Face ID. Dados são processados em RAM ou descartados via exclusão de conta pelo cliente (LGPD Art. 16). |
| Logs de Aplicação / Auditoria | CONFIDENTIAL | 1 a 5 anos | Compliance forense e segurança operacional. |
| Dados Cadastrais B2B | INTERNAL | 5 anos pós-distrato | Obrigação legal / Exercício regular de direitos (Art. 7, LGPD). |
| Documentos do SGSI | PUBLIC / INTERNAL | Mínimo 3 anos | Conformidade ISO 27001 e auditorias de certificação. |

---

## 4. Descarte de Informações Digitais (Secure Deletion)

### 4.1 Ambiente em Nuvem (AWS)
- A exclusão de informações contidas em bancos de dados (ex: RDS PostgreSQL) deve seguir procedimentos de *soft-delete* (remoção lógica) seguido da limpeza periódica e irreversível (*hard-delete*).
- **Crypto-Shredding (Trituração Criptográfica):** Para garantir o expurgo irreversível de dados sensíveis armazenados em nuvem e provedores IaaS, a TWYN prioriza a deleção ou rotação destrutiva das chaves de criptografia (KMS Customer Managed Keys) que encriptaram esses volumes, tornando a recuperação impossível.

### 4.2 Laptops e Dispositivos Pessoais (BYOD)
- Nenhum dado corporativo confidencial, em especial dados de clientes e biométricos, deve residir permanentemente no armazenamento local (discos C: ou /home) das máquinas dos desenvolvedores.
- Ao término do contrato do colaborador, a máquina deve passar por rotinas de apagamento remoto (via MDM, se aplicável) ou formatação completa.

---

## 5. Destruição de Mídia Física

Dada a natureza 100% cloud da TWYN, a companhia não gera registros biométricos ou lógicos em papel ou mídias físicas amovíveis (pen drives, HDs externos). Caso haja impressão de documentos de negócio confidenciais, estes devem ser destruídos através de fragmentadoras de papel (corte transversal) antes de seu descarte em lixo comum (Controle A.8.10 e A.7.14).

---

## 6. Conformidade e Revisão

O não cumprimento desta política configura uma quebra grave de conformidade, podendo expor a empresa a sanções da Autoridade Nacional de Proteção de Dados (ANPD). Auditorias periódicas devem ser conduzidas no S3 e no RDS para atestar que vetores biométricos inativos estão sendo descartados da forma correta.
