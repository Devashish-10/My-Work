print("My name is Devashish Uniyal and my sap id is 500095185")
file1=open("city.txt","r+")
data=file1.readlines()
names=[]
population=[]
area=[]
for city in data:
    ccity=city.split(" ")
    names.append(ccity[0])
    population.append(float(ccity[1]))
    area.append(float(ccity[2]))
print("The details :- ")
for i in range(len(names)):
    print("\n\t Name:- "+names[i]+"\n\tpopulation :- "+str(population[i])+"\n\tarea :- "+str(area[i]))
print("Cities with population of more than 10 lakhs")
for i in range(len(names)):
    if(population[i]>10):
        print("\n\tName:-"+names[i]+"\n\tpopulation :- "+str(population[i])+"\n\tarea :- "+str(area[i]))
totarea=0
for a in area:
    totarea+=a
print("\n Total area of all cities :- "+str(totarea))
