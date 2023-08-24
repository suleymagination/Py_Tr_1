users = {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
        "street": "Kulas Light",
        "suite": "Apt. 556",
        "city": "Gwenborough",
        "zipcode": "92998-3874",
        "geo": {
            "lat": "-37.3159",
            "lng": "81.1496"
        }
    }
}
print(f"users = {users}")
print(f"Data type users = {type(users)}")
print(users["id"])
print(users["name"])
print(users["username"])
print(users["email"])
print()
print(users["address"])
print(users["address"]["street"])
print(users["address"]["city"])
print(users["address"]["geo"]["lat"])

print("\nPrint to JSON format:")
import json
users_json = json.dumps(users)
print(f"users = {users_json}")
print(f"Data type users = {type(users_json)}")

print("\nPrint to JSON file:")
# Open a file for writing
with open("users_json.json", "w") as file:
    # Write the dictionary to the file
    json.dump(users_json, file)
