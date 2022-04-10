def print_menu(name, menu):
    print(name)
    try:
        menu = menu.get_menu()
        for course, meals in menu.items():
            print(f'\t{course}')
            for meal in meals:
                print(f'\t\t{meal}')
    except Exception as e:
        print(f'\tFollowing error occurred getting the menu: {e}')
