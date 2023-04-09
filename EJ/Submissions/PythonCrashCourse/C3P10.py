#3-10 Every Function: Make a list, and use every function atleast once.
Rand_List = ['Swahili','Thai','Odessa','FreightLiner','Mt. Fuji','Hawaii','21039132193']
print(Rand_List)
print(Rand_List[0])
print(Rand_List[0].title())
print(Rand_List[-1])
message = "I typed a random number like" 
print(f"{message}{Rand_List[6]}.")
Rand_List[0] = 'Tartarus'
print(Rand_List)
Rand_List.append('Weightless(Arcane Remix)')
print(Rand_List)
Rand_List.insert(1, 'Social Media')
print(Rand_List)
del Rand_List[1]
a = Rand_List.pop(0)
print(a)
Rand_List.remove('Odessa')
print(Rand_List)
print(sorted(Rand_List))
print(sorted(Rand_List, reverse=True))
Rand_List.reverse()
print(Rand_List)
print(len(Rand_List))
