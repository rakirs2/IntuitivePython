# 4-11 My Pizzas, Your Pizzas: Start with your program from 4-1, make a copy, then do the following:
friend_pizza = ['bacon','sausage','pepperoni']
pizza = ['bacon','sausage','pepperoni']
friend_pizza.append("vegitable")
pizza.append("beef")
print(friend_pizza)
print(pizza)
for gazelle in pizza[:]:
    print(f"My favorite pizzas are:{gazelle.title()}")
#Title case isn't working and I don't really know why lol
#skip