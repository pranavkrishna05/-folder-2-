const express = require('express');
const bodyParser = require('body-parser');
const authRoutes = require('../controllers/auth/registerController');

const app = express();

app.use(bodyParser.json());

app.post('/auth/register', authRoutes.register);

module.exports = app;
