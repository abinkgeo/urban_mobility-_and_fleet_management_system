import csv
import json
from vehicle import *

class FleetManager:
    def __init__(self):
       
        self.hubs = {}

    def add_hub(self, hub_name):
        """
        Adds a new hub to the fleet.

        Parameters
        ----------
        hub_name : str
            Name of the hub

        Prints
        ------
        str
            Message if hub already exists
        """
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
        else:
            print(f"Hub '{hub_name}' already exists")

    def add_vehicle_to_hub(self, hub_name, vehicle):
        """
        Adds a vehicle to an existing hub.

        Parameters
        ----------
        hub_name : str
            Name of the hub

        vehicle : Vehicle
            Vehicle object to be added

        Prints
        ------
        str
            Message if hub does not exist or vehicle is duplicate
        """
        if hub_name not in self.hubs:
            print(f"Hub '{hub_name}' does not exist")
            return

        duplicates = [v for v in self.hubs[hub_name] if v == vehicle]

        if duplicates:
            print(f"Duplicate Vehicle ID '{vehicle.vehicle_id}' not allowed in hub '{hub_name}'")
            return

        self.hubs[hub_name].append(vehicle)
        print(f"Vehicle {vehicle.vehicle_id} added to hub '{hub_name}'")

    def search_vehicles_by_hub(self, hub_name):
        """
        Searches vehicles by hub name.

        Parameters
        ----------
        hub_name : str
            Name of the hub

        Returns
        -------
        list
            List of vehicles in the hub
        """
        return self.hubs.get(hub_name, [])

    def search_vehicles_by_battery(self, threshold):
        """
        Searches vehicles whose battery percentage is above a threshold.

        Parameters
        ----------
        threshold : int
            Minimum battery percentage

        Returns
        -------
        list
            Vehicles matching battery criteria
        """
        result = []

        for vehicles in self.hubs.values():
            high_battery = [
                v for v in vehicles
                if (lambda x: x.battery_percentage > threshold)(v)
            ]
            result.extend(high_battery)

        return result

    def categorize_vehicles_by_type(self):
        """
        Categorizes vehicles based on their class type.

        Returns
        -------
        dict
            Vehicle type mapped to list of vehicles
        """
        category = {}

        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                vehicle_type = type(vehicle).__name__

                if vehicle_type not in category:
                    category[vehicle_type] = []

                category[vehicle_type].append(vehicle)

        return category

    def get_vehicle_count_by_status(self):
        """
        Counts vehicles based on maintenance status.

        Returns
        -------
        dict
            Status mapped to count of vehicles
        """
        status_count = {
            "Available": 0,
            "On Trip": 0,
            "Under Maintenance": 0,
            "StandBy":0
        }

        for vehicles in self.hubs.values():
            for vehicle in vehicles:
                status = vehicle.get_maintenance_status()
                if status in status_count:
                    status_count[status] += 1

        return status_count

    def get_vehicles_sorted_by_model(self, hub_name):
        """
        Sorts vehicles in a hub by model name.

        Parameters
        ----------
        hub_name : str
            Name of the hub

        Returns
        -------
        list
            Vehicles sorted by model
        """
        vehicles = self.hubs.get(hub_name, [])
        return sorted(vehicles, key=lambda v: v.model.lower())

    def get_vehicle_sorted_by_battery_percentage(self, hub_name):
        """
        Sorts vehicles in a hub by battery percentage (descending).

        Parameters
        ----------
        hub_name : str
            Name of the hub

        Returns
        -------
        list
            Vehicles sorted by battery percentage
        """
        vehicles = self.hubs.get(hub_name, [])
        return sorted(vehicles, key=lambda v: v.battery_percentage, reverse=True)

    def save_to_csv(self, filename):
        """
        Saves fleet data to a CSV file.

        Parameters
        ----------
        filename : str
            CSV file name
        """
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Hub",
                "VehicleType",
                "VehicleID",
                "Model",
                "Battery",
                "RentalPrice",
                "Status",
                "Seating Capcity / Max Speed "
            ])

            for hub, vehicles in self.hubs.items():
                for v in vehicles:
                    if v.__class__.__name__ == "ElectricCar":
                        extra = v.seating_capacity
                    else:
                        extra = v.max_speed_limit

                    writer.writerow([
                        hub,
                        v.__class__.__name__,
                        v.vehicle_id,
                        v.model,
                        v.battery_percentage,
                        v.get_rental_price(),
                        v.get_maintenance_status(),
                        extra
                    ])

    def load_from_csv(self, filename):
        """
        Loads fleet data from a CSV file.

        Parameters
        ----------
        filename : str
            CSV file name
        """
        self.hubs.clear()

        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)

            for row in reader:
                hub = row["Hub"]
                v_type = row["VehicleType"]

                if hub not in self.hubs:
                    self.hubs[hub] = []

                if v_type == "ElectricCar":
                    vehicle = ElectricCar(
                        row["VehicleID"],
                        row["Model"],
                        int(row["Battery"]),
                        int(row["Seating Capcity / Max Speed "])
                    )
                else:
                    vehicle = ElectricScooter(
                        row["VehicleID"],
                        row["Model"],
                        int(row["Battery"]),
                        int(row["Seating Capcity / Max Speed "])
                    )

                vehicle.set_rental_price(float(row["RentalPrice"]))
                vehicle.set_maintenance_status(row["Status"])

                self.hubs[hub].append(vehicle)

    def save_to_json(self, filename):
        """
        Saves fleet data to a JSON file.

        Parameters
        ----------
        filename : str
            JSON file name
        """
        data = {}

        for hub, vehicles in self.hubs.items():
            data[hub] = []

            for v in vehicles:
                if v.__class__.__name__ == "ElectricCar":
                    extra = v.seating_capacity
                else:
                    extra = v.max_speed_limit

                data[hub].append({
                    "type": v.__class__.__name__,
                    "vehicle_id": v.vehicle_id,
                    "model": v.model,
                    "battery": v.battery_percentage,
                    "rental_price": v.get_rental_price(),
                    "status": v.get_maintenance_status(),
                    "extra": extra
                })

        with open(filename, "w") as file:
            json.dump(data, file, indent=4)

    def load_from_json(self, filename):
        """
        Loads fleet data from a JSON file.

        Parameters
        ----------
        filename : str
            JSON file name
        """
        self.hubs.clear()

        with open(filename, "r") as file:
            data = json.load(file)

        for hub, vehicles in data.items():
            self.hubs[hub] = []

            for v in vehicles:
                if v["type"] == "ElectricCar":
                    vehicle = ElectricCar(
                        v["vehicle_id"],
                        v["model"],
                        v["battery"],
                        v["extra"]
                    )
                else:
                    vehicle = ElectricScooter(
                        v["vehicle_id"],
                        v["model"],
                        v["battery"],
                        v["extra"]
                    )

                vehicle.set_rental_price(v["rental_price"])
                vehicle.set_maintenance_status(v["status"])

                self.hubs[hub].append(vehicle)
