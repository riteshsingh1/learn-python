# list syntax are same as array in php or javascript
# lists are mutable, and can contain mix data types
fruits = ["Apple", "Mango", "Blue Berry", 2, True]

print(fruits)

# for accessing specific element we can use index
# This will result in Blue Berry
print(fruits[2])

# Accessing last element
print(fruits[-1])

# Access last 2 elements
print(fruits[3:])

# Access 2nd element
print(fruits[1:2])

# Update List
fruits[1] = "Grape"

print(fruits)

