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
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"backups/{device['host']}_{timestamp}.txt"

        
