# Packages
import colorama
from colorama import Fore, Style
import socket
import os

# Init Colorama
colorama.init()

# Socket Settings
ip = "<your local ip goes here>" # To get local ip type ipconfig in command prompt and search for IPv4 Address
port = 9090 # Change if you want

# Functions
def selector():
    print(Fore.RED + "[?] Available Actions" + Fore.BLUE + "\n1. Shutdown\n2. Restart\n3. Lock\n4. Custom Command\n5. Exit")
    userinput = input(Fore.YELLOW + "[!] Please pick an action: ")
    if userinput == '1':
        print(Fore.GREEN + "[OK] Shutting down...")
        listen("shutdown /s")
    elif userinput == '2':
        print(Fore.GREEN + "[OK] Restarting...")
        listen("shutdown /r")
    elif userinput == '3':
        print(Fore.GREEN + "[OK] Locking...")
        listen("shutdown /l")
    elif userinput == '4':
        customcmd = input(Fore.YELLOW + "[!] Your custom command: ")
        listen(customcmd)
    elif userinput == '5':
        print(Fore.RED + "[BYE] Exiting...")
        exit()
    else:
        print(Fore.RED + "[X] Unknown action")

def listen(command):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    # Bind and listen
    serverSocket.bind((ip, port));
    serverSocket.listen();
    print(Fore.GREEN + "[OK] Server listening! %a:%a"%(ip, port))
    
    # Accept connections
    while(True):
        (clientConnected, clientAddress) = serverSocket.accept();
        print(Fore.GREEN + "[OK] Connection estabilished, with client %s:%s"%(clientAddress[0], clientAddress[1]));

        dataFromClient = clientConnected.recv(1024)
        if dataFromClient.decode() == 'OK':
            print(Fore.GREEN + "[OK] Server responded with OK")
        else:
            print(Fore.RED + "[X] Time-out or slow response")

        clientConnected.send(command.encode());
        print(Fore.GREEN + "[OK] Command sent!")

        print(Fore.YELLOW + "[!] Do you wish to continue with same command? Y/N")
        continueprompt = input()

        if continueprompt == 'Y' or continueprompt == 'y':
            print(Fore.GREEN + "[OK] Continue...")
            continue
        elif continueprompt == 'N' or continueprompt == 'n':
            print(Fore.RED + "[BYE] Exiting...")
            exit()
        else:
            print(Fore.RED + "[X] Unknown response, exiting...")
            exit()

# Startup
if __name__ == '__main__':
    selector()
