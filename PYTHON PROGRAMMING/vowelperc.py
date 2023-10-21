file=str(input("ENTER THE NAME OF THE FILE:"))
file2=open(file,"r")
t1=0,t2=0
vowels=['a','e','i','o','u']
for i in file2.read():
    if i in vowels:
       t1=t1+1
    else:
       t2=t2+1
file2.close() 
p1=(t1/(t1+t2))*100
p2=(t2/(t1+t2))*100  
print("PERCENTSGE OF VOWELS ARE:",p1) 
print("PERCENTAGE OF CONSONANTS ARE:",p2)    
       