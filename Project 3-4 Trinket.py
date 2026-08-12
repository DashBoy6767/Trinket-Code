movies = [
    "Avatar: Fire and Ash",
    "The Shawshank Redemption",
    "The Godfather",
    "The Dark Knight",
    "Pulp Fiction",
    "Parasite",
    "Zootopia 2",
    "Spirited Away",
    "Everything Everywhere All at Once",
    "Interstellar"]
movies.sort()
print(movies)

while True:
  turtle=input("give me a movie to add(make sure it is capital)")
  turtle=turtle.capitalize()
  movies.append(turtle)
  movies.sort()
  

  for i in range(len(movies)):
    print(str(i + 1) + ". " + movies[i])
