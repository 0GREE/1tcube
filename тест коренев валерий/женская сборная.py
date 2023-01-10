gender=input("введите свой пол(m или f)")
age=int(input("введите ваш возраст"))

if gender=="f":
    if age>=10 and age<=15:
        print("yes")
    else:
        print("no")
else:
    print("no")


