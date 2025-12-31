import pytest
from fleet_manager import FleetManager
from vehicle import ElectricCar,ElectricScooter
import os

@pytest.fixture
def fleet():
    return FleetManager()

@pytest.fixture
def car():
    return ElectricCar(101,"Tiago EV",85,5)

@pytest.fixture
def scooter():
    return ElectricScooter(602,"River EV",65,90)

@pytest.fixture
def hub():
    fleet.hubs={"Airport":[ElectricCar(101,"Tiago EV",14,5),ElectricScooter(602,"River EV",65,90),ElectricCar(301,"BE6",79,4),ElectricScooter(303,"Ather",70,65)], "DownTown":[ElectricCar(101,"Harrier EV",12,6),ElectricScooter(201,"Ola",30,75)]}
    return fleet.hubs

def test_add_hub(fleet):
    fleet.add_hub("Airport")
    assert "Airport" in fleet.hubs
   
def test_duplicate_hub(capsys,fleet):
    fleet.add_hub("Airport")
    fleet.add_hub("Airport")
    captured=capsys.readouterr()
    assert captured.out == "Hub 'Airport' already exists\n"


def test_add_vehicle(car,fleet):
    hubname="DownTown"
    fleet.add_hub(hubname)   
    fleet.add_vehicle_to_hub(hubname,car)
    assert car in fleet.hubs[hubname]


def test_search_vehicles(scooter,fleet):
    hubname="Airport"
    fleet.add_hub(hubname)
    fleet.add_vehicle_to_hub(hubname,scooter)
    vehicles=fleet.search_vehicles_by_hub(hubname)
    assert scooter in  vehicles


def test_categorize_vehicle(fleet):
     fleet.hubs={"Airport":[ElectricCar(101,"Tiago EV",85,5),ElectricScooter(602,"River EV",65,90)], "DownTown":[ElectricCar(101,"Harrier EV",45,6),ElectricScooter(201,"Ola",14,75)]}
     vehicles={"ElectricCar":[ElectricCar(101,"Tiago EV",85,5),ElectricCar(101,"Harrier EV",45,6)],"ElectricScooter":[ElectricScooter(602,"River EV",65,90),ElectricScooter(201,"Ola",14,75)]}
     category=fleet.categorize_vehicles_by_type()
     assert category == vehicles


def test_status_count(fleet):
    fleet.hubs={"Airport":[ElectricCar(101,"Tiago EV",14,5),ElectricScooter(602,"River EV",65,90)], "DownTown":[ElectricCar(101,"Harrier EV",12,6),ElectricScooter(201,"Ola",14,75)]}
    count = { "Available": 1,"On Trip": 0,"Under Maintenance": 0,"StandBy":3}
    status = fleet.get_vehicle_count_by_status()
    assert status == count


def test_sorting_by_model(hub,fleet):
    fleet.hubs=hub
    hubname="Airport"
    list1=[ElectricScooter(303,"Ather",70,65),ElectricCar(301,"BE6",79,4),ElectricScooter(602,"River EV",65,90),ElectricCar(101,"Tiago EV",14,5)]
    list2=fleet.get_vehicles_sorted_by_model(hubname)
    assert list1==list2

def test_sorted_by_battery(hub,fleet):
    fleet.hubs=hub
    hubname="Airport"
    list1=[ElectricCar(301,"BE6",79,4),ElectricScooter(303,"Ather",70,65),ElectricScooter(602,"River EV",65,90),ElectricCar(101,"Tiago EV",14,5)]
    list2=fleet.get_vehicle_sorted_by_battery_percentage("Airport")
    assert list1== list2

def test_save_csv(fleet,tmp_path):
    file_name=tmp_path/"vehicle data.csv"
    fleet.save_to_csv(file_name)
    assert os.path.exists(file_name)== True


def test_load_csv(fleet):
    fleet.load_from_csv("Fleet data.csv")
   
    assert "Airport" in fleet.hubs
    assert "Downtown" in fleet.hubs

    v= fleet.hubs["Downtown"]

    assert v[0].vehicle_id == "23"
    assert v[0].model == "Ather"
    assert v[1].vehicle_id == "3243"
    assert v[1].model == "Cyberster"    

def test_save_json(fleet,tmp_path):
    file_name=tmp_path/"vehicle data.json"
    fleet.save_to_json(file_name)
    assert os.path.exists(file_name)==True


def test_load_json(fleet):
    fleet.load_from_json("Fleet Data.json")

    assert "Airport" in fleet.hubs
    assert "Mall" not in fleet.hubs


    v=fleet.hubs["Airport"]

    assert v[0].vehicle_id=="873"
    assert v[0].model=="tesla"
    assert v[1].vehicle_id=="3442"
    assert v[1].model =="OLA"
    