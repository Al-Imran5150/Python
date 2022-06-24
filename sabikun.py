file = open("info.txt","a")

print("Select operation.")
print("1.Add")
print("2.Sub")
print("3.Mul")
print("4.Div")

while True:
    
    choice = input("Enter choice(1,2,3,4):")

    
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        file.write("\nYour first number : "+ str(num1))
        num2 = float(input("Enter second number: "))
        file.write("\nYour first number : " + str(num2))
        if choice == '1':
            add = (num1 + num2)
            print(num1, "+", num2, "= ",add)
            file.write("\nYour result : "+str(add))
            
        elif choice == '2':
            sub = (num1 - num2)
            print(num1, "-", num2, "=",sub)
            file.write("\nYour Result : "+str(sub))
            
        elif choice == '3':
           mul = (num1 * num2)
           print(num1, "*", num2, "=",mul)
           file.write("\nYour Result : "+str(mul))
           
        elif choice == '4':
            div = (num1 / num2)
            print(num1, "/", num2, "=",div)
            file.write("\nYour Result : "+str(div))
            
        
        
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
        file.close()
    else:
        print("Invalid")
        file.close()