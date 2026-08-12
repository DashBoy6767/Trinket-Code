row=""
turtle=(int(input("Give me a number ")))

for j in range(1, turtle+1):
  

  for i in range(1, turtle+1):
    row+=(str(i*j))
    if i*j>=10 and i*j<=99:
      row+="   "
    elif i*j>=100 and i*j<=999:
      row+="  "
    elif i*j>=1000:
      row+=" "
    else:
      row+="    "
  print(row) 
  row=""
 
