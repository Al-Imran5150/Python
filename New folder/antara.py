file = open("cal_info.txt","a")
import calendar

print("Enter Year: ")
yy = input()
file.write("\nEnter year : "+ str(yy))
print("\nEnter Month Number (1-12): ")
mm = input()
file.write("\nEnter Month Number (1-12): "+ str(mm))

y = int(yy)
m = int(mm)
f = calendar.month(y, m)
print("\n", f)
file.write("\nYour result : "+ str(f))
file.close()