data=open('demo.txt','r')
data=data.read().split(':')
while True:
    que = input("What is Your Quetion : ")    
    for item in data:
         if que in item and "Is anyone available here?":
            print("Yes, available.")
            break
         elif que in item and "How much time do you provide service?":
            print("24 hours, 7 days.")
            break
         elif que in item and "Do you have any weekly holiday?":
            print("No.")
            break
         elif que in item and "What kind of service can you provide us?":
            print("Offline and online service also")
            break
         elif que in item and "What is the payment method of online delivery":
            print("Cash on delivery.")
            break
         elif que in item and "Can you show some sample of product?":
            print("Ofcourse.")
            break
         elif que in item and "Do you have any regional limitations?":
           print("No.")
           break     
         else:
           print("I don't know") 
           break   
     
    
    





