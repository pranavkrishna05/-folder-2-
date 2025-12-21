const userService = require('../../services/users/userService');
const { validateUserRegistration } = require('../../validators/userValidator');

const registerUser = async (req, res) => {
  try {
    const { email, password } = req.body;

    // Validate request body
    const { error } = validateUserRegistration(req.body);
    if (error) return res.status(400).send(error.details[0].message);

    // Register user
    const user = await userService.registerUser({ email, password });

    res.status(201).send(user);
  } catch (error) {
    console.error('Error in userController.registerUser:', error);
    res.status(500).send('Internal Server Error');
  }
};

module.exports = {
  registerUser,
};