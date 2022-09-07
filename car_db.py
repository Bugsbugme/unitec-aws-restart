# Get car details from user
# Create instance of a car with details
# Add the car instance to a database

# Initialise database
car_db = []
car_id = 0

# Loop this
while True:
    # If the database already has cars in it, print it out
    if car_db:
        print("Cars in Database:")
        for car in car_db:
            print(
                f"Car_{car['id']}:\n Make: {car['make']}\n Model: {car['model']}\n Colour: {car['colour']}\n"
            )
    car_id = car_id + 1
    # USER INPUT
    # 1 Ask for car make
    car_make = input("Enter the car make: ")
    # 2 Ask for car model
    car_model = input("Enter the car model: ")
    # 3 Ask for car colour
    car_colour = input("Enter the car colour: ")

    car = {"id": car_id, "make": car_make, "model": car_model, "colour": car_colour}

    # Print out the details of the new car
    print(
        f"\nAdding the following car to the database:\n Make: {car['make']}\n Model: {car['model']}\n Colour: {car['colour']}\n"
    )

    # Add the new car to the database
    car_db.append(car)
