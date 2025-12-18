const User = require('../models/User');

const getUserByEmail = async (email) => {
    return User.findOne({ email });
};

const createUser = async (userData) => {
    const user = new User(userData);
    return user.save();
};

module.exports = { getUserByEmail, createUser };