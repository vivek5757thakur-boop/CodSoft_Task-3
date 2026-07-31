import random
import string


def generate_password(length):
    characters = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=" * 40)
    print("      PASSWORD GENERATOR")
    print("=" * 40)

    while True:
        try:
            length = int(input("Enter password length: "))

            if length < 4:
                print("Password length should be at least 4.\n")
                continue

            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

        except ValueError:
            print("Please enter a valid number.")
            continue

        choice = input("\nGenerate another password? (y/n): ").lower()

        if choice != "y":
            print("\nThank you for using Password Generator!")
            break


if __name__ == "__main__":
    main()
