# library to make the banner
import pyfiglet
# library for handling exceptions
import sys
# lib to do all of our port and internet stuff
import socket
# to print the date and time in the banner
from datetime import datetime

# to create the banner
ascii_banner = pyfiglet.figlet_format('PORT SCANNER')
print(ascii_banner)

# Defining a target

    # create variable to create input for the user to put target ip address
    # translate hostname to IPv4
target = input(str("Target IP::   "))


# Add Banner
print("-" * 50)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 50)

try:

    # to detect all the open ports
    for port in range(1, 65535):  # the valid port range for all systems
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create variable and turn it to socket
        socket.setdefaulttimeout(0.7)  # how much time before skipping the port and try the next one
        # returns an error indicator to find an open port ,create variable that the results equal targets , socket ,
        # port and if the result of that socket is 0 which mean successful connection it prints a string that says
        # port this port is open then after that close the socket and move to the next port
        result = s.connect_ex((target, port))
        if result == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\n Exiting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!!")
    sys.exit()
