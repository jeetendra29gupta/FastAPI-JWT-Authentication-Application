import os
from datetime import datetime, timedelta

import bcrypt
from dotenv import load_dotenv
from fastapi import HTTPException
from jose import JWTError, jwt

# Load environment variables
load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY", "Secret_Key-2024")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 7))

def hash_password(password: str) -> str:
    """Hash a password using bcrypt.

    Args:
        password (str): The plain text password.

    Returns:
        str: The hashed password.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verify a plain text password against a hashed password.

    Args:
        plain_password (str): The plain text password.
        hashed_password (str): The hashed password.

    Returns:
        bool: True if the password matches, otherwise False.
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


def create_token(data: dict, token_type: str) -> str:
    """Create a JWT token.

    Args:
        data (dict): The payload data for the token.
        token_type (str): Type of token, either "access" or "refresh".

    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()
    expire_time = (
        datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        if token_type == "access"
        else datetime.now() + timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    )
    to_encode.update({"exp": expire_time})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_current_user(token: str) -> str:
    """Get the current user's username from the token.

    Args:
        token (str): The JWT token.

    Returns:
        str: The username of the current user.

    Raises:
        HTTPException: If token is invalid or expired.
    """
    credentials_exception = HTTPException(status_code=401, detail="Could not validate credentials")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return username
