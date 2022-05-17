grocery = ["Harpic", "vim bar", "deo", "Bhindi","lollypop", 56]
print(grocery)
numbers = [2, 7, 9, 11, 3]
print(numbers)
print(len(numbers))
print(max(numbers))
print(min(numbers))
# Append
numbers.append(5)
print(numbers)
# Indexing
print("index value",numbers[2])
# Slicing
print("Sliced List with default value",numbers[:])
# Extended slic
print("Extended slic",numbers[::2])
print("revesef slic",numbers[::-1])
numbers.sort()
print("Sorted list",numbers)
numbers.reverse()
print("Revesed List",numbers)