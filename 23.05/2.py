mass, rost=int(input("введите массу")), int(input("введите рост"))

imt=mass/(rost**2)
if imt>25:
    print("Избыточная масса")
elif imt<18.5:
    print("Недостаточная масса")
else:
    print("Оптимальная масса")
