param (
    [boolean]$ToDhcp = $true,
    [string]$IP = "192.168.1.101",
    [integer]$MaskBits = 24,
    [string]$Gateway = "192.168.1.1",
    [string]$Dns = "8.8.8.8",
    [string]$IPType = "IPv4",
    [string]$Adapter = (Get-NetAdapter | ? {$_.Name -eq "Wi-Fi"})
 )

# Retrieve the network adapter that you want to configure


# Remove any existing IP, gateway from our ipv4 adapter
if (($adapter | Get-NetIPConfiguration).IPv4Address.IPAddress) {
    $adapter | Remove-NetIPAddress -AddressFamily $IPType -Confirm:$false
}

if (($adapter | Get-NetIPConfiguration).Ipv4DefaultGateway) {
    $adapter | Remove-NetRoute -AddressFamily $IPType -Confirm:$false
}

# Configure the IP address and default gateway
$adapter | New-NetIPAddress `
    -AddressFamily $IPType `
    -IPAddress $IP `
    -PrefixLength $MaskBits `
    -DefaultGateway $Gateway

# Configure the DNS client server IP addresses
$adapter | Set-DnsClientServerAddress -ServerAddresses $DNS


if ($interface.Dhcp -eq "Disabled") {
    # Remove existing gateway
    if (($interface | Get-NetIPConfiguration).Ipv4DefaultGateway) {
        $interface | Remove-NetRoute -Confirm:$false
    }

    # Enable DHCP
    $interface | Set-NetIPInterface -DHCP Enabled

    # Configure the DNS Servers automatically
    $interface | Set-DnsClientServerAddress -ResetServerAddresses
}