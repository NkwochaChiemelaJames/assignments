# program to convert centimeter to meter and vise versa
value = input("are you converting to centimeter or to meter: \n")
if value == "centimeter":
    value_m = int(input("enter the value in meter: \n"))
    print("it is {} centimeter".format(value_m * 100))
elif value == "meter":
    value_cm = int(input("enter the value in centimeter: \n"))
    print("it is {} meter".format(value_cm / 100))
else:
    print("please enter centimeter or meter")