Write-Host "🚀 Sincronizando documentos locais do SGSI com o GitHub..." -ForegroundColor Cyan

# Adiciona todas as modificações
git add .

# Verifica se há algo para commitar
$hasChanges = $(git status --porcelain)
if ($hasChanges) {
    git commit -m "docs: atualização em lote do status do SGSI via macro"
    git push origin main
    Write-Host "✅ Dados sincronizados! Atualize o seu Dashboard Vercel para ver as mudanças na interface." -ForegroundColor Green
} else {
    Write-Host "ℹ️ Nenhuma alteração local encontrada. O Dashboard já está lendo a última versão." -ForegroundColor Yellow
}
