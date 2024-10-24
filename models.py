from pydantic import BaseModel


class LoginUser(BaseModel):
    """Model for user login."""
    username: str
    password: str


class SignupUser(LoginUser):
    """Model for user signup, extending LoginUser."""
    full_name: str
