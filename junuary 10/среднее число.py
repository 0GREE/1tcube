a=int(input("1 введите число"))
b=int(input("2 введите число"))
c=int(input("3 введите число"))

if a>c and a<b or a<c and a>b:
    print(a,"среднее")
if b>a and b<c or b<a and b>c:
    print(b,"среднее")
if c>a and c<b or c<a and c>b :
    print(c,"среднее")