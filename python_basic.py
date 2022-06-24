#------------------------------------------------------------------------------
# Print()- function

print("Aminul","Islam","Imran")
print("Aminul","Islam","Imran",sep="+")

print("Aminul","Islam","Imran",end="\n")
print("Student of ugv")
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Print()- multiple argument

  # Pass value as parameters
a = "I"
b = "Love"
c = "Allah"
print(a,b,c)

  # Use string formating
     # (1)- Sequential formatting pass value
a = "I"
b = "Love"
c = "Allah"    
print("{} also {} my {}".format(a,b,c))
     # (2)- Formatting the number
a = "I"
b = "Love"
c = "Allah"
print("{1} also {2} my {0}".format(a,b,c))
     # (3)- Pass value as a tuple
a = "I"
b = "Love"
c = "Allah"
print("%s also %s my %s"%(a,b,c))
     # (4)- Pass value dictionary
a = "I"
b = "Love"
c = "Allah"
print("%(a)s %(b)s %(c)s"%{"a" : "Aminul" ,"b" : "islam","c" : "imran"})
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Input()- Function

  # Input
value = input()
print(value)
  # Promot -> display message
name = input("Enter your name : ")
print(name)
  # Type Casting
name = input("Enter your name : ")
age = int(input("Enter your age : "))
print("name: {}\nage: {}".format(name,age))
  # Multiple input one line
a,b,c,d,e = input("Enter Your roll : ").split()
print("{} {} {} {} {}".format(a,b,c,d,e))
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Arithmetic Operator

num1 = 6
num2 = 5

