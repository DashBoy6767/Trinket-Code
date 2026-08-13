pets={"brody":"123456 something dr", "somebody":"676767 nothing dr", "mataeo":"123654 maybe ave"}
print(pets["brody"], pets["somebody"], pets["mataeo"])
turtle=input("give me the name of your pet")
hippo=input("give me the address")
pets[turtle]=hippo
print(pets)

animal=input("what pet do you want to change")
mammal=input("what is the adress")
pets[animal]=mammal
print(pets)
for i in pets:
  print(i)
