oldprice = 3.00
newprice = 2.00
old_video = float(input("please enter the quantiy of old videos you want:\n"))
new_video = float(input("enter new videos you want:\n"))
total = oldprice * old_video
new = newprice * new_video
totalbalace = total + new
print ("total money to pay for old video is " + "$" + str(total))
print ("total for new is " + "$" + str(new))
print ("total price for old and new is " + str(totalbalace))
