$csvFolder = "C:\Users\Public\tracks csv"
$shpFolder = "C:\Users\Public\tracks shp"
$gdalExe   = "C:\Program Files\QGIS 3.40.15\bin\ogr2ogr.exe"

# Crea cartella output se non esiste
if (-not (Test-Path $shpFolder)) {
    New-Item -ItemType Directory -Path $shpFolder | Out-Null
}

Get-ChildItem -Path $csvFolder -Filter *.csv | ForEach-Object {

    $file = $_.FullName

    # ======== SISTEMA HEADER ========
    $lines = Get-Content $file

    # Rileva separatore automaticamente
    if ($lines[0] -like "*;*") {
        $sep = ";"
    } else {
        $sep = ","
    }

    $header = $lines[0].Split($sep)

    # Rinomina prime due colonne
    $header[0] = "Easting"
    $header[1] = "Northing"

    $lines[0] = ($header -join $sep)

    # Sovrascrive CSV
    Set-Content -Path $file -Value $lines

    Write-Host "Header aggiornato:" $file

    # ======== CREA SHAPEFILE ========
    $output = Join-Path $shpFolder ($_.BaseName + ".shp")

    if ($sep -eq ";") {
        $separatorOption = "SEMICOLON"
    } else {
        $separatorOption = "COMMA"
    }

    & "$gdalExe" -f "ESRI Shapefile" $output $file `
        -oo X_POSSIBLE_NAMES=Easting `
        -oo Y_POSSIBLE_NAMES=Northing `
        -oo SEPARATOR=$separatorOption `
        -a_srs EPSG:32633 `
        -nlt POINT

    Write-Host "Creato Shapefile:" $output
}

Get-ChildItem -Path $csvFolder -Include * -File -Recurse | foreach {
    $_.Delete()
}

Write-Host "Tutti i CSV convertiti in Shapefile! & source files deleted!"