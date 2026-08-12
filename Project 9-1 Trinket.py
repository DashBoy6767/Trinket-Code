import random
playerHealth=100
robotHealth=100
defenseWeapons=["Captain America Shield", "Pillow", "Bullet Proof Vest"]
smallWeapons=["Butter Knife", "Gold Dagger", "Very Curvy Knife"]
offenseWeapons=["Modern Sword", "Medievil Sword", "Spear"]
#1a
NameChoose=input("You wake up and don't remember anything, but all you do remember is your name. But the machine is buffering and it can't decide on which name you have. Is it this or that. Type in your name to continue on")
#1b
print("After you walk around for a bit, you come to a fork in the hallway. What do you want to do, left or right. Your mind for some reason tells you to go to the right even though you wanted to think it out")
#2a
print("Once you get to an armory and see a robot for some reason. You see all the weapons and realize that the robot is running to go get a weapon. Out of instict you try to get a weapon to fight and see all sorts of weapons, a modern looking sword with light making it look a lightsaber, a medievil sword that looks like it's about to break, a spear with a sharp a large arrowhead shape, a butter knife that definetly didn't belong there, a golden dagger that looks like it's calling for you, and a very curvy knife that looks more curvy than a boomerang ")
#3a
print("Then you look to the left and see a different category that has rows and coloumns full of defense materials like a captain america shield that is literaly real, a shield potion that came directly out of a Fortnite game x2, a pillow for no reason, and a bullet proof vest")
#4a
swordPicker=random.choice(offenseWeapons)
offenseWeapons.remove(swordPicker)
print("The robot chose the "+swordPicker+". What do you want to pick if the "+swordPicker+" is unavailable choose from.")
offense=input(offenseWeapons)
while offense not in offenseWeapons:
  offense=input("Please try again object is not available please check you spelling or choice or capitalization.")
  
shieldPicker=random.choice(defenseWeapons)
defenseWeapons.remove(shieldPicker)
print("The robot chose the "+shieldPicker+". What do you want to pick if the "+shieldPicker+" is unavailable choose from.")
defense=input(defenseWeapons)
while defense not in defenseWeapons:
  defense=input("Please try again object is not available please check you spelling or choice or capitalization.")
    
knifePicker=random.choice(smallWeapons)
smallWeapons.remove(knifePicker)
print("The robot chose the "+knifePicker+". What do you want to pick if the "+knifePicker+" is unavailable choose from.")
knife=input(smallWeapons)
while knife not in smallWeapons:
  knife=input("Please try again object is not available please check you spelling or choice or capitalization.")

while True:
  if robotHealth<=0:
    print(NameChoose+" wins!!!!")
    print(NameChoose+" says that your a lllllllllloooooooosssssssssseeeeeeerrrrrrrrrrr")
    break
  elif playerHealth<=0:
    print("robot wins :(")
    print("robot says that your a lllllllllloooooooosssssssssseeeeeeerrrrrrrrrrr")
    break
    #The bots variable is three variables: swordPicker, shieldPicker, knifePicker
    #The players variable is three variables: offense, defense, knife
    #Choosing the weapons or health or run
  playerChoose=input("What do you want to use, you can use either running away(\"run\"), or using health(\"health\"), "+offense+", "+defense+", or "+knife+".")
  botChoices=[swordPicker, knifePicker, shieldPicker, "run", "health recharge"]  
  botChoose=random.choice(botChoices)
  
  
  
  if playerChoose==offense:
    print("\nthe bot chose "+ botChoose)
    
    if botChoose==swordPicker:
      print("The swords canceled out and nothing happened.")  
    
    if botChoose==knifePicker:
      chance50_50=random.randint(1, 2) 
      if chance50_50==1:
        playerHealth-=10
        print("Womp womp you got hit by the knife.")
      else:
        print("Nothing happens because you blocked the knife")
    
    if botChoose==shieldPicker:
      print("Sparks flew out and hit you.")
      playerHealth-=5
    
    if botChoose=="health":
      robotHealth-=5
      print("While it was healing you chopped its arm off so it lost 5 health")
    
    if botChoose=="run":
      print("Nothing happens the bot ran away")
    
  
  
  
  
  if playerChoose==knife:
    print("\nthe bot chose "+ botChoose)
    
    if botChoose==swordPicker:
      chance50_50=random.randint(1, 2) 
      if chance50_50==2:
        robotHealth-=10
        print("the robot got hit by the knife.")
      else:
        print("Nothing happens because because the robot blocked the knife")
    
    if botChoose==knifePicker:
      playerHealth-=5
      robotHealth-=5
      print("both of you got hurt")
    
    if botChoose==shieldPicker:
      robotHealth-=5
      print("the knife actually hit the leg")
    
    if botChoose=="health":
      print("the knife takes less health that the replenish gives")
      robotHealth+=15
    
    if botChoose=="run":
      print("robot got hit in the back")
      robotHealth-=5
  
  
  
  if playerChoose==defense:
    print("\nthe bot chose "+ botChoose)
    
    if botChoose==swordPicker:
      print("sparks fly out and hit the swords person")
      robotHealth-=5
    
    if botChoose==knife:
      print("oh no you got hit in the leg")
      playerHealth-=5
    
    if botChoose==shieldPicker:
      print("nothing happens")
      
    if botChoose=="health":
      print("you let him get health!!!! bad boy")
      robotHealth+=20
      
    if botChoose=="run":
      print("nothing happens")
      
      
      
  if playerChoose=="health": 
    print("\nthe bot chose "+ botChoose)
    
    if botChoose==swordPicker:
      print("the sword sadly does more health than the replenish gives")
      playerHealth-=10
      
    if botChoose==knifePicker:
      print("the bot tried to hurt you but couldn't")
      playerHealth+=15
      
    if botChoose==shieldPicker:
      print("Nothing happens after you gain health")
      playerHealth+=20
      
    if botChoose=="health":
      print("at least you got health yourself")
    
    if botChoose=="run":
      print("nothing happens except gaining health")
      playerHealth+=20
      
      
  if playerChoose=="run":
    print("\nthe bot chose "+ botChoose)
    
    if botChoose==swordPicker:
      print("nothing happens ")
      
    if botChoose==knifePicker:
      print("you got hit in the back")
      playerHealth-=5  
      
    if botChoose==shieldPicker:
      print("nothing happens")
      
    if botChoose=="health":
      print("the robot got the health")
      robotHealth+=20
      
    if botChoose=="run":
      print("bruh")
      
      
      
    
