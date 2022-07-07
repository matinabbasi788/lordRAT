from colorama import Fore
from platform import system as OStype
from os import system
from tools import generator , launcher
def clear():
    if "windows" in OStype() :
        system("cls")
    else :
        system("clear")
def main():
    while 1:
        clear()
        selection=input(Fore.LIGHTYELLOW_EX+ r"""

               ⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                ⠀⢠⣶⣶⣄⠀⠀⠀⠀⣾⣿⣿⣷⠀⠀⠀⠀⣾⣿⣿⣷⠀⠀⠀⠀⣰⣶⣶⡄⠀
                ⠀⠸⣿⣿⠟⠀⠀⠀⠀⠘⢿⣿⠋⠀⠀⠀⠀⠘⢿⡿⠋⠀⠀⠀⠀⠻⣿⣿⠇⠀
                ⠀⠀⠀⢸⣧⡀⠀⠀⠀⢀⣾⣿⣆⠀⠀⠀⠀⣰⣿⣷⡀⠀⠀⠀⢀⣼⠇⠀⠀⠀
               ⠀ ⠀⠀⠀⣿⣿⣄⠀⢀⣾⣿⣿⣿⣧⠀⠀⣼⣿⣿⣿⣷⡀⠀⣠⣿⣿⠀⠀⠀⠀
                ⠀⠀⠀⠀⣿⣿⠏⠀⠀⠙⣿⣿⣿⠁⠀⠀⠈⢿⣿⡿⠋⠀⠀⠹⣿⣿⠀⠀⠀⠀
                ⠀⠀⠀⠀⢹⣿⡄⠀⠀⢀⣿⣿⣿⣄⠀⠀⣀⣾⣿⣷⡀⠀⠀⣠⣿⡇⠀⠀⠀⠀
                ⠀⠀⠀⠀⠘⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⠁⠀⠀⠀⠀
                ⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀
               ⠀⠀ ⠀⠀⠀⠸⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠇⠀⠀⠀⠀⠀
                ⠀⠀⠀⠀⢠⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡄⠀⠀⠀⠀
    _________________⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠋_________________
   |                                                      |
   |                                                      |
   |  [ 1 ] Launcher                     [ 2 ] Generator  |
   |                                                      |
   |  [ 3 ] Developer information        [ 4 ] Exit       |
   |______________________________________________________| 
    
	
Enter your selection : """)

        try:
            if selection=='1':
                launcher.main()
            elif selection=='2':
                generator.main(None)
            elif selection=="3":
                clear()
                input(Fore.LIGHTYELLOW_EX+ r"""
      _---~~(~~-_.
    _{        )   )         
  ,   ) -~~- ( ,-' )_       Hi, I'm Mani
 (  `-,_..`., )-- '_,)      You can get my complete information from this site:
( ` _)  (  -~( -_ `,  }     https://adolfmacro.github.io/mani/
(_-  _  ~_-~~~~`,  ,' )     
  `~ -^(    __;-,((()))     My GitHub Address: https://github.com/adolfmacro
        ~~~~ {_ -_(())      E-mail : m4nikamran@gmail.com
               `\  }        Telegram : https://t.me/manikamran
                 { }      
    
    
    Enter to exit : """+Fore.RESET)
            elif selection=="4" : 
                exit()
        except KeyboardInterrupt:
            pass
if __name__ =="__main__":
    main()