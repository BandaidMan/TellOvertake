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

    print(tello_networks)

#print(wifi_networks)

#printing out the list
#print(wifi_interfaces2[4], wifi_interfaces2[6])
#print(wifi_interfaces[0])


def generate_XML():
    ''''
    Function generates the XML Files necessary for python to
    connect the user to the tello drones.

    It uses the unsecured template for Open security, and the
    secured template for the WPA2-Personal security
    '''
    test = [["Tello-42441", "Open"], "Tello-51883", "WPA2-Personal"]
    for item in test:
        if(item[1] == "Open"):
            path = 'Data/XML/' + item[0] + '.xml'
            if os.path.isfile(path):
                print("XML Exists -- Moving on")
            else:
                unsecured_temp_file = open('Data/XML/profile-xml-unsecured-template.xml', 'r')
                xml_lines = unsecured_temp_file.readlines()

                for line in xml_lines:
                    if "NEED_NAME" in line:
                        line.replace("NEED_NAME", item[0])
                xml_file_done = open(path, 'w')
                xml_file_done.writelines(xml_lines)
                xml_file_done.close()


generate_XML()