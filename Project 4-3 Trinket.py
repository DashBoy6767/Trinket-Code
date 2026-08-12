hippo=0
high=float('-inf')
low=float('inf')
for i in range(5):
  turtle=int(input("give me you score from 1 through 100 "))
  
  if turtle>=90 and turtle<=100:
    print("you got a gold medal")
  elif turtle>=80 and turtle<=89:
    print("you got a silver medal")
  elif turtle>=70 and turtle<=79:
    print("you got a bronze medal")
  elif turtle>=60 and turtle<=69:
    print("you got a small trophy ") 
  elif turtle>=50 and turtle<=59:
    print("you got a runnerup medal") 
  elif turtle>=40 and turtle<=49:
    print("you got a runnerup medal") 
  elif turtle>=30 and turtle<=39:
    print("you got a runnerup medal")  
  elif turtle>=20 and turtle<=29:
    print("you got a runnerup medal") 
  elif turtle>=10 and turtle<=19:
    print("you got a runnerup medal")
  elif turtle>=1 and turtle<=9:
    print("you are dumb ")
  if turtle>high:
    high=turtle
    
  if turtle<low:
    low=turtle
    
  hippo+=turtle
hippo=hippo/5  
print(high)  
print(hippo)
print(low)
