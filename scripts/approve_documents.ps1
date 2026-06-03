$docsDir = "..\docs"
$files = Get-ChildItem -Path $docsDir -Filter "*.md" -Recurse

$count = 0
foreach ($file in $files) {
    $content = Get-Content $file.FullName -Raw
    
    if ($content -match "approved_by: CEO \(Pendente\)") {
        # Update approval status
        $content = $content -replace "approved_by: CEO \(Pendente\)", "approved_by: CEO (Aprovado - Ata 001)"
        
        # Update date to today
        $content = $content -replace "date: \d{4}-\d{2}-\d{2}", "date: 2026-06-02"
        
        # Save file with UTF8 encoding
        Set-Content -Path $file.FullName -Value $content -Encoding UTF8
        $count++
        Write-Host "Updated file: $($file.Name)"
    }
}

Write-Host "Total files approved: $count"
