#importing the necessary modules
import subprocess
import os

#creating a blank list to store the output
def init_setup():
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

    for line in output.splitlines():
        if "Name" in str(line): 
            wifi_interfaces.append(line.decode("utf-8").strip().split(": ")[1])

    for line in output2.splitlines():
        #print(line.decode("utf-8"))
        wifi_interfaces2.append(line.decode("utf-8"))

    for x in range(0,2):
        wifi_interfaces2.pop(x)

       #wifi_interfaces2.append(line.decode("utf-8").strip().split(": ")[1])
    new_list = []
    for line in wifi_interfaces2:
        if line.strip() != '' and 'name' not in line and 'currently visible' not in line:
            new_list.append(line)
            
    wifi_interfaces2 = new_list

           

    #for line in wifi_interfaces2:


    wifi_interfaces2 = wifi_interfaces2[0::2]



    for index in range(0, len(wifi_interfaces2), 2):
        tmp_list = [wifi_interfaces2[index], wifi_interfaces2[index+1]]
        wifi_networks.append(tmp_list)

    for line in wifi_networks:
        
        line[0] = (line[0].split()[3])
        line[1] = (line[1].strip()[26:30])

    tello_networks = []
    for line in wifi_networks: #Get all the TELLO Networks and add them to the tello_networks list
        if "TELLO" in line[0]:
            tello_networks.append(line)

    tmp_list = []
    for item in tello_networks:
        if item not in tmp_list:
            tmp_list.append(item)

    tello_networks = tmp_list
    tello_networks.append(['TELLO-AC2C9F', 'Open'])
    tello_networks.append(['TELLO', 'Open'])
    print(tello_networks)
    print(len(tello_networks))

    for x in range(0, len(tello_networks)):
        print("(" + str(x) + ")", tello_networks[x])
    option = input("Which Tello do you prefer?: ")
    with open("Data/.data", "w") as outfile:
        outfile.write(tello_networks[x][0] + "\n")

    for x in range(0, len(wifi_interfaces)):
        print("(" + str(x) + ")", wifi_interfaces[x])
        option = input("What interface do you prefer?: ")
        with open("Data/.data", "a") as outfile:
            outfile.write(wifi_interfaces[x] + "\n")
    
    data_line = ""
    for x in tello_networks:
        data_line = data_line + x[0] + "," + x[1] + "|"
    with open("Data/.data", "a") as outfile:
            outfile.write(data_line)
#print(wifi_networks)
#save_input_in_file()
init_setup()