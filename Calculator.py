x = float(raw_input("Enter the value for x: "))
print(x)

y = float(raw_input("Enter the value for y: "))
print(y)

operation = (raw_input("Choose math operation (+, -, *, /: "))
print operation

if operation == "+":
    print(x + y)
elif operation == "-":
    print(x - y)
elif operation == "*":
    print(x * y)
elif operation == "/":
    print(x / y)

else:
    print "You are an IDIOT"

print("Do you want another calculation?")