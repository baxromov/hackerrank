class Car:
    def __init__(self, max_speed, speed_unit):
        self.max_speed = max_speed
        self.speed_unit = speed_unit


class Boat:
    def __init__(self, max_speed):
        self.max_speed = max_speed


q = int(input("CMD:"))
queries = []
for _ in range(q):
    args = input("Arguments: ").split()
    vehicle_type, params = args[0], args[1:]
    if vehicle_type == "car":
        max_speed, speed_unit = int(params[0]), params[1]
        vehicle = Car(max_speed, speed_unit)
        print("Car with the maximum speed of", vehicle.max_speed, vehicle.speed_unit)
    elif vehicle_type == "boat":
        max_speed = int(params[0])
        vehicle = Boat(max_speed)
        print("Boat with the maximum speed of", vehicle.max_speed, "knots")
    else:
        raise ValueError("invalid vehicle type")

