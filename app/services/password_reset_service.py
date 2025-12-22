from typing import Optional
from datetime import datetime, timedelta
from app.models.user import User
from app.models.password_reset import PasswordReset
from app.repositories.user_repository import UserRepository
from app.repositories.password_reset_repository import PasswordResetRepository
import secrets
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class PasswordResetService:
    """
    Service class for managing password reset operations.
    """
    
    def __init__(self, user_repository: UserRepository, password_reset_repository: PasswordResetRepository) -> None:
        self.user_repository = user_repository
        self.password_reset_repository = password_reset_repository
    
    def request_password_reset(self, email: str) -> str:
        user = self.user_repository.find_by_email(email)
        if not user:
            raise ValueError("User with this email does not exist")
        
        token = secrets.token_hex(64)
        expiration = datetime.utcnow() + timedelta(hours=24)
        reset_token = PasswordReset(user_id=user.id, token=token, expired_at=expiration)
        
        self.password_reset_repository.save(reset_token)
        self.send_reset_email(email, token)
        return token
    
    def reset_password(self, token: str, new_password: str) -> None:
        reset_token = self.password_reset_repository.find_by_token(token)
        if not reset_token or reset_token.expired_at < datetime.utcnow() or reset_token.used:
            raise ValueError("Invalid or expired token")
        
        user = self.user_repository.find_by_email_id(reset_token.user_id)
        user.password = new_password  # Assume password hasher is applied here
        self.password_reset_repository.mark_as_used(reset_token)
        self.user_repository.save(user)
        
    def send_reset_email(self, email: str, token: str) -> None:
        sender_email = "no-reply@example.com"
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = email
        msg["Subject"] = "Password Reset Request"
        
        body = f"Please use the following token to reset your password: {token}"
        msg.attach(MIMEText(body, "plain"))
        
        with smtplib.SMTP("smtp.example.com", 587) as server:
            server.starttls()
            server.login(sender_email, "your_password")
            server.sendmail(sender_email, email, msg.as_string())