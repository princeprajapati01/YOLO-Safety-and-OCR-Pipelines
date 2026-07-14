<# PowerShell helper to run the suggested git mv commands. #>
Write-Host "Running suggested git mv commands..." -ForegroundColor Cyan

$mappings = @(
    @{old='adv_model'; new='models/adv_model'},
    @{old='basic_01'; new='experiments/basic_01'},
    @{old='construction_main'; new='apps/construction_main'},
    @{old='helmetdetection'; new='projects/helmet_detection'},
    @{old='opencv_code'; new='tools/opencv_code'},
    @{old='datasets'; new='datasets/raw'},
    @{old='train'; new='datasets/train'},
    @{old='valid'; new='datasets/valid'}
)

foreach ($m in $mappings) {
    $old = $m.old
    $new = $m.new
    if (-Not (Test-Path -Path $old)) {
        Write-Host "Skipping: source not found -> $old" -ForegroundColor Yellow
        continue
    }
    $newDir = Split-Path $new -Parent
    if ($newDir -and -Not (Test-Path -Path $newDir)) {
        Write-Host "Creating parent directory $newDir" -ForegroundColor Green
        New-Item -ItemType Directory -Path $newDir | Out-Null
    }
    Write-Host "git mv '$old' '$new'" -ForegroundColor Magenta
    git mv $old $new
    if ($LASTEXITCODE -ne 0) {
        Write-Host "git mv failed for $old -> $new" -ForegroundColor Red
    }
}

Write-Host "Done. Review `git status` and commit changes." -ForegroundColor Cyan
