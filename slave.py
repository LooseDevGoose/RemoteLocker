import socket
from ctypes import *
import ctypes
import sys

try:
    def is_admin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    if is_admin():
        try:

            # Initialize s to socket
            sock = socket.socket()

            # Initialize the host
            host = input(str("Enter Master IP: "))

            # Initialize the port
            port = 8080

            # bind the socket with port and host
            sock.connect((host, port))

            print("Connected to Server.")

            # receive the command from master program
            command = sock.recv(1024)
            command = command.decode()

            # match the command and execute it on slave system
            if command == "Lock":
                print("Command is :", command)
                print('test')
                sock.send("Command received".encode())

                # you can give batch file as input here
                windll.user32.BlockInput(True)  # enable block

            elif command == "Unlock":
                print('test2')
                print("Command is :", command)
                sock.send("Command received".encode())

                # you can give batch file as input here
                windll.user32.BlockInput(False)  # disable block
        except Exception as error:
            print(error)

    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)
except Exception as error:
    print(error)

input('Press ENTER to exit')
