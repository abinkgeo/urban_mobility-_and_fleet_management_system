class FleetManager:
    def __init__(self):
      
        self.hubs = {}

    def add_hub(self, hub_name):
        if hub_name not in self.hubs:
            self.hubs[hub_name] = []
        else:
            print(f"Hub '{hub_name}' already exists")

    def add_vehicle_to_hub(self, hub_name, vehicle):
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
         return self.hubs.get(hub_name, [])
    
    def search_vehicles_by_battery(self, threshold):
        result = []

        for vehicles in self.hubs.values():
                high_battery = [v for v in vehicles if (lambda x: x.battery_percentage > threshold)(v)]
                result.extend(high_battery)

        return result

