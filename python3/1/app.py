#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [2,3,5,8,6,3,2,7]
list1 = []
i = 1
sum = 0
for i in range(len(list)):
    if i%2 != 0:
        sum = sum + list[i]
        list1.append(list[i])
print("на нечётных позициях элементы",end=' ')
print(*list1, sep = ' и ', end = '')
print(f', ответ: {sum}')