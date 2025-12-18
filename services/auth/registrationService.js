const userRepository = require('../../repositories/userRepository');
const validateEmail = require('../../utils/validateEmail');
const validatePassword = require('../../utils/validatePassword');
const sendConfirmationEmail = require('../../integrations/emailService');

const registerUser = async (email, password) => {
    if (!validateEmail(email)) {
        throw new Error('Invalid email format');
    }
    if (!validatePassword(password)) {
        throw new Error('Password does not meet complexity requirements');
    }
    const existingUser = await userRepository.getUserByEmail(email);
    if (existingUser) {
        throw new Error('Email is already in use');
    }
    const newUser = await userRepository.createUser({ email, password });
    await sendConfirmationEmail(newUser.email);
    return newUser;
};

module.exports = { registerUser };