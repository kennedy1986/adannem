theSum = 0.0
data = input("Enter a number or just enter to quit:\n ")
while data != "":
    number = float(data)
    theSum += number
    data = input("enter number:\n")
print("The sum is", theSum)
