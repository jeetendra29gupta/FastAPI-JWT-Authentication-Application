from tinydb import TinyDB, Query

# Initialize the TinyDB database
db = TinyDB('user_db.json')
User = Query()


def get_user_by_username(username: str) -> dict:
    """Fetch a user by their username.

    Args:
        username (str): The username of the user.

    Returns:
        dict: User details if found, otherwise None.
    """
    return db.get(User.username == username)


def insert_user(user_details: dict) -> int:
    """Insert a new user into the database.

    Args:
        user_details (dict): A dictionary containing user details.

    Returns:
        int: The ID of the newly created user.
    """
    return db.insert(user_details)


if __name__ == '__main__':
    # output = db.search(User.username == 'juju_raven')
    # print(output)

    # output = db.get(User.username == 'juju_raven')
    #print(output)
    db.remove(User.username == 'test_user')
    for item in db:
        print(item)
        db.remove(User.username == item['username'])