v = float(input("Enter Voltage (V): "))
r = float(input("Enter Resistance (R): "))
i = v / r
print(f"Current: {i} A")
if i < 0.5:
    print("Nature: Low current")
elif i >= 0.5 and i <= 2:
    print("Nature: Normal current")
else:
    print("Nature: High current")