s=str(input("ENTER A ROMAN NUMBER:"))
n=0
p=0
px=0
pc=0
pl=0
pi=0
for i in range(0,len(s)):
    if(s[i]=='I'):
        if(s[i+1]=='V'):
            n=n+4
            pi=1
        elif(s[i+1]=='X'):
            n=n+9
            px=1
        else:
            n+1
    elif(s[i]=='V'):
        if(pi==1):
            pi=0
            continue
        else:
            n=n+5
    elif(s[i]=='X'):
        if(px==1):
            px=0
            continue
        elif(s[i+1]=='L'):
            pl=1
            n=n+40
        elif(s[i+1]=='C'):
            p=1
            n=n+90
        else:
            n=n+10
    elif(s[i]=='L'):
        if(pl==1):
            pl=0
            continue
        else:
          n=n+50
    elif(s[i]=='C'):
        if(p==1):
            p=0
            continue
        elif(s[i+1]=='D'):
            pc=1
            n=n+400
        elif(s[i+1]=='M'):
            pm=1
            n=n+900
        else:
             n=n+100
    elif(s[i]=='D'):
        if(pc==1):
            pc=0
            continue
        else:
             n=n+500
    elif(s[i]=='M'):
         if(pm==1):
            pm=0
            continue
         else:
               n=n+1000
print("Number in Digits:",n)

    