import socks
import smtplib
import socket
import dns.resolver

# Proxy settings
proxy_host = 'global.rotating.proxyrack.net'
proxy_port = 9000
proxy_username = 'ejaz'
proxy_password = 'WR84NKS-BBBY1EG-QXC1CDU-HYYWH3U-ZYPM7ME'

# Email server settings (Gmail example)
smtp_server = 'smtp.gmail.com'
smtp_port = 587

# Force IPv4 resolution for SMTP server
smtp_server_ipv4 = socket.gethostbyname(smtp_server)
print(f'Resolved SMTP server {smtp_server} to IPv4 address: {smtp_server_ipv4}')

# Create a proxy connection
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, proxy_host, proxy_port, True, proxy_username, proxy_password)
socks.wrapmodule(smtplib)

server = None

try:
    domain = 'smtp.gmail.com'
    mx_records = dns.resolver.resolve(domain, 'MX')
    
    # Resolve only IPv4 addresses for the MX records
    mx_record_ipv4 = None
    for mx_record in mx_records:
        try:
            mx_record_ipv4 = socket.gethostbyname(str(mx_record.exchange))
            break
        except socket.gaierror:
            continue

    if mx_record_ipv4 is None:
        raise Exception('No valid IPv4 MX record found.')

    # Connect to the SMTP server
    print(f'Connecting to SMTP server {mx_record_ipv4}...')
    server = smtplib.SMTP(mx_record_ipv4, smtp_port)
    server.set_debuglevel(1)  # Enable debug output
    server.starttls()
    print('Logging in to SMTP server...')
    server.login('2020engineerahsan@gmail.com', '0RTW9J9P')

    # Verify the email address without sending an email
    from_address = '2020engineerahsan@gmail.com'
    to_address = 'syedahsannoori@gmail.com'
    print('Sending MAIL FROM command...')
    server.mail(from_address)
    print('Sending RCPT TO command...')
    code, message = server.rcpt(to_address)

    if code == 250:
        print(f'The email address {to_address} is valid.')
    else:
        print(f'The email address {to_address} is invalid: {message.decode()}')

except Exception as e:
    print(f'Error: {e}')

finally:
    if server:
        server.quit()
