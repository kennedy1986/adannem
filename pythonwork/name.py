while 1:
    try:
       print ("welcome guest ")
       name = input("please enter your name: \n")
       print ("welcome" , name)
    except valueError:
        print ("enter only alphabet please")
    except Exception:
        print ("only name is need")
    else:
        break
print ("you are welcomes back" , name)
  

    
  


