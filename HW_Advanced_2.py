from pprint import pprint
import csv

def clean_data(row):
    # Разделил строку на имя и телефон
    name, phone = row[0].split()

    # Если имя состоит из одного слова, добавить пробел
    if len(name.split()) == 1:
        name = name + " "

    # Поместил имя в поля lastname, firstname и surname
    lastname, firstname, *other = name.split()
    surname = " ".join([firstname, other[0]])

    # Привел телефон в нужный формат
    phone = "+7(999)999-99-99" if len(phone.split(" ")) == 2 else "+7(999)999-99-99 доб. 9999"

    return [lastname, firstname, surname, phone]

def remove_duplicates(contacts_list):
    # Группировал записи по ФИО
    grouped_contacts = {}
    for contact in contacts_list:
        key = contact[0] + " " + contact[1] + " " + contact[2]
        grouped_contacts[key] = grouped_contacts.get(key, []) + [contact]

    # Удалил дубликаты
    return list(grouped_contacts.values())

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(map(clean_data, rows))
    contacts_list = remove_duplicates(contacts_list)

pprint(contacts_list)

# сохранил получившиеся данные в другой файл
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contacts_list)
