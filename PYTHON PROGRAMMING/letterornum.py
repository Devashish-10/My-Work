str=input("ENTER A STRING: ")
ans1=False
ans2=False
for i in str:
    if i.isalpha() :
        ans1= True
    if i.isdigit() :
        ans2= True    
print("ENTERED STRING CONTAINS A LETTER",ans1)
print("En")