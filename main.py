#Заведём словарь, где ключом будем id ассессора, а значением -
#массив, в котором первый элемент количество ошибок ассессора,
#второй элемент - количество выполненных заданий ассессором,
#а третий - процент неправильно выполненных заданий.
#Затем найдем ассессора с наибольшим процентом неправильно
# выполненных заданий и выведем его
import csv

d={}
max_percent = 0

with open('file.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        s = row[0].split("\t")
        if s[1] not in d.keys():
            d[s[1]] = [0, 0, 0]
        if s[-1] != s[-2]:
            d[s[1]][0] += 1
        d[s[1]][1]+=1

for elem in d:
    d[elem][2] = d[elem][0]/d[elem][1]
    if max_percent<d[elem][2]:
        max_percent = d[elem][2]
for elem in d:
    if d[elem][2] == max_percent:
        print(d[elem][0])
