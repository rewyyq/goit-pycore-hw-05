from functools import wraps

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name.capitalize()] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    if contacts[name.capitalize()] in contacts:
        contacts[name.capitalize()] = phone
    else:
        raise KeyError
    return "Contact changed."

@input_error
def find_contact(args, contacts):
    if contacts[args[0].capitalize()] in contacts:
        return contacts[args[0].capitalize()]
    else:
        raise KeyError

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
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
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
