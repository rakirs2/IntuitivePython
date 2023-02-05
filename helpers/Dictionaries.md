# Dictionaries

Dictionaries are an python implementation on "HashMaps" We're not going to worry about what that means. When you understand those, I'll be coming to you for lessons :).

Fundamentally, you'll have a Key and a Value. These are traditionally noted as K,V in computer science.

They general notation in python is 
``` python
variable[key] = value
```
For now, let's just see what they can do.

## Definition
Dictionaries are defined as follows:
```Python3
dictionary = {}
```

this instantiets an empty dictionary.

If you remember the function type() in python you can see
```Python3
type(dictionary)
<class 'dict'>
```

## operations

### adding to a dictionary
```Python3
dictionary[1] = "one"
```

the state of this dictionary will now be
```Python3
dictionary
{1: "one"}
```

## Changing values in a dictionary
```Python3
numbers = {1: "one"}
numbers[1] = "uno"
```
###  is the value of numbers?
The dictionary only stores the last input

### deleting from a dictionary
Uh oh, we made a mistake. Lets fix it by removing the second value
```Python3
numbers = {1: "one", 2:"three"}
del(numbers[2])
# numbers = {1: "one"}
```

### Is a key in a dictionary?
```Python3
numbers = {1: "one", 2:"three"}
1 in numbers
# true
3 in numbers 
# false
1 in numbers.keys
# true
1 in numbers.values
# false
"one" in numbers.values
# true
```
