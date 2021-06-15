import random
num1 = random.randint(0, 10)
num2 = random.randint(0, 10)
print("First Number: " + str(num1))
print("Second Number: " + str(num2))


print("\nOperations")
print("A.Additon")
print("B.Subtraction")
print("C.Multiplication")
print("D.Division")
op = input("\nPlease choose an operation: ")

if op == 'A' or op == 'a':
    add = num1 + num2
    total = int(input("What is the sum?"))
    if total == add:
        print("Correct")
    else:
        print("Wrong! The correct answer is:" + str(add))
elif op == 'B' or op == 'b':
    diff = num1 - num2
    total = int(input("What is the difference?"))
    if total == diff:
        print("Correct")
    else:
        print("Wrong! The correct answer is:" + str(diff))
elif op == 'C' or op == 'c':
    prd = num1 * num2
    total = int(input("What is the product?"))
    if total == prd:
        print("Correct")
    else:
        print("Wrong! The correct answer is:" + str(prd))
elif op == 'D' or op == 'd':
    qnt = num1 / num2
    total = int(input("What is the quotient?"))
    if total == qnt:
        print("Correct")
    else:
        print("Wrong! The correct answer is:" + str(qnt))
else:
    print("Invalid Operation!")