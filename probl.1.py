cuvint=str(input("Dati un cuvint: "))
litera=str(input("Dati o litera: "))
for i in range (0,len(cuvint)):
    print(cuvint.replace(cuvint[i],litera))