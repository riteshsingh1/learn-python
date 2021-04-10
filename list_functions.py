lucky_numbers = [4,8,12,16,256,64,48]
friends = ['Joe', 'Phibe', 'Sheldon', 'Howard']

print(friends)

# Append function adds element in the list

friends.append("Penny")

print(friends)

# Insert Function inserts element at a position

friends.insert(1, "Leanord")

print(friends)


# remove element
friends.remove("Phibe")

print(friends)


# pop
friends.pop(0)

print(friends)


# Search Element using indexof

print(friends.index("Sheldon"))


# Count specific element in list
print(friends.count("Penny"))

# Sort
friends.sort()
print(friends)

lucky_numbers.sort()

print(lucky_numbers)

#  Reverse List
lucky_numbers.reverse()

print(lucky_numbers)

# Copy List

friends2 = friends.copy()

print(friends2)

