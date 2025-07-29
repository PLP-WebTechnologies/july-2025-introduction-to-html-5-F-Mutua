num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter your second number: "))
operator = input("Enter the arithmetic operator +, -, /, *: ")

if operator == "+":
    sum= num_1 + num_2
    print(f"{num_1} + {num_2} = {sum}")
elif operator == "-":
    sub= num_1 - num_2
    print(f"{num_1} - {num_2} = {sub}")
elif operator == "*":
    mul= num_1 * num_2
    print(f"{num_1} * {num_2} = {mul}")
elif operator == "/":
    if num_2 != 0:
        div= num_1 / num_2
        print(f"{num_1} / {num_2} = {div}")
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid operator.")








