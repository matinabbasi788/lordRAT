<p align="center">
  <img 
    width="150"
    height="150"
    src="https://github.com/AdolfMacro/AdolfMacro/blob/main/logo.png"
  >
</p>


## LordRAT :shipit:

### How it works :
The commands of the Trojan and the sender are encrypted with a common key to reduce the possibility of eavesdropping, and then connect to the target server using the entered information.


------

### General instructions for use:
Run the tool, then use the generator to create an executable file for the victim's system and save the decryption key in a safe place.
Now enter the launcher section and enter the requested information so that the launcher connects to the victim's system and that's it.

**NOTE**: Try not to enter commands that cause the program to crash, for example: Commands that ask the user to enter something and such commands.

------

### Usage :
```
git clone https://github.com/AdolfMacro/lordRAT.git
cd lordRAT
python3 main.py
```
------


### Custom commands :
- Exit :
```
exit
```


- Reading from the clipboard :

```
rclipboard
```

- Writing on the clipboard :
```
wclipboard [string(Note that you should not enter a new line)]
```


-------
#### Screenshots :

<p align="center">
  <img 
    width="409"
    height="586"
    src="https://raw.githubusercontent.com/AdolfMacro/lordRAT/main/screenshots/1.png"
  >
</p>

------

### Dependencies :
#### Libraries :
- cryptography
- clipboard
- colorama

------

#### Upcoming update schedule 🌱 :

- [ ] **Code optimization .**

- [ ] **Ability to receive long messages .**

- [ ] **The ability to receive infected system information .**

- [ ] **Ability to create popup boxes .**

- [x] **R/W clipboard .**

- [x] **Installer**
------

> The use of the lordRAT(all versions) COMPLETE RESPONSIBILITY of the END-USER. Developers assume NO liability and are NOT responsible for any misuse or damage caused by this program.
