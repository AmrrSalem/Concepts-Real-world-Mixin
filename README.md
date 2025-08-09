# Python Mixin Example — GPS Tracking

This example demonstrates how to use a **Mixin** in Python to add extra functionality to multiple, unrelated classes without duplicating code.

## What is a Mixin?

A **Mixin** is a class that provides additional methods or functionality to other classes via **multiple inheritance**.  
It is **not intended to stand alone** — you don't create instances of a mixin directly.  
Instead, it acts like an *add-on* or *plugin* for your class.

## Scenario

We have two unrelated classes:

- `Car` — represents a simple car.
- `Drone` — represents a simple drone.

Both need **GPS tracking capabilities**, but there’s no reason to make them share a common base class (e.g., `Vehicle`).  
Instead, we create a `GPSMixin` and combine it with each class.

## Benefits of a Mixin

- **Avoids code duplication** — GPS methods live in one place.
- **Keeps class hierarchies clean** — no unnecessary “is-a” relationships.
- **Adds features to unrelated classes** — works for anything that needs the extra methods.

## Example Code

```python
from datetime import datetime

class GPSMixin:
    """A mixin that provides GPS tracking functionality."""
    def get_location(self):
        return (30.0444, 31.2357)  # Cairo, Egypt
    
    def log_location(self):
        lat, lon = self.get_location()
        print(f"[{datetime.now()}] Location: ({lat}, {lon})")

class Car:
    def drive(self):
        print("The car is driving.")

class Drone:
    def fly(self):
        print("The drone is flying.")

class GPSCar(Car, GPSMixin):
    pass

class GPSDrone(Drone, GPSMixin):
    pass
