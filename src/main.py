from vehicle import *
from fleet_manager import FleetManager

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        fleet_manager = FleetManager()
        fleet_manager.add_hub("Downtown")
        fleet_manager.add_hub("Airport")

        car1 = ElectricCar("V101", "Tesla Model 3", 90, 5)
        car2 = ElectricCar("V101", "Nissan Leaf", 85, 5) 
        scooter1 = ElectricScooter("S201", "Ola S1", 80, 60)
        scooter2=ElectricScooter("S201","Ather 450",64,70)

        fleet_manager.add_vehicle_to_hub("Downtown", car1)
        fleet_manager.add_vehicle_to_hub("Downtown", car2)  
        fleet_manager.add_vehicle_to_hub("Airport", scooter1)
        fleet_manager.add_vehicle_to_hub("Airport", scooter2)


if __name__ == "__main__":
    EcoRideMain.main()
