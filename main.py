from pprint import pprint
import csv
import re

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    # TODO 1: выполните пункты 1-3 ДЗ
    contacts = []
    unik = []
    for note_str in contacts_list:
        fio_str = ' '.join(note_str[:3])
        fio_str = re.sub("[\s]+", " ", fio_str)
        fio_list = re.split(" ", fio_str)
        unik.append(fio_list[0])
        for note in note_str:
            pattern_phone = re.compile("((\+7|8)( ?)(\(?)(\d{3})(\)?)(\-?)(\ ?)(\d{3})(\-?)(\ ?)(\d{2})(\-?)(\ ?)(\d{2}))"
                                 "(\ ?)(((\(?)([д][о][б]\.)(\s?)(\d{2})((\ |\-)?)(\d{2})(\)?))?)")
            pattern_FIO = re.compile("([А-Я][а-я]+)")
            if pattern_phone.findall(note) != []:
                result = pattern_phone.findall(note)
                # print(result)
                final = pattern_phone.sub(r"+7(\5)\9-\12-\15\16\20 \22\25", note)
                fio_list.append(final)
        contacts.append(fio_list)
    unik = list(set(unik))
    contacts_unik = []
    for i in contacts:
        for ii in unik:
            if i[0] == ii:
                unik.remove(ii)
                contacts_unik.append(i)
        for ii in i:
            if ii == '':
                i.remove(ii)
    # TODO 2: сохраните получившиеся данные в другой файл
    with open("phonebook.csv", "w", encoding='utf8') as f:
      datawriter = csv.writer(f, delimiter=',')
      contacts_list = contacts_unik
      datawriter.writerows(contacts_list)