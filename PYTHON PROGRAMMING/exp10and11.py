""" print("My name is Devashish Uniyal and my sap id is 500095185")
class employee:
    def __init__(self,f,l,p):    
             self.first =f     
             self.last=l      
             self.pay=p     
    def details(self): 
             print("Email :",self.first +"."+self.last +"@company.com")
obj = employee(input("Enter the first name : "),input("Enter the last name : "),int(input("Enter the pay : "))) 
obj.details() 
"""
"""print("My name is Devashish Uniyal and my sap id is 500095185") 
class vehicle:   
    def __init__(self, name,speed,mileage,color): 
          self.name = name    
          self.speed=speed      
          self.mileage = mileage      
          self.color = color 
 
    def seating_capacity(self, capacity): 
         self.capacity = capacity
         print("The seating capacity of a {self.name} is {capacity} passengers" )
 
 
obj = vehicle("AUDIA3",250,18,"BLACK")
print("Car Name:",obj.name)
print("Maximum Speed of car is:",obj.speed)
print("Mileage of car is:",obj.mileage)
print("Your car color is :",obj.color)
 
 """