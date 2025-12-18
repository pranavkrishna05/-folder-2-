const request = require('supertest');
const app = require('../../app');
const User = require('../../models/userModel');
const sinon = require('sinon');
const emailService = require('../../integrations/emailService');

describe('POST /auth/register', () => {
  beforeEach(() => {
    sinon.stub(User, 'findOne').callsFake((query) => query.email === 'existing@example.com' ? ({ email: 'existing@example.com' }) : null);
    sinon.stub(User.prototype, 'save').resolves({ email: 'new@example.com' });
    sinon.stub(emailService).resolves();
  });

  afterEach(() => {
    sinon.restore();
  });

  it('should register a user successfully', async () => {
    const res = await request(app)
      .post('/auth/register')
      .send({ email: 'new@example.com', password: 'Password123!' });

    expect(res.status).to.equal(201);
    expect(res.body.message).to.equal('Registration successful');
  });

  it('should not register a user with existing email', async () => {
    const res = await request(app)
      .post('/auth/register')
      .send({ email: 'existing@example.com', password: 'Password123!' });

    expect(res.status).to.equal(400);
    expect(res.body.message).to.equal('Email is already in use');
  });

  it('should not register a user with invalid email format', async () => {
    const res = await request(app)
      .post('/auth/register')
      .send({ email: 'invalid-email', password: 'Password123!' });

    expect(res.status).to.equal(400);
    expect(res.body.message).to.equal('Invalid email format');
  });

  it('should not register a user with password less than 8 characters', async () => {
    const res = await request(app)
      .post('/auth/register')
      .send({ email: 'new@example.com', password: 'short' });

    expect(res.status).to.equal(400);
    expect(res.body.message).to.equal('Password must be at least 8 characters');
  });
});
