from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me command, name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
    return inner

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name.capitalize() not in contacts:
        raise KeyError
    else:
        contacts[name.capitalize()] = phone
    return "Contact changed."

@input_error
def find_contact(args, contacts):
    name = args[0]
    name = name.capitalize()
    if name in contacts:
        return contacts[name]
    raise KeyError

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ").strip()
        if not user_input:
            print("Empty command")
            continue
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(find_contact(args, contacts))
        elif command == "all":
            if contacts:
                print(contacts)
            else:
                print("Contacts are empty")
        elif user_input:
            print(f"Unknown command: '{user_input}'")

if __name__ == "__main__":
    main()
