while True:
    card_number = int(input("enter your card pin:\n"))
    if card_number != 1234560:
     print (str(card_number) + " is invalid pin")
     continue
    else:
     break
print ("congratulatio you have successfull recharge $100")     
