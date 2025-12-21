const mongoose = require('mongoose');

const UserSchema = new mongoose.Schema({
  email: {
    type: String,
    required: true,
    unique: true,
    match: [/^\S+@\S+\.\S+$/, 'is invalid'],
    index: true,
  },
  password: {
    type: String,
    required: true,
    minlength: 8,
  },
}, { timestamps: true });

const User = mongoose.model('User', UserSchema);

module.exports = User;
