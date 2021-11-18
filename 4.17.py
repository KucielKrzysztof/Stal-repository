def letters(text,letter):
    sum=0
    for x in range(0,len(text)):
        if text[x]==letter:
            sum=sum+1
    return sum
print(letters("You never get a second chance to make a first impression","e"))