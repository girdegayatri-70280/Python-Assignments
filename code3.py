h = float(input("Enter Hardness: "))
c = float(input("Enter Carbon Content: "))
t = float(input("Enter Tensile Strength: "))
c1 = h > 50
c2 = c < 0.7
c3 = t > 5600
if c1 and c2 and c3:
    grade = 10
elif c1 and c2:
    grade = 9
elif c2 and c3:
    grade = 8
elif c1 and c3:
    grade = 7
elif c1 or c2 or c3:
    grade = 6
else:
    grade = 5

print("Grade:", grade)