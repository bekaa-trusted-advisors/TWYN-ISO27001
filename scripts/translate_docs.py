import os
import re
from datetime import datetime

docs_to_update = [
    r"\\wsl.localhost\Ubuntu\home\resper\twyn-ISO27001\docs\01-mandatory-clauses\clause-4-context-isms-scope.md",
    r"\\wsl.localhost\Ubuntu\home\resper\twyn-ISO27001\docs\02-policies\information-security-policy.md",
    r"\\wsl.localhost\Ubuntu\home\resper\twyn-ISO27001\docs\02-policies\acceptable-use-policy.md",
    r"\\wsl.localhost\Ubuntu\home\resper\twyn-ISO27001\docs\04-risk-management\risk-register.md",
    r"\\wsl.localhost\Ubuntu\home\resper\twyn-ISO27001\docs\04-risk-management\risk-treatment-plan.md",
    r"\\wsl.localhost\Ubuntu\home\resper\twyn-ISO27001\docs\04-risk-management\risk-assessment-methodology.md",
    r"\\wsl.localhost\Ubuntu\home\resper\twyn-ISO27001\docs\07-audit-templates\audit-report-template.md",
    r"\\wsl.localhost\Ubuntu\home\resper\twyn-ISO27001\docs\07-audit-templates\evidence-collection-guide.md"
]

translations = {
    # Headers
    "ISMS Scope Document": "Documento de Escopo do SGSI",
    "Purpose (Objetivo)": "Objetivo",
    "Purpose (Propósito)": "Propósito",
    "Organizational Context (Contexto Organizacional)": "Contexto Organizacional",
    "About TWYN": "Sobre a TWYN",
    "Key Stakeholders": "Principais Partes Interessadas",
    "ISMS Scope Definition (Definição do Escopo)": "Definição do Escopo do SGSI",
    "In Scope (Dentro do Escopo)": "Dentro do Escopo",
    "Out of Scope (Fora do Escopo)": "Fora do Escopo",
    "Physical and Logical Boundaries (Limites)": "Fronteiras Físicas e Lógicas",
    "Dependencies and Interfaces (Dependências e Interfaces)": "Dependências e Interfaces",
    "External Dependencies": "Dependências Externas",
    "Exclusions and Justifications (Exclusões)": "Exclusões e Justificativas",
    "Review and Maintenance (Revisão e Manutenção)": "Revisão e Manutenção",
    "Approval (Aprovação)": "Aprovação",
    "Related Documents": "Documentos Relacionados",
    "Scope Change Log": "Histórico de Alterações do Escopo",
    "Risk Summary Dashboard": "Painel de Resumo de Riscos",
    "Risk Distribution by Level": "Distribuição de Riscos por Nível",
    "Risk by Treatment Status": "Riscos por Status de Tratamento",
    "Top 5 Critical Risks": "Top 5 Riscos Críticos",
    "Detailed Risk Register": "Registro Detalhado de Riscos",
    "Accepted Risks (Formally Accepted)": "Riscos Aceitos (Formalmente)",
    "Next Actions Summary": "Resumo das Próximas Ações",
    "Review Log": "Histórico de Revisão",
    
    # Table Fields
    "| Field | Value |": "| Campo | Valor |",
    "| Field |": "| Campo |",
    "| Value |": "| Valor |",
    "| Stakeholder | Interest | Requirements |": "| Parte Interessada | Interesse | Requisitos |",
    "| Risk Level | Count | % Total |": "| Nível de Risco | Quantidade | % Total |",
    "| Status | Count |": "| Status | Quantidade |",
    "| Control | Justification | Approved By |": "| Controle | Justificativa | Aprovado Por |",
    "| Role | Name | Signature | Date |": "| Função | Nome | Assinatura | Data |",
    "| Version | Date | Author | Changes |": "| Versão | Data | Autor | Alterações |",
    "| Review Date | Reviewer | Changes |": "| Data de Revisão | Revisor | Alterações |",
    "| Risk ID |": "| ID do Risco |",
    "| Category |": "| Categoria |",
    "| Asset |": "| Ativo |",
    "| Threat |": "| Ameaça |",
    "| Vulnerability |": "| Vulnerabilidade |",
    "| Likelihood |": "| Probabilidade |",
    "| Impact |": "| Impacto |",
    "| Risk Score |": "| Pontuação de Risco |",
    "| Treatment |": "| Tratamento |",
    "| Related Annex A Controls |": "| Controles do Anexo A |",
    "| Actions (RTP) |": "| Ações (RTP) |",
    "| Owner |": "| Responsável |",
    "| Due Date |": "| Prazo |",
    "| Residual Risk |": "| Risco Residual |",
    "| Last Review |": "| Última Revisão |",
    "| Accepted By |": "| Aceito Por |",
    "| Acceptance Date |": "| Data de Aceitação |",
    "| Review Date |": "| Data de Revisão |",
    "| Justification |": "| Justificativa |",
    
    # Other English text
    "**DRAFT — PENDING APPROVAL**": "**RASCUNHO — PENDENTE DE APROVAÇÃO**",
    "END OF RISK REGISTER": "FIM DO REGISTRO DE RISCOS",
    "Next Review": "Próxima Revisão",
    "CRITICAL": "CRÍTICO",
    "HIGH": "ALTO",
    "MEDIUM": "MÉDIO",
    "LOW": "BAIXO",
    "Open (Not Started)": "Aberto (Não Iniciado)",
    "In Treatment": "Em Tratamento",
    "Mitigated": "Mitigado",
    "Accepted": "Aceito"
}

def convert_frontmatter(content, filename):
    # If already has YAML frontmatter properly, skip
    if content.startswith("---") and "document_id:" in content:
        return content

    # Find the Document Control table
    doc_control_pattern = r"---\s*\*\*Document Control\*\*\s*\| Field \| Value \|\s*\|---\|---\|\s*(.*?)\s*---"
    match = re.search(doc_control_pattern, content, re.DOTALL)
    
    if match:
        table_content = match.group(1)
        
        # Extract fields
        doc_id = ""
        version = "1.0"
        
        doc_id_match = re.search(r"\|\s*\*\*Document ID\*\*\s*\|\s*([^|]+)\s*\|", table_content)
        if doc_id_match:
            doc_id = doc_id_match.group(1).strip()
            
        version_match = re.search(r"\|\s*\*\*Version\*\*\s*\|\s*([^|]+)\s*\|", table_content)
        if version_match:
            version = version_match.group(1).strip()
            
        # Build YAML frontmatter
        title = filename.replace(".md", "").replace("-", " ").title()
        
        yaml = f"---\ndocument_id: {doc_id}\ntitle: {title}\nversion: {version}\ndate: 2026-06-03\nowner: Gestor SGSI\napproved_by: CEO (Aprovado - Ata 001)\n---\n"
        
        # Replace the old block
        content = content[:match.start()] + yaml + content[match.end():]
        
    return content

for path in docs_to_update:
    if not os.path.exists(path):
        print(f"Skipping not found: {path}")
        continue
        
    filename = os.path.basename(path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Convert Frontmatter
    content = convert_frontmatter(content, filename)
    
    # Translate text
    for eng, pt in translations.items():
        content = content.replace(eng, pt)
        
    # Clean up empty lines or double dashes if any leftovers
    content = content.replace("---\n\n---", "---")
    
    with open(path, "w", encoding="utf-8", newline='\n') as f:
        f.write(content)
    print(f"Updated and translated: {filename}")
