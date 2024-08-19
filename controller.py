import model
import view
import text



def start():
    view.print_message(text.input_hello)
    while True:
        choice = view.main_menu()
        match choice:
            case 1: #Посмотреть список заметок
                view.print_note_all(model.read_file())
            case 2: #Открыть заметку
                nb = model.read_file()
                view.print_note_all(nb)
                index = model.input_index(nb, text.input_index_look)
                view.print_note(index, nb)
            case 3: #Найти заметку (по дате создания)
                nb = model.read_file()
                nb_search = model.search_note(nb)
                view.print_note_all(nb_search)
            case 4: #Добавить заметку
                nb=model.read_file()
                id = model.get_unique_id(nb)
                nb_new = model.input_note(nb, id)
                model.add_note(nb_new)
                view.print_message(text.input_note)
            case 5: #Редактировать заметку
                nb = model.read_file()
                view.print_note_all(nb)
                index = model.input_index(nb, text.edit_note)
                nb_new=model.del_note(nb, index)
                id = model.get_unique_id(nb)
                nb_new = model.input_note(nb, id)
                model.add_note(nb_new)
                view.print_message(text.input_edit_note)
            case 6: #Удалить заметку
                nb = model.read_file()
                view.print_note_all(nb)
                index = model.input_index(nb, text.input_index_del)
                nb_new=model.del_note(nb, index)
                model.add_note(nb_new)
            case 7: #Выход
                view.print_message(text.input_bye)
                break


