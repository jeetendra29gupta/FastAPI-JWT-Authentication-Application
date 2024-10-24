import requests


def get_session():
    """Create a requests session with default headers."""
    session = requests.Session()
    session.headers.update({'Content-Type': 'application/json'})
    session.headers.update({'Accept': 'application/json'})
    return session


def welcome(session, base_url):
    """Access the welcome endpoint and handle errors."""
    try:
        response = session.get(f"{base_url}/")

        if response.status_code in [200, 201]:
            return response.json()
        else:
            return {
                "error": f"Error {response.status_code}: {response.text}"
            }
    except Exception as e:
        return {"error": f"An unexpected error occurred during welcome: {e}"}


def signup(session, base_url, user_info):
    """Sign up a new user and handle errors."""
    try:
        response = session.post(f"{base_url}/signup", json=user_info)

        if response.status_code in [200, 201]:
            return response.json()
        else:
            return {
                "error": f"Error {response.status_code}: {response.text}"
            }

    except Exception as e:
        return {"error": f"An unexpected error occurred during signup: {e}"}


def login(session, base_url, user_info):
    """Log in a user and return tokens."""
    try:
        response = session.post(
            f"{base_url}/login",
            json={
                "username": user_info['username'],
                "password": user_info['password']
            }
        )

        if response.status_code in [200, 201]:
            return response.json()
        else:
            return {
                "error": f"Error {response.status_code}: {response.text}"
            }

    except Exception as e:
        return {"error": f"An unexpected error occurred during login: {e}"}


def profile(session, base_url, token):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = session.get(f"{base_url}/protected", headers=headers)

        if response.status_code in [200, 201]:
            return response.json()
        else:
            return {
                "error": f"Error {response.status_code}: {response.text}"
            }

    except Exception as e:
        return {"error": f"An unexpected error occurred during profile: {e}"}


def refresh_token(session, base_url, token):
    try:
        headers = {"Authorization": f"Bearer {token}"}
        response = session.get(f"{base_url}/refresh_token", headers=headers)

        if response.status_code in [200, 201]:
            return response.json()
        else:
            return {
                "error": f"Error {response.status_code}: {response.text}"
            }

    except Exception as e:
        return {"error": f"An unexpected error occurred during refresh token: {e}"}


def main():
    # Base URL for the API
    base_url = "http://localhost:8181"
    session = get_session()

    print("# Call the welcome endpoint")
    welcome_response_output = welcome(session, base_url)
    print(welcome_response_output)
    print()

    print("# Dummy user list")
    juju_raven = {"full_name": "Jeetendra Gupta", "username": "juju_raven", "password": "juju@raven#1814"}
    black_rose = {"full_name": "Sameer Gupta", "username": "black_rose", "password": "black@rose#1814"}
    blue_bird = {"full_name": "Prince Gupta", "username": "blue_bird", "password": "blue@bird#1814"}
    users = [juju_raven, black_rose, blue_bird]
    print(users)
    print()

    print("# Sign up users")
    for user_info in users:
        sign_response_output = signup(session, base_url, user_info)
        print(sign_response_output)
    print()

    print("# Sign up with already users")
    for user_info in users:
        sign_response_output = signup(session, base_url, user_info)
        print(sign_response_output)
    print()

    print("# Log in the given user to get tokens")
    login_response_output = login(session, base_url, juju_raven)
    print(login_response_output)
    print()

    print("# Access protected endpoint")
    access_token = login_response_output.get("access_token")
    profile_response_output = profile(session, base_url, access_token)
    print(profile_response_output)
    print()

    print("# Refresh the access token")
    refresh_token_value = login_response_output.get("refresh_token")
    refresh_response_output = refresh_token(session, base_url, refresh_token_value)
    print(refresh_response_output)
    print()

    print("#Access protected endpoint again with the new access token")
    new_access_token = refresh_response_output.get("access_token")
    profile_response_output = profile(session, base_url, new_access_token)
    print(profile_response_output)
    print()


if __name__ == '__main__':
    main()
