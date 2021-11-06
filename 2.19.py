a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
p = (a + b + c) / 2
area = (p * (p - a) * (p - b) * (p - c))**(1/2)
#cos**(1/2) to wyciągniecie pierwiastka kwadratowego
print(f"Area: {area}")