import random

right = 0
wrong = 0

def GenerateFirstNumbers():
    num1 = random.randint(0 , 10)
    return num1

def GenerateSecondNumbers():
    num2 = random.randint(0 , 10)
    return num2

while True:
    print("\nOperation")
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    operation = input("\nChoose an Operation:")

    num1 = GenerateFirstNumbers()
    num2 = GenerateSecondNumbers()
    print("First Number:\n" + str(num1))
    print("Second Number:\n" + str(num2))

    if operation == 'A' or operation == 'a':
        add = num1 + num2
        total = int(input("What is the sum?"))
        if total == add:
            print("Correct!")
        else:
            print("Wrong! The Correct Answer is" + str(add))
    elif operation == 'B' or operation == 'b':
        diff = num1 - num2
        total = int(input("What is the difference?"))
        if total == diff:
             print("Correct!")
        else:
             print("Wrong! The Correct Answer is" + str(diff))
    elif operation == 'C' or operation == 'c':
        prd = num1 * num2
        total = int(input("What is the product?"))
        if total == prd:
            print("Correct!")
        else:
            print("Wrong! The Correct Answer is" + str(prd))
    elif operation == 'D' or operation == 'd':
        quo = num1 / num2
        total = int(input("What is the quotient?"))
        if total == quo:
            print("Correct!")
        else:
            print("Wrong! The Correct Answer is" + str(quo))
    else:
        print("Invalid Operation!")
        break
    loss = input("Do you want to try another problem? (Yes/No?)")

    if loss in ["YES","Yes","yes","Y","y"]:
        pass
    elif loss in ["NO","No","no","N","n"]:
        print("Thank you for Playing Have a Great Day!")
        break
    else:
        break


