const db = require('../../config/db');

const createUser = async ({ email, password }) => {
  const result = await db.query('INSERT INTO users (email, password) VALUES (?, ?)', [email, password]);
  return result.insertId ? { id: result.insertId, email } : null;
};

const findUserByEmail = async (email) => {
  const result = await db.query('SELECT * FROM users WHERE email = ?', [email]);
  return result[0];
};

module.exports = {
  createUser,
  findUserByEmail,
};