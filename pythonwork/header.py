#varriables
old = 3.00
new = 2.00
# Accept input from users
quantity_old = int(input("please enter the number of old videos you want:\n"))
quantity_new = int(input("please enter the number of new videos you want:\n"))
# Display the invoice
print ("%4s%18s%10s%16s" % \
      ("OldVideos" , "OldVideosPrice" , "NewVideos" , "NewVideoPrice"))
  # Display price
print ("%4d%18.2f%10d$16.2f" % \
      (OldVideos, OldVideosPrice, NewVideos, NewVideoPrice))
quantity_old = OldVideos
OldVideosPrice = quantity_old * old                   
NewVideos = quantity_new
NewVideosPrice = quantity_new * new
