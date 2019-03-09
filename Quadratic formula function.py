import math

def discriminant(a,b,c):
  discrim = (b**2 - 4*a*c)
  return discrim
  
def quadFormula(a,b,c):
  discriminant(a,b,c)
  if a == 0 and b !=0: 
    x = -c/b
    return -1, x, x
  elif discriminant(a,b,c) >= 0 and a != 0:
    root_1 = (-1*b + math.sqrt(discriminant(a,b,c))) / (2*a) 
    root_2 = (-1*b - math.sqrt(discriminant(a,b,c))) / (2*a)
    if root_1 == root_2:
      return 1 , root_1 , root_2
    elif root_1 != root_2:
      return 2 , root_1 , root_2
  elif discriminant(a,b,c) < 0:
    return 0, 0, 0
  elif a == 0 and b == 0 and c != 0:
    return -2, 0, 0
  else:
    return -3, 0 , 0
  
  
water = float(input("a value"))
ribs = float(input("b value"))
steak = float(input("c value"))

roots, ans , answer = quadFormula(water,ribs,steak)
print("x =",ans,"and x =",answer,". There are",roots,"roots")