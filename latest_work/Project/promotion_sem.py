print("...........Promotion 4th semester...........\n\n")
_name = input("Enter your name : ")
_id = input("Enter your ID : ")
_sem = input("Last semester name : ")
if _sem == "3rd":
    _res = input("Are you going to show your result : ")
    if _res == "Yes" or "yes":
        _coa = input("Enter your COA result : ")
        _ad = input("Enter your Algorithm result : ")
        _op = input("Enter your Operating System result : ")
        _dbms = input("Enter your DBMS result : ")
        _dm = input("Enter your Discrete Mathematics result : ")
        _math = input("Enter your Mathematics result : ")
        if _coa == "F" or _ad == "F" or _op == "F" or _dbms == "F" or _dm == "F" or _math == "F" :
            print("Sorry! you have not passed 3rd semester ")
        elif _coa and _ad and _op and _dbms and _dm and _math == "A+" or "A" or "A-" or "B" or "C" :
            print("Congratulations! you have passed fourth semester ")    
    else:
        print("Sorry you didn't get permission.")    
       
else :
    print("Sorry you didn't get permission.")    