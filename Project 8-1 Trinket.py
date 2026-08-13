#INTRO

print("Welcome to CAMP WHISPERING PINES where whispers are your friends  P.S They are not your friends")

#MESSAGES

darkForest="You get lost and end up in the dark forest. You step in a hole and feel something on your legs. You look down and seee a slimmy creature crawling up. WHAT DO YOU DO!!! Option 1: Run or Option 2: Inspect it (Say 1 or 2)"
theEnd1="You choose to run, so it keeps on sucking your blood until you die. WHAT DO YOU DO!!! Option 1: Save and quit or Option 2: Start over (Say 1 or 2)"
weirdBuilding="You inspect it, and it looks at your superior eyes. You stare back at it and it RUNS AWAY. You shiver and start walking. Then a desolate building appears. WHAT DO YOU DO!!!. Option 1: Look at the sign or Option 2: Be bold and walk in (Say 1 or 2)"
theEnd2="You look at the sign, and it says \"No Vacancy for the Living\". WHAT DO YOU DO!!! Option 1: Save and quit or Option 2: Start over (Say 1 or 2)"
goBigOrGoHome="After making it this far, your bravery is already almost up and then you walk in. You find a polaroid camera on a crate. When you click the shutter to see if it works, the developed photo shows you standing exactly where you are—but there is a tall, thin figure standing directly behind you in the frame. WHAT DO YOU DO!!! Option 1: Snap another picture to see if the figure moved, or Option 2: Sprint for the iron door and hope it isn't locked ( Say 1 or 2)"
theEnd3="You make a run for it... and the handle FALLS OFF of the door!!! Because of the sudden weight loss. the floorboards creak and squeak AND FALL!!!WHAT DO YOU DO!!! Option 1: Save and quit or Option 2: Start over (Say 1 or 2)"
testCamera="You snap another picture to see if the figure moved. But the new picture shows a dimmed picture. Then you realize that it's the monster that is covering the entire picture.WHAT DO YOU DO!!! Option 1: You don't move your head and use the camera as your eyes or Option 2: You try to run deeper in to the building (Say 1 or 2)"
theEnd4="You run depper into the building and suddenly stopping and realizing that only one person wheres a shrek costume. That is your best friend, but it is too late as your friend slams into you. You wake up and realize you were in your bed the whole time!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
glasses="Using the camera as your glasses, you can see the different parts of the monster. You realize it looks a lot like shrek. WHAT DO YOU DO!!! Option 1: You give it a uppercut to see what happens or Option 2: You think this is all not scary at all and decide to walk through it (Say 1 or 2 )"
theEnd5="When you give it an uppercut, you realize it's your friend and he punches you back. Then you end up getting unconscience and find yourself awake in your house. You realize you were in your bed the whole time!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
theEnd6="When you run into it, you realize it's your friend and he laughs so hard his eyes fall out. Then you end up laughing to. You realize you were in your bed the whole time!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

#OPTIONS


index={"dark forest":[darkForest, "THE END 1", "WEIRD BUILDING"], "WEIRD BUILDING":[weirdBuilding, "THE END 2", "BACK OF BUILDING"], "BACK OF BUILDING":[goBigOrGoHome, "TEST CAMERA", "THE END 3"], "TEST CAMERA":[testCamera, "glasses", "THE END 4"], "glasses":[glasses, "THE END 5", "THE END 6"], "THE END 5":[theEnd5,"finale", "finally"], "THE END 6":[theEnd6, "finale", "finally"], "THE END 4":[theEnd4, "finale", "finally"], "THE END 3":[theEnd3, "finale", "finally"], "THE END 2":[theEnd2, "finale", "finally"], "THE END 1":[theEnd1, "finale", "finally"] }


#CODE
location="dark forest"

while True:
  usersChoice=input(index[location][0])
  location=index[location][int(usersChoice)]

  if (index[location][1])=="finale":
    print(index[location][0]) 
    break
