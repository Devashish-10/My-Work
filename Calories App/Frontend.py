import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.clock import Clock
from kivy.uix.progressbar import ProgressBar
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.graphics import Color
from kivy.properties import ObjectProperty
class Loading(Screen):
       def on_entry(self):
                label=Label(text="CALORIE CALCULATOR",font_size='35sp',font_name='Impact',pos_hint={'centre_x':0.5,'centre_y':0.6})
                self.add_widget(label)
                self.progress=ProgressBar(max=100,size_hint={1,None},height=30,pos_hint={'centre_x':0.8,'centre_y':0.1})
                self.add_widget(self.progress)
                self.progress.value=0
                self.update_event=Clock.schedule_interval(self.update_schedule,0.1)
                with self.progress.canvas:
                          Color(1,1,1,1)
                          self.progress_text=Label(text='Please Wait...')
                          self.progress_text.font_size='15sp'
                          self.progress_text.font_name='Impact'
                          self.progress_text.pos=(self.progress.x,self.progress.y+self.progress.height*10)
                          self.add_widget(self.progress_text)
       def update_schedule(self,dt):
                 if self.progress.value >= self.progress.max:
                        self.update_event.cancel()
                        self.manager.current='start'
                 else:
                        self.progress.value+=1
                 self.progress_text.text=f'Loading....{int(self.progress.value)}%'
       
class StartPageContent(RelativeLayout):
     
     def __init__(self):
           super(StartPageContent,self).__init__()
           button_layout=RelativeLayout()
           accept=Button(text='Prepare a Calorie plan',font_name='Impact',background_color=(0,0,1,1))
           accept.size_hint=(None,None)
           accept.size=(200,50)
           accept.pos_hint={'center_x':0.5,'center_y':0.5}
           accept.bind(on_press=self.runapp)
           button_layout.add_widget(accept)
           exit=Button(text='Exit',font_name='Impact',background_color=(1,0,0,1))
           exit.size_hint=(None,None)
           exit.size=(200,50)
           exit.pos_hint={'center_x':0.5,'center_y':0.4}
           exit.bind(on_press=CaloriesApp.exitapp)
           button_layout.add_widget(exit)
           self.add_widget(button_layout)
           
     def runapp(self,instance):
                  print("runapp")
                  self.parent.parent.current='input'
                  print("Screen after runapp",self.parent.parent.current)
                 
class StartPage(Screen):
         def __init__(self,**kwargs):
                 super(StartPage,self).__init__(**kwargs)
                 self.content=StartPageContent()
                 self.add_widget(self.content)
         
