# RowdyHacks-2023
### Sky Pirates - TellOvertake

## Introduction

TellOvertake is a drone hijacking program designed for Tello drones. 

## Project Information

### Installation
After downloading the git repository, and installing all necessary dependants just run the manage.py script.

### Description

This project is a proof-of-concept demonstration of hijacking a drone and controlling it with an Xbox controller. The goal is to highlight the potential security vulnerabilities that exist in drones and the importance of addressing them.

The project consists of two main components: the drone hijacking software and the Xbox controller interface. The drone hijacking software runs on a laptop and uses a wireless network to connect to the drone. Once connected, the software takes over the control of the drone from the original user. The software is designed to work with the DJI Tello drone and may not be compatible with other models.

The Xbox controller interface is used to control the hijacked drone. The interface is implemented using the pygames library, which allows us to read the inputs from the controller and send commands to the drone. The Xbox controller can be connected to the laptop through any USB Type A port.

To use this project, you will need a drone that is compatible with the hijacking software, an Xbox controller or keyboard, and a laptop. The project is intended for educational and research purposes only and should not be used for any illegal or malicious activities.


### Project Goals

The main goals of this project are:

* To demonstrate the potential security vulnerabilities that exist in drones and the importance of addressing them.
* To raise awareness about the risks of drone hijacking and the potential harm that can be caused by a hijacked drone.

### Technologies
* Python 3.8
* DJITelloPy
* Pygame

### Future Expansions
* To deauthenticate users at time of connection to the Tello Wifi to disable all access from the user to the device
* To add functionality using aircrack-ng and airdump-ng to break the WPA2-Personal encryption on the device.
* Add functionality to add password when requested to device to keep users from attampting to reconnect while maintaining control.
* Include Linux functionality

### Liability
* We are not authorized for any misuse of this software. The software should only be used on authorized devices and with the permission of device owners. We do not condone malicous activity or any malicous actions done with this software.

## Group Information
Aditya Dindi - BBA Cybersecurity - Sophomore

Aidan Kollar - BS Computer Science - Sophomore

Scott Roelker - BS Computer Engineering - Sophomore

Xander Newlun - BBA Cybersecurity - Junior
