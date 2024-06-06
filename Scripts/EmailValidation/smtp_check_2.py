from smtplib import SMTP

address_to_test = "2020ee297@student.uet.edu.pk"
address_to_test = "hehdheyvgyef@gmail.com"

try:
    with SMTP('gmail-smtp-in.l.google.com') as smtp:
        host_exists = True
        smtp.helo() # send the HELO command
        smtp.mail('2020engineerahsan@gmail.com') # send the MAIL command
        resp = smtp.rcpt(address_to_test)
        if resp[0] == 250: # check the status code
            deliverable = True
        elif resp[0] == 550:
            deliverable = False
        else:
            print(resp[0])
        print(f'The mail is : {deliverable}')

except smtplib.SMTPServerDisconnected as err:
    print("SMTP connection error")