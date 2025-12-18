const User = require('../../models/userModel');
const sendConfirmationEmail = require('../../integrations/emailService');
const bcrypt = require('bcrypt');

module.exports = {
  registerUser: async (email, password) => {
    // Validate email format
    const emailRegex = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
    if (!emailRegex.test(email)) {
      throw new Error('Invalid email format');
    }
    // Validate password complexity
    if (password.length < 8) {
      throw new Error('Password must be at least 8 characters');
    }
    // Check if email is already in use
    const existingUser = await User.findOne({ email });
    if (existingUser) {
      throw new Error('Email is already in use');
    }
    // Hash the password
    const hashedPassword = await bcrypt.hash(password, 10);
    // Create new user
    const user = new User({ email, password: hashedPassword });
    await user.save();
    // Send confirmation email
    await sendConfirmationEmail(email);
    return user;
  }
};
