from vehicle import *
from fleet_manager import FleetManager

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        fleet_manager = FleetManager()

       
        fleet_manager.add_hub("Downtown")
        fleet_manager.add_hub("Airport")

   
        car = ElectricCar("C101", "Tesla Model 3", 90, 5)
        scooter = ElectricScooter("S201", "Ola S1", 80, 60)

   
        fleet_manager.add_vehicle_to_hub("Downtown", car)
        fleet_manager.add_vehicle_to_hub("Airport", scooter)


        print("\nVehicles at Downtown Hub:")
        for v in fleet_manager.get_vehicles_by_hub("Downtown"):
            print(v.model)

        print("\nVehicles at Airport Hub:")
        for v in fleet_manager.get_vehicles_by_hub("Airport"):
            print(v.model)


if __name__ == "__main__":
    EcoRideMain.main()
