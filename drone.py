import constants
import copy
from location import Location
from tools import Distance

class Drone:
    drone_count = constants.DRONE_COUNT

    def __init__(self, origin_location, battery = constants.INITIAL_BATTERY,
        capacity = constants.CAPACITY_OF_DRONE, weather = constants.WEATHER_COST_UNIT_MASS ):
        """
            Args:
                origin_location: (Location) Location of the drone.
                battery: (int) Battery of the drone.
                capacity: (double) Maximum limit of the mass that the drone can carry.
                weather: (double) Factor of weather to be considered while calculating the cost.
        """
        
        # Count of the drones
        Drone.drone_count = Drone.drone_count + 1
        # Unique id of the drone
        self.id = Drone.drone_count

        self.battery = battery
        self.capacity = capacity

        # initially the remaining capacity is the actual capacity
        self.remaining_capacity = capacity

        self.weather = weather
        self.current_location = copy.deepcopy(origin_location)

        # Distance that can be travelled with the current battery
        self.trav_dist = self.battery * constants.KM_PER_BATTERY_UNIT

        # Distance between the pickup point and the drone
        self.point_dist = None
        self.work_done = None

    
    def chargeBatteryFully(self):
        """ Charges the battery to full
        """
        self.battery = 100


    def getDistance(self, pickup_location):
        """ Calculate distance between the drone and the pickup location
            Args:
                pickup_location: (Location) Location of the hub.

            Returns:
                (double) Distance between the drone and the pickup point.
        """
        drone_coord = self.current_location.getLatLong()
        pickup_coord = pickup_location.getLatLong()
        self.point_dist = Distance(drone_coord, pickup_coord)
        return self.point_dist

   
    def distanceCanBeCovered(self):
        """ Calculates the amount of distance that drone can travel with given battery.
            Returns:
                (double) Distance that can be covered with the given battery.
        """
        self.trav_dist = self.battery * constants.KM_PER_BATTERY_UNIT
        return self.trav_dist


    def Capacity(self):
        """ 
            Returns:
                (double) The mass that can still be loaded on the drone.
        """
        return self.remaining_capacity
