const registerService = require('../../services/auth/registerService');

module.exports = {
  register: async (req, res) => {
    try {
      const { email, password } = req.body;
      const user = await registerService.registerUser(email, password);
      res.status(201).json({ message: 'Registration successful', user });
    } catch (error) {
      res.status(400).json({ message: error.message });
    }
  }
};