print(num1 + num2)  # Addition
print(num1 - num2)  # Substraction
print(num1 * num2)  # Multiplication
print(num1 / num2)  # Division-float
print(num1 // num2) # Division-floor
print(num1 % num2)  # Modulus
print(num1 ** num2) # Power
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Comparision/Relational operators

num1 = 6
num2 = 5

print(num1 == num2)  # Equal
print(num1 != num2)  # Not Equal
print(num1 > num2)   # greater than
print(num1 < num2)   # less than
print(num1 >= num2)  # greater than equal
print(num1 <= num2)  # less than equal
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Logical operators

num1 = 6
num2 = 5

print(num1 == 6 and  num2== 5)  # AND
print(num1 == 6 or  num2== 5)   # OR
print(not num1 == 6)            # NOT
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#Memberships operator 

char1 = "Aminul islam"
char2 = "Al Imran"
print("Ami" in char1 ) # Check string
print("imran" not in char2 )

if "Aminul" in char1:
   print("paichi")
else:
 print("painay")    
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#Identity operators

num1 = 50
num2 = 50
 
print(num1 is num2 ) # memory location check
print(num1 is not num2 )
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Bitwise Operators

num1 = 5
num2 = 4

print(num1 & num2) # Bitwise And(&)
    # 5 = 00000101
    # 4 = 00000100
    # --------------
    #     00000100 = 4         

print(num1 | num2) # Bitwise Or(|)
print(~ num2) # Bitwise Not(~)
print(num1 ^ num2) # Bitwise XOR(^)
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Assignment operators

a = 5
a += 10 # a = a + 10
print(a)

a = 5
a -= 10 # a = a - 10
print(a)

a = 5
a *= 10 # a = a * 10
print(a)

a = 5
a /= 10 # a = a / 10
print(a)

a = 5
a //= 10 # a = a // 10 
print(a)

a = 5
a %= 10 # a = a % 10
print(a)

a = 5
a **= 10 # a = a ** 10
print(a)
#------------------------------------------------------------------------------

 
#------------------------------------------------------------------------------
# Flow control/descision making

   # Small project use if-else
print("Application for Courses \n ---------------------------------------")
name = input("Enter your name : ")
sem = input("Enter your semester : ")
gender = input("Enter your gender : ")
cgpa = float(input("Enter your last semester CGPA : "))

if sem == "3rd":
    if gender == "male" and cgpa > 3.50:
         
            print("Congraculation!🥳🥳  Mr. ",name,"You are selected our course")
    
    elif gender == "female" and cgpa > 3.20:
        
            print("Congraculation!🥳🥳  Ms.",name,"You are selected our course")       
else :
 print("Sorry! Its course not for you")
 
   # Small project use loop

 print("Proposel project ❤️❤️ \n---------------------" )
                                                           # Creator Al-Imran
 print("Crush : Are you love me ?")
 ans = input("You :")
 
 if ans == "yes":
    print("\nCrush : Then propose to me ten times.")
    propose =  input("you : It's ok :- ")
    i=1
    n= int(input("How much time :"))
    while i<=n: 
     print(propose)
     i += 1
    if n>9:
     print("Crush : I love you 2 🥰😘😍")  
    else:
     print("Crush : Sorry! i don't like") 
      
 else:
     print("Crush : Sorry! i don't like it.") 
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Data types

    # (1)->None
    
     a = 10
     a = None 
     print(a)
   
    # (2)->Boolean
      
     print(6<4)
     
    # (3)->Number(int,float,complex)
     
     a = print(55,type(55)) # int number
     b = print(55.48,type(55.48)) # float number
     c = print(78 + 40j,type(78 + 40j)) # comlpex number 
     
    # (4)->String
    
      # Single line
      
     s1 = print('Aminul islam',type('Aminul islam'))
     s2 = print('Aminul islam',type("Aminul islam"))
    
      # multi line 
      
     s3 = '''My name is al imran
             i am a student'''            
#------------------------------------------------------------------------------      
    

#------------------------------------------------------------------------------            
# String method

 s = "Aminul islam al-imran"
 p = "01976672506"
 d = "33333imraniiii"
 f = "Aminul \n islam"

 print(s.capitalize())
 
 print(s.title())
 
 print(s.upper())
 
 print(s.casefold())
 
 print(s.lower())
 
 print(s.join("*/"))
 
 print(s.find("imran"))

 print(s.center(50))
 
 print(s.rjust(50))
 
 print(s.count("i"))
 
 print(d.strip("3i")) # delete
 
 print(s.split()) # divide and convert to list of array
 
 print(f.splitlines(False)) 
 
 print(s.rpartition("al"))
 
 print(s.swapcase())
 
 print(s.endswith("o")) # last value
 
 print(s.startswith("Aminul")) # first value
 
 print(s.zfill(50))
 
 print(s.replace("Aminul", "Imran"))
 
 print(s.islower())
 
 print(s.istitle())
 
 print(s.isupper())
 
 print(s.isnumeric())
 
 print(p.isdecimal())
 
 print(p.isdecimal())
 
 print(s.isalpha())
 
 print(s.isalnum())
 
 print(s.isspace())
#------------------------------------------------------------------------------ 


#------------------------------------------------------------------------------
# List 

list1 = ["Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby"]
list2 = ["Nirob","Turjo","Badhon"]
list3 = ["Humayra","Limon",["Antara","marzia"]] # Nested List
     
print(list1)

print(list1+list2+list3) # Constructor

print(list1[2]) # Index

print(list1[1:3]) # Range

 # Add/Insert

list1 = ["Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby"]
list2 = ["Nirob","Turjo","Badhon"]
list3 = ["Humayra","Limon",["Antara","marzia"]] # Nested List

list1.append("Hridoy") # Add to last index
print(list1)

list2.extend(["Akash","Prince","Shanta"]) # Add to multiple string
print(list2)

list3.insert(1, "Mehedi") # Add to specific index 
print(list3)

 # Change
 
list1 = ["Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby"]
list2 = ["Nirob","Turjo","Badhon"]
list3 = ["Humayra","Limon",["Antara","marzia"]] # Nested List

list2[1] = "Asriful Parvez"
print(list2)

list1[1:3] = ["Afsana","Choto"] # Changed using Range
print(list1)

 # Delete
 
list1 = ["Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby"]
list2 = ["Nirob","Turjo","Badhon"]
list3 = ["Humayra","Limon",["Antara","marzia"]] # Nested List

del list1[3:5]
print(list1)

list1.remove("Aminul")
print(list1)

list1.pop()
print(list1)

list1.clear()
print(list1)

 # Loop
 
list1 = ["Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby"]
list2 = ["Nirob","Turjo","Badhon"]
list3 = ["Humayra","Limon",["Antara","marzia"]] # Nested List

for i in list1:
   print(i) 
   
for i in list3:  # Using nested list
    if type(i) == list:
        for j in i:
            print(j)
    else :
       print(i)   

 # Length
 
list1 = ["Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby"]
list2 = ["Nirob","Turjo","Badhon"]
list3 = ["Humayra","Limon",["Antara","marzia"]] # Nested List

print(len(list1))

print(len(list2[1]))

print(len(list3[2]))

 # Membership
 
list1 = ["Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby"]

name = input("Search your name : ")
if name in list1:
    print("paichi")
else :
    print("Painay")
    
 # Repitation
 
list1 = ["Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby"]

print(list1*3)

 # Copy 
 
list1 = ["Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby"]
list2 = ["Nirob","Turjo","Badhon"]
list3 = ["Humayra","Limon",["Antara","marzia"]] # Nested List

list1 += list2.copy()
print(list1)

#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# List method

list1 = ["Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby"]
list2 = [3,8,9,2,48,6,]

print(list1.index("Zerin")) # index

print(list1.count("Aminul")) # Count

list1.reverse() # reverse
print(list2)

list1.sort() # Sort
print(list1)

list1.sort(key=len) # sort use object
print(list1)

print(sorted(list1))

print(max(list2))

print(min(list2))

print(sum(list2))

#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Tuple 

list1 = ("Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby")
list2 = [3,8,9,2,48,6,]
list3 = tuple(("Aminul","Rima","Sabikun Nahar","Zerin","Fazle Rabby")) # constructor

print(list1.index("Zerin")) # index

print(list1.count("Aminul")) # Count

print(max(list2))

print(min(list2))

print(sum(list2))
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Dictionary

list1 = {"stu1" : "Aminul",   
         "stu2" : "Rima",
         "stu3" : "sabikun"}

print(type(list1))


list2 = {"1" : "Nirob", # int 
         "2" : "Badhon",
         "3" : "Akash"}

print(list2)

print(list2["1"])

list3 = {"name" : "Aminul islam", # Mixed
         "age" : 22,
         "2" : "Imran"}
 
print(list3)      
        
list4 = dict({"name" : "Aminul islam", # Constructor
               "age" : 22,
               "2" : "Imran"})

print(list4) 

list5 = dict(name = "Aminul islam", # Constructor 2
             age = 22,
             nickname = "Imran",)

print(list5)   

list6 = dict({"name" : "Aminul islam", # nested set
              "age" : 22,
              "info" : {"id" : "12111028",
                        "sem" : "3rd", 
                        "dep" : "cse"}})

print(list6) 

print(list6["info"]["id"])

print(list6.get("age")) # Using get method

 # Add/insert and change
 
list1 = dict({"name" : "Aminul islam", 
               "age" : 22,
               "2" : "Imran"})

list1["stu3"] = "Humayra"
list1["2"] = "cse" # Change

print(list1)

 # Delete
 
list6 = dict({"name" : "Aminul islam", # nested set
              "age" : 22,
              "info" : {"id" : "12111028",
                        "sem" : "3rd", 
                        "dep" : "cse"}})

del list6["age"] 

print(list6)

list6.pop("name")

print(list6)

list6.popitem()

print(list6)

 # for loop
 
list6 = dict({"name" : "Aminul islam", # nested set
              "age" : 22,
              "info" : {"id" : "12111028",
                        "sem" : "3rd", 
                        "dep" : "cse"}})

for i,j in list6.items():
    
    print(i,"=", j)

for i in list6.values():
   print(i)    

 # Method 
 
list6 = dict({"name" : "Aminul islam", # nested set
              "age" : 22,
              "info" : {"id" : "12111028",
                        "sem" : "3rd", 
                        "dep" : "cse"}})
new = {"building" : "B2",}

print(list6.keys()) 

print(list6.values())

print(list6.items())

list6.update(new)

print(list6)
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Set ( Unorder Unindexed no dublicate value )

set1 = {"aminul","Rima","Sabikun",1,2,3} # List,set and dictionary no assigned

print(set1)

set2 = set(("Humayra","Nirob","Badhon")) # use constructor

print(set2)

 # loop
 
set1 = {"aminul","Rima","Sabikun",1,2,3} 

for i in set1:
    print(i)

 # Add
 
set1 = {"aminul","Rima","Sabikun",1,2,3}

set1.add("Imran")

print(set1)

set1.update(["Akash","Hridoy"])

print(set1)

 # Delete
 
set1 = {"aminul","Rima","Sabikun",1,2,3}

set1.remove("aminul")

print(set1)

set1.discard(1)

print(set1)

set1.pop()

print(set1)

set1.clear()

print(set1)

 # Join
 
set1 = {"aminul","Rima","Sabikun",1,2,3}
set2 = set(("Humayra","Nirob","Badhon"))

set1.update(set2)

print(set1)

set1.union(set2)

print(set1)

 # set oparetion
 
a,b = {1,6,3,7,5},{2,6,5,8}

a.union(b)

print(a.union(b))

a.intersection(b)

print(a.intersection(b))

a.difference(b)

print(a.difference(b))

a.symmetric_difference(b)

print(a.symmetric_difference(b))

a,b = {1,6,3,7,5},{2,6,5,8}

c = frozenset(b)

print(b)

print(a.issubset(b))

print(a.issuperset(b))

print(a.isdisjoint(b))
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
# Function

a = int(input("Enter your first number : "))
b = int(input("Enter your second number : "))

def Calculator(a,b):
  op =  input("Type Your Operations : ")
  if op == "+":
    print(a + b)      
  elif op == "-": 
    print(a - b)
    
Calculator(a,b)    
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------

 