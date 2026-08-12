import random, time
j= [ ("Alabama:", "Montgomery"),
    ("Alaska:", "Juneau"),
    ("Arizona:", "Phoenix"),
    ("Arkansas:", "Little Rock"),
    ("California:", "Sacramento"),
    ("Colorado:", "Denver"),
    ("Connecticut:", "Hartford"),
    ("Delaware:", "Dover"),
    ("Florida:", "Tallahassee"),
    ("Georgia:", "Atlanta"),
    ("Hawaii:", "Honolulu"),
    ("Idaho:", "Boise"),
    ("Illinois:", "Springfield"),
    ("Indiana:", "Indianapolis"),
    ("Iowa:", "Des Moines"),
    ("Kansas:", "Topeka"),
    ("Kentucky:", "Frankfort"),
    ("Louisiana:", "Baton Rouge"),
    ("Maine:", "Augusta"),
    ("Maryland:", "Annapolis"),
    ("Massachusetts:", "Boston"),
    ("Michigan:", "Lansing"),
    ("Minnesota:", "St. Paul"),
    ("Mississippi:", "Jackson"),
    ("Missouri:", "Jefferson City"),
    ("Montana:", "Helena"),
    ("Nebraska:", "Lincoln"),
    ("Nevada:", "Carson City"),
    ("New Hampshire:", "Concord"),
    ("New Jersey:", "Trenton"),
    ("New Mexico:", "Santa Fe"),
    ("New York:", "Albany"),
    ("North Carolina:", "Raleigh"),
    ("North Dakota:", "Bismarck"),
    ("Ohio:", "Columbus"),
    ("Oklahoma:", "Oklahoma City"),
    ("Oregon:", "Salem"),
    ("Pennsylvania:", "Harrisburg"),
    ("Rhode Island:", "Providence"),
    ("South Carolina:", "Columbia"),
    ("South Dakota:", "Pierre"),
    ("Tennessee:", "Nashville"),
    ("Texas:", "Austin"),
    ("Utah:", "Salt Lake City"),
    ("Vermont:", "Montpelier"),
    ("Virginia:", "Richmond"),
    ("Washington:", "Olympia"),
    ("West Virginia:", "Charleston"),
    ("Wisconsin:", "Madison"),
    ("Wyoming:", "Cheyenne")]
    

start=time.time()
while True:
  turtle=random.choice(j)
  hippo=input("what is the state capital for "+turtle[0])
  
  if hippo==turtle[1]:
    print("correct")
    j.remove(turtle)
    if  len(j)==0:
      print("You completed it")
      end=time.time()
      print(end-start)
      break
  else:
    print("incorrect, the answer is "+turtle[1])
    
