---
**Document Control**
| Campo | Valor |
|-------|-------|
| **Document ID** | SGSI-POLICY-011 |
| **Version** | 1.0 |
| **Author** | BEKAA Consultoria — Ricardo Esper |
| **Approved By** | **[CEO TWYN]** ⚠️ ASSINATURA OBRIGATÓRIA |
| **Approval Date** | [Pendente] |
| **Effective Date** | [Pendente] |
| **Próxima Revisão** | Anual após aprovação |
| **ISO 27001:2022 Mapping** | **A.8.24**, **A.8.25** |
| **Classification** | **PUBLIC** |
---

# Política de Criptografia
## Cryptography Policy — TWYN

---

## 1. Propósito

Garantir a confidencialidade, a integridade e a autenticidade das informações protegidas pela TWYN, formalizando o uso obrigatório de controles criptográficos efetivos e robustos em repouso e em trânsito. Esta política assegura a aderência legal à privacidade de dados biométricos exigida pela LGPD.

---

## 2. Escopo

Aplica-se a toda infraestrutura (Servidores, Bancos de Dados, Buckets S3), aplicações da Plataforma Face ID, comunicações de rede e endpoints de usuários que manipulem dados classificados como CONFIDENTIAL ou RESTRICTED.

---

## 3. Diretrizes de Uso da Criptografia

### 3.1 Criptografia em Trânsito
Todas as comunicações envolvendo sistemas da TWYN, clientes da API e ambientes internos, incluindo tráfego público e autenticação, devem ocorrer através de protocolos seguros.
- O uso de **TLS 1.2** é o mínimo obrigatório, sendo o **TLS 1.3** a recomendação padrão (Default).
- É estritamente proibido o tráfego HTTP em texto claro ou uso de protocolos legados (SSLv3, TLS 1.0/1.1) para expor a API Face ID na internet.
- Chaves SSH seguras (ED25519 ou RSA ≥ 2048-bit) devem ser usadas para acessos administrativos.

### 3.2 Criptografia em Repouso
Dados biométricos e operacionais da TWYN armazenados fisicamente (discos, bancos e nuvem) devem ser encriptados para evitar o acesso não autorizado por agentes físicos ou invasores.
- **Armazenamento em Nuvem:** Bancos de dados (Amazon RDS) e objetos (S3) devem estar 100% criptografados utilizando algoritmos simétricos robustos, preferencialmente **AES-256**.
- **Dispositivos Físicos:** Os laptops e workstations dos colaboradores que possuam qualquer nível de acesso aos sistemas da TWYN devem possuir criptografia total de disco nativa (FDE - Full Disk Encryption), como BitLocker para Windows ou FileVault para macOS (Controle A.8.1).

---

## 4. Gestão de Chaves Criptográficas (Key Management)

Os processos detalhados para a operação do ciclo de vida das chaves estão definidos no *SGSI-SOP-004 - Gestão de Segredos*. Os princípios fundamentais ditados por esta política incluem:
- **Separação de Funções:** As chaves (KMS) que criptografam as bases biométricas não podem ser livremente exportadas ou acessadas por desenvolvedores.
- **Rotação:** Todas as chaves e segredos em nuvem devem ser rotacionados regularmente de acordo com as metodologias do provedor AWS.
- **Perda e Comprometimento:** O comprometimento de uma chave privada ou KMS Master Key configurará um Incidente de Segurança Crítico e acionará os mecanismos do *Incident Response Plan*.

---

## 5. Exceções e Algoritmos Obsoletos

É expressamente proibido aos desenvolvedores criar rotinas próprias de "hash" ou implementar algoritmos caseiros. Somente bibliotecas criptográficas de amplo uso de mercado são permitidas.

O uso de funções de Hash consideradas fracas para armazenamento de senhas (ex: MD5 ou SHA-1 isolados) é proibido, devendo-se utilizar algoritmos robustos com *Salt* e *Key Stretching* (como Argon2, bcrypt ou PBKDF2).
