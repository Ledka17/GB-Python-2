import yaml

list_key1 = ['23€',
          'msg_༺-ì',
          'msg_ധ']

n_key2 = 5

dict_key3 = {'key1': 'val1',
             'key2': 'val2'}

data_to_yaml = {'message': list_key1, 'quantity': n_key2, 'value': dict_key3}

with open('file.yaml', 'w', encoding='utf-8') as f_n:
    yaml.dump(data_to_yaml, f_n, default_flow_style=False, allow_unicode = True)

#проверка введенных данных
with open('file.yaml', encoding='utf-8') as f_n:
    print(f_n.read())
#message:
#- 23€
#- msg_༺-ì
#- msg_ധ
#quantity: 5
#value:
#  key1: val1
#  key2: val2
