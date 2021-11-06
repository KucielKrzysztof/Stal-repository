x=int(input("Enter the amount in PLN: "))
y=x
fives=0
twos=0
ones=0
while x>0:
    if x>=5:
        fives=fives+1
        x=x-5
    elif x>=2:
        twos=twos+1
        x=x-2
    elif x>=1:
        ones=ones+1
        x=x-1
print(f"he amount of PLN {y} in coins")
print(f"5zł - {fives}")
print(f"2zł - {twos}")
print(f"1zł - {ones}")