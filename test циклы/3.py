count = 0
maximum = 0
for i in range(1, 5):
    x = int(input("введите число"))
    if x % 2 != 0:
        count += 1
        if x > maximum:
            maximum = x 
if count > 0:
    print(count)
    print(maximum)
else:
    print("NO")