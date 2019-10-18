
grade = float(input("enter your score "))
if grade > 0 and grade < 0.6:
    print("F")
elif grade >= 0.6 and grade < 0.7:
    print("D")
elif grade >= 0.7 and grade < 0.8:
    print("C")
elif grade >= 0.8 and grade < 0.9:
    print("B")
elif grade >= 0.9 and grade <= 1.0:
    print("A")
else:
    print("your score is out of range")
          
         
#>= 0.9     A
#>= 0.8     B
#>= 0.7     C
#>= 0.6     D
#<0.6 F
