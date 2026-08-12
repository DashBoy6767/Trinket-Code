turtle=0
row=""
j=["😄", "🥸", "😎","🥶", "😈", "👺", "👾" ]
for i in range(7):
  turtle+=1
  for i in range(turtle):
    row+=j[i]+" "
  print(row)  
  row=""
