Name = input("Name: ")
One = float(input("\n1st Quarter: "))
Two = float(input("2nd Quarter: "))
Three = float(input("3rd Quarter: "))
Four = float(input("4th Quarter: "))

total = One + Two + Three + Four
average = total/4
print("\nAverage: " + str(average))

if (average >= 98 and average <=100):
    print("Remarks: With Highest Honors")
elif average >= 95:
    print("Remarks: With High Honors")
elif average >= 90:
    print("Remarks: With Honors")
elif average >= 75:
    print("Remarks: Passed")
elif average >= 51:
    print("Remarks: Failed")
else:
    print("Error: Invalid Grade")