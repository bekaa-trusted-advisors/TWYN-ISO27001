---
document_id: SGSI-SOP-003
title: "Procedimento Operacional Padrão — Segurança no Trabalho Remoto"
version: "1.0"
status: Draft
classification: INTERNAL
approval_date: null
effective_date: null
next_review: null
owner: Gestor SGSI
related_policies:
  - SGSI-POLICY-001  # Política de Segurança da Informação
  - SGSI-POLICY-002  # Política de Classificação da Informação
  - SGSI-POLICY-007  # Política de Uso Aceitável (AUP)
annex_a_controls:
  - "A.6.7"   # Trabalho remoto
  - "A.8.1"   # Dispositivos de endpoint do usuário
  - "A.5.14"  # Transferência de informação
  - "A.8.5"   # Autenticação segura
---

# SGSI-SOP-003 — Segurança no Trabalho Remoto

## 1. Objetivo

Este Procedimento Operacional Padrão (SOP) estabelece os requisitos obrigatórios de segurança da informação para todos os colaboradores da **TWYN** que exercem atividades profissionais fora das instalações físicas da organização, seja em regime remoto integral ou híbrido.

O documento visa garantir que:

- A confidencialidade, integridade e disponibilidade das informações da TWYN sejam preservadas independentemente da localização do colaborador;
- O tratamento de dados pessoais sensíveis — em especial dados biométricos protegidos pela LGPD (Art. 11) — ocorra exclusivamente em ambientes e dispositivos seguros;
- As obrigações decorrentes da ISO/IEC 27001:2022 e dos controles do Anexo A sejam atendidas de forma contínua;
- Os riscos específicos do trabalho remoto sejam identificados, tratados e monitorados.

## 2. Escopo

### 2.1 Aplicabilidade

Este SOP aplica-se a:

| Público | Descrição |
|---|---|
| Colaboradores CLT | Todos os funcionários em regime remoto ou híbrido |
| Prestadores de serviço | Terceiros com acesso a sistemas ou dados da TWYN |
| Estagiários | Quando autorizados a exercer trabalho remoto |
| Gestores | Responsáveis pela aprovação e supervisão do trabalho remoto |

### 2.2 Ambientes cobertos

- Residências dos colaboradores;
- Espaços de coworking;
- Locais temporários de trabalho (viagens, deslocamentos);
- Qualquer localização fora das instalações da TWYN.

### 2.3 Exclusões

Conforme definido na Cláusula 4 do SGSI, os laptops e dispositivos pessoais **não fazem parte do escopo do ISMS**. Entretanto, este SOP define requisitos mínimos de segurança que devem ser atendidos por qualquer dispositivo utilizado para acessar recursos da TWYN, independentemente de propriedade.

## 3. Referências Normativas

| Referência | Descrição |
|---|---|
| ISO/IEC 27001:2022 | Sistema de Gestão de Segurança da Informação |
| ISO/IEC 27002:2022 | Controles de segurança da informação |
| LGPD (Lei 13.709/2018) | Lei Geral de Proteção de Dados Pessoais |
| LGPD Art. 11 | Tratamento de dados pessoais sensíveis (biometria) |
| SGSI-POLICY-001 | Política de Segurança da Informação |
| SGSI-POLICY-002 | Política de Classificação da Informação |
| SGSI-POLICY-007 | Política de Uso Aceitável (AUP) |

## 4. Definições

| Termo | Definição |
|---|---|
| **Trabalho Remoto** | Execução de atividades profissionais fora das instalações da TWYN |
| **Dados Biométricos** | Dados pessoais sensíveis utilizados para identificação de pessoa natural (LGPD Art. 5º, II) |
| **VPN** | Rede Virtual Privada — canal criptografado para acesso seguro a recursos corporativos |
| **MFA** | Autenticação Multifator — exigência de dois ou mais fatores para autenticação |
| **Classificação da Informação** | Categorização em PUBLIC, INTERNAL, CONFIDENTIAL ou RESTRICTED conforme SGSI-POLICY-002 |
| **Clean Desk** | Prática de manter a área de trabalho livre de documentos e mídias sensíveis |

## 5. Elegibilidade e Aprovação

### 5.1 Critérios de elegibilidade

Para ser elegível ao trabalho remoto, o colaborador deve:

