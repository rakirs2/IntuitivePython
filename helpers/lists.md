# Python List functions

## Adding to a list

```python3
listA = []
listA.append("an element)
print(listA)
```
## Accessing a list by index
```python3
listA = ["one", "two", "three"]
print(listA[0], listA[1], listA[-1])
```
one two three

## Item is in a list
```python3
listA = ["one", "two", "three"]
print("one" in listA)
```
True


## Remove from list by value
```python3
listA = ["one", "two", "three"]
listA.remove("two")
print(listA)
```
one, three