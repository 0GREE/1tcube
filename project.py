from plyer import *
from psutil import *
from threading import *
cpuf=cpu_freq()
bytes=net_io_counters()
disk=disk_io_counters()
ram=virtual_memory()
cpupers=cpu_percent(interval=1)
def start():
    #сканер нагрузки процессора
    if cpupers>20:
        notification.notify(title='Внимание!',message='Cлишком большая нагрузка на ЦП!',timeout = (15))
    print("текующее потребление процесора в процентах:",cpupers)

    #использование ОП
    if ram.used>6310000000:
        notification.notify(title='Внимание!',message='Cлишком большая нагрузка оперативную память!',timeout = (15))
    print("текующее потребление оперативной памяти", ram.used)

    #потребление диска
    if disk.read_count>2000000:
        notification.notify(title='Внимание!',message='Cлишком много считывания с диска!',timeout = (15))
    print("количество считываний с диска",disk.read_count)

    #потребление сетевого входа и выхода
    if bytes.bytes_sent>44322477 or bytes.bytes_recv>784842885:
        notification.notify(title='Внимание!',message='Cлишком много потребления сети!',timeout = (15))    
    print("кол-во потребления сети отправки",bytes.bytes_sent)
    print("кол-во потребления сети получения",bytes.bytes_recv)

    # частота процессора
    if cpuf.current>1400:
        notification.notify(title='Внимание!',message='Cлишком большая частота процесора!',timeout = (15))
    print("частота процессора",cpuf.current)

#частота сканирования
time = Timer(10.0, start)
time.start()  






 

