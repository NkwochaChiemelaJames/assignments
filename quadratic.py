# a program to solve quadratic equation
print("please input the value for a, b and c")
a = int(input())
b = int(input())
c = int(input())
norm = (b**2)-4*a*c
root_norm = norm**0.5
add_b_pos = -b + root_norm
add_b_neg = -b - root_norm
dnorm_pos = add_b_pos/2*a
dnorm_neg = add_b_neg/2*a
print("the positive answer is", dnorm_pos)
print("the negative answer is", dnorm_neg)
