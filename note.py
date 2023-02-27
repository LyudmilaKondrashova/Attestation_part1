# Ввод данных заметки

# Ввод id заметки
def get_id():
    id = int(input('Введите id заметки: '))
    return id

# Ввод заголовка заметки
def get_header():
    header = input('Введите заголовок заметки: ')
    return header

# Ввод содержимого заметки
def get_text():
    text = input('Введите содержимое заметки: ')
    return text

# Ввод даты заметки для задачи поиска заметки по дате
def get_data():
    print('Введите дату заметки:')
    flag = False
    while not flag:
        year = input('Введите год (4 цифры): ')
        if (len(year) != 4) or (year[0] == '0'):
            print('Год введен некорректно! Попробуйте ввести еще раз!')
        else:
            flag = True
    flag = False
    while not flag:
        month = input('Введите номер месяца (от 1 до 12): ')
        if (len(month) == 0) or (len(month) > 2) or (int(month) < 1) or (int(month) > 12):
            print('Месяц введен некорректно! Попробуйте ввести еще раз!')
        else:
            flag = True
    flag = False               
    month30 = [4, 6, 9, 11]
    while not flag:
        day = input('Введите день месяца: ')
        if (len(day) > 2) or (len(day) == 0) or (int(day) < 1) or (int(day) > 31):
            print('День месяца введен некорректно! Попробуйте ввести еще раз!')
        elif (int(month) in month30) and (int(day) == 31):
            print('День месяца введен некорректно! Попробуйте ввести еще раз!')
        elif (int(month) == 2):
            if (int(year) % 4 == 0) and (int(day) > 29):
                print('День месяца введен некорректно! Попробуйте ввести еще раз!')
            elif (int(year) % 4 != 0) and (int(day) > 28):
                print('День месяца введен некорректно! Попробуйте ввести еще раз!')
            else:
                flag = True
        else:
            flag = True
    if len(month) == 1:
        month = '0' + month
    if len(day) == 1:
        day = '0' + day
    data = day + '-' + month + '-' + year
    return data

# Фомирование заметки с заданными id, заголовком, содержимым и датой
def get_note(id, header, text, data):
    new_note = {}
    new_note['id'] = id
    new_note['header'] = header
    new_note['text'] = text
    new_note['data'] = data
    return new_note