class CollectInputContent(RelativeLayout):
         Age_input=ObjectProperty(None)
         Weight_input=ObjectProperty(None)
         Height_input=ObjectProperty(None)
         gender_btn=ObjectProperty(None)
         exercise_stat=ObjectProperty(None)
         diet_plan=ObjectProperty(None)
         def __init__(self,):
                 print("Entering collectinputcontent")
                 self.exercise_status_value=""
                 self.gender=""
                 self.diet=""
                 super(CollectInputContent,self).__init__()
                 layout=RelativeLayout()
                 Age_label=Label(text='Age',font_name='Impact')
                 Age_label.pos_hint={'center_x':0.4,'center_y':0.8}
                 self.Age_input=TextInput(multiline=False)
                 self.Age_input.pos_hint={'center_x':0.5,'center_y':0.8}
                 self.Age_input.size_hint = (None, None)
                 self.Age_input.size=(150,50)
                 layout.add_widget(Age_label)
                 layout.add_widget(self.Age_input)
                 Weight_Label=Label(text='Weight in kgs:',font_name='Impact')
                 Weight_Label.pos_hint={'center_x':0.3,'center_y':0.7}
                 self.Weight_input=TextInput(multiline=False)
                 self.Weight_input.pos_hint={'center_x':0.5,'center_y':0.7}
                 self.Weight_input.size_hint = (None, None)
                 self.Weight_input.size=(150,50)
                 layout.add_widget(Weight_Label)
                 layout.add_widget(self.Weight_input)
                 Height_Label=Label(text='Height in cms:',font_name='Impact')
                 Height_Label.pos_hint={'center_x':0.3,'center_y':0.6}
                 self.Height_input=TextInput(multiline=False)
                 self.Height_input.pos_hint={'center_x':0.5,'center_y':0.6}
                 self.Height_input.size_hint = (None, None)
                 self.Height_input.size=(150,50)
                 layout.add_widget(Height_Label)
                 layout.add_widget(self.Height_input)
                 gender_dropdown=DropDown()
                 genders=["Female","Male"]
                 for gender in genders:
                         btn=Button(text=gender,font_name="Impact",size_hint_y=None,height=44)
                         btn.bind(on_release=lambda btn:gender_dropdown.select(btn.text))
                         btn.bind(on_release=self.gender_select)
                         gender_dropdown.add_widget(btn)
                 gender_btn=Button(text="Gender",font_name="Impact")
                 gender_btn.pos_hint={'center_x':0.5,'center_y':0.5}
                 gender_btn.size_hint=(None,None)
                 gender_btn.size=(150,50)
                 gender_btn.bind(on_release=gender_dropdown.open)
                 gender_dropdown.bind(on_select=lambda instance, value: setattr(gender_btn, 'text', value))
                 self.add_widget(gender_btn)
                 exercise_dropdown=DropDown()
                 Exercise_Status=[
                         "No Exercise","15 to 30 minutes","30 minutes to 1hour", "1 to 2 hours","More than 2 hours"]
                 for status in Exercise_Status:
                         btn=Button(text=status,font_name="Impact",size_hint_y=None,height=44)
                         btn.bind(on_release=lambda btn:exercise_dropdown.select(btn.text))
                         btn.bind(on_release=self.exercise_status)
                         exercise_dropdown.add_widget(btn)
                 exercise_stat=Button(text="Exercise Status",font_name="Impact")
                 exercise_stat.pos_hint={'center_x':0.5,'center_y':0.4}
                 exercise_stat.size_hint=(None,None)
                 exercise_stat.size=(150,50)
                 exercise_stat.bind(on_release=exercise_dropdown.open)
                 exercise_dropdown.bind(on_select=lambda instance, value: setattr(exercise_stat, 'text', value))
                 self.add_widget(exercise_stat)
                 diet_dropdown=DropDown()
                 diets_plans=["Maintainence Calories", "Bulking Calories","Cutting Calories"]
                 for i in diets_plans:
                         btn=Button(text=i,font_name="Impact",size_hint_y=None,height=44)
                         btn.bind(on_release=lambda btn:diet_dropdown.select(btn.text))
                         btn.bind(on_release=self.dietplan)
                         diet_dropdown.add_widget(btn)
                 diet_plan=Button(text="Diet Plan",font_name="Impact")
                 diet_plan.pos_hint={'center_x':0.5,'center_y':0.3}
                 diet_plan.size_hint=(None,None)
                 diet_plan.size=(150,50)
                 diet_plan.bind(on_release=diet_dropdown.open)
                 diet_dropdown.bind(on_select=lambda instance, value: setattr(diet_plan, 'text', value))
                 self.add_widget(diet_plan)
                 Submit=Button(text='Calculate',font_name='Impact')
                 Submit.pos_hint={'center_x':0.5,'center_y':0.2}
                 Submit.size_hint=(None,None)
                 Submit.size=(150,50)
                 Submit.bind(on_press=self.createBMR)
                 layout.add_widget(Submit)
                 self.add_widget(layout)
              
         def gender_select(self,instance):
                 print("Selected Gender:",instance.text)
                 self.gender=instance.text
                 
         def exercise_status(self,instance):
                 print("Selected Exercise Schedule:",instance.text)
                 self.exercise_status_value=instance.text
         def dietplan(self,instance):
                 print("Selected Diet Plan:",instance.text)
                 self.diet=instance.text
                
         def createBMR(self,instance):
                 from Backend import CalorieAppBackend
                 print("createBMR")
                 h=float(self.Height_input.text)
                 w=float(self.Weight_input.text)
                 age=int(self.Age_input.text)
                 g=str(self.gender)
                 d=str(self.diet)
                 e=str(self.exercise_status_value)
                 bmr=CalorieAppBackend.calc_BMR(self,h,w,age,g)
                 
                 if d=="Maintainence Calories":
                         calories=CalorieAppBackend.calc_Main(self,h,w,age,g,e)
                 elif d=="Bulking Calories":
                         calories=CalorieAppBackend.calc_bulk(self,h,w,age,g,e)
                 else:
                         calories=CalorieAppBackend.calc_cut(self,h,w,age,g,e)
                 
                 self.bmr=bmr
                 self.calories=calories
                 
                 self.parent.parent.current='output'
                 output_screen=self.parent.parent.get_screen('output')
                 output_screen.calculation(bmr,calories)
