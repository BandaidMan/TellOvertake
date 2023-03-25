#importing the necessary modules
import subprocess

#creating a blank list to store the output
wifi_interfaces = []

#running the command to get the wifi interfaces
output = subprocess.check_output(["ipconfig"])
#print(output)

'''
for line in output.splitlines():
    print(line.decode("utf-8"))
'''

#looping through the output and appending the interface names to the list
for line in output.splitlines():
    if "Ethernet" in line.decode("utf-8"):
        wifi_interfaces.append(line.decode("utf-8"))

#printing out the list
print(wifi_interfaces)
