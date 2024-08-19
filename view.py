import text


def main_menu() -> int: #Вывод главного меню
    print('\n' + '='*34)
    print(text.main_menu)
    print('='*34)
    while True:
        choice = input(f'\n {text.input_choice}')
        if choice.isdigit() and 0 < int(choice)< 8:
            return int(choice)
        
def print_message(message: str): #Вывод информационного сообщения
    print('\n' + '='*len(message))
    print(message)
    print('='*len(message) + '\n')

def print_note_all(nb: list[dict[str, str]]): #Вывод списка заметок
    if nb:
        print('\n' + '='*76)
        for i, note in enumerate(nb, 1):
            print(f'{i:>4}. {note.get('id'):>3} | {note.get('tituler'):>20} | {note.get('body'):>30} | {note.get('date'):>10}')
        print('='*76+'\n')
    else:
        print_message(text.load_error)


def print_note (index: int, nb: list[dict[str, str]]): #Вывод выбранной заметки
    if nb:
        for i, note in enumerate(nb, 1):
            if i == index:
                print_message(note.get('body'))   



        

