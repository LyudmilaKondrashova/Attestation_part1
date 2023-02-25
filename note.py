def get_id():
    id = int(input('Введите id искомой заметки: '))
    return id

def get_header():
    header = input('Введите заголовок заметки: ')
    return header

def get_text():
    text = input('Введите содержимое заметки: ')
    return text

def get_note(id, header, text, data):
    new_note = {}
    new_note['id'] = id
    new_note['header'] = header
    new_note['text'] = text
    new_note['data'] = data
    return new_note