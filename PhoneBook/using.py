from input import get_info
from logger import creating_csv, creating_txt, read_contact

def operate():
    print('Добавить новый контакт\n2. Показать телефонную книгу')
    mode = int(input())
    if mode == 1:
        n = get_info()
        creating_txt(n)
        creating_csv(n)
    elif mode == 2:
        print(read_contact())
    else:
        print('Некорректная команда')