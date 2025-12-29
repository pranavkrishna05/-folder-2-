"""
Service for handling email sending.
"""

import smtplib
from email.mime.text import MIMEText

class EmailService:
    """
    Handles sending password reset emails and other communications.
    """

    SMTP_SERVER = "smtp.example.com"
    SMTP_PORT = 587
    FROM_EMAIL = "noreply@example.com"
    EMAIL_PASSWORD = "your-email-password"

    def send_password_reset_email(self, email: str, token: str) -> None:
        """
        Sends a password reset email with the reset token link.
        """
        reset_link = f"https://example.com/password-reset?token={token}"
        subject = "Password Reset Request"
        body = f"Click the following link to reset your password: {reset_link}\nThis link will expire in 24 hours."

        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = self.FROM_EMAIL
        msg["To"] = email

        with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
            server.starttls()
            server.login(self.FROM_EMAIL, self.EMAIL_PASSWORD)
            server.sendmail(self.FROM_EMAIL, [email], msg.as_string())
```