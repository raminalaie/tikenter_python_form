from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
   
   
class frist(GridLayout):
      def __init__(self, **kwargs):
            super(frist,self).__init__(**kwargs)
            
            self.cols = 1
            self.inside = GridLayout()
            self.inside.cols = 2
            
            self.inside.add_widget(Label(text = "first_name"))
            self.fname = TextInput(multiline = False)
            self.inside.add_widget(self.fname)
            
                       
            self.inside.add_widget(Label(text = "last_name"))
            self.lname = TextInput(multiline = False)
            self.inside.add_widget(self.lname)
            
            
            self.inside.add_widget(Label(text = "id_number"))
            self.idnumber = TextInput(multiline = False)
            self.inside.add_widget(self.idnumber)
            
            self.inside.add_widget(Label(text = "number"))
            self.number_phon = TextInput(multiline = False)
            self.inside.add_widget(self.number_phon)
                        
            self.add_widget(self.inside)
            
            self.submit = Button(text ="SUBMIT" , font_size = 50, size = (32,32))
            self.submit.bind(on_press = self.pressed)
            self.add_widget(self.submit)
            
      def pressed(self,instance):
            name = self.fname.text
            lname = self.lname.text
            id_number = self.idnumber.text
            number = self.number_phon.text
            
            print("fname = ", name, "lanme = ", lname , "idnumber = " , id_number, "number = ", number )
            
            self.fname.text = ""
            self.lname.text = ""
            self.idnumber.text = ""
            self.number_phon.text = ""
            
                  
class regester(App):
      def build(self):
            return frist()
      
regester().run()      