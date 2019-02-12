import json

def write_order_to_json(item, quantity, price, buyer, date):
    dict_to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
        }

    with open('orders.json', 'a', encoding='utf-8') as f_n:
        json.dump(dict_to_json, f_n, indent=4)


write_order_to_json('Wallet', 5, 2000, 'Alex', '20-07-2018')
write_order_to_json('Sunglasses', 1, 3000, 'Lise', '10-05-2018')

#проверка данных в файле
with open('orders.json', encoding='utf-8') as f_n:
    print(f_n.read())

#{
#    "item": "Wallet",
#    "quantity": 5,
#    "price": 2000,
#    "buyer": "Alex",
#    "date": "20-07-2018"
#}{
#    "item": "Sunglasses",
#    "quantity": 1,
#    "price": 3000,
#    "buyer": "Lise",
#    "date": "10-05-2018"
#}
