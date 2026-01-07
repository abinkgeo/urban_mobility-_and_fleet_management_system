Eco-Ride Urban Mobility System

A Python console application that manages electric vehicles across multiple hubs.
This project is built to practice Object-Oriented Programming (OOP) concepts and basic data handling in  Python.

 What This Project Shows

 Object-Oriented Programming in Python

 Real-world modeling of vehicles and hubs

 Clean separation of logic and user interaction

 File handling using CSV and JSON

 Basic unit testing using pytest

Key Features

 Add fleet hubs (e.g., Downtown, Airport)

 Add Electric Cars and Electric Scooters

 Prevent duplicate vehicle IDs

 Search vehicles by hub or battery level

 View vehicles grouped by type

 Sort vehicles by model, battery, or price

 Fleet analytics (count by status)

 Save and load data using CSV and JSON

Project Structure
urban_mobility-_and_fleet_management_system/
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

git Design Overview

Vehicle is the base class

ElectricCar and ElectricScooter extend Vehicle

FleetManager handles all business logic

main.py handles user input and menu

Hubs and vehicles follow an aggregation relationship

File Storage

CSV for flat data storage

JSON for nested hub-vehicle data

Custom objects are manually serialized and restored

Learning Outcome

This project helps in understanding:

OOP principles in Python

Working with collections and dictionaries

File I/O

Basic testing practices

Writing clean and readable code

Author

Abin Geo