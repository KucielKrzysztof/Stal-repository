Names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
longest = ""
for n in range (0,len(Names)):
    if len(Names[n])>len(longest):
        longest = Names[n]
print(longest)