print("My name is Devashish Uniyal and my sap id is 500095185")
def check_baggage(baggage_weight):
    if(0<=baggage_weight<=40):
        return True
    else:
         return False
def check_immigration(expiry_year):
    if 2030<=expiry_year<=2050: 
         return True
    else:
         return False
def check_security(noc_status):
    if noc_status=='valid'or noc_status=='VALID' : 
         return True
    else:
         return False
def traveller():
    dict={}
    Id=int(input("Enter Id:"))
    dict['ID']=Id
    name=input("Enter Name:")
    dict['name']=name
    Id=int(input("Enter Baggage weight:"))
    dict['weight']=Id
    Id=int(input("Enter passport expiry year:"))
    dict['year']=Id
    name=input("Enter noc status:")
    dict['noc']=name
    f1=check_baggage(dict['weight']) 
    f2=check_immigration(dict['year'])
    f3=check_security(dict['noc'])
    print("Traveller name:",dict['name'],"Traveller ID:",dict['ID'])
    if f1==f2==f3==True:
         print("Passenger is allowed to travel")
    else:
         print("Passenger has to be rechecked")
traveller()
