txt=input("введите текст")
count=len(txt)*60
rub=0
cop=0
for i in range(1, len(txt)):
    if count>=100:
        count-=100
        rub+=1
    if count<100:
        cop+=count
print(rub,cop)
