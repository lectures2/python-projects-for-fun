import socket

def get_network_info():
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = get_mac()

    return ip_address, mac_address

def get_mac():
    try:
        # Replace 'eth0' with the appropriate network interface name
        with open('/sys/class/net/eth0/address') as file:
            mac_address = file.read().strip()

        return mac_address
    except FileNotFoundError:
        return None

# Retrieve the IP address and MAC address
ip_address, mac_address = get_network_info()

# Display the network information
if ip_address:
    print(f"IP Address: {ip_address}")
else:
    print("Failed to retrieve IP address.")

if mac_address:
    print(f"MAC Address: {mac_address}")
else:
    print("Failed to retrieve MAC address.")
