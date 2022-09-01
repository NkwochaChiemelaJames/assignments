def workingsector(sector):
    # f0r the government sector
    if sector == "yes":
        grade = int(input("please enter your level\n"))
        salary = 150000
        salary2 = ((19/100)*salary) + salary
        salary3 = ((19/100)*salary) + salary2
        salary4 = ((19/100)*salary) + salary3
        salary5 = ((19/100)*salary) + salary4
        salary6 = ((19/100)*salary) + salary5
        salary7 = ((19/100)*salary) + salary6
        salary8 = ((19/100)*salary) + salary7
        salary9 = ((19/100)*salary) + salary8
        salary10 = ((19/100)*salary) + salary9
        if grade == 1:
            print("your wage is", salary)
        elif grade == 2:
            print("your wage is", salary2)
        elif grade == 3:
            print("your wage is", salary3)
        elif grade == 4:
            print("your wage is", salary4)
        elif grade == 5:
            print("your wage is", salary5)
        elif grade == 6:
            print("your wage is", salary6)
        elif grade == 7:
            print("your wage is", salary7)
        elif grade == 8:
            print("your wage is", salary8)
        elif grade == 9:
            print("your wage is", salary9)
        elif grade == 10:
            print("your wage is", salary10)
        else:
            print("please input a correct level")
    # for the private sector
    elif sector == "no":
        print("you are definitely working in the private sector")
        salary_private = int(input("please enter the basic salary for a level 1 worker\n"))
        grade_private = int(input("please enter your level\n"))
        salary_private2 = ((19 / 100) * salary_private) + salary_private
        salary_private3 = ((19 / 100) * salary_private) + salary_private2
        salary_private4 = ((19 / 100) * salary_private) + salary_private3
        salary_private5 = ((19 / 100) * salary_private) + salary_private4
        salary_private6 = ((19 / 100) * salary_private) + salary_private5
        salary_private7 = ((19 / 100) * salary_private) + salary_private6
        salary_private8 = ((19 / 100) * salary_private) + salary_private7
        salary_private9 = ((19 / 100) * salary_private) + salary_private8
        salary_private10 = ((19 / 100) * salary_private) + salary_private9
        if grade_private == 1:
            print("your wage is" , salary_private )
        elif grade_private == 2:
            print("your wage is", salary_private2)
        elif grade_private == 3:
            print("your wage is", salary_private3)
        elif grade_private == 4:
            print("your wage is", salary_private4)
        elif grade_private == 5:
            print("your wage is", salary_private5)
        elif grade_private == 6:
            print("your wage is", salary_private6)
        elif grade_private == 7:
            print("your wage is", salary_private7)
        elif grade_private == 8:
            print("your wage is", salary_private8)
        elif grade_private == 9:
            print("your wage is", salary_private9)
        elif grade_private == 10:
            print("your wage is", salary_private10)
        else:
            print("input levels from 1 to 10")
    else:
        print("reply with yes/no")


workingsector(input("are you working for the government \n(reply with yes/no)\n"))
import guide     

