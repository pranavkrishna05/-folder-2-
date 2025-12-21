const userRepository = require('../../repositories/users/userRepository');
const bcrypt = require('bcrypt');
const { sendConfirmationEmail } = require('../../utilities/emailUtility');

const registerUser = async ({ email, password }) => {
  // Encrypt password
  const hashedPassword = await bcrypt.hash(password, 10);

  // Create user
  const user = await userRepository.createUser({ email, password: hashedPassword });

  // Send confirmation email
  await sendConfirmationEmail(user.email);

  return user;
};

module.exports = {
  registerUser,
};