turtle=0
row=""
j=[str(1), str(2), str(3), str(4), str(5), str(6), str(7), str(8), str(9), str(10)]
for i in range(10):
  turtle+=1
  for i in range(turtle):
    row+=j[i]+" "
  print(row)
  row=""
