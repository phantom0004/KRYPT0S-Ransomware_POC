rule ip_address_find
{
    meta:
        author = "Daryl Gatt"
        description = "Identifies any IPv4 or/and IPv6 addresses, with optional port numbers."
        date = "2024-09-13"

    strings:
        // IPv4 & IPv6 Addresses
        $ipv4_address = /[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}/
        $ipv6_address = /((([0-9a-fA-F]{1,4}:){6}([0-9a-fA-F]{1,4}|:))|(([0-9a-fA-F]{1,4}:){0,5}::([0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4}))/

        // IPv4 & IPv6 Addresses with Port Numbers
        $ipv4_address_with_port = /[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}:[0-9]{1,5}/
        $ipv6_address_with_port = /((([0-9a-fA-F]{1,4}:){6}([0-9a-fA-F]{1,4}|:))|(([0-9a-fA-F]{1,4}:){0,5}::([0-9a-fA-F]{1,4}:){0,5}[0-9a-fA-F]{1,4})):[0-9]{1,5}/

    condition:
        any of them
}
