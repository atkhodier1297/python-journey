# Dictionaries in PY are used for key value pairs.
# Every key must be unique.
# Keys must be spelled CORRECT

customer = {
    "name": "John",
    "age": 30,
    "is_verified": True
}
customer["name"] = "Jack"
# Changes key

customer["birthdate"] = "Feb 12 1997"
# Adds a key to customer

print(customer["age"])
print(customer)