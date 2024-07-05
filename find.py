import mac_vendor_lookup

def get_mac_info(mac_address):
    mac_vendor_lookup.MacLookup().update_vendors()  # Update the local vendor list
    vendor = mac_vendor_lookup.MacLookup().lookup(mac_address)
    return vendor

mac_address = "FA96BDE31FF6"  # Replace with the MAC address you want to look up
info = get_mac_info(mac_address)
print(info)
