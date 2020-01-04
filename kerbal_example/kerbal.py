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
    "Mach": "Mach",
    "Angle_Of_Attack": "Angle_Of_Attack",
    "Latitude": "Latitude",
    "Longitude": "Longitude",

    "Apoapsis": "Apoapsis",
    "Periapsis": "Periapsis",
    "Semi_Major_Axis": "Semi_Major_Axis",
    "Semi_Minor_Axis": "Semi_Minor_Axis",
    "Period": "Period",
    "Eccentricity": "Eccentricity"
}

class Flight_Debug:
    def __init__(self):
        self.mean_altitude = random.random()
        self.speed = random.random()
        self.mach = random.random()
        self.angle_of_attack = random.random()
        self.latitude = random.random()
        self.longitude = random.random()

class Orbit_Debug:
    def __init__(self):
        self.apoapsis = random.random()
        self.periapsis = random.random()
        self.semi_major_axis = random.random()
        self.semi_minor_axis = random.random()
        self.period = random.random()
        self.eccentricity = random.random()
        

class Vessel_Debug:
    def __init__(self):
        pass

    def flight(self):
        return Flight_Debug()

    def orbit(self):
        return Orbit_Debug()

#This is used to update the data display with each respective parameter.
def update_parameters(vessel, database_project = DATABASE_PROJECT, database_params = DATABASE_PARAMETERS, debug=False):
    #Get flight data
    flight = vessel.flight()
    orbit = vessel.orbit
    #Get all the datapoints
    altitude = flight.mean_altitude
    mach = flight.mach
    aoa = flight.angle_of_attack
    latitude = flight.latitude
    longitude = flight.longitude

    #Get orbit data
    apoapsis = orbit.apoapsis
    periapsis = orbit.periapsis
    semi_major_axis = orbit.semi_major_axis
    semi_minor_axis = orbit.semi_minor_axis
    period = orbit.period
    eccentricity = orbit.eccentricity

    if debug:
        print("Starting update")

    #Spacecraft data
    api.update_data(database_params['Altitude'], database_project, altitude, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Mach'], database_project, mach, debug=debug)
    api.update_data(database_params['Angle_Of_Attack'], database_project, aoa, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Latitude'], database_project, latitude, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Longitude'], database_project, longitude, type_of_op=api.REPLACE_OP, debug=debug)

    #Orbital elements
    api.update_data(database_params['Apoapsis'], database_project, apoapsis, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Periapsis'], database_project, periapsis, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Semi_Major_Axis'], database_project, semi_major_axis, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Semi_Minor_Axis'], database_project, semi_minor_axis, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Period'], database_project, period, type_of_op=api.REPLACE_OP, debug=debug)
    api.update_data(database_params['Eccentricity'], database_project, eccentricity, type_of_op=api.REPLACE_OP, debug=debug)


    if debug:
        print("Ending update")

#Create connection to krpc
def create_connection(name_val):
    conn = krpc.connect()
    print("Connection acquired")
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
    run(debug=False)
