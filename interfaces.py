#importing the necessary modules
import subprocess
import os

#creating a blank list to store the output
wifi_interfaces = []

#running the command to get the wifi interfaces
#output = subprocess.check_output(["ipconfig"])
#output = subprocess.check_output(["netsh wlan show interfaces"])
output = subprocess.check_output("netsh wlan show interfaces")
#print(repr(output))
#print(output)
with open("output.txt", "w") as outfile:
    outfile.write(str(output))



for line in output.splitlines():
    if "Name" in str(line): 
        wifi_interfaces.append(line.decode("utf-8").strip().split(": ")[1])

'''
for line in output.splitlines():
    if "Name" in line: 
        wifi_interfaces.append(line)
'''
'''
#looping through the output and appending the interface names to the list
for line in output.splitlines():
    if "Ethernet" in line.decode("utf-8"):
        wifi_interfaces.append(line.decode("utf-8"))
'''

#printing out the list
print(wifi_interfaces)
#print(wifi_interfaces[0])