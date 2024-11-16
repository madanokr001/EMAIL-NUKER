from pystyle import Colorate, Colors
import os
import sys
from Tools.Bomb import *
from Tools.BombRandom import *
from Tools.BombAT import *
from Tools.BombHTML import *

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.red_to_white,"""

    ██░ ██  ▄▄▄       ██▀███   ▄▄▄       ██ ▄█▀ ██▓ ██▀███   ██▓
    ▓██░ ██▒▒████▄    ▓██ ▒ ██▒▒████▄     ██▄█▒ ▓██▒▓██ ▒ ██▒▓██▒
    ▒██▀▀██░▒██  ▀█▄  ▓██ ░▄█ ▒▒██  ▀█▄  ▓███▄░ ▒██▒▓██ ░▄█ ▒▒██▒
    ░▓█ ░██ ░██▄▄▄▄██ ▒██▀▀█▄  ░██▄▄▄▄██ ▓██ █▄ ░██░▒██▀▀█▄  ░██░
    ░▓█▒░██▓ ▓█   ▓██▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒ █▄░██░░██▓ ▒██▒░██░
    ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒ ▒▒ ▓▒░▓  ░ ▒▓ ░▒▓░░▓  
    ▒ ░▒░ ░  ▒   ▒▒ ░  ░▒ ░ ▒░  ▒   ▒▒ ░░ ░▒ ▒░ ▒ ░  ░▒ ░ ▒░ ▒ ░
    ░  ░░ ░  ░   ▒     ░░   ░   ░   ▒   ░ ░░ ░  ▒ ░  ░░   ░  ▒ ░
    ░  ░  ░      ░  ░   ░           ░  ░░  ░    ░     ░      ░    

═══════════════════════════════════════════════════════════════════
1. ANSWER : HOW TO GET APP PASSWORD?
2. HARA-KIRI : https://www.youtube.com/watch?v=lSURGX0JHbA  
═══════════════════════════════════════════════════════════════════
                              
╔══════════════════════════════════════════════════════════════════╗
║                      HARA-KIRI version 1.0                       ║
║══════════════════════════════════════════════════════════════════║
║                                                                  ║
║                      [01] EMAIL BOMB                             ║
║                      [02] EMAIL RANDOMIZE BOMB                   ║
║                      [03] EMAIL ATTACHMENT BOMB                  ║
║                      [04] EMAIL HTML BOMB                        ║                                                    
║                      [05] EXIT                                   ║ 
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝

                       
"""))


def main():
    while True:
        logo()
        select = input(Colorate.Horizontal(Colors.red_to_white,"""
╔═══[root@HARA-KIRI]
║
║═══> 
"""))

        if select == "1" or select.lower() == "1":
            email_main()
            
        elif select == "2" or select.lower() == "03":
            email_random_main()

        elif select == "3" or select.lower() == "03":
            email_attachment_main()

        elif select == "4" or select.lower() == "04":
            email_html_main()
        

        elif select == "5" or select.lower() == "05":
            sys.exit()
    
             


if __name__ == "__main__":
    main()
