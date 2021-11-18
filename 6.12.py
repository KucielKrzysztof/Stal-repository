Array =[15,8,31,47,2,19]
print("existed array: ",end ='')
for n in range(0,len(Array)):
    print(Array[n], end =' ')
print(f"\nreverse array: ", end='')
for n in range(len(Array)-1,-1,-1):
    print(Array[n], end =' ')