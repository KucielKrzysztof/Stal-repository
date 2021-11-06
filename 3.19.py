x=int(input("Enter the dog's age in human years: "))
ages=0
for n in range(1,x+1):
    if n <=2:
        ages=ages+10.5
    else:
        ages=ages+4
print(f"The dog's age in dog’s years is {ages} years.")