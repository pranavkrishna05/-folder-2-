const nodemailer = require('nodemailer');

module.exports = async (email) => {
  const transporter = nodemailer.createTransport({
    service: 'Gmail',
    auth: {
      user: process.env.EMAIL_USER,
      pass: process.env.EMAIL_PASS
    }
  });

  const mailOptions = {
    from: process.env.EMAIL_USER,
    to: email,
    subject: 'Confirmation Email',
    text: 'Thank you for registering!'
  };

  await transporter.sendMail(mailOptions);
};
