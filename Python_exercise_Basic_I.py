 # Problem 1

poem = '''Twinkle, twinkle, Little star,
                How I wonder what you are!
                        Up above the world so high,
                        like a diamond in the sky.
          Twinkle, twinkle, Little star,
                          How I wonder what you are'''
                          
print(poem)                         

 # Problem 2
 
import sys # modules
print("Python version check ")
print(sys.version)
print("Python version info ")
print(sys.version_info)

 # Problem 3
 
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

 # Problem 4
 
print("Calculate the aria of circle ")
redius = float(input("Value of redius : "))
area = 3.1416*(redius**2)
print("Aria is : ",area)

 # Problem 5
 
first = input("Enter your first name : ")
second = input("Enter your second name : ")

print("First operation : {} {} ".format(first,second))
temp = None 
temp = first
first = second
second = temp

print("Second operation : {} {} ".format(first,second))

 # Problem 6
 
numbers=input("Enter numbers:").split()
list = (numbers)
tup = tuple((numbers))
print(list)
print(tup)

 # Problem 7
 
 # Problem 8
 
color_list = input("Enter your colors : ").split()
print("First color : {} & second color : {} ".format(color_list[0],color_list[-1]))

 # Problem 9
 
date = ["04","06","2022"]
print("Your exam date : {} / {} / {} ".format(date[0],date[1],date[2]))

 # problem 10


