#Задание 2
#Заведём словарь, где ключом будем id ассессора, а значением -
#массив, в котором первый элемент количество ошибок ассессора,
#второй элемент - количество выполненных заданий ассессором,
#а третий - доля неправильно выполненных заданий.
#Затем найдем ассессора с наибольшей долей неправильно
# выполненных заданий и выведем его
import csv

d={}
max_percent = 0

with open('file.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        s = row[0].split("\t")
        if s[1] not in d.keys(): #если ассессора еще нет в словаре, заводим
            d[s[1]] = [0, 0, 0]
        if s[-1] != s[-2]: #если ассессор ошибся, добавляем 1 к ошибкам
            d[s[1]][0] += 1
        d[s[1]][1]+=1 #добавляем 1 к выполненным заданиям ассессора

for elem in d:
    d[elem][2] = d[elem][0]/d[elem][1] #высчитываем долю совершенных ошибок ассессора
    if max_percent<d[elem][2]: #ищем наибольшую долю совершенных ошибок
        max_percent = d[elem][2]
for elem in d:
    if d[elem][2] == max_percent:
        print(d[elem][0])
#ассессор с id 236 имеет самую большую долю неверно выполненных заданий (0,57), значит он хуже всех справился с заданием 
