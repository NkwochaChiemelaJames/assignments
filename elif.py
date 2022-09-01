"""greet a user
input ur jamb score
if score is 70 to 100
print excellent result
but if score is 60 to 69
print very good
if score range 50 to 59
print good
but if score is 40 to 49
print fair
but if score is 0 to 39
print poor"""

print("how ae you" '\n' "enter your score")
score = int(input())
if score in range(70, 101):
    print("excellent")
elif score in range(60, 70):
    print("very good")
elif score in range(50, 60):
    print("good")
elif score in range(40, 50):
    print("fair")
elif score in range(0, 40):
    print("poor")
else:
    print("invalid score")