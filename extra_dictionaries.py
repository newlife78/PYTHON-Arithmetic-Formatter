# Example 1:
new_dict = dict()  # similar to ' new_dict = {} '
print(new_dict)

new_dict = {
    "name": "Paul",
    "age": 40
}
print(new_dict)

new_dict["children"] = ["Paul", "Betty"]
print(new_dict)

new_dict["Fun"] = {
    "Fun 1": 10,
    "Fun 2": 15
}
print(f'{new_dict}\n')


# Example 2:
my_dict = {"Name": [], "Address": [], "Age": []}
print(my_dict)

my_dict["Name"].append("Paul")
my_dict["Address"].append("Portugal")
my_dict["Age"].append(40)
print(my_dict)
