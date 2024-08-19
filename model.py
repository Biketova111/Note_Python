import os
import csv
import text
import view
import datetime


noteboke: list[dict[str, str]]=[]
path = 'notebook.csv'

if not os.path.exists(path): #Создание файла при его отсутствии
    nb = open(path, 'w')
    nb.close()

def read_file(): #Чтение файла, сортировка по дате
    noteboke=[]
    with open(path, 'r', encoding='UTF-8') as file:
        file_reader = csv.reader(file, delimiter=';')
        for row in file_reader:
            noteboke.append({'id':int(row[0]), 'tituler': row[1], 'body':row[2], 'date':row[3]})
        result_nb = sorted(noteboke, key=lambda x: datetime.datetime.strptime(x['date'], '%d.%m.%Y'))
    return result_nb

def input_index(nb: list[dict[str, str]], message: str) -> int: #Получение индекса заметки
    if nb:
        while True:
            index = input(message)
            if index.isdigit and 0 <int(index) < len(nb)+1:
                return int(index)

def get_unique_id(nb: list[dict[str, str]]) -> int: #Получение иникального id
    result= list(sorted(item['id'] for item in nb))
    unique_id = 1
    for i in range(len(result)):
        if unique_id == result[i]:
            unique_id+=1
    return int(unique_id)
    

def input_note(nb: list[dict[str, str]], id): #Создание новой заметки
    view.print_message(text.new_note)
    nb.append({'id':id,
                'tituler':input(text.input_new_tituler),
                'body':input('\n' + text.input_new_body),
                'date':datetime.datetime.now().strftime('%d.%m.%Y')})
    return nb

def add_note(nb: list[dict[str, str]]): #Запись файла
     with open(path, 'w', encoding='UTF-8') as file:
        names = ['id', 'tituler', 'body', 'date']
        file_write = csv.DictWriter(file, delimiter=';', lineterminator='\r', fieldnames=names)
        file_write.writerows(nb)
        
def search_note (nb: list[dict[str, str]]): #Поиск заметки по дате
    if nb:
        date = input(text.input_date)
        result_note = list(filter(lambda x: x.get('date')==date, nb))
        return result_note

def del_note(nb: list[dict[str, str]], index: int): #Удаление заметки
    if nb:
        nb.pop(index-1)
        return nb
   
   
