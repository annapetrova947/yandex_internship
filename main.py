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




'''from datetime import datetime
f = open('text2.txt', 'r')
i=0 #счетчик для подсчета количества ассессоров
sum_time = 0 #сумма врмени для 1 микротаска для подсчета среднего времени на микротаск
for line in f:
    str = line.split("\t")
    str_date_begin = str[-2] #выделяем строку с датой и врменем начала
    str_date_finish = str[-1] #выделяем строку с датой и временем конца
    microtasks_str = str[-3]
    microtask = float(microtasks_str) #количество микротасков у ассессора
    str_date_finish_new = str_date_finish.replace("\n", "")

    date_begin = str_date_begin.split(" ") #разделяем дату и время
    date_finish = str_date_finish_new.split(" ")

    data_begin_day = date_begin[0] #дата начала
    data_begin_time = date_begin[-1] #время начала
    data_finish_day = date_finish[0] #дата конца
    data_finish_time = date_finish[-1] #время конца





#обрабатываем дату начала
    data_begin_day_spl = data_begin_day.split("-")
    year_begin = data_begin_day_spl[0]
    month_begin = data_begin_day_spl[1]
    day_begin = data_begin_day_spl[2]

#обрабатываем время начала
    data_begin_time_spl = data_begin_time.split(":")
    hours_begin = data_begin_time_spl[0]
    minuts_begin = data_begin_time_spl[1]
    seconds_begin = data_begin_time_spl[2]


#обрабатываем дату конца
    data_finish_day_spl = data_finish_day.split("-")
    year_finish = data_finish_day_spl[0]
    month_finish = data_finish_day_spl[1]
    day_finish = data_finish_day_spl[2]

#обрабатываем время конца
    data_finish_time_spl = data_finish_time.split(":")
    hours_finish = data_finish_time_spl[0]
    minuts_finish = data_finish_time_spl[1]
    seconds_finish = data_finish_time_spl[2]

#разница в секундах между временем конца и временем начала
    start = datetime(int(year_begin), int(month_begin), int(day_begin), int(hours_begin), int(minuts_begin), int(seconds_begin))
    finish = datetime(int(year_finish), int(month_finish), int(day_finish), int(hours_finish), int(minuts_finish), int(seconds_finish))
    duration = finish - start
    duration_in_seconds = duration.total_seconds()
    #print(duration_in_seconds)

    time_for_microtask = duration_in_seconds/microtask #время на один microtask
    #print(time_for_microtask)
    #считаем среднее время на один микротаск

    sum_time+=time_for_microtask
    i+=1
avarage_time_for_microtask = sum_time/i
print(avarage_time_for_microtask)'''

