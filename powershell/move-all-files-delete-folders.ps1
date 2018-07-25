Get-ChildItem -Path source -Recurse -File | Move-Item -Destination dest
Get-ChildItem -Path source -Recurse -Directory | Remove-Item -Recurse