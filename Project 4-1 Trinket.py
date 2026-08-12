p=input("make a password ")
#check numbers
num=False
while True:
  
  for letter in p:
    print(letter)
    if letter in['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] :
      num=True
  #check letters  
  let=False
  if len(p)>=8:
    let=True
  #access checking
  
  if num==True and let==True: 
    print("access granted")
    break
  else:
    p=input("please try again not enough/none of the required character" )
      
      
#This is for checking the password------------------------>  
turtle=input("reenter")  
for i in range(5):
  if turtle==p:
    print("correct")
    break
  else:
    if i!=4:
      turtle=input("try again")
      
    else:
       print("your are locked out forever") 
