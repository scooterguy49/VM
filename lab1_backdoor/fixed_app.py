users = {
    "alice": {"password": "alice123", "role": "user"},
    "bob": {"password": "bob123", "role": "admin"},
    "charlie": {"password": "charlie123", "role": "user"}
}


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
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in users and users[username]["password"] == password:
        print("\nLogin successful.")
        return username, users[username]["role"]

    print("\nAccess denied.")
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
                view_admin_panel()
            else:
                print("\nAccess denied. Admins only.")

        elif choice == "3":
            print("\nGoodbye.")
            break

        else:
            print("\nInvalid option.")


if __name__ == "__main__":
    main()

