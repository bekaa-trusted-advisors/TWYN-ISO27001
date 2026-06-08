---
**Document Control**
| Campo | Valor |
|-------|-------|
| **Document ID** | SGSI-POLICY-008 |
| **Version** | 1.0 |
| **Author** | BEKAA Consultoria — Ricardo Esper |
| **Approved By** | **CEO (Ata 001)** |
| **Approval Date** | 2026-06-08 |
| **Effective Date** | 2026-06-08 |
| **Próxima Revisão** | Anual após aprovação |
| **ISO 27001:2022 Mapping** | **A.8.25**, **A.8.26**, **A.8.27**, **A.8.28** |
| **Classification** | **INTERNAL** |
---

# Política de Desenvolvimento Seguro
## Secure Development Policy — TWYN

---

## 1. Propósito

Esta **Política de Desenvolvimento Seguro** estabelece os requisitos obrigatórios para o ciclo de vida de desenvolvimento de software (SDLC) da plataforma Face ID da TWYN. Seu objetivo é garantir que a segurança seja incorporada "by design" e "by default" em todo o código produzido, prevenindo vulnerabilidades que possam comprometer a confidencialidade de dados biométricos e a infraestrutura AWS.

---

## 2. Escopo

Aplica-se a todo código-fonte, infraestrutura como código (IaC), scripts e automações desenvolvidos ou mantidos pela TWYN, incluindo colaboradores internos e contratados terceirizados.

---

## 3. Diretrizes de Segurança no Ciclo de Desenvolvimento (SDLC)

### 3.1. Arquitetura e Modelagem de Ameaças (Secure by Design)
- Todo novo microsserviço ou funcionalidade crítica que manipule dados biométricos deve passar por uma sessão de *Threat Modeling* (Modelagem de Ameaças) antes do início do desenvolvimento.
- Os princípios de **Privilégio Mínimo** e **Defesa em Profundidade** devem guiar o desenho da arquitetura técnica (Controle A.8.27).

### 3.2. Controle de Versão e Revisão de Código
- Todo o código deve residir na organização oficial do GitHub da TWYN.
- É estritamente proibido realizar "commits" diretos na branch `main`. Todo código deve ser desenvolvido em *feature branches* e integrado via *Pull Requests* (PRs).
- É exigida a revisão formal (*Peer Review*) de pelo menos 1 (um) desenvolvedor que não seja o autor do código antes do merge.

### 3.3. Separação de Ambientes
- Devem existir ambientes estritamente separados para Desenvolvimento (Dev), Homologação/Teste (Staging) e Produção (Prod) (Controle A.8.31).
- É terminantemente proibido o uso de chaves ou credenciais de Produção em ambientes de Desenvolvimento/Staging.

### 3.4. Gestão de Dados de Teste
- Sob nenhuma circunstância, dados biométricos reais ou bases de dados de produção contendo PII (Personally Identificable Information) poderão ser copiados para ambientes de desenvolvimento ou teste.
- Os testes devem utilizar dados sintéticos, gerados artificialmente ou devidamente anonimizados (Controle A.8.33).

### 3.5. Automação de Segurança (DevSecOps)
- O pipeline de CI/CD (GitHub Actions) deve executar varreduras automatizadas em todos os PRs:
  - **SAST** (Static Application Security Testing) para detectar vulnerabilidades no código.
  - **SCA** (Software Composition Analysis) para detectar bibliotecas de terceiros com CVEs conhecidos.
  - Varredura de credenciais rígidas (*hardcoded secrets*).
- PRs que falharem nos testes de segurança bloqueantes não poderão ser promovidos para Produção.

---

## 4. Codificação Segura (Secure Coding Guidelines)

Os desenvolvedores devem seguir as melhores práticas reconhecidas no mercado (ex: OWASP Top 10) para evitar vulnerabilidades como:
- Injeção de Código (SQL, NoSQL, Command Injection).
- Quebra de Autenticação e Controle de Acesso (Broken Access Control).
- Configurações Inseguras e Componentes Desatualizados.
- Falhas Criptográficas.

---

## 5. Violações

A inobservância desta política, em especial o bypass intencional dos pipelines de segurança ou a exposição de credenciais no código-fonte, sujeitará o colaborador a medidas disciplinares conforme as sanções previstas na Política de Uso Aceitável (AUP).