1. Ter concluído o treinamento obrigatório de conscientização em segurança da informação;
2. Ter assinado o Termo de Responsabilidade de Trabalho Remoto (Anexo A deste SOP);
3. Possuir dispositivo que atenda aos requisitos mínimos de segurança definidos na Seção 6.1;
4. Dispor de conexão de internet estável e segura;
5. Ter sido aprovado pelo gestor direto e pelo Gestor SGSI.

### 5.2 Processo de aprovação

```
Colaborador solicita → Gestor direto avalia → Gestor SGSI valida requisitos
de segurança → Aprovação registrada → Colaborador assina termo
```

1. O colaborador preenche o formulário de solicitação de trabalho remoto;
2. O gestor direto avalia a adequação funcional;
3. O Gestor SGSI valida o cumprimento dos requisitos técnicos e de segurança;
4. A aprovação é registrada e arquivada por, no mínimo, 12 meses;
5. O colaborador assina o Termo de Responsabilidade (Anexo A).

### 5.3 Revogação

O direito ao trabalho remoto pode ser revogado a qualquer momento em caso de:

- Descumprimento dos requisitos de segurança deste SOP;
- Incidente de segurança causado por negligência;
- Alteração nas funções que exijam presença física;
- Decisão administrativa fundamentada.

## 6. Requisitos de Segurança

### 6.1 Segurança de Dispositivos (A.8.1)

Todo dispositivo utilizado para acessar recursos da TWYN — seja corporativo ou pessoal — **deve atender obrigatoriamente** aos seguintes requisitos:

| Requisito | Especificação | Verificação |
|---|---|---|
| **Sistema Operacional** | Versão suportada pelo fabricante, com atualizações automáticas habilitadas | Trimestral |
| **Atualizações de Segurança** | Patches críticos aplicados em até 72 horas após disponibilização | Mensal |
| **Antivírus / EDR** | Solução ativa com definições atualizadas (atualização mínima diária) | Mensal |
| **Criptografia de Disco** | BitLocker (Windows), FileVault (macOS) ou LUKS (Linux) habilitado em todo o disco | Na aprovação e semestralmente |
| **Bloqueio de Tela** | Bloqueio automático após **5 minutos** de inatividade | Trimestral |
| **Senha do Dispositivo** | Mínimo de 8 caracteres ou biometria para desbloqueio | Na aprovação |
| **Firewall Local** | Firewall do sistema operacional ativo e configurado | Trimestral |
| **Backup** | Dados de trabalho armazenados em repositórios corporativos (GitHub, AWS S3), nunca apenas localmente | Contínuo |

> **Nota:** Embora os dispositivos estejam fora do escopo do ISMS (Cláusula 4), o não cumprimento destes requisitos implica na revogação do acesso remoto.

### 6.2 Segurança de Rede (A.5.14)

#### 6.2.1 Requisitos gerais

- Utilizar preferencialmente rede doméstica protegida por WPA2 ou WPA3;
- A senha do roteador doméstico deve ser alterada do padrão de fábrica;
- O firmware do roteador deve ser atualizado regularmente;
- Redes públicas (cafeterias, aeroportos, hotéis) são **proibidas** para acesso a dados classificados como CONFIDENTIAL ou RESTRICTED.

#### 6.2.2 Uso de VPN

| Cenário | VPN Obrigatória? |
|---|---|
| Acesso ao Console AWS (IAM) | **SIM** |
| Acesso a repositórios GitHub privados | **SIM** |
| Acesso a sistemas internos da TWYN | **SIM** |
| Execução de Terraform (IaC) | **SIM** |
| Acesso a dados classificados como CONFIDENTIAL ou RESTRICTED | **SIM** |
| Acesso a e-mail corporativo | RECOMENDADO |
| Navegação geral (sem acesso a recursos corporativos) | NÃO |

#### 6.2.3 Redes públicas

- **PROIBIDO**: Acessar, processar ou visualizar dados classificados como RESTRICTED em redes públicas, **mesmo com VPN ativa**;
- **PROIBIDO**: Acessar, processar ou visualizar dados biométricos em redes públicas;
- Dados classificados como CONFIDENTIAL só podem ser acessados em redes públicas **com VPN ativa e em caráter excepcional**, mediante justificativa registrada;
- Dados PUBLIC e INTERNAL podem ser acessados em redes públicas com VPN ativa.

### 6.3 Autenticação e Controle de Acesso (A.8.5)

