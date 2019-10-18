while True:
 name = input("enter username:\n")
 if name == "":
  continue
 amount = int(input("enter the price you wish to pay:\n"))
 if amount >= 10 and amount <= 15:
     print("we have itel and tecno")
 else:
     print("no phone for that price now,please try again")
 break 
print("welcome " + name + "thank you for checking inn")

  
 
