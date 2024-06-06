# use an appropriate path to import
from verifier.verifier import Verifier

# Use normal SMTP to connect to the server
normal_verifier = Verifier(source_addr='2020engineerahsan@gmail.com') # No proxy
results = normal_verifier.verify('syedahsannoori@gmail.com')

# Use socks proxy to connect over SMTP
socks_verifier =  Verifier(
    source_addr='2020engineerahsan@gmail.com',
    proxy_type='socks5',
    proxy_addr='socks5.your-proxy-provider.com', #38.154.227.167
    proxy_port=5868,
    proxy_username='zfbzvjqm',
    proxy_password='y87xzme3pxct'
)
results = socks_verifier.verify('syedahsannoori@gmail.com')