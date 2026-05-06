$txtFolder   = "C:\Users\Public\tracks"
$csvFolder   = "C:\Users\Public\tracks csv"
$shpFolder   = "C:\Users\Public\tracks shp"
$gdalExe     = "C:\Program Files\QGIS 3.40.15\bin\ogr2ogr.exe"

# Crea cartelle di output se non esistono
foreach ($folder in @($csvFolder, $shpFolder)) {
    if (-not (Test-Path $folder)) {
        New-Item -ItemType Directory -Path $folder | Out-Null
    }
}

# ======== Converti TXT in CSV ========
Get-ChildItem -Path $txtFolder -Filter *.txt | ForEach-Object {
    $txtFile = $_.FullName
    $csvFile = Join-Path $csvFolder ($_.BaseName + ".csv")

    $csv = Import-Csv -Path $txtFile -Header Col1,Col2,Col3,Col4,Col5,Col6 | Select-Object -Skip 1
    $csvFiltered = $csv | Select-Object @{Name="Easting";Expression={$_.Col3}}, @{Name="Northing";Expression={$_.Col4}}
    $csvFiltered | Export-Csv -Path $csvFile -NoTypeInformation

    Write-Host "? Convertito TXT ? CSV:" $txtFile
}

# ======== Converti CSV in Shapefile ========
Get-ChildItem -Path $csvFolder -Filter *.csv | ForEach-Object {
    $input  = $_.FullName
    $output = Join-Path $shpFolder ($_.BaseName + ".shp")

    & "$gdalExe" -f "ESRI Shapefile" $output $input `
        -oo X_POSSIBLE_NAMES=Easting `
        -oo Y_POSSIBLE_NAMES=Northing `
        -oo SEPARATOR=COMMA `
        -a_srs EPSG:32633

    Write-Host "? Creato Shapefile:" $output
}

Get-ChildItem -Path $txtFolder -Include * -File -Recurse | foreach {
    $_.Delete()
}
Get-ChildItem -Path $csvFolder -Include * -File -Recurse | foreach {
    $_.Delete()
}

Write-Host "?? Tutti i TXT convertiti in CSV e tutti i CSV in Shapefile! & source files deleted!"