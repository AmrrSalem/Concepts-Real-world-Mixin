"""
Example of using a Mixin in Python.

Scenario:
    We have unrelated classes (e.g., Car and Drone) that both need GPS tracking
    capabilities. Instead of duplicating GPS methods in both, we create a GPSMixin
    and add it via multiple inheritance.

Why Mixin?
    - The GPS functionality is independent from the core identity of Car or Drone.
    - Both classes can "opt in" to GPS features without forcing a common base class.
    - The mixin is not intended to be instantiated directly.
"""

from datetime import datetime


class GPSMixin:
    """
    A Mixin that provides GPS tracking functionality.

    Note:
        This class is not meant to be instantiated on its own.
        It is intended to be combined with other classes via multiple inheritance.
    """

    def get_location(self):
        """
        Simulate retrieving the current GPS coordinates.

        Returns:
            tuple: A (latitude, longitude) pair.
        """
        # Dummy data for example purposes
        return (30.0444, 31.2357)  # Coordinates for Cairo, Egypt

    def log_location(self):
        """
        Print the current location with a timestamp.
        """
        lat, lon = self.get_location()
        print(f"[{datetime.now()}] Location: ({lat}, {lon})")


class Car:
    """
    Represents a simple car.
    """

    def drive(self):
        """
        Simulate driving.
        """
        print("The car is driving.")


class Drone:
    """
    Represents a simple drone.
    """

    def fly(self):
        """
        Simulate flying.
        """
        print("The drone is flying.")


class GPSCar(Car, GPSMixin):
    """
    A Car with GPS tracking capability.
    """
    pass


class GPSDrone(Drone, GPSMixin):
    """
    A Drone with GPS tracking capability.
    """
    pass


if __name__ == "__main__":
    car = GPSCar()
    car.drive()
    car.log_location()

    drone = GPSDrone()
    drone.fly()
    drone.log_location()
