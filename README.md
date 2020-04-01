# Drone_project
## Prerequisite
Install geopy
```python
pip install geopy
```

## Run the Code
```python
python3 run.py
```


## Codebase Overview

### run.py
This file takes a demo Hub and order to run the system.
### tools.py
It contains helper functions that are used in other files.
### constants.py
It contains the constants being used in other files.
### drone.py
Implementation of Drone class with supporting functions.
### hub.py
Implementation of Hub class with supporting functions.
### station.py
Implementation of Station class.
### cost_calculation.py
Implementation of Cost_Calculation class.
### location.py
Implementation of Location class.



## Assumptions
* Station is assumed to be just a destiation.
* A drone delivers an order from hub to station.
* We're not dealing with the movement of drone as of now. The task is to just get the id of the most efficient drone.
* The hub only deals with one order at a time.
* As there were no specifications in the document regarding handling multpile deliveries, the system doesn't update the supplies of the hub.


## Future Scope
* Handle possible scenarios where error could occur.
* Add test files for each of the classes.
* Create another version where the system deals with:
  * Drone selected actually going out for delivery.
  * Updatation of the supplies at the hub.
  * Give more emphasis to the stations as well.
