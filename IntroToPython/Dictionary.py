# So this will be a dictionary where there will be 2 values. one value will be the key and the other will be its value.
# To support our stance here we have key that is Jan and the value is January

# to store multiple values in a singe variabel we will be using lists

Month_conversion = {
    "Jan": "January",
    "Feb": "Februray",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
     6: "July",
    7: "August",

}

print(Month_conversion["Jan"])
print(Month_conversion.get("Feb"))
print(Month_conversion.get(7))


# lets say you enetred a key, but it was not in teh list, you can output a default value such as:
print(Month_conversion.get("Luv", "Not a valid key"))
