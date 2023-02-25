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
            print('ИСКОМАЯ ЗАМЕТКА:')
            # print(find_note)
            model.print_note(find_note)
    #     elif us_ch == 3:
    #         model.find_subscriber_phone()
    #     elif us_ch == 4:
    #         model.new_subscriber()
    #     elif us_ch == 5:
    #         model.save_to_text()
    #     else:
    #         model.finish_work()

def user_choice_find(us_ch_fd):
    if us_ch_fd == 1:  # Найти заметку по номеру id
        return model.find_note_id()
        #     button_click()
        # elif us_ch == 2:    # Найти заметку
        #     us_ch_find = view.menu_find()
        #     model.find_subscriber_surname()
    #     elif us_ch == 3:
    #         model.find_subscriber_phone()
    #     elif us_ch == 4:
    #         model.new_subscriber()
    #     elif us_ch == 5:
    #         model.save_to_text()
    #     else:
    #         model.finish_work()