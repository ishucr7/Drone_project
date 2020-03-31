from geopy.distance import geodesic
import math

INF = math.inf

def Distance(coord1, coord2):
    return geodesic(coord1,coord2).km
