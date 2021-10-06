a = float(input("ghadetono vard konid (mesle 185):  "))
b = float(input("vazentono vard konid (bar hasb kg ): "))


def my_function(a,b):
   c = b / (a/100)**2
   if ( c < 18.5):
        print(" be shdeat laghar")
   elif ( c >= 18.5 and c <=24.9):
        print(" mamoli")
   elif ( c >= 25 and c <=29.9):
        print(" ezafe vazn dari")
   elif ( c >= 30 and c <=35 ):
        print("kheili ezafe vazn dari")
   else:
        print("kheili kheili kheili ezafe vazn dari")
    
my_function(a,b)