# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE

# x.insert(3, 4)

x.append(4)
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE

x.extend(y)
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE

# x.pop(4)
# x.remove(9)
del x[4]
print(x, 'Removed the 8')

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE

x.insert(5, 99)
print(x, 'insert 99')

# Print the length of list x
# YOUR CODE HERE

# Print all the values in x multiplied by 1000
# YOUR CODE HERE
