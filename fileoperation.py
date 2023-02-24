import json

data_note = {}
data_note['notes'] = []

def write_file_json(filelname, notes):
    filejson = open(filelname, 'w', encoding='utf-8')
    json.dump(notes, filejson)
    print('Заметка успешно сохранена в файл заметок')
    filejson.close()

def read_all_notes(filelname):
    filejson = open(filelname)
    with filejson:
        data = json.load(filejson)
        for note in data['notes']:
            data_note['notes'].append({
            'id': note['id'],
            'header': note['header'],
            'text': note['text'],
            'data': note['data']
    })
    filejson.close()
    return data_note