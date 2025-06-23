import json 
import os
from datetime import datetime
from netmiko import ConnectHandler, NetMikoTimeoutException, NetMikoAuthenticationException


# Load the devices inventort
with open("inventory.json") as f:
    devices = json.load(f)


# Create a folder for backups
os.makedirs("backups", exist_ok=True)

for device in devices:
    try:
        connection = ConnectHandler(**device)
        output = connection.send_command("show running-config")
        timestamp = datetime.now().strftime("%Y%M%d_%H%M%S")
        filename = f"backups/{device['host']}_backup_{timestamp}.txt"

        with open(filename, "w") as file:
            file.write(output)

            print(f"Backup saved: {filename}")
            connection.disconnect()


    except NetMikoTimeoutException:
        print(f"Connection timed out for device: {device['host']}")
    except NetMikoAuthenticationException:
        print(f"Authentication failed for device: {device['host']}")
    except Exception as e:
        print(f"Other error with device {device['host']}: {e}")


        
