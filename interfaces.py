#importing the necessary modules
import subprocess
import os

#creating a blank list to store the output
def init_setup():
    if os.path.isfile("Data/.data"):
        os.remove("Data/.data")
    xml_clear = os.listdir("Data/XML/")
    for item in xml_clear:
        if item.endswith(".xml"):
            os.remove(os.path.join("Data/XML/", item))


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
        line[0] = (line[0].split()[len(line[0].split())-1])
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
        outfile.write(wifi_interfaces[int(option)] + "\n")
    
    data_line = ""
    for x in tello_networks:
        data_line = data_line + x[0] + "," + x[1] + "|"
    with open("Data/.data", "a") as outfile:
            outfile.write(data_line)

def generate_XML():
    data = read_data()
    networks = data[2]
    for item in networks:
        if(item[1] == "Open"):
            path = 'Data/XML/' + item[0] + '.xml'
            if os.path.isfile(path):
                print("XML Exists -- Moving on")
            else:
                unsecured_temp_file = open('Data/XML/template/profile-xml-unsecured-template.xml', 'r')
                xml_lines = unsecured_temp_file.readlines()
                xml_lines[2] = "<name>" + item[0] + "</name>\n"
                xml_lines[5] = "\t\t\t<name>" + item[0] + "</name>\n"
                print(xml_lines[2])
                xml_file_done = open(path, 'w')
                xml_file_done.writelines(xml_lines)
                xml_file_done.close()
                command = 'netsh wlan add profile filename=\"' + path +  '\" interface=\"' + data[1] + '\"'
                print(command)
                os.system(command)
        else:
            print("At this time we are unable to attack secured drones!")

        


def read_data():
    data = []
    with open("Data/.data", "r") as datafile:
        lines = datafile.readlines()
        data.append(lines[0].strip())
        data.append(lines[1].strip())
        temp_list = lines[2][:-1].split('|')
        tmp_list = []
        for drones in temp_list:
            working = drones.split(',')
            tmp_list.append(working)
        data.append(tmp_list)
    return data

init_setup()
generate_XML()