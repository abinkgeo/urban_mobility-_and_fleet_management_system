from vehicle import *
from fleet_manager import FleetManager

class EcoRideMain:
    @staticmethod
    def main():
        print("Welcome to Eco-Ride Urban Mobility System")

        fleet_manager = FleetManager()

        while True:
            print("\n1. Add Hub")
            print("2. Add Vehicle to Hub")
            print("3. Search Vehicles by Hub ")
            print("4. Search Vehicles by Battery more than 80% ")
            print("5. View vehicle by group")
            print("6. Fleet Analytics")
            print("7. View Vehicles sorted by Model ")
            print("8. View Vehicles Sorted by Battery ")
            print("9. View Vehicles Sorted by Rental Price ")
            print("10. Exit")

            choice = input("Enter your choice: ")

            
            if choice == "1":
                hub_name = input("Enter Hub Name: ")
                fleet_manager.add_hub(hub_name)

          
            elif choice == "2":
                hub_name = input("Enter Hub Name: ")

                print("\nSelect Vehicle Type")
                print("1. Electric Car")
                print("2. Electric Scooter")
                v_type = input("Enter choice: ")

                vehicle_id = input("Enter Vehicle ID: ")
                model = input("Enter Model Name: ")
                battery = int(input("Enter Battery Percentage: "))

                if v_type == "1":
                    seats = int(input("Enter Seating Capacity: "))
                    vehicle = ElectricCar(vehicle_id, model, battery, seats)

                elif v_type == "2":
                    speed = int(input("Enter Max Speed Limit: "))
                    vehicle = ElectricScooter(vehicle_id, model, battery, speed)

                
                else:
                    print("Invalid Vehicle Type")
                    continue
                
                price = float(input("Enter Rental Price: "))
                vehicle.set_rental_price(price)
                
                
                print("\nSet Vehicle Status")
                print("1. Available")
                print("2. On Trip")
                print("3. Under Maintenance")

                status_choice = input("Enter status choice: ")

                if status_choice == "1":
                    vehicle.set_maintenance_status("Available")
                elif status_choice == "2":
                     vehicle.set_maintenance_status("On Trip")
                elif status_choice == "3":
                     vehicle.set_maintenance_status("Under Maintenance")
                else:
                     print("Invalid status choice, defaulting to Available")
                     vehicle.set_maintenance_status("Available")
                fleet_manager.add_vehicle_to_hub(hub_name, vehicle)

            elif choice == "3":
                hub_name = input("Enter Hub Name: ")
                vehicles = fleet_manager.search_vehicles_by_hub(hub_name)

                if not vehicles:
                    print("No vehicles found or hub does not exist")
                else:
                    print(f"\nVehicles in {hub_name} Hub:")
                    for v in vehicles:
                        print(v.vehicle_id, v.model, v.battery_percentage)

           
            elif choice == "4":
                result = fleet_manager.search_vehicles_by_battery(80)

                if not result:
                    print("No vehicles with battery more than  80%")
                else:
                    print("\nVehicles with Battery more than 80%:")
                    for v in result:
                        print(v.vehicle_id, v.model, v.battery_percentage)

            elif choice == "5":  
                category = fleet_manager.categorize_vehicles_by_type()

                if not category:
                     print("No vehicles available")
                else:
                    for v_type, vehicles in category.items():
                        print(f"\n{v_type}:")
                        for v in vehicles:
                            print(v.vehicle_id, v.model)            

            elif choice == "6":
                summary = fleet_manager.get_vehicle_count_by_status()

                print("\nFleet Analytics Summary:")
                for status, count in summary.items():
                     print(f"{status}: {count}")


            elif choice == "7":
                hub_name = input("Enter Hub Name: ")
                vehicles = fleet_manager.get_vehicles_sorted_by_model(hub_name)

                if not vehicles:
                    print("No vehicles found or hub does not exist")
                else:
                    print(f"\nVehicles in {hub_name} Hub (Sorted by Model):")
                    for v in vehicles:
                        print(v)


            elif choice == "8":
                hub_name = input("Enter Hub Name: ")
                vehicles = fleet_manager.get_vehicles_sorted_by_battery(hub_name)

                if not vehicles:
                    print("No vehicles found or hub does not exist")
                else:
                    print(f"\nVehicles in {hub_name} Hub (Sorted by Battery):")
                    for v in vehicles:
                        print(v)

            
            elif choice == "9":
                hub_name = input("Enter Hub Name: ")
                vehicles = fleet_manager.get_vehicles_sorted_by_rental_price(hub_name)

                if not vehicles:
                    print("No vehicles found or hub does not exist")
                else:
                    print(f"\nVehicles in {hub_name} Hub (Sorted by Rental Price):")
                    for v in vehicles:
                        print(f"{v.vehicle_id} | {v.model} | $ {v.get_rental_price()} | {v.get_maintenance_status()}")

            
            
            elif choice == "10":
                print("Exiting Eco-Ride System")
                break

            else:
                print("Invalid choice, try again")


if __name__ == "__main__":
    EcoRideMain.main()
