#Программа, которая принимает на вход список чисел в одной строке и выводит на экран в одну строку значения, которые повторяются в нём более одного раза
def lst_new(a):
    a.sort()
    a += ['']
    i = 0
    new_a = []
    while i < len(a)-1:
        k = 1
        while a[i] == a[i+k]:
            k += 1
        if k > 1:
            new_a.append(a[i])
        i += k
    return new_a

a = [int(i) for i in input().split()]
print(lst_new(a))
