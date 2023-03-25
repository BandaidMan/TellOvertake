import wlanapi
import time

def connect_to_network_interface(ssid, interface_guid):
    """Connects to the specified SSID on the specified network interface."""
    wlan = wlanapi.WlanApi()
    interface = wlan.get_interface(interface_guid)
    profile_xml = f"""
    <?xml version="1.0"?>
    <WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
        <name>{ssid}</name>
        <SSIDConfig>
            <SSID>
                <name>{ssid}</name>
            </SSID>
        </SSIDConfig>
        <connectionType>ESS</connectionType>
        <connectionMode>auto</connectionMode>
        <MSM>
            <security>
                <authEncryption>
                    <authentication>WPA2PSK</authentication>
                    <encryption>AES</encryption>
                    <useOneX>false</useOneX>
                </authEncryption>
                <sharedKey>
                    <keyType>passPhrase</keyType>
                    <protected>false</protected>
                    <keyMaterial>mypassword</keyMaterial>
                </sharedKey>
            </security>
        </MSM>
    </WLANProfile>
    """
    profile = interface.profile_manager.create(profile_xml)
    network = interface.network_profile_manager.connect(profile)
    print(f"Connected to {ssid} on {interface.name}.")

# GUIDs for the network interfaces you want to connect to
interface_guid_1 = "{00000000-0000-0000-0000-000000000001}"
interface_guid_2 = "{00000000-0000-0000-0000-000000000002}"

# SSIDs for the networks you want to connect to
ssid_1 = "MyNetwork1"
ssid_2 = "MyNetwork2"

# Connect to the first network interface
connect_to_network_interface(ssid_1, interface_guid_1)

# Wait for the connection to be established
time.sleep(10)

# Disconnect from the first network interface
wlan = wlanapi.WlanApi()
interface = wlan.get_interface(interface_guid_1)
interface.disconnect()

# Connect to the second network interface
connect_to_network_interface(ssid_2, interface_guid_2)

# Wait for the connection to be established
time.sleep(10)

# Disconnect from the second network interface
wlan = wlanapi.WlanApi()
interface = wlan.get_interface(interface_guid_2)
interface.disconnect()
