---
document_id: SGSI-POLICY-011
title: Política de Criptografia
version: 1.0
date: 2026-06-09
classification: Público
owner: Gestor SGSI
approved_by: CEO (Aprovado)
next_review: Anual
annex_a_controls: "A.8.24, A.8.25"
---

# Política de Criptografia

## 1. Propósito
Garantir a confidencialidade, integridade e autenticidade das informações tratadas pela TWYN, formalizando o uso obrigatório de controles criptográficos robustos (em repouso e em trânsito). Esta política é essencial para aderência à proteção de dados biométricos exigida pela LGPD.

## 2. Escopo
Aplica-se a toda a infraestrutura (Servidores, Bancos de Dados, Buckets S3), aplicações da Face ID Platform API, comunicações de rede e dispositivos de usuários que manipulem dados classificados como CONFIDENCIAL ou RESTRITO.

## 3. Diretrizes de Uso da Criptografia (A.8.24)

### 3.1 Criptografia em Trânsito
Todas as comunicações envolvendo sistemas da TWYN, clientes da API e ambientes internos devem ocorrer através de protocolos seguros.
- O uso de **TLS 1.2** é o mínimo obrigatório, sendo o **TLS 1.3** a recomendação padrão.
- É estritamente proibido o tráfego HTTP em texto claro ou uso de protocolos obsoletos (SSLv3, TLS 1.0/1.1) para exposição na internet.
- Chaves SSH seguras (ED25519 ou RSA ≥ 2048-bit) devem ser usadas para acessos administrativos.

### 3.2 Criptografia em Repouso
Dados biométricos e dados operacionais da TWYN armazenados fisicamente devem ser encriptados para evitar o acesso não autorizado.
- **Armazenamento em Nuvem:** Bancos de dados (Amazon RDS) e objetos (S3) devem estar obrigatoriamente criptografados utilizando algoritmos simétricos robustos (ex: **AES-256**) combinados ao AWS KMS.
- **Dispositivos Físicos:** Os notebooks e estações de trabalho dos colaboradores com acesso aos sistemas da TWYN devem possuir criptografia total de disco (FDE - Full Disk Encryption), como BitLocker para Windows ou FileVault para macOS.

## 4. Gestão de Chaves Criptográficas (A.8.25)
Os processos detalhados para a gestão do ciclo de vida das chaves estão definidos no documento de procedimento técnico (SGSI-SOP-004 - Gestão de Segredos).
- **Separação de Funções:** As chaves (KMS) que criptografam as bases biométricas não podem ser exportadas livremente ou acessadas por desenvolvedores.
- **Rotação:** Todas as chaves e segredos em nuvem devem ser rotacionados regularmente de acordo com as diretrizes de segurança da nuvem AWS.
- **Perda e Comprometimento:** O comprometimento de uma chave privada ou KMS Master Key configura um Incidente de Segurança Crítico.

## 5. Exceções e Algoritmos Obsoletos
- É expressamente proibido à equipe de engenharia criar rotinas próprias de "hash" ou implementar algoritmos caseiros. Apenas bibliotecas criptográficas validadas e de amplo uso de mercado são permitidas.
- O uso de funções de hash consideradas fracas para armazenamento de senhas (ex: MD5, SHA-1) é proibido. Deve-se utilizar algoritmos robustos com sal e derivação lenta (ex: Argon2, bcrypt ou PBKDF2).

## 6. Histórico de Revisão
| Data | Versão | Autor | Descrição |
|------|--------|-------|-----------|
| 2026-06-09 | 1.0 | Gestor SGSI | Conversão do cabeçalho para YAML padrão e padronização (PT-BR). |
