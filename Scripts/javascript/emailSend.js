const nodemailer = require('nodemailer');

// Create a transporter object using SMTP transport
let transporter = nodemailer.createTransport({
    host: 'smtp.gmail.com',
    port: 587,
    secure: false, // true for 465, false for other ports
    auth: {
        user: '2020engineerahsan@gmail.com', // Your email address
        pass: '0RTW9J9P' // Your password
    }
});

// Setup email data
let mailOptions = {
    from: '2020engineerahsan@gmail.com', // Sender address
    to: 'syedahsannoori@gmail.com', // List of recipients
    subject: 'Test Email', // Subject line
    text: 'Hello, this is a test email from Node.js!' // Plain text body
};

// Send email
transporter.sendMail(mailOptions, (error, info) => {
    if (error) {
        console.error('Error occurred:', error);
    } else {
        console.log('Email sent:', info.response);
    }
});

/**
Switch to a more secure service

If you still can’t sign in from the site, app, or program, consider switching to a service that uses more secure sign-in technology, like Sign in with Google.

All Google services use the latest security measures.
**/
