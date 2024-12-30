def cal():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (Addition, Subtraction, Multiplication, Division): ")
 
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Math Error!!!!"
    else:
        result = "Invalid Operation"

    print("The result for your selected operation is: " + str(result))


cal()