$ErrorActionPreference = 'Stop'
$exampleRoot = Join-Path $PSScriptRoot 'examples'
$buildRoot = Join-Path $env:TEMP 'codex-cpp-notes-20261001'
New-Item -ItemType Directory -Path $buildRoot -Force | Out-Null
$failures = @()
$compiled = 0
$ran = 0
$lf = [char]10
$expected = @{
    '01_hello' = @('Hello World!')
    '03_constants' = @('80 5')
    '04_conditions' = @('Hero alive','B','O 5 7')
    '05_switch' = @('Latte')
    '06_flags' = @('1','0')
    '08_functions' = @('15','5','4')
    '09_recursion' = @('120 55 55')
    '10_scope' = @('1 2 100')
    '11_array_pointer' = @('10 20 30 ','30','11 20 30 ')
    '12_reference' = @('80','300 300')
    '13_board' = @('10 20 30 ','40 50 60 ','60')
    '14_string' = @('3','Kim','3')
    '16_find' = @('2','-1')
    '17_struct_enum' = @('Kim 85','1')
    '18_class' = @('Warrior 70')
    '19_lifetime' = @('0','2','0')
    '20_dynamic' = @('10 20 30 ')
    '21_polymorphism' = @('Fireball','Heal')
    '22_cast' = @('Sword attack','1','10')
    '24_list' = @('99 1 3 5 ')
    '25_template' = @('30','4','Sword')
    '26_operator' = @('1')
    '27_baseball' = @('1S 2B')
    '28_diagonal' = @('1 1')
    '29_singleton' = @('Game starts')
}
Get-ChildItem -LiteralPath $exampleRoot -Filter '*.cpp' | ForEach-Object {
    $sourceFile = $_
    $exePath = Join-Path $buildRoot ($sourceFile.BaseName + '.exe')
    $objPath = Join-Path $buildRoot ($sourceFile.BaseName + '.obj')
    $compileLog = & cl.exe /nologo /std:c++17 /EHsc /utf-8 /W4 "/Fe:$exePath" "/Fo:$objPath" $sourceFile.FullName 2>&1
    if ($LASTEXITCODE -ne 0) {
        $failures += $sourceFile.Name
        Write-Output $compileLog
        return
    }
    $compiled++
    if ($sourceFile.BaseName -eq '15_getline') {
        $startInfo = New-Object System.Diagnostics.ProcessStartInfo
        $startInfo.FileName = $exePath
        $startInfo.UseShellExecute = $false
        $startInfo.CreateNoWindow = $true
        $startInfo.RedirectStandardInput = $true
        $startInfo.RedirectStandardOutput = $true
        $sampleProcess = [System.Diagnostics.Process]::Start($startInfo)
        $sampleProcess.StandardInput.WriteLine('10')
        $sampleProcess.StandardInput.WriteLine('hello world')
        $sampleProcess.StandardInput.Close()
        $actual = $sampleProcess.StandardOutput.ReadToEnd()
        $sampleProcess.WaitForExit()
        if ($sampleProcess.ExitCode -ne 0) { throw 'getline execution failed' }
        $sampleProcess.Dispose()
        if ($actual.Trim() -ne '10: hello world') { throw 'getline output mismatch' }
    } else {
        $actual = (& $exePath) -join $lf
        if ($LASTEXITCODE -ne 0) { throw ('Execution failed: ' + $sourceFile.Name) }
        if ($expected.ContainsKey($sourceFile.BaseName)) {
            $expectedText = $expected[$sourceFile.BaseName] -join $lf
            if ($actual.Trim() -ne $expectedText.Trim()) {
                throw ('Output mismatch: ' + $sourceFile.Name + ' actual=' + $actual)
            }
        }
    }
    $ran++
}
if ($failures.Count -gt 0) { throw ('Compile failures: ' + ($failures -join ', ')) }
Write-Output ("Verified: {0} compiled, {1} ran; expected output comparisons passed." -f $compiled, $ran)
