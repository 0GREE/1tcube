count = 0
text=input("введите ")

a = text.find('f')
b = text.rfind('f')
if a == -1:
    print("NO")
elif a == b:
    print(a)
else:
    print(a, b)

