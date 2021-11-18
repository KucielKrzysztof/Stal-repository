def sum(number):
    su=0
    number=str(number)
    for x in range(0,len(number)):
        su=su+int(number[x])
    return su
print(sum(7182))