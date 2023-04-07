# Создать телефонный справочник
# согласно структуре: Ф, И, О, номер телефона

# Программа должна уметь:
# - вводить и сохранять данные
# - выводить данные на печать
# - осуществлять поиск (например, по имени или фамилии человека)
# - изменение данных
# - удаление данных

# Программа не должна быть линейной


def add_new_contact():
    lastname = input('Введите фамилию: ')
    firstname = input('Введите имя: ')
    middlename = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    with open('boook.txt','a') as f:
        f.write(f"{lastname}, {firstname}, {middlename}, {phone}\n")
    print('Новая запись успешно добавлена')


def delete_record():
    search_lastname = input('Введите фамилию записи, которую необходимо удалить: ')
    with open('boook.txt','r') as f:
        contacts = f.readlines()
    with open('boook.txt','w') as f:
        deleted = False
        for contact in contacts:
            if not search_lastname in contact:
                f.write(contact)
            else:
                deleted = True
            if deleted:
                print('Запись успешно удалена.')
            else:
                print('Запись не найдена.')


def search_by_lastname():
    search_lastname = input('Введите фамилию для поиска: ')
    with open('boook.txt','r') as f:
        found = False
        for line in f:
            if search_lastname in line:
                print(line.strip())
                found = True
            if not found:
                print('Запись не найдена.')


def edit_contact():
    search_lastname = input('Введите фамилию записи, которую необходимо изменить: ')
    with open('boook.txt','r') as f:
        contacts = f.readlines()
    with open('boook.txt','w') as f:
        edited = False
        for contact in contacts:
            if not search_lastname in contact:
                f.write(contact)
            else:
                lastname, firstname, middlename, phone = contact.strip().split(',')
                newlastname = input('Введите новую фамилию: ')
                newfirstname = input('Введите новое имя: ')
                newmiddlename = input('Введите новое отчество: ')
                newphone = input('Введите новый номер телефона: ')
                f.write(f"{newlastname}, {newfirstname}, {newmiddlename}, {newphone}\n")
                edited = True
            if edited:
                print('Запись успешно изменена.')
            else:
                print('Запись не найдена.')


def print_all_records():
    with open('boook.txt','r') as f:
        print('Фамилия Имя Отчество - телефон')
        for line in f:
            print(line.strip())


def main():
    while True:
        print('----------------------------')
        print('Телефонный справочник - меню:')
        print('1. Добавить запись')
        print('2. Удалить запись')
        print('3. Поиск записи по фамилии')
        print('4. Изменить запись')
        print('5. Вывести все записи')
        print('0. Выход')
        choice = input('Выберите действие: ')

        if choice == '1':
            add_new_contact()
        elif choice == '2':
            delete_record()
        elif choice == '3':
            search_by_lastname()
        elif choice == '4':
            edit_contact()
        elif choice == '5':
            print_all_records()
        elif choice == '0':
            print('До свиданья ))')
            break
        else:
            print('Неверный пункт меню')


main()