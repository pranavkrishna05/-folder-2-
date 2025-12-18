const request = require('supertest');
const express = require('express');
const registrationController = require('../controllers/auth/registrationController');
const app = express();

app.use(express.json());
app.use('/auth', registrationController);

describe('User Registration', () => {
    it('should register a user and send confirmation email', async () => {
        const response = await request(app)
            .post('/auth/register')
            .send({ email: 'test@example.com', password: 'Password123!' });

        expect(response.status).toBe(201);
        expect(response.body.email).toBe('test@example.com');
    });

    it('should not register a user with an existing email', async () => {
        await request(app)
            .post('/auth/register')
            .send({ email: 'duplicate@example.com', password: 'Password123!' });

        const response = await request(app)
            .post('/auth/register')
            .send({ email: 'duplicate@example.com', password: 'Password123!' });

        expect(response.status).toBe(400);
        expect(response.body.message).toBe('Email is already in use');
    });

    it('should not register a user with invalid data', async () => {
        const response = await request(app)
            .post('/auth/register')
            .send({ email: 'invalid-email', password: 'short' });

        expect(response.status).toBe(400);
        expect(response.body.message).toBe('Invalid email format');
    });
});