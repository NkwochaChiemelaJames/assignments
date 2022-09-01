def mul_1(a):
    for i in range(1,11):
        ansa1  = str(a) + "x" + str((i+1)-1) + "=" + str(a*((i+1)-1))
        #print(ansa1)
        return ansa1
m1 = mul_1(1)
m2 = mul_1(2)
zip = zip(m1,m2)
print(zip)
print(m1 + "|" + m2)
