import json

information = {
    "name": "Araz",
    "age": 14,
    "city": "Baku"
}

with open("info.json", "w") as file:
    json.dump(information, file)               # json.dumb(information, file) --->  JSON yaz

print("Məlumat fayla yazıldı!")

with open("info.json", "r") as file:
    loaded_info = json.load(file)              # loaded_info = json.load(file) ---> Python üçün dict formatına çevirir

print("Fayldan oxunan məlumat:", loaded_info)  # loaded_info ---> 