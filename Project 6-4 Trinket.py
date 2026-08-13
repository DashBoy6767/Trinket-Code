pets={"brody":"67.6767676767676767", "somebody":"100", "something":"99.99999999999999999999"}
print(pets["brody"], pets["somebody"], pets["something"])
turtle=input("give me the name of your student")
hippo=input("give me the grade")
pets[turtle]=hippo
print(pets)

animal=input("what student do you want to change")
mammal=input("what is the grade")
pets[animal]=mammal
print(pets)
for i in pets:
  print(i)
