import view
import model

def button_click():
    us_choice = view.menu()
    user_choice(us_choice)

def user_choice(us_ch):
    if us_ch  < 1 or us_ch > 7:
        print('Введено некорректное значение! Попробуйте еще раз!')
        button_click()
    else:
        if us_ch == 1:  # Создать заметку
            model.create_note()
            print('*******************************************')
            button_click()
        elif us_ch == 2:    # Найти заметку
            flag = False
            while not flag:
                us_ch_find = view.menu_find()
                if us_ch_find  < 1 or us_ch_find > 3:
                    print('Введено некорректное значение! Попробуйте еще раз!')
                else:
                    flag = True
            find_note = user_choice_find(us_ch_find)
            if len(find_note) != 0:
                print('\nИСКОМАЯ ЗАМЕТКА:')
                model.print_note(find_note)
                print('*******************************************')
                button_click()
            else:
                print('Не найдено заметок, удовлетворяющих условиям поиска!')
                button_click()
        elif us_ch == 3:    # Вывести список всех заметок (id, заголовок и дата)
            print('\nСписок всех заметок (id, заголовок и дата):')
            model.print_list_note()
            print('*******************************************')
            button_click()
        elif us_ch == 4:    # Вывести содержимое всех заметок
            model.print_all_note()
            print('*******************************************')
            button_click()
        elif us_ch == 5:    # Обновить заметку
            model.update_note()
            print('*******************************************')
            button_click()
        else:
            model.finish_work()

def user_choice_find(us_ch_fd):
    if us_ch_fd == 1:  # Найти заметку по номеру id
        return model.find_note_id()
    elif us_ch_fd == 2:    # Найти заметку по дате
        return model.find_note_date()
    else:
        print('*******************************************')
        button_click()