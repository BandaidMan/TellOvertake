# Importing the necessary modules
import subprocess
import os

def init_setup():
    """
    Initializes the setup by removing any existing XML files and .data file, then retrieves and 
    displays a list of available Tello drone networks and interfaces, and prompts the user to select 
    their preferred options for Tello network and interface. The selected options are then saved in 
    the .data file.
    """
    if os.path.isfile("Data/.data"):
        # Remove the .data file if it already exists
        os.remove("Data/.data")

    xml_clear = os.listdir("Data/XML/")
    for item in xml_clear:
        if item.endswith(".xml"):
            # Remove any existing XML files
            os.remove(os.path.join("Data/XML/", item))

    wifi_interfaces = []
    raw_found_networks = []
    wifi_networks = []

    # Retrieve the wifi interfaces using the 'netsh wlan show interfaces' command
    output = subprocess.check_output("netsh wlan show interfaces")
    # Retrieve the available wifi networks using the 'netsh wlan show networks' command
    output2 = subprocess.check_output("netsh wlan show networks")

    # Parse the output to extract the wifi interface names
    for line in output.splitlines():
        if "Name" in str(line): 
            wifi_interfaces.append(line.decode("utf-8").strip().split(": ")[1])

    # Parse the output to extract the available wifi networks
    for line in output2.splitlines():
        raw_found_networks.append(line.decode("utf-8"))

    # Remove the first two elements from the raw_found_networks list
    for x in range(0,2):
        raw_found_networks.pop(x)

    # Remove any empty lines and lines containing irrelevant information from the raw_found_networks list
    new_list = []
    for line in raw_found_networks:
        if line.strip() != '' and 'name' not in line and 'currently visible' not in line:
            new_list.append(line)
    raw_found_networks = new_list

    # Retrieve only the network names from the raw_found_networks list
    raw_found_networks = raw_found_networks[0::2]

    # Combine the network names and their respective signal strengths into a list
    for index in range(0, len(raw_found_networks), 2):
        tmp_list = [raw_found_networks[index], raw_found_networks[index+1]]
        wifi_networks.append(tmp_list)

    # Parse the wifi network list to extract the names and signal strengths of the Tello networks
    for line in wifi_networks:
        line[0] = (line[0].split()[len(line[0].split())-1])
        line[1] = (line[1].strip()[26:30])

    tello_networks = []
    for line in wifi_networks: # Get all the TELLO Networks and add them to the tello_networks list
        if "TELLO" in line[0]:
            tello_networks.append(line)

    # Remove any duplicate Tello networks from the tello_networks list
    tmp_list = []
    for item in tello_networks:
        if item not in tmp_list:
            tmp_list.append(item)
    tello_networks = tmp_list

    # Display the list of available Tello networks and prompt the user to select their preferred option
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
    # Read data from file
    data = read_data()
    # Get the network list from the read data
    networks = data[2]
    # Loop through each network in the list
    for item in networks:
        # Check if the network is open
        if(item[1] == "Open"):
            # Set the path of the xml file
            path = 'Data/XML/' + item[0] + '.xml'
            # Check if the xml file already exists
            if os.path.isfile(path):
                # Print a message indicating that the xml file already exists
                print("XML Exists -- Moving on")
            else:
                # Open the xml template file
                unsecured_temp_file = open('Data/XML/template/profile-xml-unsecured-template.xml', 'r')
                # Read the lines from the xml template file
                xml_lines = unsecured_temp_file.readlines()
                # Replace the network name in the xml template
                xml_lines[2] = "<name>" + item[0] + "</name>\n"
                xml_lines[5] = "\t\t\t<name>" + item[0] + "</name>\n"
                # Print the updated xml template
                print(xml_lines[2])
                # Create the xml file
                xml_file_done = open(path, 'w')
                xml_file_done.writelines(xml_lines)
                xml_file_done.close()
                # Create the command to add the xml profile to the wifi interface
                command = 'netsh wlan add profile filename=\"' + path +  '\" interface=\"' + data[1] + '\"'
                # Print the command to add the xml profile to the wifi interface
                print(command)
                # Add the xml profile to the wifi interface
                os.system(command)
        else:
            # Print a message indicating that the network is not open
            print("At this time we are unable to attack secured drones!")

def read_data():
    # create an empty list to store the data read from the file
    data = []
    
    # open the file in read mode
    with open("Data/.data", "r") as datafile:
        # read all lines from the file and store them in the variable 'lines'
        lines = datafile.readlines()
        
        # add the first line (Tello network name) to the 'data' list, removing any leading/trailing whitespaces
        data.append(lines[0].strip())
        
        # add the second line (WiFi interface name) to the 'data' list, removing any leading/trailing whitespaces
        data.append(lines[1].strip())
        
        # split the third line (Tello networks and their security status) by '|' and remove the last character (which is '\n')
        temp_list = lines[2][:-1].split('|')
        tmp_list = []
        
        # loop through the Tello networks and their security status
        for drones in temp_list:
            # split each Tello network and its security status by ',' and add them to 'tmp_list'
            working = drones.split(',')
            tmp_list.append(working)
        
        # add the list of Tello networks and their security status to the 'data' list
        data.append(tmp_list)
    
    # return the 'data' list
    return data

init_setup()
generate_XML()