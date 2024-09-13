rule ip_address_find
{
    meta:
        author = "Daryl Gatt"
        description = "Identifies any IPv4 or/and IPv6 addresses, with optional port numbers."
        date = "2024-09-13"

    strings:
        // Identify just IP addresses
        $ipv4_match = /(?:(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])\.){3}(?:25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])/
        $ipv6_match = /\b([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}\b|\b([0-9a-fA-F]{1,4}:){1,7}:\b|\b::[0-9a-fA-F]{1,4}\b/
        
        // Get range of ports
        $port_numbers = /\b(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[1-5]?[0-9]{1,4})\b/

    condition:
        ($ipv4_match or $ipv6_match) or ($ipv4_match and $port_numbers) or ($ipv6_match and $port_numbers)
}
