---
document_id: SGSI-POLICY-010
title: Política de Uso de Software e Licenciamento
version: 1.0
date: 2026-06-08
classification: INTERNAL
owner: Gestor SGSI / CTO
approved_by: CEO (Pendente)
annex_a_controls: "A.5.32, A.8.19"
---

# Política de Uso de Software e Licenciamento (Software Licensing Policy)

## 1. Propósito
Garantir que todo o software utilizado pela **TWYN** em seus ambientes operacionais, corporativos e de desenvolvimento esteja em estrita conformidade com as leis de propriedade intelectual, direitos autorais e termos contratuais de licenciamento, mitigando riscos legais, financeiros e de segurança da informação (como malwares atrelados a softwares piratas).

## 2. Escopo
Esta política aplica-se a todos os colaboradores, estagiários, prestadores de serviço e terceiros que utilizem equipamentos de propriedade da TWYN, bem como equipamentos pessoais (BYOD) usados para acessar o ambiente corporativo e de produção da TWYN.

## 3. Diretrizes Gerais de Licenciamento

1. **Uso Exclusivo de Software Legítimo:** É terminantemente proibido o download, a instalação, o armazenamento ou a execução de software não licenciado, cópias ilegais ("pirataria"), *cracks*, *keygens* ou ferramentas de evasão de licença em qualquer equipamento da TWYN.
2. **Propriedade Intelectual (A.5.32):** A TWYN respeita estritamente os direitos autorais. Todo software de código fechado (comercial) deve possuir uma licença de uso válida e paga em nome da TWYN, ou estar coberto por licenças de uso corporativo gerenciadas pelo setor de TI.
3. **Gerenciamento Centralizado:** A aquisição de qualquer licença de software pago (IDEs, ferramentas de design, produtividade) deve ser solicitada formalmente via ticket e aprovada pela Diretoria/CTO antes da compra.

## 4. Software de Código Aberto (Open Source - OSS)

Dado que a arquitetura da TWYN envolve desenvolvimento de software (Node.js, AWS, Kubernetes), o uso de pacotes de código aberto é incentivado, porém regulado:
- **Licenças Permitidas:** O uso de bibliotecas com licenças permissivas (MIT, Apache 2.0, BSD) é aprovado por padrão.
- **Licenças Restritivas (Virais):** O uso de bibliotecas com licenças do tipo *Copyleft* forte (ex: GPL v2/v3, AGPL) **deve ser aprovado previamente** pelo CTO e Gestor SGSI, para evitar a obrigação de abertura do código-fonte proprietário da plataforma Face ID da TWYN.
- **Auditoria de Dependências:** O CI/CD deve realizar varreduras automatizadas (ex: ferramentas como Snyk ou Trivy) para identificar tanto vulnerabilidades quanto licenças incompatíveis no código.

## 5. Instalação em Sistemas Operacionais (A.8.19)

- **Equipamentos Corporativos:** A instalação de software em laptops da empresa deve ser limitada ao catálogo aprovado pela TI. Usuários padrão não devem possuir privilégios de administrador local sem justificativa aprovada.
- **Ambiente de Produção (AWS/EKS):** Nenhuma instalação manual de software é permitida nos clusters de produção ou instâncias EC2. Toda a infraestrutura e dependências de software devem ser provisionadas exclusivamente através de Infraestrutura como Código (Terraform) e pipelines de CI/CD (GitHub Actions).

## 6. Softwares Proibidos

Fica explicitamente proibida a instalação e uso de:
1. Clientes de Torrent (P2P) para fins não corporativos.
2. Ferramentas de *hacking* ou escaneamento de rede não homologadas pela equipe de segurança operacional (SecOps).
3. Softwares de mineração de criptomoedas.
4. Qualquer software que a detecção de *endpoint* (Antivírus/EDR) sinalize como Potencialmente Indesejado (PUP).

## 7. Monitoramento e Auditoria
A TWYN reserva-se o direito de auditar os equipamentos corporativos e ambientes em nuvem periodicamente (através de ferramentas de inventário e MDM) para garantir que apenas softwares licenciados e aprovados estejam em uso. Softwares não autorizados serão removidos imediatamente.

## 8. Violações
A violação desta política configura falta grave, sujeita a medidas disciplinares (conforme a Política de Segurança da Informação [SGSI-POLICY-001]), incluindo rescisão contratual e responsabilização civil ou criminal por danos de propriedade intelectual repassados à TWYN.

---
**Histórico de Revisões**
| Versão | Data | Alteração | Autor |
|--------|------|-----------|-------|
| 1.0 | 2026-06-08 | Criação da política de uso de software licenciado | Gestor SGSI |
