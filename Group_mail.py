import smtplib, ssl, csv
from email.message import EmailMessage

def level1(Lead, Mercury, Cadmium, Hexavalentchromium, Polybrominatedbiphenyls, polybrominateddiphenylethers):
    def mail(item_name):
        sender = 'serverside00@gmail.com'
        password = 'lurykwqzwdqjtpub' 
        
        Subject = 'IMPORTANT NOTICE ON PCB COMPLIANCE!'
        body_message = (f'\"{item_name}\"- compliance is identified and retify the compliance as soon as possible to avoid non compliance')
        
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

    if( Lead > 0.1):
        mail("Lead")
    if( Mercury > 0.1):
        mail("Mercury")
    if( Cadmium > 0.1):
        mail("Cadmium")
    if( Hexavalentchromium > 0.1):
        mail("Hexavalentchromium")
    if( Polybrominatedbiphenyls > 0.1):
        mail("Polybrominatedbiphenyls")
    if( polybrominateddiphenylethers > 0.1):
        mail("polybrominateddiphenylethers")
