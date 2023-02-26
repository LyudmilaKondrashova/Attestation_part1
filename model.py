import note
import fileoperation
import constants
import datetime

def create_note():
    notes = fileoperation.read_all_notes(constants.note_file_name, False)
    if len(notes) == 0:
        id_note = 1
    else:
        maxId = 0
        for item in notes:
            currentId = item.pop('id')
            if maxId < currentId:
                maxId = currentId
        id_note = maxId + 1
    header = note.get_header()
    text = note.get_text()
    data_note = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    new_note = note.get_note(id_note, header, text, data_note)
    fileoperation.write_file_json(constants.note_file_name, new_note)

def find_note_id():
    find_note = []
    notes = fileoperation.read_all_notes(constants.note_file_name, True)
    print(notes)    ########
    if len(notes) == 0:
        print('Файл заметок пустой!')
        return find_note
    else:
        id = note.get_id()
        if (id <= 0) or (id > len(notes)):
            print('Введено некорректное значение id!')
            return find_note
        else:
            for item in notes:
                item_id = item.pop('id')
                if item_id == id:
                    find_note.append({
                    'id': item_id,
                    'header': item.pop('header'),
                    'text': item.pop('text'),
                    'data': item.pop('data')
                })
    return find_note

def find_note_date():
    find_note = []
    notes = fileoperation.read_all_notes(constants.note_file_name, True)
    print(notes)    ########
    if len(notes) == 0:
        print('Файл заметок пустой!')
        return find_note
    else:
        date = note.get_data()
        for item in notes:
            item_data = item.pop('data')
            if item_data.find(date) != -1:
                find_note.append({
                'id': item.pop('id'),
                'header': item.pop('header'),
                'text': item.pop('text'),
                'data': item_data
                })
    return find_note

def print_note(pr_note):
    print('-------------------------------------------')
    for item in pr_note:
        print('ID: ', item.pop('id'))
        print('ЗАГОЛОВОК: ', item.pop('header'))
        print('ТЕКСТ: ', item.pop('text'))
        print('ДАТА: ', item.pop('data'))
        print('-------------------------------------------')

def print_list_note():
    notes = fileoperation.read_all_notes(constants.note_file_name, True)
    k = 1
    for item in notes:
        print(k, ' ID: ', item.pop('id'), ' ЗАГОЛОВОК: ', item.pop('header'),
        ' ДАТА: ', item.pop('data'))
        k += 1

def print_all_note():
    notes = fileoperation.read_all_notes(constants.note_file_name, True)
    print_note(notes)

def update_note():
    notes = fileoperation.read_all_notes(constants.note_file_name, True)
    update_note = find_note_id()
    print('РЕДАКТИРУЕМАЯ ЗАПИСКА:')
    print_note(update_note)
    print('Введите новые данные:')
    notes[update_note['id']]['header'] = note.get_header()
    notes[update_note['id']]['text'] = note.get_text()
    notes[update_note['id']]['data'] = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    fileoperation.write_file_json_all_notes(constants.note_file_name, notes)
    # if len(notes) == 0:
    #     id_note = 1
    # else:
    #     maxId = 0
    #     for item in notes:
    #         currentId = item.pop('id')
    #         if maxId < currentId:
    #             maxId = currentId
    #     id_note = maxId + 1
    # header = note.get_header()
    # text = note.get_text()
    # data_note = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    # new_note = note.get_note(id_note, header, text, data_note)
    # fileoperation.write_file_json(constants.note_file_name, new_note)
    
def finish_work():
    print('Программа прекращает свою работу!')
    exit()