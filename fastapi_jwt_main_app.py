import uvicorn
from fastapi import FastAPI, HTTPException, Header, status

from database import get_user_by_username, insert_user
from models import SignupUser, LoginUser
from utils import hash_password, verify_password, create_token, get_current_user

app = FastAPI()


@app.get("/", response_model=dict)
async def index() -> dict:
    """Welcome endpoint.

    Returns:
        dict: A welcome message.
    """
    return {"status_code": status.HTTP_200_OK, "detail": "Welcome to FastAPI JWT Application"}


@app.post("/signup", response_model=dict, status_code=status.HTTP_201_CREATED)
async def signup(user: SignupUser) -> dict:
    """User signup endpoint.

    Args:
        user (SignupUser): The user signup data.

    Returns:
        dict: A success message and user details.

    Raises:
        HTTPException: If the username is already registered.
    """
    # Check if the username is already taken
    if get_user_by_username(user.username):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=f"Username: {user.username}, already registered")

    # Prepare user data for insertion
    user_details = {
        "full_name": user.full_name,
        "username": user.username,
        "hashed_password": hash_password(user.password),
    }

    user_id = insert_user(user_details)

    return {
        "detail": f"User created successfully, user ID {user_id}!",
        "user": {"full_name": user.full_name, "username": user.username},
    }


@app.post("/login", response_model=dict)
async def login(user: LoginUser) -> dict:
    """User login endpoint.

    Args:
        user (LoginUser): The user login data.

    Returns:
        dict: Access and refresh tokens.

    Raises:
        HTTPException: If the credentials are invalid.
    """
    user_details = get_user_by_username(user.username)

    # Validate user credentials
    if not user_details or not verify_password(user.password, user_details['hashed_password']):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    # Create access and refresh tokens
    access_token = create_token({"sub": user.username}, "access")
    refresh_token = create_token({"sub": user.username}, "refresh")

    return {
        "token_type": "bearer",
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


@app.get("/protected")
async def protected(authorization: str = Header(...)) -> dict:
    """Protected endpoint requiring a valid token.

    Args:
        authorization (str): The authorization header containing the token.

    Returns:
        dict: A welcome message with the username.

    Raises:
        HTTPException: If the authorization code is invalid.
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authorization code")

    token = authorization.split(" ")[1]
    current_user = await get_current_user(token)
    return {"message": f"Welcome, {current_user}!"}


@app.get("/refresh_token")
async def refresh_user_token(authorization: str = Header(...)) -> dict:
    """Refresh access and refresh tokens.

    Args:
        authorization (str): The authorization header containing the token.

    Returns:
        dict: New access and refresh tokens.

    Raises:
        HTTPException: If the authorization code is invalid.
    """
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authorization code")

    token = authorization.split(" ")[1]
    current_user = await get_current_user(token)

    # Create new tokens
    access_token = create_token({"sub": current_user}, "access")
    refresh_token = create_token({"sub": current_user}, "refresh")

    return {
        "token_type": "bearer",
        "access_token": access_token,
        "refresh_token": refresh_token,
    }


if __name__ == '__main__':
    uvicorn.run("fastapi_jwt_main_app:app", host="0.0.0.0", port=8181, reload=True)
