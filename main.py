#                                                                Sem_1

# a = int(input("Your age?"))
# if a < 12:
#     print("child")
# elif a < 45:
#     print("midman")
# else:
#     print("oldman")


# import math
# n = int(input("speed"))
# m = int(input("km"))
# res = m // n + int(m % n > 0)
# print(res)


# a = int(input("First"))
# b = int(input("Second"))
# c = int(input("Third"))
# sum = a + b + c
# res = sum // 2 + int(sum % 2 >0 )
# print(res)


# Задача №5. Решение в группах
# Вагоны в электричке пронумерованы натуральными
# числами, начиная с 1 (при этом иногда вагоны
# нумеруются от «головы» поезда, а иногда – с
# «хвоста»; это зависит от того, в какую сторону едет
# электричка). В каждом вагоне написан его номер.
# Витя сел в i-й вагон от головы поезда и обнаружил,
# что его вагон имеет номер j. Он хочет определить,
# сколько всего вагонов в электричке. Напишите
# программу, которая будет это делать или сообщать,
# что без дополнительной информации это сделать
# невозможно.
# Input: 3 4(ввод на разных строках)
# Output: 6

# i = int(input("Kuda sel Vitya?"))
# j = int(input("Kakoy vagon?"))
# if i!=j:
#     res = i+j-1
#     print(res)
# else:
#     print("Imposible")


# Задача №7. Решение в группах
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES


# y= int(input("Year?"))

# if y % 4 == 0 and y % 100 !=0 or y % 400 == 0:
#     print("yes")
# else:
#     print("no")

#                                                                             Sem_2

# n = int(input())
# while n != 1:
#     print(n)
#     n = int(input())


# while True:
#     n = input()
#     print(n)
#     if n == "q":
        

# for i in range(0,5,1):
#     print(i,"Hello")


# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while


# n = int(input('number: '))
# count = 0
# n1 = 1
# n2 = 2
# while count < n-1:
#     nf = n1 * n2
#     n1 = nf
#     n2 = n2+1
#     count = count + 1
# print(nf)

# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

# n = int(input("number: "))
# i = 0
# n1 = 0
# n2 = 1
# f = 0
# while f <=n:
#     f = n1+n2
#     n2 = n1
#     n1 = f
#     i += 1
# if n !=n2:
#     print(-1)
# else:
#     print(i)


# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2


# sp=[-20, 30, -40, 50, 10, -10]
# n = 6
# count = 0
# maxim = 0
# for i in range(len(sp)):
#     if sp[i] > 0:
#         count += 1
#         if maxim < count:
#             maxim = count
#     else:
#         count = 0
# print(maxim)


# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# n = int(input("kolvo: "))
# maxa = 0
# mina = 999999999
# for i in range(n):
#     a = int(input("kg: "))
#     if a > maxa:
#         maxa = a
#     if a < mina:
#         mina = a
# print(maxa, mina)
    






#                                                                      Sem_3
# a = list()
# b = []
# b.append(10)
# for i in range(0, 5):
#     a.append(i)
# print(a)
# print(b)

# списки
# sp = [4,2,5,2]
# for i in range(len(sp)):
#     print(sp(i))

# sp = [1,2,4,5,6,7]
# print(sp[:3])
# print(sp[3:])
# print(sp[-4:])
# sp = sp[::-1]
# print(sp)

# множества
# mn = set()
# mn = {1,2,3}
# mn.add(4)
# print(*mn)
# sp = [1,1,22,22,4,4]
# print(*set(sp))

# словари
# sl = dict()
# sl = {"login":"vasya", "password":"nevasya"}
# sl["address"] = "Moscow"
# print(sl["login"])
# print(sl)
# print(list(sl.keys()))
# print(list(sl.values()))
# for key, value in sl.items():
#     print(key, '-',value)
# print(list(sl.items()))
# sl = dict(sorted(list(sl.items())))
# print(sl)

# sp = [1,2,3]
# sp2 = sp.copy()
# sp.append(5)
# print(sp)
# print(sp2)
# print(id(sp),id(sp2))

# sp = [1,2,3]
# print(dir(sp))
# help(sp.insert)
# sp.insert(0,8)
# print(sp)


# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# sp = [1,1,2,0,-1,3,4,4]
# print(len(set(sp)))

# sp = [1,1,2,0,-1,3,4,4]
# sl = {}
# for el in sp:
#     sl[el] = sl.get(el,0) + 1
#     if el not in sl:
#         sl[el] = 1
#     else:
#         sl[el] +=1
# print(sl)
# print(sl.get(8,-1))


# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# sp = [1,2,3,4,5]
# k = 3
# print(*sp[len(sp)-k+1:],*sp[:k])


# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# sp = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},{"VI": "S005"}, {"VII": "S005"}, {" V ":" S009"}, {" VIII":" S007"}]
# sp2 = []
# sp3 = set()
# for el in sp:
#     sp2.append(list(el.values()))
#     sp3.add(*el.values())
# print(sp3)                                    


# sp = [0,-1,5,2,3]
# count = 0
# for i in range(len(sp)-1):
#     if sp[i] < sp[i+1]:
#         count += 1
# print(count)
