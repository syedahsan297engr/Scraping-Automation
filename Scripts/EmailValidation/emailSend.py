import smtplib
from email.mime.text import MIMEText

def send_verification_email(email, verification_code):
    sender_email = '2020engineerahsan@gmail.com'
    subject = 'Email Verification'
    message = f'Please verify your email address by entering the following code: {verification_code}'

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = email

    try:
        smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_server.starttls()
        smtp_server.login(sender_email, '0RTW9J9P')
        smtp_server.sendmail(sender_email, [email], msg.as_string())
        smtp_server.quit()
        print("Verification email sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the verification email: {e}")

# Usage
email_to_verify = 'syedahsannoori@gmail,com'
verification_code = 'ABC123'  # Generate a random verification code
send_verification_email(email_to_verify, verification_code)
