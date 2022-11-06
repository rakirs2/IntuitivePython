import pokebase

## https://pokebase.readthedocs.io/en/latest/

## pokemon by numbers from ranges;

## how to get certain ranges

## get certain types?


## what is wrong with this?
for i in range(4,7):
    print(i, pokebase.pokemon(i))


# ## how can we simplify it?
# gen_resource = pokebase.generation(1)

# print(gen_resource)
# for pokemon in gen_resource.pokemon_species:
#     print(pokemon)