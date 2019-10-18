total = 0
counter = 0
while True:
    entry = input("enter number:\n")
    if entry == "":
        break
    number = float(entry)
    total += number
    counter += 1
    average = total/counter
print (total)    
print ("your average is " , str(average))    
