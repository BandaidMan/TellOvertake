import os

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

def reconnect():
    data = read_data()
    network = data[0]
    command = 'netsh wlan disconnect interface=\"' + data[1] + '\"';
    os.system(command)
    command = 'netsh wlan connect name=\"' + network + '\" interface=\"' + data[1] + '\"'
    print(command)
    os.system(command)

reconnect()