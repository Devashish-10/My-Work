str=input("Enter a string:")
c={}
for i in str:
    if i in c:
        c[i]+=c[i]#calculate frequency of the character and storing in array c
    else :
        c[i]=1 # do not change its frequency   

highest_frequency=max(c)
print("Character with highest frequency is ", highest_frequency)
