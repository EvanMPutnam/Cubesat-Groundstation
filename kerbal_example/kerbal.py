import krpc

import sys
import random
import time

#API import
sys.path.append("../src")
import api

#Default database params for a kerbal space program dashboard.
DATABASE_PROJECT = "KERBAL_Test"
DATABASE_PARAMETERS = {
    "Altitude": "Altitude",
    "Speed": "Speed",
    "Mach": "Mach",
    "Angle_Of_Attack": "Angle_Of_Attack",
    "Latitude": "Latitude",
    "Longitude": "Longitude",
}

class Flight_Debug:
    def __init__(self):
        self.mean_altitude = random.random()
        self.speed = random.random()
        self.mach = random.random()
        self.angle_of_attack = random.random()
        self.latitude = random.random()
        self.longitude = random.random()

class Vessel_Debug:
    def __init__(self):
        pass

    def flight(self):
        return Flight_Debug()

#This is used to update the data display with each respective parameter.
def update_parameters(vessel, database_project = DATABASE_PROJECT, database_params = DATABASE_PARAMETERS, debug=False):
    #Get flight data
    flight = vessel.flight()
    #Get all the datapoints
    altitude = flight.mean_altitude
    speed = flight.speed
    mach = flight.mach
    aoa = flight.angle_of_attack
    latitude = flight.latitude
    longitude = flight.longitude
    #Update viewer
    if debug:
        print("Starting update")
    api.update_data(database_params['Altitude'], database_project, altitude, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Speed'], database_project, speed, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Mach'], database_project, mach, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Angle_Of_Attack'], database_project, aoa, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Latitude'], database_project, latitude, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Longitude'], database_project, longitude, type_of_op=api.REPLACE_OP, debug=debug)
    if debug:
        print("Ending update")

#Create connection to krpc
def create_connection(name_val):
    conn = krpc.connect(name = name_val)
    vessel = conn.space_center.active_vessel
    return conn, vessel

#Update data every second you can.
def run(debug=False):
    print(debug)
    if debug == True:
        conn = None
        vessel = Vessel_Debug()
    else:
        conn, vessel = create_connection("Hello Kerbal!")
    while True:
        #Sleep for a second and go nuts!
        time.sleep(1)
        update_parameters(vessel, debug=debug)
        

if __name__ == "__main__":
    run(debug=True)
