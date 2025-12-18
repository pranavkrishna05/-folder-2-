const express = require('express');
const router = express.Router();
const registrationService = require('../../services/auth/registrationService');
const { validateRegistrationInput } = require('../../utils/validation');

// @route   POST api/auth/register
// @desc    Register user
// @access  Public
router.post('/', async (req, res) => {
    const { errors, isValid } = validateRegistrationInput(req.body);

    if (!isValid) {
        return res.status(400).json(errors);
    }

    try {
        const user = await registrationService.registerUser(req.body);
        res.status(201).json(user);
    } catch (error) {
        res.status(400).json({ error: error.message });
    }
});

module.exports = router;