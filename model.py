import note
import fileoperation
import constants
import datetime

def create_note():
    notes = fileoperation.read_all_notes(constants.note_file_name)
    # print(notes)
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
    data_note = str(datetime.datetime.now())
    new_note = note.get_note(id_note, header, text, data_note)
    fileoperation.write_file_json(constants.note_file_name, new_note)

def find_note_id():
    find_note = []
    notes = fileoperation.read_all_notes(constants.note_file_name)
    print(notes)    ########
    if len(notes) == 0:
        print('Файл заметок пустой!')
        return find_note
    else:
        id = note.get_id()
        for item in notes:
            if item.pop('id') == id:
                find_note.append({
                'header': item.pop('header'),
                'text': item.pop('text'),
                'data': item.pop('data')
            })
    return find_note

def print_note(pr_note):
    print('ЗАГОЛОВОК: ', pr_note[0].pop('header'))
    print('ТЕКСТ: ', pr_note[0].pop('text'))
    print('ДАТА: ', pr_note[0].pop('data'))