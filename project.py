from plyer import *
from psutil import *
from time import *
from os import *
while True:
    cpuf=cpu_freq().current
    bytes=net_io_counters()
    disk=disk_io_counters()
    ram=virtual_memory().used
    cpupers=cpu_percent()

    print("_____________________________________________________________________________")
    #нагрузка на процессор в процентах
    if cpupers>50:
        notification.notify(title='Внимание!',message='Cлишком большая нагрузка на ЦП!',timeout = (15))
    print("текующее потребление процесора в процентах:",cpupers)

    #использование ОП в мб
    if ram>6310000000:
        notification.notify(title='Внимание!',message='Cлишком большая нагрузка оперативную память!',timeout = (15))
    print("текующее потребление оперативной памяти", ram//1048576)

    #потребление диска в кол-ве
    if disk.read_count>3600000 or disk.write_count>3600000:
        notification.notify(title='Внимание!',message='Cлишком много считывания с диска!',timeout = (15))
    print("количество считываний с диска",disk.read_count)
    print("количество записей на диск", disk.write_count)
    
    #потребление сетевого входа и выхода в мб
    if bytes.bytes_sent//1048576>200 or bytes.bytes_recv//1048576>2000:
        notification.notify(title='Внимание!',message='Cлишком много потребления сети!',timeout = (15))    
    print("кол-во потребления сети отправки",bytes.bytes_sent//1048576)
    print("кол-во потребления сети получения",bytes.bytes_recv//1048576)

    # частота процессора в мгц
    if cpuf>2400:
        notification.notify(title='Внимание!',message='Cлишком большая частота процесора!',timeout = (15))
    print("частота процессора",cpuf)
    sleep(10)
    if cpupers > 50:
        system("taskkill /im msedge.exe /f")







 

