from abc import ABC,abstractmethod
class Vehicle(ABC):
    
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = None

        self.__rental_price = 300
        self.__maintenance_status = None

        self.set_battery_percentage(battery_percentage)
        
    def set_rental_price(self, price):
        if price >= 0:
            self.__rental_price = price
        else:
            raise ValueError("Rental price cannot be negative")

    def set_maintenance_status(self, status):
        self.__maintenance_status = status

    def set_battery_percentage(self, battery):
        if 0 <= battery <= 100:
            self.battery_percentage = battery
        else:
            raise ValueError("Battery percentage must be between 0 and 100")

    def get_maintenance_status(self):
        return self.__maintenance_status
    
    def get_rental_price(self):
        return self.__rental_price



    def set_maintenance_status(self, status):
         allowed = ["Available", "On Trip", "Under Maintenance"]
         if status in allowed:
                 self.__maintenance_status = status
         else:
                raise ValueError("Invalid maintenance status")

    def set_battery_percentage(self, battery):
        if 0 <= battery <= 100:
            self.battery_percentage = battery
        else:
            raise ValueError("Battery percentage must be between 0 and 100")

    def get_maintenance_status(self):
        return self.__maintenance_status
    
    def get_rental_price(self):
        return self.__rental_price


    @abstractmethod
    def calculate_trip_cost(self,distance):
        pass

    def __eq__(self, value):
        if not isinstance(value,Vehicle):
            return False
        else:
            return self.vehicle_id==value.vehicle_id
        
    def __str__(self):
        return f"{self.vehicle_id} | {self.model}. | {self.battery_percentage} | {self.get_maintenance_status()}" 
class ElectricCar(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,seating_capacity):
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity=seating_capacity

    def calculate_trip_cost(self,distance):
        return 5+(.50*distance)


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, battery_percentage,max_speed_limit):
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit=max_speed_limit

    def calculate_trip_cost(self,distance):
       return 1+(.15*distance)