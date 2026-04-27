import re

# List of suspicious patterns (basic "signature-based detection")
SUSPICIOUS_PATTERNS = [
    r"os\.system",
    r"subprocess",
    r"eval\(",
    r"exec\(",
    r"__import__",
    r"open\(",
    r"rm ",
    r"del ",
]

def is_malicious(user_input):
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, user_input):
            return True
    return False

def greet():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

def add():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a + b)
    except ValueError:
        print("Error: Please enter valid integers.")

def subtract():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result:", a - b)
    except ValueError:
        print("Error: Please enter valid integers.")

def show_help():
    print("""
Available commands:
- greet     : Greet the user
- add       : Add two integers
- subtract  : Subtract two integers
- help      : Show this help menu
- exit      : Exit the program
""")

def main():
    print("=== Virus Scanner Simulation ===")
    print("Type 'help' to see commands.\n")

    while True:
        user_input = input(">>> ")

        # Virus scanning step
        if is_malicious(user_input):
            print("⚠️ WARNING: Malicious command detected and blocked!")
            continue

        # Command handling
        if user_input == "greet":
            greet()
        elif user_input == "add":
            add()
        elif user_input == "subtract":
            subtract()
        elif user_input == "help":
            show_help()
        elif user_input == "exit":
            print("Exiting program...")
            break
        else:
            print("Unknown command. Type 'help' for options.")

if __name__ == "__main__":
    main()