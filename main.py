from bot import AddressBook, actions as contacts_actions
from sorter import sorter
from note import Note, NameNote, NoteBook, Text



note_book = NoteBook()
note_book.recover_from_file()


def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except ValueError:
            return 'Not enough params. Type help.'
    return inner


@input_error
def list_of_params(*args):
    conteiner = args[0].split()

    if not conteiner:
        raise ValueError
    
    return conteiner


def incorrect_application(*args):
    return "No such application!"


def close(*args):
    note_book.save_to_file()
    return "Good bye!"


def initialize_addressbook():

    address_book = AddressBook()

    print("Choose command: <show all>, <add>, <update>, <mail>, <update birthday>, <check birthday>, <iterator>, <find>, <delete> or <up> to get back to menu.")
    print("Phone should be in format <095-123-45-67> or <095 123 45 67>")
    print("Date should be in format <01.01.2000>")

    while True:
        print("-" * 50)
        command = input("Type command >>>>> ").strip()

        handler_response = handler(command, contacts_actions)
        func = handler_response[0]
        args = handler_response[1]

        result = func(address_book, args)

        if command in ["up"]:
            print("Now you are back to main menu!")
            break

        if result:
            print(result)


"""This block you can delete"""
# def initialize_notebook():

#     # notebook = NoteBook()

#     print("Choose command: .")  # here must be added commands for working with notebook

#     while True:
#         print("-" * 50)
#         command = input("Type command >>>>> ").strip()

#         # # uncomment when NoteBook is ready:
#         # handler_response = handler(command, notebook_actions)
#         # func = handler_response[0]
#         # args = handler_response[1]
#         #
#         # result = func(notebook, args)
#         #

#         if command in ["up"]:
#             print("Now you are back to main menu!")
#             break

#         # if result:
#         #     print(result)


def start_work_with_files():

    print("Enter to sorting or input command <up> to back to main menu!")

    while True:
        print("-" * 50)
        command = input("Push enter to start sorting or input command <up> to back to main menu! >>>>> ").strip()
        
        

        if command in ["up"]:
            print("Now you are back to main menu!")
            break
        
        sorter()



@input_error
def add_note(*args):
    lst = list_of_params(*args)

    if len(lst) > 1:
        note_book.add_notes(Note(NameNote(lst[0]), Text(' '.join(lst[1:]))))

        if lst[0] in [k for k in note_book.keys()]:
            note_book.get(lst[0]).add_tag(input('Please enter the tag for this note: ').split(', '))

        return f'Note {lst[0]} was added'
    else:
        raise ValueError


def show_notes(*args):
    gen_obj = note_book.paginator(note_book)
    for i in gen_obj:
        print('*' * 50)
        print(i)
        input('Press any key')
    return "You don't have more notes"


@input_error
def add_tag(*args):
    lst = list_of_params(*args)
    print(lst[0])
    if len(lst) > 1:
        note_book.get(lst[0]).add_tag(lst[1:])
        return f'Note {lst[0]} was update'
    else:
        raise ValueError
    
    
@input_error
def get_notes(*args):
    lst = list_of_params(*args)
    list_of_notes = {}
    
    for k, v in note_book.items():
        if lst[0] == k:
            return f'{lst[0]}: {v.text}'
        
        if str(v.text).startswith(lst[0]):
            list_of_notes.update({k: v.text})
        
        if k.startswith(lst[0]):
            list_of_notes.update({k: v.text})

    if list_of_notes:
        return list_of_notes
    return f'Not notes that start with {lst[0]}'


def remove_note(*args):
    note_book.pop(args[0])
    return f'Note {args[0]} was delete'
        


choices = {
    "contacts": initialize_addressbook,
    # "notebook": initialize_notebook,
    "files": start_work_with_files,
    "incorrect_application": incorrect_application,
    'add note': add_note,
    'show notes': show_notes,
    'add tag': add_tag,
    'remove note': remove_note,
    'note': get_notes,
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
    return actions.get("incorrect_command"), None


def main():

    while True:
        print("-" * 50)
        command = input("With what do you want to work? Type <contacts>, <notebook> or <files>. Or type <exit> to quit bot. >>>>> ").strip()
        choice, function = menu_handler(command)

        result = function()
        if result:
            print(result)

        if command in ["close", "exit", "good bye"]:
            break


if __name__ == "__main__":
    main()
