from hub import Hub
import constants

# Hub1
h1 = Hub(constants.DRONES, constants.H1_COORD , 'h1', constants.STATIONS, constants.HUB_SUPPLIES)

# Pickup coordinates for hub1
PICK_UP = {
    'name': 'h1',
    'coord': constants.H1_COORD
}

DROP = {
    'name': 's1',
    'coord': constants.S1_COORD
}
h1.getOrder(PICK_UP, DROP, constants.ORDER_1)

efficient_drone = h1.Efficient_drone()
print("The most efficient drone is ", efficient_drone)

cost  = h1.setDelivery()
print("The cost for the drone is ", cost)