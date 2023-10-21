print("My name is Devashish Uniyal and my sap id is 500095185")
with open('rhythm.txt','r+') as file1:
    dict={}
    count=0
    for i in file1:
        temp=i.split()
        for i in temp:
            i=i.upper()
            if i not in dict:
                dict[i]=1
            else:
                dict[i]+=1
        count+=len(temp)
with open('words.txt','w+')as file2: 
             data = file2.write("Total words-"+str(count)+"\n")
             for i in dict.keys():
                 file2.write(str(i)+"-"+str(dict[i])+"\n")
             file2.seek(0)
             print(file2.read())
             

