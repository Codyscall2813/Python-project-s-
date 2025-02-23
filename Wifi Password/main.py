import subprocess

def get_connected_wifi_name():
    try:
        data = subprocess.check_output(["netsh", "wlan", "show", "interfaces"]).decode("utf-8").split("\n")
        for line in data:
            if "SSID" in line:
                return line.split(":")[1].strip()
    except subprocess.CalledProcessError as e:
        print("Failed to retrieve Wi-Fi interface data.")
        return None

def get_wifi_password(profile_name):
    try:
        data = subprocess.check_output(["netsh", "wlan", "show", "profile", profile_name, "key=clear"]).decode("utf-8").split("\n")
        for line in data:
            if "Key Content" in line:
                return line.split(":")[1].strip()
        return "No password found"
    except subprocess.CalledProcessError as e:
        print(f"Failed to retrieve password for {profile_name}.")
        return None

def main():
    connected_wifi = get_connected_wifi_name()
    if connected_wifi:
        password = get_wifi_password(connected_wifi)
        if password:
            print(f"Connected Wi-Fi: {connected_wifi}")
            print(f"Password: {password}")
        else:
            print(f"No password found for the connected Wi-Fi: {connected_wifi}")
    else:
        print("No Wi-Fi network is currently connected.")

if __name__ == "__main__":
    main()
