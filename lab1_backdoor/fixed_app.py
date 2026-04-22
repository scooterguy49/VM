from datetime import datetime

users = {
    "alice": {"password": "alice123", "role": "user"},
    "bob": {"password": "bob123", "role": "admin"},
    "charlie": {"password": "charlie123", "role": "user"}
}

MAX_LOGIN_ATTEMPTS = 3
LOG_FILE = "lab1_audit.log"


def log_event(event_type, username, details=""):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(f"[{timestamp}] {event_type} | User: {username} | {details}\n")


def display_menu():
    print("\nSystem Menu")
    print("1. View Profile")
    print("2. View Admin Panel")
    print("3. Exit")


def view_profile(username, role):
    print(f"\nWelcome, {username}.")
    print(f"Your role is: {role}")


def view_admin_panel():
    print("\n*** ADMIN PANEL ***")
    print("Sensitive configuration settings")
    print("User management tools")
    print("System security options")


def login():
    print("=== Secure Access Portal ===")

    attempts = 0

    while attempts < MAX_LOGIN_ATTEMPTS:
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        if username in users and users[username]["password"] == password:
            print("\nLogin successful.")
            log_event("LOGIN_SUCCESS", username, f"Role: {users[username]['role']}")
            return username, users[username]["role"]

        attempts += 1
        remaining = MAX_LOGIN_ATTEMPTS - attempts

        log_event(
            "LOGIN_FAILURE",
            username if username else "UNKNOWN",
            f"Invalid credentials. Remaining attempts: {remaining}"
        )

        print("\nAccess denied.")
        if remaining > 0:
            print(f"Remaining login attempts: {remaining}")

    log_event("ACCOUNT_LOCKOUT", username if username else "UNKNOWN", "Maximum login attempts exceeded")
    print("\nToo many failed login attempts. Access has been locked.")
    return None, None


def main():
    username, role = login()

    if username is None:
        return

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_profile(username, role)

        elif choice == "2":
            if role == "admin":
                log_event("ADMIN_PANEL_ACCESS", username, "Authorized admin access")
                view_admin_panel()
            else:
                log_event("ADMIN_PANEL_DENIED", username, "Unauthorized admin panel attempt")
                print("\nAccess denied. Admins only.")

        elif choice == "3":
            log_event("LOGOUT", username, "User exited the program")
            print("\nGoodbye.")
            break

        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    main()
