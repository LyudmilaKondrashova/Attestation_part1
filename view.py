# Пользовательские меню

# Главное меню
def menu():
    print("\nВыберите необходимое действие:\n"
    "1. Создать заметку\n"
    "2. Найти заметку\n"
    "3. Вывести список всех заметок (id, заголовок и дата)\n"
    "4. Вывести содержимое всех заметок\n"
    "5. Обновить заметку\n"
    "6. Удалить заметку\n"
    "7. Закончить работу")
    try:
        choice = int(input())
    except ValueError:
        print('Введены некорректные данные! Программа прекращает свою работу!')
        exit()
    return choice

# Меню поиска заметки
def menu_find():
    print("\nВыберите необходимое действие:\n"
    "1. Найти заметку по номеру id\n"
    "2. Найти заметку по дате\n"
    "3. Вернуться назад")
    try:
        choice = int(input())
    except ValueError:
        print('Введены некорректные данные! Программа прекращает свою работу!')
        exit()
    return choice