"""
This is a sample code for demonstrating session management and role-based access control.

Note:
Please do not use this code without modifications or think of this as absolute.
The goal is to get everyone thinking in the direction, and provide an ideal usage scenario.
"""

# Session Management
SESSION = {
    'user_id': None,
    'username': None,
    'first_name': None,
    'role': None,  # e.g., 'admin' or 'user'
    'login_status': False
}


# Login and Access Control
def login(username, password):
    # Authenticate user - this is a simplified example -
    # DB-code for verifying user
    # If the user is authticated, retreieve user info from DB, like user role, id, email, name and etc
    if username == "admin":
        SESSION['user_id'] = 1
        SESSION['username'] = username
        SESSION['role'] = 'admin'
        SESSION['login_status'] = True
        print("Logged in as admin")
    elif username == "user":
        SESSION['user_id'] = 2
        SESSION['username'] = username
        SESSION['role'] = 'user'
        SESSION['login_status'] = True
        print("Logged in as user")
    else:
        print("Invalid credentials")


# Role-Based Access Control
def is_logged_in():
    if SESSION['login_status']:
        return True
    return False


def is_user_admin():
    if SESSION['role'] == 'admin':
        return True
    return False


def checkout():
    if is_logged_in():
        print("Proceed to checkout")
    else:
        print("Please log in to checkout")


def view_admin_panel():
    if is_user_admin():
        print("Welcome to the admin panel")
    else:
        print("Access denied: Admins only")
