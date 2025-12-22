export const validateEmail = (email: string): void => {
    const emailRegex = /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/;
    if (!emailRegex.test(email)) {
        throw new Error('Invalid email format');
    }
};

export const validatePassword = (password: string): void => {
    const minLength = 8;
    if (password.length < minLength) {
        throw new Error('Password must be at least 8 characters long');
    }
};
