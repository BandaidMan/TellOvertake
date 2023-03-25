#importing the necessary modules
import subprocess

#creating a blank list to store the output
wifi_interfaces = []

#running the command to get the wifi interfaces
output = subprocess.check_output(["iwconfig"])

#looping through the output and appending the interface names to the list
for line in output.splitlines():
    if "IEEE" in line:
        wifi_interfaces.append(line.split()[0])

#printing out the list
print(wifi_interfaces)