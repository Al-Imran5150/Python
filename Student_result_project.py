class Students:
    def __init__(self,name,_id,semester,result):
        self.name = name
        self.sem = semester
        self.id = _id
        self.res = result
    def get_name (self):
        return self.name
    def get_result (self):
        return self.res
    def get_view (self):
        return f" Name : {self.name}\n ID : {self.id}\n Semester : {self.sem}\n Result : {self.res}\n"
    
students_list = [
    Students("Md Aminul Islam", 12111028, "3rd", 3.87),
    Students("Sabikun Nahar", 12111001, "3rd", 3.83),
    Students("Afsana akter", 12111008, "3rd", 3.85),
    Students("Nirob Hossen", 12111002, "3rd", 3.76),
    Students("Humayra Akter", 12111028, "3rd", 3.79),
    ]
_res = float(input("Result : "))
for stu in students_list:
    if stu.get_result() >= _res:
     print(stu.get_view())
    
class Students:
    def __init__(self,name,_id,semester,result):
        self.name = name
        self.sem = semester
        self.id = _id
        self.res = result
    def get_name (self):  
        return self.name 
    def get_result (self):  
        return self.res 
    def get_view (self):  
        return f" Name : {self.name}\n ID : {self.id}\n Semester : {self.sem}\n Result : {self.res}\n"  
        
students_list = [
    Students("Md Aminul Islam", 121, "3rd", 3.87),
    Students("Md Riyadul Islam", 122, "3rd", 3.89),
    Students("Afsana Akter", 123, "3rd", 3.92),
    Students("Md Raj", 124, "3rd", 4.00),
    Students("Humayra Akter", 125, "3rd", 3.82),
]

_res = float(input("Enter your result : "))
for stu in students_list:
    if stu.get_result() >= _res :
     print(stu.get_view())
    