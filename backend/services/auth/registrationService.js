const bcrypt = require('bcryptjs');
const { User } = require('../../models');
const sendConfirmationEmail = require('../../utils/email');

async function registerUser(userData) {
    const { email, password } = userData;

    // Check if email already exists
    const existingUser = await User.findOne({ email });
    if (existingUser) {
        throw new Error('Email already in use');
    }

    // Hash the password
    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(password, salt);

    // Create the user
    const newUser = new User({
        email,
        password: hashedPassword
    });

    await newUser.save();

    // Send confirmation email
    await sendConfirmationEmail(newUser.email);

    return newUser;
}

module.exports = {
    registerUser
};