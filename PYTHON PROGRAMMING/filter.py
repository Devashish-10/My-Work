def check(x):
   if(x%2==0 or x%4==0):
       return 1
a=list(filter(check,range(2,22)))
print(a)