turtle=0
row=""
emoji=["😄", "🥸", "😎","🥶", "😈", "👺", "👾", "👾", "👾" , "👾", "👾"]
for i in range(7):
  turtle+=1
  for i in range(turtle):
    row+=emoji[i]+" "
  print(row)  
  row=""
