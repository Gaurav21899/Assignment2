# Printing Country Names
countries_and_capitals = {"India": "Delhi", "USA": "Washington_DC", "China": "Beijing", "Russia": "Moscow"}
print("Countries_Name:")
for Countries in countries_and_capitals.keys():
    print(Countries)

# Inserting One Country and its Capital
new_country = "Canada"
new_capital = "Ottawa"

countries_and_capitals[new_country] = new_capital
print(countries_and_capitals)

# Print the length of the dictionary
print(len(countries_and_capitals))

# # Remove an element from the dictionary
countries_and_capitals.pop("China")
print(countries_and_capitals)
print("Process Completed")

