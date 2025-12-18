const express = require('express');
const router = express.Router();
const registrationService = require('../../services/auth/registrationService');

router.post('/register', async (req, res) => {
    try {
        const { email, password } = req.body;
        const result = await registrationService.registerUser(email, password);
        res.status(201).json(result);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
});

module.exports = router;