n=int(input("введите ко-во столбиков"))

if n>=3 and n<=19:
    for i in range(1, n+1):
        if i==1 or i==n:
            print("*"*19)
        else:
            print("*                 *")