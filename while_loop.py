# example 1
n = 153
sum = 0
while n > 0:
    r = n % 10
    sum += r
    n = n/10
print(sum)

# example 2
x = 0
while x < 5:
    print("x is" + str(x))
    x = x + 1
print("cannot move further")

# example 3
student = 5
while student > 0:
    print("someone just left")
    student-=1
print("all student gone")
    