| Requisito | Especificação |
|---|---|
| **MFA** | Obrigatório para **todos** os acessos a sistemas corporativos, sem exceção |
| **Senhas** | Mínimo de **14 caracteres**, combinando maiúsculas, minúsculas, números e caracteres especiais |
| **Rotação de Senhas** | A cada **90 dias**, sem reutilização das últimas 12 senhas |
| **Gerenciador de Senhas** | Uso obrigatório de gerenciador de senhas aprovado pela TWYN |
| **Timeout de Sessão** | Sessões inativas encerradas automaticamente após **15 minutos** |
| **Compartilhamento de Credenciais** | **Terminantemente proibido** |
| **AWS IAM** | Acesso somente via credenciais IAM individuais com MFA habilitado |
| **Chaves SSH/GPG** | Protegidas por passphrase; chaves privadas nunca compartilhadas |

#### 6.3.1 Sessões e tokens

- Tokens de acesso devem ter validade máxima de 8 horas;
- Sessões de console AWS devem ser encerradas ao final do expediente;
- Credenciais temporárias (STS) devem ser preferidas sobre credenciais de longa duração;
- O uso de `aws-vault` ou ferramenta equivalente é recomendado para proteção de credenciais AWS locais.

### 6.4 Tratamento de Dados (A.5.14 / LGPD Art. 11)

#### 6.4.1 Regras por classificação

| Classificação | Armazenamento Local | Impressão | Compartilhamento |
|---|---|---|---|
| **PUBLIC** | Permitido | Permitido | Livre |
| **INTERNAL** | Permitido com criptografia | Permitido com descarte seguro | Canais aprovados |
| **CONFIDENTIAL** | Somente cache temporário | Somente com aprovação do gestor | Canais criptografados |
| **RESTRICTED** | **PROIBIDO** | **PROIBIDO** | Somente com autorização formal |

#### 6.4.2 Dados biométricos — regras específicas

Devido à natureza sensível dos dados biométricos processados pela TWYN:

1. **É PROIBIDO** armazenar dados biométricos em dispositivos locais (laptops, pen drives, HDs externos);
2. **É PROIBIDO** imprimir dados biométricos em qualquer circunstância;
3. **É PROIBIDO** transferir dados biométricos por e-mail, mensageiros instantâneos ou qualquer canal não criptografado;
4. **É PROIBIDO** capturar telas (screenshots) contendo dados biométricos;
5. O processamento de dados biométricos deve ocorrer **exclusivamente** em ambientes AWS autorizados;
6. Todo acesso a dados biométricos deve ser registrado em log de auditoria;
7. O download de datasets biométricos para ambiente local é **estritamente proibido**.

#### 6.4.3 Descarte de informações

- Documentos físicos com informação INTERNAL ou superior devem ser destruídos com fragmentadora (corte cruzado, nível P-4 ou superior);
- Mídias eletrônicas devem ser sanitizadas conforme NIST SP 800-88;
- Lixeira do sistema operacional deve ser esvaziada regularmente.

### 6.5 Segurança Física do Ambiente de Trabalho (A.6.7)

#### 6.5.1 Clean Desk (Mesa Limpa)

- Ao se ausentar do posto de trabalho, o colaborador deve:
  - Bloquear a tela do computador (Win+L / Cmd+Ctrl+Q);
  - Guardar documentos físicos em local fechado;
  - Remover notas adesivas com informações sensíveis;
  - Desconectar mídias removíveis.

#### 6.5.2 Privacidade de tela

- Utilizar filtro de privacidade no monitor quando trabalhar em ambientes com possibilidade de visualização por terceiros (coworking, locais públicos);
- Posicionar a tela de modo a evitar visualização por janelas, câmeras ou outras pessoas;
- Em videoconferências, verificar o que está visível no plano de fundo antes de ativar a câmera;
- Utilizar fundo virtual ou desfocado em chamadas quando houver informações visíveis no ambiente.

#### 6.5.3 Espaço de trabalho

- O local de trabalho remoto deve, preferencialmente:
  - Ser um cômodo com porta que possa ser fechada;
  - Não ser compartilhado com pessoas não autorizadas durante o manuseio de dados CONFIDENTIAL ou RESTRICTED;
  - Ter acesso restrito a menores de idade e visitantes ao equipamento de trabalho.

### 6.6 Segurança nas Comunicações (A.5.14)

#### 6.6.1 Canais aprovados

