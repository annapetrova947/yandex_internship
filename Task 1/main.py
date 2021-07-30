# Задание 1
# Оплата будет высчитываться исходя из количества микрозаданий.
# Посчитаем сколько в среднем времени у ассессоров уходит на 1 микрозадание (пусть на одно микрозадание уходит t секунд)
# Оплата будет высчитываться t*(количество микрозаданий)/30*N


from datetime import datetime
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

#обрабатываем дату начала (для подсчета поличества секунд, которе потребовалось ассессору для выполнения работы)
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
    
    time_for_microtask = duration_in_seconds/microtask #время на один microtask
   
    sum_time+=time_for_microtask #заготовки для подсчета среднего времени на микротаск
    i+=1
    
avarage_time_for_microtask = sum_time/i
print(avarage_time_for_microtask)

#568 секунд в среднем уходит у ассессора на выполнение одного микротаска
# оплата будет высчитываться 568*(количество микротасков)/30*N
