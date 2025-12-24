class Vehicle:
    
    def __init__(self, vehicle_id, model, battery_percentage):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = None

        self.__rental_price = None
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


