import datetime

FRIDAY = 4


def print_menu(name, menu):
    print(name)

    if datetime.datetime.today().weekday() > FRIDAY:
        print('\tData o víkendu jsou nedostupná vzhledem k různému času vystavení menu restauracemi.')
        return

    try:
        menu = menu.get_menu()
        for course, meals in menu.items():
            print(f'\t{course}')
            for meal in meals:
                print(f'\t\t{meal}')
    except Exception as e:
        print(f'\tPro dnešek nebylo nalezeno menu.')
