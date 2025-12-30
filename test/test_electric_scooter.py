import pytest
from vehicle import ElectricScooter

@pytest.fixture
def scooter():
    return ElectricScooter(303,"Ather",70,65)

def test_scooter_object(scooter):
    assert scooter.vehicle_id==303
    assert scooter.model=="Ather"
    assert scooter.battery_percentage==70
    assert scooter.max_speed_limit==65
    
def test_car_trip_cost(scooter):
    distance=500
    assert scooter.calculate_trip_cost(distance)==76


def test_maintenance_status():
    s=ElectricScooter(201,"Ola",14,75)
    assert s.get_maintenance_status()=="StandBy"

