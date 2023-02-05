#the problem is creating a list open the list close the list and then reopen it then close it and print it.
import pickle
favorites = ['football', 'wrestling', 'weightlifting', 'coding']
f = open('favorites.dat', 'wb')
pickle.dump(favorites, f)
f.close()
load_favorites= open('favorites.dat', 'rb')
loaded_favorites=pickle.load(load_favorites)
load_favorites.close()
print(loaded_favorites)
