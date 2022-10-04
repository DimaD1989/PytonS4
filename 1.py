# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))

# data1 = input("Введите число ")

# #Короткое решение
# print(sum([int(i) for i in data1 if i.isdigit()]))

# in_number = float(input('Введите вещественное число: '))
# num_int = int(str(in_number).replace('.', ''))
# sum = 0
# while num_int > 0:
#     cut_digit = num_int % 10
#     sum = sum + cut_digit
#     num_int //= 10
# print(f"{in_number}", f"{sum}", sep=" -> ")

# number = int(input("Введите число: "))
# list_number = list()
# count = 1
# for i in range(1, number + 1):
#     count = count * i
#     list_number.append(count)
# print(list_number)

# number = int(input("Введите число N: "))
# list_number = {}
# count = 0
# for i in range(1, number+1):
#     list_number[i] = int(round((1 + 1 / i) ** i, 0))
#     count = count + list_number[i]
# print(list_number, count)
# Задача 1

# numb = float(input())
# summ = 0
# for el in str(numb):
#     if el != '.':
#         summ += int(el)
# print(summ)

# n = float(input('Введите число - '))
# while n % 1 > 0:
#     n *= 10
# summ = 0
# while n > 0:
#     summ += n % 10
#     n //= 10
# print(int(summ))

# N = input("Введите число: ")
# sum = 0
# for i in N:
#     if i != "." and i != ",":
#         sum = sum + int(i)
# print(sum)
# задача 2
# number = int(input("Введите число: "))
# product = 1
# arr = []

# for i in range(1, number+1):
#     product *= i
#     arr.append(product)
# print(arr)

# num = int(input("Введите число: "))
# dic = {}
# sum = 0

# for i in range(1, num+1):
#     dic[i] = round((1+1/i)**i)
#     sum += dic[i]
# print(f'{dic} -> {sum}')
# задача 4
# numN = int(input('Введите число N: '))
# list = []
# for i in range(-numN,numN+1):
#     list.append(i)
# print(list)
# position1 = int(input('Укажите первую позицию цифры из списка, которую нужно перемножить: '))
# position2 = int(input('Укажите вторую позицию цифры из списка, которую нужно перемножить: '))
# print(f'Произведение чисел = {list[(position1-1)]*list[(position2-1)]}')

# input = int(input(" Input N: "))

# array = []

# for i in range(input*-1,input+1):
#     array.append(i)

# with open ('file.txt') as data:
#     op = 1
#     for line in data.readlines():
#         pos = line
#         op = array[int(pos)] * op
#     print(array, " = ", op)

# import random
# n=int(input('input number '))
# list=[]
# for i in range(n):                      # генератор случайных чисел
#     a=random.randint(-n, n)
#     list.append(a)   
# print (list)
# index_list = input(f'введите позиции элементов от 1 до {n} через пробел').split()
# result=1
# for j in range(len(index_list)):        # перебор элементов с номерами позиций
#     a=int(index_list[j])-1
#     print (f'{result}*{int(list[a])}', end=' ')
#     result*=int(list[a])    
# print (f'= {result}')
# перемешивание алгоритма
# arr = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_arr = []
# random_num = None

# while len(new_arr) < len(arr):
#     random_num = arr[random.randint(0, len(arr))-1]
#     if not random_num in new_arr:
#         new_arr.append(random_num)
# print(new_arr)

# import random

# spisok=[1,2,3,4,5,6]
# for i in range(len(spisok)):
#     n=random.randint(0,len(spisok)-1)
#     spisok[i], spisok[n] = spisok[n], spisok[i]
# print(spisok)

# import random 
# y = ['Apple', '2 ', '-5675 ', '0.678 ', 'morning']
# random.shuffle(y)
# print(y)

# list = ["Anna", "Alex", 3.14159, 0]
# for i in range(len(list)):
#     index_a = random.randint(0, len(list) - 1)
#     list[i], list[index_a]=list[index_a],list[i]

# Зададчи доп с семинара
# Задача 2 
# transleterate = \
#   {'а': 'a','б': 'b','в': 'v','г' : 'g','д' : 'd','е' : 'e','ж' : 'zh','з' : 'z','и' : 'i',
#   'й' : 'y','к' : 'k','л' : 'l','м' : 'm','н' : 'n','о' :'o','п' : 'p','р' : 'r','с' : 's',
#   'т' : 't','у' : 'u','ф' : 'f','х' : 'kh','ц' : 'ts','ч' : 'ch','ш' : 'sh','щ' : 'shch',
#   'ь' : '\'','ы' :'y','ъ' : '','э' : 'e','ю' : 'yu','я' : 'ya'}
# text = input('input: ')

# for i in text:
#     print(transleterate[i], end = "")
# Задача 1
# aplphabetE = \
# ['a', 'b', 'v', 'g', 'd', 'e', 'yo', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p','r', 
# 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '\'', 'e', 'yu', 'ya']

# aplphabetR = \
# ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 
# 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

# base = input('Введите слово: ')
# word=[]

# for i in range(len(base)):
#     word.append(aplphabetR.index(base[i]))
#     index = word[i]
#     print(aplphabetE[index], end='')


# t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

# start_index = ord('а')
# title = 'Переводим этот текст, сейчас!'
# print(title.lower())

# slug = ""
# for s in title.lower():

# 	if "а" <= s <= "я":
# 		slug += t[ord(s) - ord('а')]
	
# 	else:
# 		slug += s

# t = ['a', 'b', 'v', 'g', 'd', 'e', 'zh', 'z', 'i', 'y', 'k', 'l', 'm', 'n', 'o', 'p', 'r', 's', 't', 'u', 'f', 'kh', 'ts', 'ch', 'sh', 'shch', '', 'y', '', 'e', 'yu', 'ya']

# start_index = ord('а')
# title = 'Переводим этот текст, сейчас!'
# print(title.lower())

# slug = ""
# for s in title.lower():
#     print(ord('a'),ord(s))
#     if "а" <= s <= "я":
#         slug += t[ord(s) - ord('а')]
#     else:
#         slug += s
# Задача 1
# numbs = list(map(int, input('  input:').split()))
# count = 0
# for i in range(1,len(numbs)):
#     if numbs[i-1] < numbs[i]:
#         count += 1

# print(count)
k=2

a = round(random()*100, )
b = round(random()*100, )
c = round(random()*100, )
print(a, b, c)
result = ''
if b == 0: result = f"{a}*x**{k} + {c}*x**{k-2} = 0"
if b == 0 and c == 0: result =  f"{a}*x**{k} = 0"
else: result =  f"{a}*x**{k} + {b}*x**{k-1} + {c}*x**{k-2} = 0 "

with open("file44.txt", "w") as file44:
    file44.write(result)














# num = input()
# res = 0
# for digit in num:
#     if digit.isdigit():
#       res += int(digit)  
# print("Сумма:", res)




