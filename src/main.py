from vehicle import *


class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")
        vehicles=[ElectricCar("T01","Tesla CyberTruck",90,5),
                 ElectricScooter("S01","Ola S1 ",40,90),
                 ElectricCar("B06","Mahindra BE6",60,5),
                 ElectricScooter("R01","Ather 450",45,75),
                 ElectricCar("M01","MG Cyberster",80,2)]
        
        distance=50
        for v in vehicles:
            cost=v.calculate_trip_cost(distance)
            print(f"{v.model} cost : ${cost}")



if __name__ == "__main__":
    EcoRideMain.main()
