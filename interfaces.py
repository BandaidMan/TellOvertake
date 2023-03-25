#importing the necessary modules
import subprocess
import os

#creating a blank list to store the output
wifi_interfaces = []
wifi_interfaces2 = []
wifi_networks = []

#running the command to get the wifi interfaces
#output = subprocess.check_output(["ipconfig"])
#output = subprocess.check_output(["netsh wlan show interfaces"])
output = subprocess.check_output("netsh wlan show interfaces")
output2 = subprocess.check_output("netsh wlan show networks")
#print(repr(output))
#print(output)
'''
with open("output.txt", "w") as outfile:
    outfile.write(str(output))
'''

for line in output.splitlines():
    if "Name" in str(line): 
        wifi_interfaces.append(line.decode("utf-8").strip().split(": ")[1])

for line in output2.splitlines():
    #print(line.decode("utf-8"))
    wifi_interfaces2.append(line.decode("utf-8"))

for x in range(0,2):
    wifi_interfaces2.pop(x)

   #wifi_interfaces2.append(line.decode("utf-8").strip().split(": ")[1])

for line in wifi_interfaces2:
    if line == '':
        wifi_interfaces2.remove(line)
    if "Interface name" in str(line):
        wifi_interfaces2.remove(line)

wifi_interfaces2 = wifi_interfaces2[0::2]
wifi_interfaces2 = wifi_interfaces2[ : -1]
for index in range(0, len(wifi_interfaces2), 2):
    tmp_list = [wifi_interfaces2[index], wifi_interfaces2[index+1]]
    wifi_networks.append(tmp_list)

print(wifi_networks)

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
#print(wifi_interfaces2[4], wifi_interfaces2[6])
#print(wifi_interfaces[0])