| Finalidade | Canal Aprovado | Canal Proibido |
|---|---|---|
| Comunicação interna | Slack corporativo, Microsoft Teams | WhatsApp pessoal, Telegram pessoal |
| E-mail | E-mail corporativo (@twyn.com.br) | E-mail pessoal (Gmail, Hotmail, etc.) |
| Compartilhamento de código | GitHub (repositórios privados) | Google Drive pessoal, Dropbox pessoal |
| Transferência de arquivos | AWS S3 (buckets autorizados), GitHub | WeTransfer, pen drives pessoais |
| Videoconferência | Google Meet corporativo, Zoom licenciado | Plataformas não autorizadas |
| Documentação técnica | Confluence, Notion corporativo | Documentos locais não sincronizados |

#### 6.6.2 Regras gerais de comunicação

1. **É PROIBIDO** utilizar e-mail pessoal para qualquer comunicação profissional;
2. **É PROIBIDO** encaminhar e-mails corporativos para contas pessoais;
3. Informações classificadas como CONFIDENTIAL ou RESTRICTED devem ser compartilhadas apenas por canais criptografados;
4. Discussões sobre dados biométricos ou informações RESTRICTED devem ser realizadas exclusivamente em canais corporativos com controle de acesso;
5. Gravações de reuniões contendo informações CONFIDENTIAL devem ser armazenadas em repositórios aprovados com controle de acesso adequado.

## 7. Relato de Incidentes em Ambiente Remoto

### 7.1 Tipos de incidentes

O colaborador em trabalho remoto deve relatar **imediatamente** os seguintes eventos:

| Tipo de Incidente | Exemplos | Prazo para Relato |
|---|---|---|
| **Perda ou roubo de dispositivo** | Laptop, celular, token MFA, pen drive | **Imediato** (máximo 1 hora) |
| **Acesso não autorizado** | Tela visualizada por terceiro, acesso suspeito | **Imediato** (máximo 2 horas) |
| **Malware / Phishing** | E-mail suspeito, comportamento anômalo do sistema | **Imediato** (máximo 2 horas) |
| **Vazamento de dados** | Envio acidental de informação, exposição de credenciais | **Imediato** (máximo 1 hora) |
| **Falha de segurança** | VPN inoperante, MFA desativado, disco descriptografado | Até 4 horas |
| **Comprometimento de credenciais** | Senha exposta, token comprometido | **Imediato** (máximo 30 minutos) |

### 7.2 Procedimento de relato

