from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Abstract base class representing a generic electric vehicle.

    This class defines common attributes and behaviors for all vehicles
    in the Eco-Ride Urban Mobility System.
    """

    def __init__(self, vehicle_id, model, battery_percentage):
        """
        Initializes a Vehicle object.

        Parameters
        ----------
        vehicle_id : str
            Unique identifier for the vehicle

        model : str
            Model name of the vehicle

        battery_percentage : int
            Battery charge percentage (0–100)
        """
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery_percentage = None

        self.__rental_price = 300
        self.__maintenance_status = "Available"

        self.set_battery_percentage(battery_percentage)

    def set_rental_price(self, price):
        """
        Sets the rental price for the vehicle.

        Parameters
        ----------
        price : float
            Rental price value

        Raises
        ------
        ValueError
            If rental price is negative
        """
        if price >= 0:
            self.__rental_price = price
        else:
            raise ValueError("Rental price cannot be negative")

    

    def set_battery_percentage(self, battery):
        """
        Sets the battery percentage of the vehicle.

        Parameters
        ----------
        battery : int
            Battery percentage value

        Raises
        ------
        ValueError
            If battery percentage is out of range
        """
        if 0 <= battery <= 100:
            self.battery_percentage = battery
            if battery <=15:
                self.set_maintenance_status("StandBy")

        else:
            raise ValueError("Battery percentage must be between 0 and 100")

    def get_maintenance_status(self):
        """
        Gets the maintenance status of the vehicle.

        Returns
        -------
        str
            Current maintenance status
        """
        return self.__maintenance_status

    def get_rental_price(self):
        """
        Gets the rental price of the vehicle.

        Returns
        -------
        float
            Rental price
        """
        return self.__rental_price

    def set_maintenance_status(self, status):
        """
        Sets the maintenance status with validation.

        Parameters
        ----------
        status : str
            Allowed values: Available, On Trip, Under Maintenance

        Raises
        ------
        ValueError
            If status is invalid
        """
        allowed = ["Available", "On Trip", "Under Maintenance","StandBy"]
        if status in allowed:
            self.__maintenance_status = status
        else:
            raise ValueError("Invalid maintenance status")


    def get_maintenance_status(self):
        """
        Returns the maintenance status.

        Returns
        -------
        str
            Maintenance status
        """
        return self.__maintenance_status

    def get_rental_price(self):
        """
        Returns the rental price.

        Returns
        -------
        float
            Rental price
        """
        return self.__rental_price

    @abstractmethod
    def calculate_trip_cost(self, distance):
        """
        Calculates trip cost based on distance.

        Parameters
        ----------
        distance : int
            Total distance in kilometers

        Returns
        -------
        float
            Calculated trip fare
        """
        pass

    def __eq__(self, value):
        """
        Compares two vehicles based on vehicle ID.

        Parameters
        ----------
        value : Vehicle
            Vehicle object to compare

        Returns
        -------
        bool
            True if vehicle IDs match, else False
        """
        if not isinstance(value, Vehicle):
            return False
        else:
            return self.vehicle_id == value.vehicle_id

    def __str__(self):
        """
        Returns string representation of the vehicle.

        Returns
        -------
        str
            Vehicle details as string
        """
        return f"{self.vehicle_id} | {self.model} | {self.battery_percentage} | {self.get_maintenance_status()}"


class ElectricCar(Vehicle):
    """
    Represents an electric car vehicle.
    """

    def __init__(self, vehicle_id, model, battery_percentage, seating_capacity):
        """
        Initializes an ElectricCar object.

        Parameters
        ----------
        vehicle_id : str
            Vehicle ID

        model : str
            Vehicle model

        battery_percentage : int
            Battery percentage

        seating_capacity : int
            Number of seats
        """
        super().__init__(vehicle_id, model, battery_percentage)
        self.seating_capacity = seating_capacity

    def calculate_trip_cost(self, distance):
        """
        Calculates trip cost for an electric car.

        Parameters
        ----------
        distance : int
            Distance traveled in kilometers

        Returns
        -------
        float
            Trip cost
        """
        return 5 + (0.50 * distance)


class ElectricScooter(Vehicle):
    """
    Represents an electric scooter vehicle.
    """

    def __init__(self, vehicle_id, model, battery_percentage, max_speed_limit):
        """
        Initializes an ElectricScooter object.

        Parameters
        ----------
        vehicle_id : str
            Vehicle ID

        model : str
            Vehicle model

        battery_percentage : int
            Battery percentage

        max_speed_limit : int
            Maximum speed limit
        """
        super().__init__(vehicle_id, model, battery_percentage)
        self.max_speed_limit = max_speed_limit

    def calculate_trip_cost(self, distance):
        """
        Calculates trip cost for an electric scooter.

        Parameters
        ----------
        distance : int
            Distance traveled in kilometers

        Returns
        -------
        float
            Trip cost
        """
        return 1 + (0.15 * distance)
