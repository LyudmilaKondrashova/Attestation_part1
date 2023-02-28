# Операции с заметками
import note
import fileoperation
import constants
import datetime

# Создание новой заметки
def create_note():
    notes = fileoperation.read_all_notes(constants.note_file_name)
    
    # Определяем id создаваемой заметки
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

# Поиск заметки по id
def find_note_id():
    find_note = []
    notes = fileoperation.read_all_notes(constants.note_file_name, True)
    if len(notes) == 0:
        print('Файл заметок пустой!')
        return find_note
    else:
        id = note.get_id()
        if (id <= 0):
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

# Поиск заметки по дате
def find_note_date():
    find_note = []
    notes = fileoperation.read_all_notes(constants.note_file_name, True)
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

# Печать найденных заметок для задачи поиска заметки
def print_note(pr_note):
    print('-------------------------------------------')
    for item in pr_note:
        print('ID: ', item.pop('id'))
        print('ЗАГОЛОВОК: ', item.pop('header'))
        print('ТЕКСТ: ', item.pop('text'))
        print('ДАТА: ', item.pop('data'))
        print('-------------------------------------------')
    
# Печать заметки исходной заметки для задачи обновления заметки с заданным id
def print_update_note(pr_note):
    print('-------------------------------------------')
    id = pr_note[0].pop('id')
    print('ID: ', id)
    print('ЗАГОЛОВОК: ', pr_note[0].pop('header'))
    print('ТЕКСТ: ', pr_note[0].pop('text'))
    print('ДАТА: ', pr_note[0].pop('data'))
    print('-------------------------------------------')
    return id

# Печать списка заметок (id, заголовок и дата заметки)
def print_list_note():
    notes = fileoperation.read_all_notes(constants.note_file_name, True)
    k = 1
    for item in notes:
        print(k, ' ID: ', item.pop('id'), ' ЗАГОЛОВОК: ', item.pop('header'),
        ' ДАТА: ', item.pop('data'))
        k += 1

# Печать содержимого всех заметок
def print_all_note():
    notes = fileoperation.read_all_notes(constants.note_file_name, True)
    print_note(notes)

# Редактирование заметки с заданным id
def update_note():
    notes = fileoperation.read_all_notes(constants.note_file_name, True)
    update_notes = {}
    update_notes['notes'] = []
    update_note = find_note_id()
    if len(update_note) == 0:
        print('Программа прекращает свою работу')
        exit()
    print('\nРЕДАКТИРУЕМАЯ ЗАМЕТКА:')
    update_id = print_update_note(update_note)
    print('ВВЕДИТЕ НОВЫЕ ДАННЫЕ:')
    for item in notes:
        item_id = item.pop('id')
        if item_id != update_id:
            update_notes['notes'].append({
                'id': item_id,
                'header': item.pop('header'),
                'text': item.pop('text'),
                'data': item.pop('data')
                })
        else:
            update_notes['notes'].append({
                'id': update_id,
                'header': note.get_header(),
                'text': note.get_text(),
                'data': datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                })
    fileoperation.write_file_json_all_notes(constants.note_file_name, update_notes)
    print('Заметка успешно отредактирована в файле заметок')

# Удаление заметки с заданным id
def delete_note():
    notes = fileoperation.read_all_notes(constants.note_file_name, True)
    new_notes = {}
    new_notes['notes'] = []
    delete_note = find_note_id()
    if len(delete_note) == 0:
        print('Программа прекращает свою работу')
        exit()
    delete_id = delete_note[0].pop('id')
    for item in notes:
        item_id = item.pop('id')
        if item_id != delete_id:
            new_notes['notes'].append({
                'id': item_id,
                'header': item.pop('header'),
                'text': item.pop('text'),
                'data': item.pop('data')
                })
    fileoperation.write_file_json_all_notes(constants.note_file_name, new_notes)
    print('Заметка успешно удалена в файле заметок')
        
# Завершение работы
def finish_work():
    print('Программа прекращает свою работу!')
    exit()