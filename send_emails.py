import smtplib, ssl

sender = 'serverside00@gmail.com'
password = 'lurykwqzwdqjtpub'
receiver = 'vkalaiyarasan978@gmail.com'

body_msg = '''Subject: pcb compliance
check the process that you are doing and prevent from non compliance.'''


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, body_msg)