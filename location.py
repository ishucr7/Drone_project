import constants
class Location:
    def __init__(self, latitude, longitude):
        """
            Args:
                latitude: (double) Latitude of the location
                longitude: (double) Longitude of the location
        """
        self.Latitude = latitude
        self.Longitude = longitude


    def getLatLong(self):
        """
            Returns:
                (tuple) Latitude and Longitude of the location
        """
        return (self.Latitude, self.Longitude)


    def gps_helper(self):
        # Let's assume that the function is in coordination with the GPS
        # and it gets the location coordinates from GPS somehow and calls the
        # updatedLocation function to update the location
        self.updateLocation(constants.GPS_HELPER_LON, constants.GPS_HELPER_LAT)


    def updateLocation(self, longitude, latitude):
        """ Updates the coordinates of the Location
            Args:
                latitude: (double) Latitude of the location
                longitude: (double) Longitude of the location
        """
        self.Latitude = latitude
        self.Longitude = longitude
