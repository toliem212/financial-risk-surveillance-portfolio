$ErrorActionPreference = "Stop"

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    throw "Máy chưa có Git."
}

python .\scripts\check_public_repo.py

if (-not (Test-Path ".git")) {
    git init
}

git branch -M main
git add .
git commit -m "Publish sanitized financial-risk-surveillance portfolio"

$remote = Read-Host "Dán URL repo PUBLIC GitHub HTTPS"
if ([string]::IsNullOrWhiteSpace($remote)) {
    throw "Chưa có URL repo GitHub."
}

$existing = git remote get-url origin 2>$null
if ($LASTEXITCODE -eq 0 -and $existing) {
    git remote set-url origin $remote
} else {
    git remote add origin $remote
}

git push -u origin main
