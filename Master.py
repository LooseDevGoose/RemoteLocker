import socket
import os
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
            # Initialize socket variable
            sock = socket.socket()

            # Initialize host variable
            host = socket.gethostname()

            # Initialize the port
            port = 8080

            # Bind the socket with port and host
            sock.bind(('', port))

            print("waiting for slave connections...")

            # Listen for connections
            sock.listen()

            conn, addr = sock.accept()

            print(addr, "is connected to server")

            # Take command as input
            command = input(str("Enter Command [Lock]  or [Unlock]: "))

            # Send Command
            conn.send(command.encode())

            print("Command has been sent successfully.")

            data = conn.recv(1024)

            if data:
                print("command received and executed successfully.")

        except Exception as error:
            print(error)

    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, " ".join(sys.argv), None, 1)

except Exception as error:
    print(error)

input('Message to prevent window from closing: presented to you by Mick Hilhorst')
