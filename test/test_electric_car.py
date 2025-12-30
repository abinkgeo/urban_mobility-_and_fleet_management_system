import pytest
from vehicle import ElectricCar

@pytest.fixture
def car():
    return ElectricCar(301,"BE6",79,4)
    
def test_car_object(car):
    assert car.vehicle_id==301
    assert car.model=="BE6"
    assert car.battery_percentage==79
    assert car.seating_capacity==4

def test_trip_cost(car):
    distance=500
    assert car.calculate_trip_cost(distance)== 255

def test_maintenance():
    c=ElectricCar(403,"Commet",14,3)
    assert c.get_maintenance_status()=="StandBy"


def test_invalid_maintenace():
    c=ElectricCar(103,"MG",60,5)
    with pytest.raises(ValueError):
        c.set_maintenance_status("Low Battery")


def test_str(capsys,car):
    print(car)
    captured=capsys.readouterr()
    assert captured.out == "301 | BE6 | 79 | Available\n"

