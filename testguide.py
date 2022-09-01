def gradefunctioncaller(level):
    from testproject import level
    if level == 1:
        retire1((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
    elif level == 2:
        retire2((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
    elif level == 3:
        retire3((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
    elif level == 4:
        retire4((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
    elif level == 5:
        retire5((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
    elif level == 6:
        retire6((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))  
    elif level == 7:
        retire7((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
    elif level == 8:
        retire8((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))
    elif level == 9:
        retire9((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))             
    elif level == 10:
        retire10((int(input("Input Your age:\n"))),(int(input("Input Your Year of appointment:\n"))))


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



        

        
