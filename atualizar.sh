#!/bin/bash
echo "🚀 Sincronizando documentos locais do SGSI com o GitHub..."

# Adiciona todas as modificações
git add .

# Verifica se há algo para commitar
if ! git diff-index --quiet HEAD --; then
    git commit -m "docs: atualização em lote do status do SGSI via macro"
    git push origin main
    echo "✅ Dados sincronizados! Atualize o seu Dashboard Vercel para ver as mudanças na interface."
else
    echo "ℹ️ Nenhuma alteração local encontrada. O Dashboard já está lendo a última versão."
fi
