import smtplib

# Email to be validated
email_to_validate = 'syedahsannoori@gmail.com'

# SMTP server details
smtp_server = 'smtp.gmail.com'  # Example SMTP server
smtp_port = 587  # Typically 587 for TLS

def validate_email_via_smtp(email):
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        
        # Optionally, log in to the SMTP server if necessary
        # server.login('your_smtp_username', 'your_smtp_password')
        
        # Use verify or rcpt command
        code, message = server.verify(email)
        server.quit()
        
        if code == 250:
            return True
        else:
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

# Validate the email
is_valid = validate_email_via_smtp(email_to_validate)
print(f"The email address '{email_to_validate}' is {'valid' if is_valid else 'invalid'}.")
