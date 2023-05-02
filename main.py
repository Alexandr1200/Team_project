from bot import AddressBook, actions as contacts_actions
from note import NoteBook, choices as notebook_actions
from sorter import sorter


def incorrect_application(*args):
    return "No such application!"


def incorrect_command(*args):
    return "No such command! Enter another one!"


def close(*args):
    return "Good bye!"


def initialize_addressbook():

    # commands_completer = get_commands_from_actions(contacts_actions)
    address_book = AddressBook()

    print("Choose command: <show all>, <add>, <update>, <mail>, <update birthday>, <check birthday>, <iterator>, <find>, <delete> or <up> to get back to menu.")
    print("Phone should be in format <095-123-45-67> or <095 123 45 67>")
    print("Date should be in format <01.01.2000>")

    while True:
        print("-" * 50)

        # command = prompt('Type command >>>>> ', completer=commands_completer).strip()
        command = input('Type command >>>>> ').strip()

        handler_response = handler(command, contacts_actions)
        func = handler_response[0]
        args = handler_response[1]

        result = func(address_book, args)

        if command in ["up"]:
            print("Now you are back to main menu!")
            break

        if result:
            print(result)


def initialize_notebook():

    notebook = NoteBook()
    notebook.recover_from_file()

    print("Choose command: <add note>, <show notes>, <add tag>, <remove note> or <note>.")

    while True:
        print("-" * 50)
        command = input("Type command >>>>> ").strip()

        handler_response = handler(command, notebook_actions)
        func = handler_response[0]
        args = handler_response[1]

        result = func(notebook, args)

        if command in ["up"]:
            print("Now you are back to main menu!")
            notebook.save_to_file()
            break

        if result:
            print(result)


def start_work_with_files():

    print("Enter to sorting or input command <up> to back to main menu!")

    while True:
        print("-" * 50)
        command = input("Push enter to start sorting or input command <up> to back to main menu! >>>>> ").strip()

        if command in ["up"]:
            print("Now you are back to main menu!")
            break
        
        sorter()


choices = {
    "contacts": initialize_addressbook,
    "notebook": initialize_notebook,
    "files": start_work_with_files,
    "incorrect_application": incorrect_application,
    "close": close,
    "exit": close,
    "good bye": close,
}


def menu_handler(string):
    command = string.lower()

    for choice, function in choices.items():
        if command.startswith(choice):
            return choice, function

    return None, choices.get("incorrect_application")


def handler(string, actions):
    command = string.lower()

    for action, func in actions.items():
        if command.startswith(action):
            args = string[len(action):].strip().split(' ')
            args = list(filter(lambda x: x.strip() if x else None, args))
            return func, args
    return incorrect_command, None


def main():

    while True:
        print("-" * 50)
        command = input('With what do you want to work? Type <contacts>, <notebook> or <files>. Or type <exit> to quit bot. >>>>> ').strip()
        choice, function = menu_handler(command)

        result = function()
        if result:
            print(result)

        if command in ["close", "exit", "good bye"]:
            break


if __name__ == "__main__":
    main()
