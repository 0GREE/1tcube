x = int(input("введите число"))
count = 0
maximum = 0
for i in range(1, x + 1): 
    if i % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x
if count > 0:
    print(count)
    print(maximum)
else:
    print("NO")