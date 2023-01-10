a=int(input("введите длину 1 стороны"))
b=int(input("введите длину 2 стороны"))
c=int(input("введите длину 3 стороны"))

if a==b and a==c:
    print("это равностороний треугольник")
if a==b and a!=c or a!=b and a==c:
    print("треугольник равнобедреный")
if a!=b and a!=c and b!=c:
    print("треугольник разностороний")