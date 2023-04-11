from plyer import *
from psutil import *

cputemp=cpu_percent(interval=1)
if cputemp>21:
    notification.notify(title='Внимание!',message='Cлишком большая нагрузка на ЦП!',timeout = (15))
print(cputemp)
    

