import constants
from cost_calculation import Cost_Calculation
from drone import Drone
from location import Location
from station import Station
from tools import Distance
from tools import INF

class Hub:
    #  Count of hubs created so far
    hub_count = 0
    def __init__(self, drones, coord, name, stations, supplies):
        """
            Args:
                drones: (list) List of drones to be generated at the hub.
                coord: (pair) Latitude and Longitude of the hub's location.
                name: (str) Name of the hub.
                stations: (list) List of the stations linked to the hub.
                supplies: (list) List of the supplies that the hub has.
        """
        # increment the hub count
        Hub.hub_count = Hub.hub_count + 1
        # unique id of the hub
        self.id = Hub.hub_count
        self.drones = []
        self.stations = []
        self.name = name
        self.No_of_drone_present = constants.DRONES_AT_HUB
        self.stations = []
        self.location = Location(coord[0], coord[0])

        # Create drones
        for drone in drones:
            self.drones.append(Drone(self.location, weather = drone['weather'], 
                battery = drone['battery'], capacity = drone['capacity'],))

        # Create Stations
        for station in stations:
            self.stations.append(Station(station['name'], station['coord']))

        self.Supplies = supplies
        
        # Binary value -- whether the hub/station supplies the need of the order.
        self.Supplies_status = constants.CANNOT_DELIVER

        # Distance between source loc and dest location
        self.Order_dist = None

        self.ordered_supplies = None
        #  The mass of ordered supplies
        self.Order_Mass = None
        # Name of the source from where the supply is to be picked up.
        self.Source_Name = None
        self.Source_coord = None
        # Name of the destination from where the supply is to be dropped.
        self.Dest_Name = None
        self.Dest_coord = None
        # The drone that is selected for the order
        self.selected_drone = None


    def getDistance(self):
        """ Calculate the distance between the Source and the Destination.
            Returns:
                (double) Distance between source and destination.
        """
        self.Order_dist = Distance(self.Source_coord, self.Dest_coord)
        return self.Order_dist


    def getOrder(self, pick_up_point, drop_point, list_of_supplies):
        """ Gets the order.
            Args:
                pick_up_point: (object) Details of the pick up point.
                drop_point: (object) Details of the drop point.
                list_of_supplies: (list) List of the supplies needed.
        """
        self.Supplies_status = constants.CANNOT_DELIVER

        self.Source_Name = pick_up_point['name']
        self.Source_coord = pick_up_point['coord']

        self.Dest_Name = drop_point['name']
        self.Source_coord = drop_point['coord']
        
        self.ordered_supplies = list_of_supplies
        self.Order_Mass = self.getMass()
        self.getDistance()


    def Efficient_drone(self):
        """ Calculates which drone is the most efficient.
            Returns:
                (int) Id of the most efficient drone.
        """
        # Mass of the order received.
        capacity_required = self.getMass()
        # To store the id of the most efficient drone.
        efficient_drone = None
        # To keep track of the nearest drone so far.
        minm_dist_so_far = INF

        for drone in self.drones:
            # Distance that can be travelled by drone >= distance required to complete order.
            if drone.distanceCanBeCovered() > self.Order_dist:
                # Drone can pick up the order or not.
                if drone.remaining_capacity > capacity_required:
                    dist_from_pickup = drone.getDistance(self.location)
                    # Get such drone that is nearest to the pickup point
                    if dist_from_pickup < minm_dist_so_far:
                        efficient_drone = drone.id
                        self.selected_drone = drone
                        minm_dist_so_far = dist_from_pickup

        return efficient_drone


    def setDelivery(self):
        """ Calculates the work done and the total cost of the operation.
            Returns:
                (double) Total cost of the operation.
        """
        cc = Cost_Calculation()
        cost = cc.workDone(self.selected_drone, self.Order_Mass, self.getDistance())
        return cost


    def getMass(self):
        """ Calculates the mass of the order received.
            Returns:
                (double) Total mass of the order.
        """
        mass = 0
        for supply in self.ordered_supplies:
            mass = mass + (self.ordered_supplies[supply]['quantity'] * 
                self.ordered_supplies[supply]['mass'])
        return mass


    def suppliesStatus(self):
        """ See if the hub can satisfy the needs of the order.
            Returns:
                (bool) True or False.
        """
        # returns true if the hub can supply the ordered items
        for key,value in self.ordered_supplies.items():
            # Quantity required > quantity we have then False
            if value['quantity'] > self.Supplies[key]['quantity']:
                self.Supplies_status = constants.CANNOT_DELIVER
                return False
        self.Supplies_status = constants.CAN_DELIVER
        return True
            
