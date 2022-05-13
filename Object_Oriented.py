#------------------------------------------------------------------------------
# Object
a = 10  
b = "Aminul"
print(a)
print(b)
#------------------------------------------------------------------------------



#------------------------------------------------------------------------------
# Class 
class Imran:
    # "Aminul Islam"
    age =22
    
ob = Imran()
print(Imran.age)

class Cartoon:
    series = "Tv Series" # Class Variable
    
obj1 = Cartoon()
obj2 = Cartoon()

obj1.name = "Tom & jerry"
obj1.ch = "CN"

obj2.name = "Chota beam"
obj2.ch = "Nick"

print(obj1.name)
print(obj1.ch)
print()
print(obj2.name)
print(obj2.ch)

 # _init_/Constructor 
class Cartoon:
    "Aminul"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(self.name)
        print(self.age)
        
     
obj1 = Cartoon("Tom & jerry",10)
obj2 = Cartoon("Chota beam","Nick")

obj1.show()
print(Cartoon.__doc__)

#----------------------------------------------------------------------------
class Person:
    def __init__(self,name,date,age):
        self.name = name
        self.date = date
        self.age = age
    def show(self):
        print(self.name)
        print(self.date)
        print(self.age)
    
    def set_name(self, new_name):
        if self.validation(new_name):
            print("Name is non valid")
            return 
        self.name = new_name 
    def validation(self,str):
        return "0" in str   
        
person1 = Person("Aminul","20/11/2000",22)
person1.set_name("Imran")
print(person1.name)

#----------------------------------------------------------------------------

class Person:
    def __init__(self,name,date,age):
        self.name = name
        self.date = date
        self.age = age
    def show(self):
        print(self.name)
        print(self.date)
        print(self.age)

person_list1 = Person("name", "date", 3)
person_list = [Person("name", "date", 3),
               Person("name", "date", 3),
               Person("name", "date", 3)
              ]
print(person_list1.show())  

#----------------------------------------------------------------------------

class Person:
    def __init__(self,name,date,age):
        self.name = name
        self.date = date
        self.age = age
        
    def get_name (self):
        return self.name
    
    def get_date (self):
        return self.date
    
    def date (self):
        return self.date
    
    def get_summary (self):
        return f"Name : {self.name}, Date : {self.date}, age : {self.age}"
    
    def set_name(self, new_name):
        if self.validation(new_name):
            print("Name is non valid")
            return 
        self.name = new_name 
    def validation(self,str):
        return "0" in str
    
    

person_list = [Person("name", 41 , 3),
               Person("name", 50 , 3),
               Person("name", 60 , 3)]
              
for man in person_list:
   if man.get_date() is not None and man.get_date() >= 45:
        print(man.get_summary())

      