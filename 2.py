a = float(input("add aval ro vard konid: "))
b = float(input("add dovom ro vared konid: "))
c = float(input("add sevomo vard konid:"))

def my_function(a,b,c):
  if (a < b + c and b < a + c and c < a + b):
    print("mitavan mosalas sakht :)) !!")
  else :
    print("nmishe add ha eshtebas !!! ;((")
    
my_function(a,b,c)