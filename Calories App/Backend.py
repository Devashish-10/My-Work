import math
class CalorieAppBackend:
     
     def __init__(self):
         self.bmr=None
     
     def calc_BMR(self,height,weight,age,gender):
         
          weight=float(weight)
          height=float(height)
          age=int(age)
          gender=str(gender)
          try: 
               if(gender=="Female"):
                  self.bmr=447.593+(9.247*weight)+(3.098*height)-(4.330*age)
                  return self.bmr
               else:
                  self.bmr=88.362+(13.297*weight)+(4.799*height)-(5.677*age)
                  return self.bmr  
          except Exception as e:
                      raise  ValueError("An error occured"+str(e))
     def calc_Main(self,height,weight,age,gender,exercise):
            cal=0
            self.bmr=CalorieAppBackend.calc_BMR(self,height,weight,age,gender)
            try:
                      if(exercise=="No Exercise"):
                           cal=self.bmr*1.2
                      elif(exercise=="15 to 30 minutes"):
                          cal=self.bmr*1.375
                      elif(exercise=="30 minutes to 1 hour"):
                          cal=(self.bmr*1.55) 
                      
                      elif(exercise=="1 to 2 hours"):
                          cal=self.bmr*1.725
                      elif(exercise=="More than 2 hours"):
                           cal=self.bmr*1.9
                      
                      
            except Exception as e:
                      raise  ValueError("An error occured"+str(e))
            return cal
     def calc_bulk(self,height,weight,age,gender,exercise):
             cal=0
             self.bmr=CalorieAppBackend.calc_BMR(self,height,weight,age,gender)
             try:
                      if(exercise=="No Exercise"):
                           cal=(self.bmr*1.2)+((self.bmr*1.2)*0.1)
                      elif(exercise=="15 to 30 minutes"):
                          cal=(self.bmr*1.375)+((self.bmr*1.375)*0.1)
                      elif(exercise=="30 minutes to 1 hour"):
                          cal=(self.bmr*1.55)+((self.bmr*1.55)*0.1)
                      elif(exercise=="1 to 2 hours"):
                           cal=(self.bmr*1.725)+((self.bmr*1.725)*0.1)
                      elif(exercise=="More than 2 hours"):
                          cal=(self.bmr*1.9)+((self.bmr*1.9)*0.1)

             except Exception as e:
                      raise  ValueError("An error occured"+str(e))
             return cal
     def calc_cut(self,height,weight,age,gender,exercise):
             cal=0
             self.bmr=CalorieAppBackend.calc_BMR(self,height,weight,age,gender)
             try:
                      if(exercise=="No Exercise"):
                           cal=(self.bmr*1.2)-((self.bmr*1.9)*0.1)
                      elif(exercise=="15 to 30 minutes"):
                           cal=(self.bmr*1.375)-((self.bmr*1.375)*0.1)
                      elif(exercise=="30 minutes to 1 hour"):
                           cal=(self.bmr*1.55)-((self.bmr*1.55)*0.1)
                      elif(exercise=="1 to 2 hours"):
                           cal=(self.bmr*1.725)-((self.bmr*1.725)*0.1)
                      elif(exercise=="More than 2 hours"):
                           cal=(self.bmr*1.9)-((self.bmr*1.9)*0.1)
                 
             except Exception as e:
                      raise  ValueError("An error occured"+str(e))
             return cal
     
     def calc_fat_perc(self,waist,height,gender,hip,neck):
           
           try:
                 if(gender=="Female"):
                       body_fat=(163.205) * math.log10(waist+hip-neck)-(97.684 * math.log10(height)) -78.387
                 else:
                       body_fat=86.010 * math.log10(waist - neck)-(70.041 * math.log10(height)) + 36.76
           except Exception as e:
                  raise ValueError("An error occured while calculating fat%"+str(e))
           return body_fat
           
                    


           
                 
                 
          