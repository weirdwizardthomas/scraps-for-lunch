from src.sites import *

if __name__ == '__main__':

    print('Jina krajina')
    for course, meals in jina_krajina.get_menu().items():
        print(f'\t{course}')
        for meal in meals:
            print(f'\t\t{meal}')

    print('Pricny rez')
    for course, meals in pricny_rez.get_menu().items():
        print(f'\t{course}')
        for meal in meals:
            print(f'\t\t{meal}')

    print('Kathmandu')
    for course, meals in kathmandu.get_menu().items():
        print(f'\t{course}')
        for meal in meals:
            print(f'\t\t{meal}')