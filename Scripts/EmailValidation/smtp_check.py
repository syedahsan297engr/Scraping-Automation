import smtplib
import dns.resolver

def verify_email_smtp(email):
    try:
        # Extract domain
        domain = email.split('@')[1]
        
        # Get MX record for the domain
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(mx_records[0].exchange)
        
        # Set up SMTP connection
        server = smtplib.SMTP(mx_record)
        server.set_debuglevel(0)  # Set to 1 for detailed debug output
        server.connect(mx_record)
        server.helo(server.local_hostname)  # server.local_hostname(Get local server hostname)
        server.mail('2020engineerahsan@gmail.com')  # Use your real email here
        code, message = server.rcpt(email)
        server.quit()
        
        # Check the response code
        if code == 250:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Test the function
email_to_check = 'ejaz_ahmed@outlook.com'
is_valid = verify_email_smtp(email_to_check)
print(f"Email '{email_to_check}' is valid: {is_valid}")

'''
    Extract Domain: Extract the domain part of the email (i.e., gmail.com).
    Get MX Record: Perform a DNS lookup to get the MX (Mail Exchange) record for the domain. This tells you which mail server is responsible for receiving emails for that domain.
    SMTP Connection: Connect to the mail server using the SMTP protocol.
    HELO/EHLO: Introduce yourself to the mail server.
    MAIL FROM: Specify the sender's email address (can be any valid email address).
    RCPT TO: Specify the recipient's email address (the one you're verifying).
    Check Response Code: Check the response code from the server. A code of 250 indicates the email address is valid.
'''