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


def exit(*args):
    note_book.save_to_file()
    return 'Bye'


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


choices = {add_note: 'add note',
            show_notes: 'show notes',
            add_tag: 'add tag',
            remove_note: 'remove note',
            get_notes: 'note'}