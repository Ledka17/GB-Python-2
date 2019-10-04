#Программа определяющая является ли год високосным
def def_year(x):
    if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:
        return 'Високосный'
    else:
        return 'Обычный'

x = int(input())
print(def_year(x))
