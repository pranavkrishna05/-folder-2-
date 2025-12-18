const nodemailer = require('nodemailer');

const sendConfirmationEmail = async (email) => {
    // Configure transport and retriever service
    let transporter = nodemailer.createTransport({
        service: 'gmail',
        auth: {
            user: 'your-email@gmail.com',
            pass: 'your-password'
        }
    });

    let mailOptions = {
        from: 'your-email@gmail.com',
        to: email,
        subject: 'Welcome to Our App!',
        text: 'Thank you for registering an account with us!'
    };

    return transporter.sendMail(mailOptions);
};

module.exports = { sendConfirmationEmail };