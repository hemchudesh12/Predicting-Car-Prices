import pandas as pd
import numpy as np

# Define the features and their corresponding coefficients
features = {'mileage': 500, 'brand': 1000, 'model_year': 120, 'engine_size': 100, 'transmission': 200, 'condition': 300, 'color': 400, 'interior': 500, 'exterior': 600, 'fuel_type': 700, 'drive_type': 800, 'num_doors': 900, 'num_seats': 1000, 'weight': 1100, 'length': 1200, 'width': 1300}

# Define the minimum and maximum values for each feature
min_values = {'mileage': 0, 'brand': 1, 'model_year': 1900, 'engine_size': 0, 'transmission': 0, 'condition': 1, 'color': 1, 'interior': 1, 'exterior': 1, 'fuel_type': 1, 'drive_type': 1, 'num_doors': 2, 'num_seats': 2, 'weight': 0, 'length': 0, 'width': 0}

max_values = {'mileage': 200000, 'brand': 100, 'model_year': 2022, 'engine_size': 10000, 'transmission': 10, 'condition': 5, 'color': 5, 'interior': 5, 'exterior': 5, 'fuel_type': 5, 'drive_type': 5, 'num_doors': 5, 'num_seats': 7, 'weight': 5000, 'length': 5000, 'width': 2000}

# Define the list of brands and their corresponding indices
brands = ['Toyota', 'Honda', 'Ford', 'Nissan', 'Chevrolet', "Hyundai", "Kia", "Volkswagen", "Audi", "BMW", "Mercedes-Benz", "Tesla", "Porsche", "Subaru", "Mazda"]
brand_indices = {'Toyota': 1, 'Honda': 2, 'Ford': 3, 'Nissan': 4, 'Chevrolet':5,"Hyundai":6,"Kia":7,"Volkswagen":8,"Audi":9,"BMW":10,"Mercedes-Benz":11,"Tesla":12,"Porsche":13,"Subaru":14,"Mazda":15}

# Define the list of model years
model_years = pd.Series([1900,1910,1920,1930,1940,1950,1960,1970,1980,1990,2000,2010,2022])

# Define the list of transmission types
transmissions = pd.Series(['Automatic', 'Manual', "CVT"])

# Define the list of fuel types
fuel_types = pd.Series(['Gasoline', "Diesel", "Hybrid"])

# Define the list of drive types
drive_types = pd.Series(['Front-wheel drive', "Rear-wheel drive", "All-wheel drive"])

# Define the list of interior conditions
interior_conditions = pd.Series(['Excellent', "Good", "Fair", "Poor"])

# Define the list of exterior conditions
exterior_conditions = pd.Series(['Excellent', "Good", "Fair", "Poor"])

# Ask the user for input
print("Enter the car's features:")
while True:
	try:
		print("Choose the mileage (in thousands):")
		for i in range(21):
			print(f"{i+1}. {i*10000}")
		mileage_index = int(input("Enter the number of the mileage: "))
		mileage = (mileage_index - 1) * 10000
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the brand:")
		for i in range(len(brands)):
			print(f"{i+1}. {brands[i]}")
		brand_index = int(input("Enter the number of the brand: "))
		brand = list(brand_indices.keys())[brand_index - 1]
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")
while True:
	try:
		print("Choose the model year:")
		for i in range(len(model_years)):
			print(f"{i+1}. {model_years.iloc[i]}")
		model_year_index = int(input("Enter the number of the model year: "))
		model_year = model_years.iloc[model_year_index - 1]
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the transmission:")
		for i in range(len(transmissions)):
			print(f"{i+1}. {transmissions.iloc[i]}")
		transmission_index = int(input("Enter the number of the transmission: "))
		transmission = transmissions.iloc[transmission_index - 1]
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the fuel type:")
		for i in range(len(fuel_types)):
			print(f"{i+1}. {fuel_types.iloc[i]}")
		fuel_type_index = int(input("Enter the number of the fuel type: "))
		fuel_type = fuel_types.iloc[fuel_type_index - 1]
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the drive type:")
		for i in range(len(drive_types)):
			print(f"{i+1}. {drive_types.iloc[i]}")
		drive_type_index = int(input("Enter the number of the drive type: "))
		drive_type = drive_types.iloc[drive_type_index - 1]
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the interior condition:")
		for i in range(len(interior_conditions)):
			print(f"{i+1}. {interior_conditions.iloc[i]}")
		interior_condition_index = int(input("Enter the number of the interior condition: "))
		interior_condition = interior_conditions.iloc[interior_condition_index - 1]
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the exterior condition:")
		for i in range(len(exterior_conditions)):
			print(f"{i+1}. {exterior_conditions.iloc[i]}")
		exterior_condition_index = int(input("Enter the number of the exterior condition: "))
		exterior_condition = exterior_conditions.iloc[exterior_condition_index - 1]
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the engine size :")
		engine_size_index = int(input("Enter the engine size (50 - 100l): "))
		engine_size = engine_size_index+49
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the num doors:")
		num_doors_index = int(input("Enter the number of doors (2-5): "))
		num_doors = num_doors_index
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the num seats:")
		num_seats_index = int(input("Enter the number of seats (4-9): "))
		num_seats = num_seats_index
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the weight (in pounds):")
		weight_index = int(input("Enter the weight (in 1000 to 5000 pounds): "))
		weight = weight_index
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the length (in feet):")
		length_index = int(input("Enter the length (5 - 12 feet): "))
		length = length_index
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

while True:
	try:
		print("Choose the width (in feet):")
		width_index = int(input("Enter the width (8 - 17 feet): "))
		width = width_index
		break
	except ValueError:
		print("Invalid input. Please enter a valid number.")

# Calculate price based on user's input
price = sum([features[key] * (value - min_values[key]) / (max_values[key] - min_values[key]) for key,value in zip(features.keys(), [mileage , brand_indices[brand], model_year])])*85

print("Predicted car price: ${:.2f}".format(price))