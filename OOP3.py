from loguru import logger
class Vechicle:
    def __init__(self, name, max_speed, mileage, color="White"):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.vech_colour=color
    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"
class Bus(Vechicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    pass
class Car(Vechicle):
    pass
if __name__ == '__main__':
    schoolbus = Bus('SchoolVolvo', 180, 12)
    print("Colour:", schoolbus.vech_colour, "Name:", schoolbus.name, "MAXSPEED:", schoolbus.max_speed, "AGE:", schoolbus.mileage)
    #logger.debug(schoolbus.seating_capacity())
    #logger.debug(schoolbus.vech_colour)
    my_car = Car("Audi RS3", 240, 5)
    logger.debug("Colour:", my_car.vech_colour, "Name:", my_car.name, "MAXSPEED:", my_car.max_speed, "AGE:", my_car.mileage)
