import smtplib
import dns.resolver
import re
import random
import requests
import socket

# Function to send a verification email
def send_verification_email(email_address, verification_token):
    # Code to send the verification email using your email service provider
    # You need to replace the placeholders with your email service provider's details
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = '2020engineerahsan@gmail.com'
    sender_password = '...'

    subject = 'Email Verification'
    body = f'Please verify your email address by clicking the following link: https://yourwebsite.com/verify?token={verification_token}'

    message = f'Subject: {subject}\n\n{body}'

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, email_address, message)

# Function to generate a random verification token
def generate_verification_token():
    # Generate a random alphanumeric token of length 10
    token_length = 10
    characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(characters) for _ in range(token_length))

# Function to check email syntax
def check_email_syntax(email_address):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email_address)
    if match is None:
        raise ValueError('Bad Syntax')

# Function to verify email using SMTP
def verify_email_with_smtp(email_address, mxRecord):
    # Get local server hostname
    host = socket.gethostname()

    # SMTP lib setup
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(host)
    # server.mail('syedahsannoori@gmail.com')
    server.mail('hwuhuwyetgtd@gmail.com')
    code, message = server.rcpt(str(email_address))
    server.quit()

    # Assume 250 as Success
    if code == 250:
        return True
    else:
        return False

# Function to verify email using a proxy server
def verify_email_with_proxy(email_address):
    proxy_list = [
        '38.154.227.167:5868',
        '185.199.229.156:7492',
        '45.94.47.66:8110'
    ]

    for proxy in proxy_list:
        try:
            # Configure proxy
            proxies = {
                'http': f'http://{proxy}',
                'https': f'https://{proxy}'
            }

            # Make a request to the SMTP server using the proxy
            response = requests.get(f'http://smtp.gmail.com', proxies=proxies)
            
            # Assume 200 as Success
            if response.status_code == 200:
                return True
        except Exception as e:
            print(f'Error occurred with proxy {proxy}: {e}')

    return False

def verify_email(email_address):
    try:
        # Step 1: Check email syntax
        check_email_syntax(email_address)

        # Step 2: Get MX record
        domain_name = email_address.split('@')[1]
        records = dns.resolver.resolve(domain_name, 'MX')
        mxRecord = str(records[0].exchange)

        # Step 3: Verify email using SMTP
        smtp_verification_result = verify_email_with_smtp(email_address, mxRecord)

        if smtp_verification_result:
            return True
        else:
            # Step 4: If SMTP verification fails, send a verification email
            verification_token = generate_verification_token()
            send_verification_email(email_address, verification_token)
            return False  # Return False indicating that email verification is pending
    except Exception as e:
        print(f'Error occurred during email verification: {e}')
        return False

# Example usage
email_address = 'ejaz_ahmed@outlook.com'
# email_address = 'syedahsannoori@gmail.com'
verification_result = verify_email(email_address)
if verification_result:
    print('Email is valid.')
else:
    print('Email verification pending.')
