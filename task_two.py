def hello():
    return "How can I help you?"

def add_contact(username, phone, contacts):
    contacts[username] = phone
    return "Contact added."

def change_contact(username, phone, contacts):
    if username in contacts:
        contacts[username] = phone
        return "Contact updated."
    else:
        return "Contact not found."

def show_phone(username, contacts):
    if username in contacts:
        return f"Phone number for {username}: {contacts[username]}"
    else:
        return "Contact not found."

def show_all(contacts):
    if contacts:
        result = "All contacts:\n"
        for username, phone in contacts.items():
            result += f"{username}: {phone}\n"
        return result.strip()
    else:
        return "No contacts found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ").strip().lower()
        command, *args = user_input.split()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print(hello())

        elif command == "add":
            if len(args) == 2:
                username, phone = args
                print(add_contact(username, phone, contacts))
            else:
                print("Invalid 'add' command. Usage: add [username] [phone]")

        elif command == "change":
            if len(args) == 2:
                username, phone = args
                print(change_contact(username, phone, contacts))
            else:
                print("Invalid 'change' command. Usage: change [username] [new_phone]")

        elif command == "phone":
            if len(args) == 1:
                username = args[0]
                print(show_phone(username, contacts))
            else:
                print("Invalid 'phone' command. Usage: phone [username]")

        elif command == "all":
            print(show_all(contacts))

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()