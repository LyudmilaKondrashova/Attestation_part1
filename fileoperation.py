# Операции с файлом заметок
import json

# Запись в файл для задачи создания новой заметки
def write_file_json(filelname, note):
    try:
        with open(filelname, encoding='utf-8') as filejson:
            try:
                data = json.load(filejson)
            except json.decoder.JSONDecodeError as err:
                data = {}
                data['notes'] = []            
    except FileNotFoundError as err:
        data = {}
        data['notes'] = []
    data['notes'].append(note)
    with open(filelname, 'w', encoding='utf-8') as filejson:
        json.dump(data, filejson, ensure_ascii = False, indent = 2)
    print('Заметка успешно сохранена в файл заметок')
    filejson.close()

# Запись в файл для задачи редактирования заметки
def write_file_json_all_notes(filelname, notes):
    with open(filelname, 'w', encoding='utf-8') as filejson:
        json.dump(notes, filejson, ensure_ascii = False, indent = 2)
    filejson.close()

# Чтение всех заметок из файла
def read_all_notes(filelname, flag_operation = False):
    data_note = []
    try:
        with open(filelname, encoding='utf-8') as filejson:
            try:
                data = json.load(filejson)
            except json.decoder.JSONDecodeError as err:
                return data_note
        for item in data['notes']:
            data_note.append({
            'id': item.pop('id'),
            'header': item.pop('header'),
            'text': item.pop('text'),
            'data': item.pop('data')
            })
        filejson.close()
    except FileNotFoundError as err:
        if not flag_operation:
            return data_note
        else:
            print('Файл заметок отсутствует! Программа прекращает свою работу!')
            exit()
    return data_note