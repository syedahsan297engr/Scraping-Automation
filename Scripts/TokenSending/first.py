from flask import Flask, request, redirect, url_for
import os
import secrets
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'syedahsannoori@gmail.com'
app.config['MAIL_PASSWORD'] = '....'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

# Generate authentication token
def generate_token():
    return secrets.token_hex(16)

# Send email with authentication token
def send_email(email, token):
    msg = Message('Email Verification', sender='syedahsannoori@gmail.com', recipients=[email])
    msg.body = f'Your verification token is: {token}'
    mail.send(msg)

# Route for email verification
@app.route('/verify-email', methods=['GET', 'POST'])
def verify_email():
    if request.method == 'POST':
        email = request.form['email']
        token = generate_token()
        send_email(email, token)
        return f'Verification email sent to {email}.'
    return '''
    <form method="post">
        <label for="email">Enter your email:</label><br>
        <input type="email" id="email" name="email" required><br>
        <button type="submit">Send Verification Email</button>
    </form>
    '''

# Route for confirming email with token
@app.route('/confirm-email/<email>/<token>', methods=['GET'])
def confirm_email(email, token):
    # In a real application, you would verify the token against a database or some other storage mechanism
    # For simplicity, this example just checks if the token matches
    user_token = request.args.get('token')
    if user_token == token:
        return f'Email {email} verified successfully!'
    else:
        return 'Invalid token, please try again.'

if __name__ == '__main__':
    app.run(debug=True)
