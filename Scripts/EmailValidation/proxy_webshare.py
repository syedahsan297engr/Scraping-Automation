import smtplib
import socket
import socks
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
# email_to_check = 'syedahsannoori@gmail.com'
# is_valid = verify_email_smtp(email_to_check)
# print(f"Email '{email_to_check}' is valid: {is_valid}")


def get_ipv4_mx_record(domain):
    mx_records = dns.resolver.resolve(domain, 'MX')
    for mx in mx_records:
        mx_record = str(mx.exchange)
        try:
            # Resolve the MX record to an IPv4 address
            ipv4_records = dns.resolver.resolve(mx_record, 'A')
            if ipv4_records:
                return mx_record, str(ipv4_records[0])
        except dns.resolver.NoAnswer:
            continue
    return None, None

def verify_email_smtp_with_proxy(email, proxy_host, proxy_port, proxy_username, proxy_password, proxy_type=socks.SOCKS5):
    try:
        # Extract domain
        domain = email.split('@')[1]
        
        # Get IPv4 MX record for the domain
        mx_record, ipv4_address = get_ipv4_mx_record(domain)
        if not ipv4_address:
            print("No IPv4 address found for the domain's MX record.")
            return False
        
        # Set up the SOCKS proxy
        socks.set_default_proxy(proxy_type, proxy_host, proxy_port, username=proxy_username, password=proxy_password)
        socket.socket = socks.socksocket
        
        # Set up SMTP connection
        server = smtplib.SMTP(ipv4_address)
        server.set_debuglevel(0)  # Set to 1 for detailed debug output
        server.connect(ipv4_address)
        server.helo(socket.gethostname())  # server.local_hostname is optional, default is socket.gethostname()
        server.mail('your-email@example.com')  # Use your real email here
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

# Usage
email = 'syedahsannoori@gmail.com'
proxy_host = '38.154.227.167'
proxy_port = 5868  # Typical port for SOCKS5
proxy_username = 'zfbzvjqm'
proxy_password = 'y87xzme3pxct'
is_valid = verify_email_smtp_with_proxy(email, proxy_host, proxy_port, proxy_username, proxy_password)
print(f'Email address {email} is {"valid" if is_valid else "invalid"}')
