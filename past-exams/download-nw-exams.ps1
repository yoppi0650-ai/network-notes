$ErrorActionPreference = "Stop"

$years = @(
    @{ Era = "R7";  Year = 2025; Page = "2025r07" },
    @{ Era = "R6";  Year = 2024; Page = "2024r06" },
    @{ Era = "R5";  Year = 2023; Page = "2023r05" },
    @{ Era = "R4";  Year = 2022; Page = "2022r04" },
    @{ Era = "R3";  Year = 2021; Page = "2021r03" },
    @{ Era = "R1";  Year = 2019; Page = "2019h31" },
    @{ Era = "H30"; Year = 2018; Page = "2018h30" },
    @{ Era = "H29"; Year = 2017; Page = "2017h29" },
    @{ Era = "H28"; Year = 2016; Page = "2016h28" },
    @{ Era = "H27"; Year = 2015; Page = "2015h27" },
    @{ Era = "H26"; Year = 2014; Page = "2014h26" },
    @{ Era = "H25"; Year = 2013; Page = "2013h25" },
    @{ Era = "H24"; Year = 2012; Page = "2012h24" },
    @{ Era = "H23"; Year = 2011; Page = "2011h23" },
    @{ Era = "H22"; Year = 2010; Page = "2010h22" },
    @{ Era = "H21"; Year = 2009; Page = "2009h21" }
)

$outputDir = Join-Path $PWD "network-specialist-past-exams"
New-Item -ItemType Directory -Force -Path $outputDir | Out-Null

function Get-PdfHrefs {
    param([string]$Html)

    $pattern = 'href="([^"]+\.pdf)"'
    $matches = [regex]::Matches($Html, $pattern)

    $result = @()
    foreach ($m in $matches) {
        $result += $m.Groups[1].Value
    }

    return $result
}

function Find-HrefByFileName {
    param(
        [string[]]$Hrefs,
        [string]$FileName
    )

    foreach ($href in $Hrefs) {
        if ($href -like "*$FileName") {
            return $href
        }
    }

    return $null
}

function Save-Pdf {
    param(
        [string]$PageUrl,
        [string[]]$Hrefs,
        [string]$SourceFileName,
        [string]$OutputFileName
    )

    $href = Find-HrefByFileName -Hrefs $Hrefs -FileName $SourceFileName

    if (-not $href) {
        Write-Warning "NOT FOUND: $SourceFileName"
        return
    }

    $outputPath = Join-Path $outputDir $OutputFileName

    if (Test-Path $outputPath) {
        Write-Host "SKIP $OutputFileName"
        return
    }

    $baseUri = [System.Uri]$PageUrl
    $pdfUri = [System.Uri]::new($baseUri, $href)

    Invoke-WebRequest -Uri $pdfUri.AbsoluteUri -OutFile $outputPath
    Write-Host "OK   $OutputFileName"
}

foreach ($y in $years) {
    Write-Host ""
    Write-Host "=== $($y.Era) / $($y.Year) ==="

    $pageUrl = "https://www.ipa.go.jp/shiken/mondai-kaiotu/$($y.Page).html"

    try {
        $response = Invoke-WebRequest -Uri $pageUrl
    }
    catch {
        Write-Warning "FAILED TO OPEN: $pageUrl"
        continue
    }

    $hrefs = Get-PdfHrefs -Html $response.Content

    $nwAm2QsHref = $null
    foreach ($href in $hrefs) {
        if ($href -match '_nw_am2_qs\.pdf$') {
            $nwAm2QsHref = $href
            break
        }
    }

    if (-not $nwAm2QsHref) {
        Write-Warning "NW AM2 source not found on: $pageUrl"
        continue
    }

    $prefixMatch = [regex]::Match($nwAm2QsHref, '([^/]+)_nw_am2_qs\.pdf$')
    if (-not $prefixMatch.Success) {
        Write-Warning "Could not determine exam prefix: $nwAm2QsHref"
        continue
    }

    $prefix = $prefixMatch.Groups[1].Value
    $baseName = "$($y.Era)-$($y.Year)"

    $targets = @(
        @{ Source = "${prefix}_koudo_am1_qs.pdf";  Output = "${baseName}-AM1-problems.pdf" },
        @{ Source = "${prefix}_koudo_am1_ans.pdf"; Output = "${baseName}-AM1-solutions.pdf" },

        @{ Source = "${prefix}_nw_am2_qs.pdf";      Output = "${baseName}-AM2-problems.pdf" },
        @{ Source = "${prefix}_nw_am2_ans.pdf";     Output = "${baseName}-AM2-solutions.pdf" },

        @{ Source = "${prefix}_nw_pm1_qs.pdf";      Output = "${baseName}-PM1-problems.pdf" },
        @{ Source = "${prefix}_nw_pm1_ans.pdf";     Output = "${baseName}-PM1-solutions.pdf" },
        @{ Source = "${prefix}_nw_pm1_cmnt.pdf";    Output = "${baseName}-PM1-grading-comments.pdf" },

        @{ Source = "${prefix}_nw_pm2_qs.pdf";      Output = "${baseName}-PM2-problems.pdf" },
        @{ Source = "${prefix}_nw_pm2_ans.pdf";     Output = "${baseName}-PM2-solutions.pdf" },
        @{ Source = "${prefix}_nw_pm2_cmnt.pdf";    Output = "${baseName}-PM2-grading-comments.pdf" }
    )

    foreach ($target in $targets) {
        try {
            Save-Pdf `
                -PageUrl $pageUrl `
                -Hrefs $hrefs `
                -SourceFileName $target.Source `
                -OutputFileName $target.Output
        }
        catch {
            Write-Warning "FAILED: $($target.Output) : $($_.Exception.Message)"
        }
    }
}

Write-Host ""
Write-Host "DONE"
Write-Host "Output: $outputDir"
