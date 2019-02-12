import re, csv

def get_data(list_adr):
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    for name in list_adr:
        with open(name, 'r',encoding='cp1251') as f:
            string = f.read()
            
            pattern = r'Изготовитель системы: *(\w*)\b'
            match = re.search(pattern, string)
            os_prod_list.append(match[1])

            pattern = r'Название ОС: *(\w*)\b'
            match = re.search(pattern, string)
            os_name_list.append(match[1])

            pattern = r'Код продукта: *(\w*)\b'
            match = re.search(pattern, string)
            os_code_list.append(match[1])

            pattern = r'Тип системы: *(\w*)\b'
            match = re.search(pattern, string)
            os_type_list.append(match[1])

    main_data = [['Изготовитель системы'], ['Название ОС'], ['Код продукта'], ['Тип системы']]
    main_data[0] += os_prod_list
    main_data[1] += os_name_list
    main_data[2] += os_code_list
    main_data[3] += os_type_list

    return main_data


def write_to_csv(adr_csv):
  files = ['info_1.txt', 'info_2.txt', 'info_3.txt']
  data = get_data(files)
  with open(adr_csv, 'w', encoding='utf-8') as f_csv:
    f_n_writer = csv.writer(f_csv, quoting=csv.QUOTE_NONNUMERIC)
    f_n_writer.writerows(data)

#вызов функции
write_to_csv('my.csv')

#проверка полученного файла
with open('my.csv', 'r', encoding='utf-8') as f_n:
    print(f_n.read())
#"Изготовитель системы","LENOVO","ACER","DELL"
#"Название ОС","Microsoft","Microsoft","Microsoft"
#"Код продукта","00971","00971","00971"
#"Тип системы","x64","x64","x86"
