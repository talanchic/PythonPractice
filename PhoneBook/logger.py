from input import get_info as info

def read_contact():
    with open('Phonebook.csv', 'r', encoding ='utf-8') as f:
        return f.read()

def creating_csv(info):
    file = 'Phonebook.csv'
    with open(file, 'a', encoding ='utf-8') as data:
        data.write(f'Имя: {info[0]}; Фамилия: {info[1]}; телефон: {info[2]}; доп. информация: {info[3]}\n' )

def creating_txt(info):
    file2 = 'Phonebook.txt'
    with open(file2, 'a', encoding = 'utf-8') as data:
        data.write(f'Имя: {info[0]}\nФамилия: {info[1]}\nтелефон: {info[2]}\nдоп. информация: {info[3]}\n\n' )
