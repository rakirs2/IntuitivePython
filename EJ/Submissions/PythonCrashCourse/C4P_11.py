#4-11 My Pizzas, Your Pizzas: Start with your program from 4-1, make a copy, then do the following:
friend_pizza = ['bacon','sausage','pepperoni']
pizza = ['bacon','sausage','pepperoni']
friend_pizza.append("vegitable")
pizza.append("beef")
print(friend_pizza)
print(pizza)
print("My favorite pizzas are:")
for pizzas in pizza[:3]:
    print(f"My favorite pizzas are:{pizzas.title()}")
for friends in pizza[:3]:
    print(f"My friend's favorite pizzas are:{friends.title()}")