class CollectInput(Screen):
         def __init__(self,**kwargs):
                 print("Entering collectinput")
                 super(CollectInput,self).__init__(**kwargs)
                 self.content=CollectInputContent()
                 self.add_widget(self.content)
                
class Output(Screen):
         bmr_value=ObjectProperty(None)
         cal_value=ObjectProperty(None)
         
         def __init__(self,**kwargs):
                 super(Output,self).__init__(**kwargs)
         def calculation(self,bmr,calories):
                 print("Output Screen")
                 layout=RelativeLayout()
                 bmr_label=Label(text='BMR',font_name='Impact')
                 bmr_label.pos_hint={'center_x':0.4,'center_y':0.8}
                 self.bmr_value=Label(text=str(bmr),font_name='Impact')
                 self.bmr_value.pos_hint={'center_x':0.5,'center_y':0.8}
                 layout.add_widget(bmr_label)
                 layout.add_widget(self.bmr_value)
                 Cal_label=Label(text='Required Calorie Intake',font_name='Impact')
                 Cal_label.pos_hint={'center_x':0.3,'center_y':0.6}
                 self.cal_value=Label(text=str(calories),font_name='Impact')
                 self.cal_value.pos_hint={'center_x':0.5,'center_y':0.6}
                 layout.add_widget(Cal_label)
                 layout.add_widget(self.cal_value)
                 Calculate=Button(text="Calculate Body Fat",font_name='Impact')
                 Calculate.pos_hint={'center_x':0.5,'center_y':0.4}
                 Calculate.size_hint=(None,None)
                 Calculate.size=(150,50)
                 Calculate.bind(on_press=self.switch_to_calcfat)
                 layout.add_widget(Calculate)
                 self.add_widget(layout)
         def switch_to_calcfat(self,instance):
                 app=App.get_running_app()
                 app.root.current='final'
