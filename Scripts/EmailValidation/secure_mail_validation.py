import re
import dns.resolver
import smtplib

# List of known disposable email domains
disposable_domains = set([
    'mailinator.com', 'tempmail.com', '10minutemail.com',
    # Add more known disposable domains as needed
])

def is_valid_syntax(email):
    """ Check if the email address has valid syntax """
    regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(regex, email) is not None

def has_mx_record(domain):
    """ Check if the domain has an MX record """
    try:
        mx_records = dns.resolver.resolve(domain, 'MX')
        return True
    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN):
        return False

def is_disposable_email(email):
    """ Check if the email address is from a disposable email provider """
    domain = email.split('@')[1]
    return domain in disposable_domains

def verify_email_smtp(email):
    """ Verify if the email address exists using SMTP verification """
    try:
        domain = email.split('@')[1]
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_record = str(mx_records[0].exchange)
        
        server = smtplib.SMTP()
        server.set_debuglevel(0)
        server.connect(mx_record)
        server.helo(server.local_hostname)
        server.mail('2020engineerahsan@gmail.com')  # Use your real email here
        code, message = server.rcpt(email)
        server.quit()
        
        return code == 250
    except smtplib.SMTPServerDisconnected:
        # This exception means the connection was unexpectedly closed by the server
        print(f"SMTP server disconnected unexpectedly for {email}")
        return False
    except smtplib.SMTPRecipientsRefused:
        # This exception means the recipients were refused
        print(f"SMTP recipient refused for {email}")
        return False
    except Exception as e:
        # Any other exception
        print(f"An error occurred during SMTP verification for {email}: {e}")
        return False

def validate_email(email):
    """ Perform all checks on the email address """
    if not is_valid_syntax(email):
        return "Invalid Syntax"
    
    domain = email.split('@')[1]
    
    if not has_mx_record(domain):
        return "Invalid Domain"
    
    if is_disposable_email(email):
        return "Disposable Email"
    
    if not verify_email_smtp(email):
        return "Email Does Not Exist"
    
    return "Email is Valid"

# Hardcoded email examples
emails = [
    "plainaddress",
    "housseee@gmail.com",
    "user@domain.com",
    "user@mailinator.com",
    "test@nonexistentdomain.com",
    "ejaz_ahmed@outlook.com",
    "usama@jfreaks.com",
    "syedahsan@gmail.com",
    "noori@gmail.com",
    "ahuwewghgxtte6@gmail.com"
]

# Validate each email
for email in emails:
    result = validate_email(email)
    print(f"Validation result for '{email}': {result}")
