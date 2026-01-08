## Eco-Ride Urban Mobility System

## Overview

Eco-Ride Urban Mobility System is a Python console application that manages electric vehicles across multiple hubs.
The project is designed to practice Object-Oriented Programming (OOP) concepts and basic data handling in Python.

## Project Objectives

- Apply Object-Oriented Programming principles in Python
- Model real-world entities such as vehicles and hubs
- Maintain clean separation between business logic and user interaction
- Practice file handling and persistence
- Write basic unit tests

## Key Features

- Add fleet hubs (e.g., Downtown, Airport)
- Add electric cars and electric scooters
- Prevent duplicate vehicle IDs
- Search vehicles by hub or battery level
- View vehicles grouped by type
- Sort vehicles by model, battery level, or price
- Fleet analytics (vehicle count by status)
- Save and load data using CSV and JSON

## Project Structure

urban_mobility_and_fleet_management_system/
│
├── src/
│   ├── vehicle.py
│   ├── electric_car.py
│   ├── electric_scooter.py
│   ├── fleet_manager.py
│   └── main.py
│
├── tests/
├── requirements.txt
├── pytest.ini
└── README.md

## Design Overview

- Vehicle is the base class
- ElectricCar and ElectricScooter extend Vehicle
- FleetManager handles all business logic
- main.py handles user input and menu
- Hubs and vehicles follow an aggregation relationship

## Data Persistence

- CSV is used for flat vehicle data
- JSON is used for nested hub–vehicle data
- Custom objects are manually serialized and restored

## Testing

- Unit tests are written using pytest
- Core business logic is tested independently

## Learning Outcomes

- Object-Oriented Programming in Python
- Working with collections and dictionaries
- File I/O
- Basic testing practices
- Writing clean and readable code

## Author

Abin Geo
