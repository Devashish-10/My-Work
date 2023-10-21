with open('oldfile.txt','r+') as f1:
    data=f1.read()
with open ('newfile.txt','w+')as f2:
    f2.write(data.replace('\"','\\\"'))
    f2.seek(0)
    data2=f2.read()
print("Old content of file:",data)
print("new content of the file:",data2)