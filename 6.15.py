Colors = ['red','green','blue','white']
file = open('colors.txt', 'w') #write to file
file.write('Colors:') #write heading line
for n in range(0,len(Colors)):
    file.write(f'\n{Colors[n]}')
file.close() #close file