# program to convert centimeter to meter and vise versa
print("are you converting to centimeter or to meter")
if value == "centimeter":
    print("enter the value in meter")
    value_m = int(input())
    m = value_m * 100
    print("it is ", m, "centimeter")
elif value == "meter":
    print("enter the value in centimeter")
    value_cm = int(input())
    cm = value_cm / 100
    print("it is ", cm, "meter")
else:
    print("please enter centimeter or meter")
