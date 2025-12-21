const { registerUser } = require('../../services/users/userService');
const { validateEmail, validatePassword } = require('../../validators/userValidator');

const registerUserController = async (req, res) => {
  try {
    const { email, password } = req.body;

    // Validate email and password
    if (!validateEmail(email) || !validatePassword(password)) {
      return res.status(400).json({ message: 'Invalid email or password format' });
    }

    // Register user
    const user = await registerUser({ email, password });

    res.status(201).json({ message: 'User registered successfully', user });
  } catch (error) {
    console.error('Error registering user:', error);
    res.status(500).json({ message: 'Internal server error' });
  }
};

module.exports = {
  registerUserController,
};