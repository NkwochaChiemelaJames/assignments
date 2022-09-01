#Function to calclate retirement date and retirement age for all levels.
def retire1(age,appyear):
    print(f"Your retirement age is {age+30}, by the year {appyear+30}")

def retire2(age,appyear):
    print(f"Your retirement age is {age+29}, by the year {appyear+29}")

def retire3(age,appyear):
    print(f"Your retirement age is {age+28}, by the year {appyear+28}")

def retire4(age,appyear):
    print(f"Your retirement age is {age+27}, by the year {appyear+27}")

def retire5(age,appyear):
    print(f"Your retirement age is {age+26}, by the year {appyear+26}")

def retire6(age,appyear):
    print(f"Your retirement age is {age+25}, by the year {appyear+25}") 

def retire7(age,appyear):
    print(f"Your retirement age is {age+24}, by the year {appyear+24}")

def retire8(age,appyear):
    print(f"Your retirement age is {age+23}, by the year {appyear+23}")
    
def retire9(age,appyear):
    print(f"Your retirement age is {age+22}, by the year {appyear+22}")

def retire10(age,appyear):
    print(f"Your retirement age is {age+21}, by the year {appyear+21}")                 

def workingsector(sector):
    # f0r the government sector
    if sector == "yes":
        grade = int(input("please enter your level:\n"))
        salary = 150000
        salary2 = ((19/100)*salary) + salary
        salary3 = ((19/100)*salary2) + salary2
        salary4 = ((19/100)*salary3) + salary3
        salary5 = ((19/100)*salary4) + salary4
        salary6 = ((19/100)*salary5) + salary5
        salary7 = ((19/100)*salary6) + salary6
        salary8 = ((19/100)*salary7) + salary7
        salary9 = ((19/100)*salary8) + salary8
        salary10 = ((19/100)*salary9) + salary9
        if grade == 1:
            retire1((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary)
        elif grade == 2:
            retire2((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary2)
        elif grade == 3:
            retire3((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary3)
        elif grade == 4:
            retire4((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary4)
        elif grade == 5:
            retire5((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary5)
        elif grade == 6:
            retire6((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary6)
        elif grade == 7:
            retire7((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary7)
        elif grade == 8:
            retire8((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary8)
        elif grade == 9:
            retire9((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary9)
        elif grade == 10:
            retire10((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary10)
        else:
            print("please input a correct level")
    # for the private sector
    elif sector == "no":
        print("you are definitely working in the private sector")
        salary_private = int(input("please enter the basic salary for a level 1 worker\n"))
        grade_private = int(input("please enter your level\n"))
        salary_private2 = ((19 / 100) * salary_private) + salary_private
        salary_private3 = ((19 / 100) * salary_private2) + salary_private2
        salary_private4 = ((19 / 100) * salary_private3) + salary_private3
        salary_private5 = ((19 / 100) * salary_private4) + salary_private4
        salary_private6 = ((19 / 100) * salary_private5) + salary_private5
        salary_private7 = ((19 / 100) * salary_private6) + salary_private6
        salary_private8 = ((19 / 100) * salary_private7) + salary_private7
        salary_private9 = ((19 / 100) * salary_private8) + salary_private8
        salary_private10 = ((19 / 100) * salary_private9) + salary_private9
        if grade_private == 1:
            retire1((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is" , salary_private)
        elif grade_private == 2:
            retire2((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary_private2)
        elif grade_private == 3:
            retire3((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary_private3)
        elif grade_private == 4:
            retire4((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary_private4)
        elif grade_private == 5:
            retire5((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary_private5)
        elif grade_private == 6:
            retire6((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary_private6)
        elif grade_private == 7:
            retire7((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary_private7)
        elif grade_private == 8:
            retire8((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary_private8)
        elif grade_private == 9:
            retire9((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary_private9)
        elif grade_private == 10:
            retire10((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
            print("your wage is", salary_private10)
        else:
            print("input levels from 1 to 10")
    else:
        print("reply with yes/no")

try:
    workingsector(input("are you working for the government \n(reply with yes/no)\n"))
except:
    print("look for your error")
