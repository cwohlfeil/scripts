Import-Module BitsTransfer

$etc = "C:\Windows\System32\drivers\etc\hosts"
$hosts = "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling/hosts"
# Paranoid version: http://sbc.io/hosts/alternates/fakenews-gambling-porn-social/hosts
#$level1 = http://list.iblocklist.com/?list=ydxerpxkpcfqjaybcssw&fileformat=p2p&archiveformat=zip
#$level2 = http://list.iblocklist.com/?list=gyisgnzbhppbvsphucsw&fileformat=p2p&archiveformat=zip
Start-BitsTransfer -Source $hosts -Destination .\hosts
Copy-Item .\hosts -Destination $etc