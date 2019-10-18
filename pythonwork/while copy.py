while True:
    try:
        i =int(input("enter number "))
        if i < 10:
         print("super")
        else:
         print("bad")
    except ValueError:
         print("you cant enter letter")
    except Exception:
         print("wrong input")     
