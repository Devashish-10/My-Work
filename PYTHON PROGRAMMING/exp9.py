""" print("My name is Devashish Uniyal and my sap id is 500095185") 
no = int(input("Enter the number of the test cases :- "))
for i in range(0,no):
    n,d =input("Enter numerator and denominator:").split()    
    try: 
         print(int(n)/int(d))    
    except(ZeroDivisionError): 
         print("Error Code: integer division or modulo by zero") 
    except (ValueError): 
         print("Error Code: invalid literal for int() with base 10: ",d)  
    else: 
         print("Division done without errors")     
"""
"""print("My name is Devashish Uniyal and my sap id is 500095185")
mylist=[1,2,3,"4",5] 
sum=0 
for i in mylist:    
    try: 
        sum=sum+i    
    except TypeError: 
        print("Wrong operand types")
print(sum) 
try: 
    print(mylist[5]) 
except IndexError: 
    print("list index out of range")
 """
"""print("My name is Devashish Uniyal and my sap id is 500095185") 
try: 
    file1=open("oldfile.txt","w+")  
    file1.write('\"HELLO PUNE"')
    file2=open("newfile.txt","w+")     
    data = file1.read() 
    data2="" 
    for i in range(0,len(data)):         
        if(data[i]=="\""): 
            data2+="\\\"" 
        else: 
            data2+=data[i]    
            print("Writing data into new file")  
            file2.write(data2) 
    
    print("The old contents of the file are :- \n")
    for i in range(0,len(data)): 
        print(data[i])
    print("The new contents of the file are :- \n")
    for i in range(0,len(data2)): 
        print(data2[i])
    file1.close()    
    file2.close() 
except: 
    print("Error occured") """
