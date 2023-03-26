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

def switch_network():
    data = read_data()
    curr_network = data[0]
    networks = data[2]
    interface = data[1]
    if len(networks) == 1:
        os.system("py reconnect.py")
    else:
        curr_index = 0
        network_length = len(networks)
        for index in range(0, network_length):
            if networks[index] == curr_network:
                curr_index = 0

        curr_index = curr_index + 1
        if(curr_index >= len(networks)):
            curr_index = 0
    new_network = networks[curr_index]
    data[0] = new_network
    os.remove("Data/.data")
    with open("Data/.data", "w") as datafile:
        datafile.writelines(data)
        datafile.close()
        os.system('py reconnect.py')