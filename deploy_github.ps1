# PowerShell GitHub 快速推送發布腳本
Write-Host "===================================================" -ForegroundColor Cyan
Write-Host " 南投國中 115 二年級隔宿露營簡報 - GitHub 發布小助手" -ForegroundColor Yellow
Write-Host "===================================================" -ForegroundColor Cyan

# 檢查是否有登入 gh
$auth = gh auth status 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "`n尚未登入 GitHub，即將啟動瀏覽器授權登入..." -ForegroundColor Yellow
    gh auth login --web -h github.com -p https
}

# 建立或推送至 GitHub Repo
$repoName = "115-nantou-camping-guide"
Write-Host "`n正在 GitHub 建立專案倉庫 [$repoName] 並推送..." -ForegroundColor Green

gh repo create $repoName --public --source=. --remote=origin --push

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n✅ 恭喜！專案已成功推送到 GitHub：" -ForegroundColor Green
    gh repo view --web
} else {
    Write-Host "`n若已有同名倉庫，嘗試直接 push..." -ForegroundColor Yellow
    git push -u origin main
}
