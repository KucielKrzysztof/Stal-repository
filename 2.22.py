import random
x=random.randint(1, 6)
y=int(input("Your number: "))
while x!=y:
    print("False")
    y=int(input("Your number: "))
print(True)