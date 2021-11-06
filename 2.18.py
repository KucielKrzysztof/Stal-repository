x=input("Height(cm): ")
x=int(x)
inch=x/2.54
feet=int(inch/12)
inch=inch-(feet*12)
print(f"I am {x}cm tall, i.e. {feet} feet and {int(inch)} inches.")