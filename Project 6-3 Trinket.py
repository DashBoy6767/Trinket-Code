dictionary={"dog":"perro", "table":"mesa", "clean":"limpia"}
print(dictionary["dog"], dictionary["table"], dictionary["clean"])
turtle=input("give me a word")
hippo=input("give me the spanish translation")
dictionary[turtle]=hippo
print(dictionary)

animal=input("what word do you want to change")
mammal=input("what is the translation ")
if animal in dictionary:
  print(dictionary)
  for i in dictionary:
    print(i)
else:
  print("not there")
  
