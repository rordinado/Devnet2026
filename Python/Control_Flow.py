

# cars = [
#     {"make": "Toyota", "model": "Corolla"},
#     {"make": "Honda", "model": "Civic"},
#     {"make": "Ford", "model": "Mustang"}
# ]

# if cars == []:
#     print("This list is empty:")
# else:
#     print("This list is not empty")
#     print(cars)


value = "red"

match value:
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case "yellow":
        print("Slow down")
    case _:
        print("Unknown")

car = {"make": "Toyota", "year": 2020}



