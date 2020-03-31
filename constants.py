# DRONE
CAPACITY_OF_DRONE = 100
INITIAL_TRAVEL_DISTANCE = 100
NOT_FLYING = 0
DRONE_COUNT = 0
FLYING = 1
GRAVITY_FACTOR = 10
WEATHER_COST_UNIT_MASS = 10
KM_PER_BATTERY_UNIT = 100
CHARGE_PER_BATTERY_UNIT = 1
MAINTAINENCE_COST = 10

# HUB
DRONES_AT_HUB = 6
CANNOT_DELIVER = 0
CAN_DELIVER = 1
H1_COORD = (12.00, 34.00)
S1_COORD = (14.00, 17.00)
STATIONS = [{'name': 'S1', 'coord': S1_COORD}]
HUB_SUPPLIES = {
    'medicine A': {
        'quantity': 20,
        'mass': 1
    },
    'medicine B': {
        'quantity': 20,
        'mass': 1
    },
    'medicine C': {
        'quantity': 20,
        'mass': 1
    }
}

DRONES = [
    {
        'weather': 2,
        'battery': 45,
        'capacity': 2
    },
    {
        'weather': 6,
        'battery': 5,
        'capacity': 20
    },
    {
        'weather': 10,
        'battery': 100,
        'capacity': 100
    }
]

ORDER_1 = {
    'medicine A': {
        'quantity': 10,
        'mass': 1
    },
    'medicine B': {
        'quantity': 5,
        'mass': 1
    },
    'medicine C': {
        'quantity': 15,
        'mass': 1
    }
}
# LOCATION
GPS_HELPER_LAT = 1.00
GPS_HELPER_LON = 1.00
# BATTERY
INITIAL_BATTERY = 100