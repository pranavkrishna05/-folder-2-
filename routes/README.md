# README for Routes

Below are the descriptions of different routes and their error handling.

## Login Route

### Email Validation
```javascript
// Email Validation
function isValidEmail(email) {
    const emailRegex = /^\S+@\S+\.\S+$/;
    return emailRegex.test(email);
}
```

### Error Messages
```javascript
// Improved Error Messages
function getErrorMessage(error) {
    switch (error.code) {
        case 'INVALID_EMAIL':
            return 'The provided email is not valid. Please enter a valid email address.';
        case 'RATE_LIMIT_EXCEEDED':
            return 'Too many login attempts. Please try again later.';
        default:
            return 'An unexpected error occurred. Please try again later.';
    }
}
```

### Rate Limiting
```javascript
// Rate Limiting Logic
let loginAttempts = 0;
const MAX_ATTEMPTS = 5;
const RETRY_TIME = 15 * 60 * 1000; // 15 minutes

function rateLimit() {
    if (loginAttempts >= MAX_ATTEMPTS) {
        throw { code: 'RATE_LIMIT_EXCEEDED' };
    }
    loginAttempts++;
    setTimeout(() => { loginAttempts = 0; }, RETRY_TIME); // Reset attempts after retry time
}
```
