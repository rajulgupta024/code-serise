d1 = {}
print(type(d1))
d2 = {"Harry" : "Burger",
        "Rohan":"Fish", 
        "Skillf":"Roti", 
        "Shubham":{"B":"maggie", "L":"roti","D":"Chicken"}}
d2["Ankit"] = "Junk Food"
d2[420] = "Kabab"
print(d2)

# Deleting a element from the dictonary
del d2[420]
print(d2)
print(d2["Shubham"]["B"])

# Copy the dict
d3 = d2.copy()
print(d3)

# To find value of a key
print(d2.get("Harry"))

# To update the value
d2.update({"Leena" : "Icecream"})
print(d2)

# To print keys
print(d2.keys())

# To print dict all items
print(d2.items())