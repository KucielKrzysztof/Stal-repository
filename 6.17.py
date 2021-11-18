#nie czaje za bardzo
Array1 = [4,36,12,28,9,44,5]
Array2 = [5,1,36]
for x in Array1:
    appear=False
    for y in Array2:
        if x==y:
            appear=True
    if appear==False:
        print(x)