x=int(input("введите число "))
y=x%7
t=x%17
if x>999 and x<10000:
    if y==0 or t==0:
        print("yes")
    else:
         print("no")
    