class CalcFat(Screen):
        Height_input=ObjectProperty(None)
        Waist_input=ObjectProperty(None)
        Neck_input=ObjectProperty(None)
        Hip_input=ObjectProperty(None)
        gender=''
        def __init__(self,**kwargs):
                 super(CalcFat,self).__init__(**kwargs)
                 layout=RelativeLayout()
                 Height_Label=Label(text='Height in cms:',font_name='Impact')
                 Height_Label.pos_hint={'center_x':0.3,'center_y':0.7}
                 self.Height_input=TextInput(multiline=False)
                 self.Height_input.pos_hint={'center_x':0.5,'center_y':0.7}
                 self.Height_input.size_hint = (None, None)
                 self.Height_input.size=(150,50)
                 layout.add_widget(Height_Label)
                 layout.add_widget(self.Height_input)
                 Hip_Label=Label(text='Hips size in cms:',font_name='Impact')
                 Hip_Label.pos_hint={'center_x':0.3,'center_y':0.6}
                 self.Hip_input=TextInput(multiline=False)
                 self.Hip_input.pos_hint={'center_x':0.5,'center_y':0.6}
                 self.Hip_input.size_hint = (None, None)
                 self.Hip_input.size=(150,50)
                 layout.add_widget(Hip_Label)
                 layout.add_widget(self.Hip_input)
                 Waist_Label=Label(text='Waist size in cms:',font_name='Impact')
                 Waist_Label.pos_hint={'center_x':0.3,'center_y':0.5}
                 self.Waist_input=TextInput(multiline=False)
                 self.Waist_input.pos_hint={'center_x':0.5,'center_y':0.5}
                 self.Waist_input.size_hint = (None, None)
                 self.Waist_input.size=(150,50)
                 layout.add_widget(Waist_Label)
                 layout.add_widget(self.Waist_input)
                 Neck_Label=Label(text='Neck size in cms:',font_name='Impact')
                 Neck_Label.pos_hint={'center_x':0.3,'center_y':0.4}
                 self.Neck_input=TextInput(multiline=False)
                 self.Neck_input.pos_hint={'center_x':0.5,'center_y':0.4}
                 self.Neck_input.size_hint = (None, None)
                 self.Neck_input.size=(150,50)
                 layout.add_widget(Neck_Label)
                 layout.add_widget(self.Neck_input)
                 gender_dropdown=DropDown()
                 genders=["Female","Male"]
                 for gender in genders:
                         btn=Button(text=gender,font_name="Impact",size_hint_y=None,height=44)
                         btn.bind(on_release=lambda btn:gender_dropdown.select(btn.text))
                         btn.bind(on_release=self.gender_select)
                         gender_dropdown.add_widget(btn)
                 gender_btn=Button(text="Gender",font_name="Impact")
                 gender_btn.pos_hint={'center_x':0.5,'center_y':0.3}
                 gender_btn.size_hint=(None,None)
                 gender_btn.size=(150,50)
                 gender_btn.bind(on_release=gender_dropdown.open)
                 gender_dropdown.bind(on_select=lambda instance, value: setattr(gender_btn, 'text', value))
                 self.add_widget(gender_btn)
                 Submit=Button(text="Calculate",font_name='Impact')
                 Submit.pos_hint={"center_x":0.5,"center_y":0.2}
                 Submit.size_hint=(None,None)
                 Submit.size=(150,50)
                 Submit.bind(on_press=self.show_fat)
                 layout.add_widget(Submit)
                 self.add_widget(layout)
        def gender_select(self,instance):
                 print("Selected Gender:",instance.text)
                 self.gender=instance.text
        def show_fat(self,instance):
                from Backend import CalorieAppBackend
                height=float(self.Height_input.text)
                waist=float(self.Waist_input.text)
                neck=float(self.Neck_input.text)
                hip=float(self.Hip_input.text)
                gender=str(self.gender)
                fat=CalorieAppBackend.calc_fat_perc(self,waist,height,gender,hip,neck)
                self.fat=fat
                app=App.get_running_app()
                app.root.current='sfinal'
                show_fatscreen=app.root.get_screen('sfinal')
                show_fatscreen.calculate_fat(fat)
class ShowFinalResult(Screen):
        def __init__(self,**kwargs):
                 super(ShowFinalResult,self).__init__(**kwargs)
        def calculate_fat(self,fat):
                print("calcculate_fat")
                layout=RelativeLayout()
                Fat_label=Label(text=f"Your Body Fat Percentage is around: {fat}%",font_name='Impact')
                Fat_label.pos_hint={'center_x':0.5,'center_y':0.5}
                layout.add_widget(Fat_label)
                self.add_widget(layout)
                
class CaloriesApp(App):
        def build(self):
                sm=ScreenManager()
                loading_ob=Loading(name='load')
                loading_ob.on_entry()
                startpage_ob=StartPage(name='start')
                collectinput_ob=CollectInput(name='input')
                output_ob=Output(name='output')
                calc_ob=CalcFat(name='final')
                show_ob=ShowFinalResult(name='sfinal')
                sm.add_widget(loading_ob)
                sm.add_widget(startpage_ob)
                sm.add_widget(collectinput_ob)
                sm.add_widget(output_ob)
                sm.add_widget(calc_ob)
                sm.add_widget(show_ob)
                sm.current='load'
                print("Current Screen:",sm.current) 
                print(sm.screen_names)
                print(kivy.__version__)
                return sm
        def exitapp(self):
                App.get_running_app().stop()

if __name__ == '__main__':
        app=CaloriesApp()
        CaloriesApp.instance=app
        app.run()
                          