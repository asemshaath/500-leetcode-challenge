"""

-ParkingSystem
 add a car
 check if the car has a space based on the type

"""

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self._availble_spots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self._availble_spots[carType] > 0:
            self._availble_spots[carType] -= 1
            return True
        return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
