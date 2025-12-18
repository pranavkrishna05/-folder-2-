const nodemailer = require('nodemailer');

async function sendConfirmationEmail(userEmail) {
    const transporter = nodemailer.createTransport({
        service: 'Gmail',
        auth: {
            user: 'your-email@gmail.com',
            pass: 'your-email-password'
        }
    });

    const mailOptions = {
        from: 'your-email@gmail.com',
        to: userEmail,
        subject: 'Account Registration Confirmation',
        text: 'Thank you for registering. Please confirm your email address.'
    };

    await transporter.sendMail(mailOptions);
}

module.exports = sendConfirmationEmail;