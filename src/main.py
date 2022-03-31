from src.sites import *

if __name__ == '__main__':
    for course, meals in jina_krajina.get_menu().items():
        print(course)
        for meal in meals:
            print(f'\t{meal}')
