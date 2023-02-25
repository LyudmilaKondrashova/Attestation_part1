import json

def write_file_json(filelname, note):
    with open(filelname, encoding='utf-8') as filejson:
        try:
            data = json.load(filejson)
        except json.decoder.JSONDecodeError as err:
            data = {}
            data['notes'] = []
        data['notes'].append(note)
    with open(filelname, 'w', encoding='utf-8') as filejson:
        json.dump(data, filejson, ensure_ascii = False, indent = 2)
    print('Заметка успешно сохранена в файл заметок')
    filejson.close()

def read_all_notes(filelname):
    data_note = []
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
    return data_note