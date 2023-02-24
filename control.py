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
        if us_ch == 1:
            model.create_note()
            button_click()
    #     elif us_ch == 2:
    #         model.find_subscriber_surname()
    #     elif us_ch == 3:
    #         model.find_subscriber_phone()
    #     elif us_ch == 4:
    #         model.new_subscriber()
    #     elif us_ch == 5:
    #         model.save_to_text()
    #     else:
    #         model.finish_work()