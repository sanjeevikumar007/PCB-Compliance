import smtplib, ssl, csv
from email.message import EmailMessage

sender = 'serverside00@gmail.com'
password = 'lurykwqzwdqjtpub'

Subject = 'IMPORTANT NOTICE PCB COMPLIANCE!'
body_message = 'check the compliance and retify the compliance as soon as possible to avoid non compliance'

context = ssl.create_default_context()
server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)

server.login(sender, password)

with open('C:\\Users\\sanje\\OneDrive\\Desktop\\SMTP FILE\\mails.csv','r') as csvfile:
    datareader = csv.reader(csvfile)
    for row in datareader:
        em = EmailMessage()
        em['From'] = sender
        em['To'] = row
        em['Subject'] = Subject
        em.set_content(body_message)
        server.send_message(em)
        print('The message sent')

    server.close()