1. **Isolar** o dispositivo afetado (desconectar da rede se possível);
2. **Comunicar** ao Gestor SGSI via canal de incidentes (Slack #seguranca-incidentes ou e-mail seguranca@twyn.com.br);
3. **Registrar** o incidente com:
   - Data e hora da descoberta;
   - Descrição do evento;
   - Dados ou sistemas potencialmente afetados;
   - Ações já tomadas;
4. **Preservar** evidências (não apagar logs, não formatar dispositivos);
5. **Aguardar** instruções do Gestor SGSI antes de tomar ações corretivas adicionais.

### 7.3 Em caso de perda ou roubo de dispositivo

Além do procedimento geral:

1. Solicitar bloqueio remoto do dispositivo (se disponível);
2. Revogar imediatamente todas as sessões ativas (AWS, GitHub, e-mail);
3. Alterar todas as senhas armazenadas no dispositivo;
4. Registrar boletim de ocorrência policial (se aplicável);
5. Informar ao DPO/Encarregado de Dados se o dispositivo continha dados pessoais.

## 8. Monitoramento e Verificações de Conformidade

### 8.1 Verificações periódicas

| Verificação | Frequência | Responsável | Método |
|---|---|---|---|
| Conformidade de dispositivos | Trimestral | Gestor SGSI | Checklist de autoavaliação |
| Revisão de acessos AWS/GitHub | Mensal | Gestor SGSI | Auditoria de logs IAM/GitHub |
| Teste de VPN | Trimestral | Gestor SGSI | Verificação de conectividade |
| Revisão de MFA ativo | Mensal | Gestor SGSI | Relatório de autenticação |
| Treinamento de conscientização | Semestral | Gestor SGSI | Registro de participação |
| Revisão de permissões Terraform | Trimestral | Gestor SGSI | Auditoria de state files |
| Simulação de phishing | Semestral | Gestor SGSI | Teste controlado |

### 8.2 Autoavaliação do colaborador

Trimestralmente, cada colaborador deve preencher o checklist de autoavaliação (Anexo B), declarando conformidade com os requisitos deste SOP. O Gestor SGSI pode solicitar evidências (screenshots, relatórios de sistema) para validação.

### 8.3 Auditoria

O Gestor SGSI reserva-se o direito de:

- Solicitar evidências de conformidade a qualquer momento;
- Realizar verificações remotas dos requisitos de segurança;
- Solicitar relatórios de ferramentas de segurança instaladas;
- Auditar logs de acesso a sistemas corporativos.

> **Nota:** Todas as verificações respeitam a privacidade do colaborador e limitam-se aos aspectos de segurança da informação relacionados ao trabalho.

## 9. Termo de Responsabilidade e Checklist do Colaborador

### Anexo A — Termo de Responsabilidade de Trabalho Remoto

```
TERMO DE RESPONSABILIDADE — TRABALHO REMOTO SEGURO

Eu, _______________________________________________, portador(a) do
CPF nº ___.___.___-__, colaborador(a) da TWYN, declaro que:

1. Li e compreendi integralmente o SGSI-SOP-003 (Segurança no Trabalho Remoto);
2. Comprometo-me a cumprir todos os requisitos de segurança nele estabelecidos;
3. Estou ciente de que o descumprimento pode acarretar sanções disciplinares;
4. Comprometo-me a relatar imediatamente qualquer incidente de segurança;
5. Autorizo verificações de conformidade periódicas em meu ambiente de trabalho;
6. Comprometo-me a manter meu dispositivo atualizado e protegido conforme
   os requisitos da Seção 6.1;
7. Estou ciente de que dados classificados como RESTRICTED e dados biométricos
   NÃO devem ser armazenados em meus dispositivos locais;
8. Comprometo-me a utilizar exclusivamente canais de comunicação aprovados
   para assuntos profissionais;
9. Estou ciente de que o uso de e-mail pessoal para fins corporativos é proibido;
10. Reconheço que o acesso remoto pode ser revogado a qualquer momento por
    motivos de segurança.

Data: ___/___/______
Assinatura: _______________________________
Gestor Direto: ____________________________
Gestor SGSI: ______________________________
```

### Anexo B — Checklist de Autoavaliação Trimestral

| # | Item de Verificação | Sim | Não | N/A | Observação |
|---|---|---|---|---|---|
| 1 | Sistema operacional atualizado (última versão suportada) | ☐ | ☐ | ☐ | |
| 2 | Atualizações automáticas habilitadas | ☐ | ☐ | ☐ | |
| 3 | Antivírus/EDR ativo e atualizado | ☐ | ☐ | ☐ | |
| 4 | Criptografia de disco completo habilitada | ☐ | ☐ | ☐ | |
| 5 | Bloqueio automático de tela configurado (≤5 min) | ☐ | ☐ | ☐ | |
| 6 | Firewall do SO ativo | ☐ | ☐ | ☐ | |
| 7 | VPN funcional e utilizada conforme SOP | ☐ | ☐ | ☐ | |
| 8 | MFA ativo em todos os serviços corporativos | ☐ | ☐ | ☐ | |
| 9 | Gerenciador de senhas em uso | ☐ | ☐ | ☐ | |
| 10 | Senhas alteradas nos últimos 90 dias | ☐ | ☐ | ☐ | |
| 11 | Nenhum dado RESTRICTED armazenado localmente | ☐ | ☐ | ☐ | |
| 12 | Nenhum dado biométrico armazenado localmente | ☐ | ☐ | ☐ | |
| 13 | Apenas canais de comunicação aprovados em uso | ☐ | ☐ | ☐ | |
| 14 | E-mail pessoal NÃO utilizado para fins corporativos | ☐ | ☐ | ☐ | |
| 15 | Ambiente de trabalho com privacidade adequada | ☐ | ☐ | ☐ | |
| 16 | Prática de Clean Desk observada | ☐ | ☐ | ☐ | |
| 17 | Senha do roteador doméstico alterada do padrão | ☐ | ☐ | ☐ | |
| 18 | Firmware do roteador atualizado | ☐ | ☐ | ☐ | |
| 19 | Treinamento de conscientização em dia | ☐ | ☐ | ☐ | |
| 20 | Nenhum incidente de segurança não reportado | ☐ | ☐ | ☐ | |

**Colaborador:** _________________________ **Data:** ___/___/______

**Validado por (Gestor SGSI):** _________________________ **Data:** ___/___/______

## 10. Consequências do Não Cumprimento

### 10.1 Gradação de sanções

O descumprimento dos requisitos deste SOP será tratado conforme a gravidade e recorrência da infração:

| Nível | Descrição | Exemplos | Sanção |
|---|---|---|---|
| **Leve** | Descumprimento sem impacto direto à segurança | Bloqueio de tela > 5 min, atraso na autoavaliação | Advertência verbal e orientação |
| **Moderado** | Risco potencial à segurança da informação | Uso de rede pública sem VPN, atraso em atualização crítica | Advertência formal por escrito |
| **Grave** | Violação com impacto real ou potencial significativo | Armazenamento local de dados RESTRICTED, uso de e-mail pessoal para dados CONFIDENTIAL | Suspensão do acesso remoto + advertência formal |
| **Crítico** | Violação intencional ou com dano efetivo | Compartilhamento de credenciais, vazamento de dados biométricos, recusa em reportar incidente | Suspensão do acesso remoto + processo disciplinar conforme CLT |

### 10.2 Processo disciplinar

1. O Gestor SGSI registra a não conformidade;
2. O colaborador é notificado e tem direito a apresentar justificativa em até 5 dias úteis;
3. O Gestor SGSI, em conjunto com o gestor direto e RH, define a sanção aplicável;
4. A decisão é comunicada formalmente ao colaborador;
5. O registro é arquivado no prontuário de segurança do colaborador;
6. Em caso de reincidência, a sanção do nível imediatamente superior é aplicada.

### 10.3 Implicações legais

- Violações que resultem em vazamento de dados pessoais podem gerar responsabilidades nos termos da LGPD;
- A TWYN pode ser obrigada a comunicar incidentes à ANPD e aos titulares de dados;
- O colaborador pode responder civil e criminalmente por danos causados por negligência comprovada.

## 11. Registros e Evidências

### 11.1 Registros obrigatórios

| Registro | Responsável | Retenção Mínima | Local de Armazenamento |
|---|---|---|---|
| Termos de Responsabilidade assinados | Gestor SGSI | 5 anos após desligamento | Repositório SGSI |
| Checklists de autoavaliação | Gestor SGSI | 3 anos | Repositório SGSI |
| Solicitações e aprovações de trabalho remoto | Gestor SGSI | 3 anos | Repositório SGSI |
| Registros de treinamento | Gestor SGSI | 5 anos | Repositório SGSI |
| Registros de incidentes | Gestor SGSI | 5 anos | Repositório SGSI |
| Resultados de auditorias e verificações | Gestor SGSI | 3 anos | Repositório SGSI |
| Registros de não conformidade | Gestor SGSI | 5 anos | Repositório SGSI |
| Logs de acesso VPN | Gestor SGSI | 12 meses | Sistema de logs |
| Relatórios de simulação de phishing | Gestor SGSI | 3 anos | Repositório SGSI |

### 11.2 Proteção dos registros

- Todos os registros são classificados como INTERNAL ou superior;
- O acesso é restrito ao Gestor SGSI, gestores diretos (para seus subordinados) e auditores autorizados;
- Os registros devem ser protegidos contra alteração não autorizada;
- Backups devem seguir a política de backup da TWYN.

## 12. Disposições Finais

- Este SOP entra em vigor na data de sua aprovação pelo Gestor SGSI;
- Todos os colaboradores em regime remoto devem ser notificados sobre este SOP em até 10 dias úteis após sua aprovação;
- Colaboradores já em regime remoto têm prazo de 30 dias corridos para se adequar aos requisitos aqui estabelecidos;
- Dúvidas sobre este SOP devem ser direcionadas ao Gestor SGSI;
- Este SOP será revisado no mínimo anualmente ou quando houver mudanças significativas no ambiente de ameaças, na legislação aplicável ou na estrutura organizacional da TWYN.

## 13. Histórico de Revisões

| Versão | Data | Autor | Descrição da Alteração |
|---|---|---|---|
| 1.0 | 2026-06-02 | Gestor SGSI | Versão inicial do procedimento |

---

**Classificação:** INTERNAL
**Documento:** SGSI-SOP-003
**Próxima Revisão:** 12 meses após aprovação ou conforme necessidade

*Este documento é propriedade da TWYN e seu conteúdo é classificado como INTERNAL. A distribuição não autorizada é proibida.*
