import constants
class Cost_Calculation:
    def __init__(self):
        # The additional cost required due to additional work done
        self.work_done_cost = 0
        # The overall cost of the order
        self.cost = 0
        # self.drone = drone
    
    def workDone(self, drone, order_mass, distance):
        # Consider the weather factor
        self.work_done_cost = order_mass * (drone.weather +
            constants.GRAVITY_FACTOR)
        self.cost_Calculation(self.work_done_cost, distance)
        return self.cost
    
    def cost_Calculation(self,work_done_cost, distance):
        # Cost due to the battery consumption
        battery_consumption = (distance / constants.KM_PER_BATTERY_UNIT)
        battery_cost =  battery_consumption * constants.CHARGE_PER_BATTERY_UNIT

        # Overall cost of the order
        self.cost = battery_cost + constants.MAINTAINENCE_COST + work_done_cost
