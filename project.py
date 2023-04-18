from plyer import *
from psutil import *
from time import *
cpuf=cpu_freq()
bytes=net_io_counters()
disk=disk_io_counters()
ram=virtual_memory()
cpupers=cpu_percent()
g=0
while True:
    print("_____________________________________________________________________________")
    #сканер нагрузки процессора в процентах
    if cpupers>50:
        notification.notify(title='Внимание!',message='Cлишком большая нагрузка на ЦП!',timeout = (15))
    print("текующее потребление процесора в процентах:",cpupers)

    #использование ОП в мб
    if ram.used>6310000000:
        notification.notify(title='Внимание!',message='Cлишком большая нагрузка оперативную память!',timeout = (15))
    print("текующее потребление оперативной памяти", ram.used//1048576)

    #потребление диска в кол-ве
    if disk.read_count>2000000 or disk.write_count>2000000:
        notification.notify(title='Внимание!',message='Cлишком много считывания с диска!',timeout = (15))
    print("количество считываний с диска",disk.read_count)
    print("количество записей на диск", disk.write_count)
    #потребление сетевого входа и выхода в мб
    if bytes.bytes_sent>69091233 or bytes.bytes_recv>1509232157:
        notification.notify(title='Внимание!',message='Cлишком много потребления сети!',timeout = (15))    
    print("кол-во потребления сети отправки",bytes.bytes_sent//1048576)
    print("кол-во потребления сети получения",bytes.bytes_recv//1048576)

    # частота процессора в мгц
    if cpuf.current>2400:
        notification.notify(title='Внимание!',message='Cлишком большая частота процесора!',timeout = (15))
    print("частота процессора",cpuf.current)
    sleep(10)








 

