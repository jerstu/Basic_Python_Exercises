#  dictionary - key/value pairs
customer = {
    "name": "John Smith",
    "age":  30,
    "is_verified": True
}


print(customer["name"])                         # print value
customer["name"] = "Jack Smith"                 # assign value
print(customer.get("name"))                     # method to return value, returns none instead of error
print(customer.get("birthday", "Jan 1 1980"))   # method with default value instead of none
customer["birthday"] = "Aug 16 1982"            # assigns new key/value pair
print(customer["birthday"])                     # print new value
