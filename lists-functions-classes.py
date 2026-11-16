class Vehicle:
  def __init__(self, vehicle_type):
    self.vehicle_type = vehicle_type

class Automobile(Vehicle):
  def __init__(self, year, make, model, doors, roof):
    super().__init__("car")
    self.year = year
    self.make = make
    self.model = model
    self.doors = doors
    self.roof = roof

year = input("Enter the year: ")
make = input("Enter the make: ")
model = input("Enter the model: ")

car = Automobile(year, make, model, doors, roof)

while True:
  roof = input("Enter the roof type (sun roof or solid): ").lower()
  if roof in ["solid", "sun roof"]:
    print("Please enter 'solid' or 'sun roof'.")

while True:
  doors = input("Enter the roof type (2 or 4): ")
  if doors in ["2", "4"]:
    print("Please enter '2' or '4'.")
