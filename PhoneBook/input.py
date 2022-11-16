def get_info ():
    info = []
    name = input('Укажите имя: ')
    info.append(name)
    surname = input('Укажите фамилию: ')
    info.append(surname)
    phone = input('Укажите телефон: ')
    info.append(phone)
    about = input('Дополинтельная информация: ')
    info.append(about)
    return info
