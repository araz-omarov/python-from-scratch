person = {
    "Name": "Araz",
    "Age": 14,
    "City": "Baku"
}

print(person["Name"])   # Araz
print(person["Age"])  # 14

person["Age"] = 14
print(person)  # {'Name': 'Araz', 'Age': 14, 'City': 'Baku'}

person["profession"] = "Student"
print(person)  # {'ad': 'Araz', 'yaş': 21, 'şehir': 'Lənkəran', 'profession': 'Student'}

del person["City"]
print(person)  # {'Name': 'Araz', 'Age': 14, 'profession': 'Student'}

print(person.keys())   # dict_keys(['Name', 'Age', 'profession'])
print(person.values()) # dict_values(['Araz', 14, 'Student'])
print(person.items())  # dict_items([('Name', 'Araz'), ('Age', 14), ('profession', 'Student')]) 