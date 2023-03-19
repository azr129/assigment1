class vehicle:
    def __init__(self, spotsize):
        self.spotsize = spotsize

    def get_spot_size(self):
        return self.spotsize 

class driver:
    def __init__(self, id, vehicle):
        self.id = id
        self.vehicle = vehicle
        self.paymentdue = 0
    
    def get_vehicle(self):
        return self.vehicle

    def get_id(self):
        return self.id
    
    def charge(self, amount):
        self.paymentdue += amount

class car(vehicle):
    def __init__(self):
        super().__init__(1)

class limo(vehicle):
    def __init__(self):
        super().__init__(2)

class SemiTruck(vehicle):
    def __init__(self):
        super().__init__(3)

class ParkingFloor:
    def __init__(self, spotcount):
        self.sports = [0] * spotcount
        self.vehiclemap = {}
    
    def park_vehicle(self,vehicle):
        size=vehicle.get_spot_size()
        l, r= 0, 0
        while r < len (self.sports):
            if self.sports[r] !=0:
                l = r + 1
            if r - l + 1 == size:
                #enough spots was found, park the vehicle
                for j in range(l,r+1):
                    self.spots[j]=1
                self.vehiclemap[vehicle]= [l,r]
                return True
            r += 1
        return False

    def removeVehicle(self,vehicle):
        start, end= self.vehiclemap[vehicle]
        for i in range(start, end + 1):
            self.sports[i]=0
        del self.vehiclemap[vehicle]

    def get_parking_spots(self):
        return self.sports
    
    def get_vehicle_sports(self,veicle):
        return self.vehiclemap.get(vehicle)

class ParkingGarage:
    def __init__(self, floorcount, spots_per_floor):
        self.parking_floors = [ParkingFloor(spots_per_floor)for _ in range(floorcount)]
    
    def park_vehicle(self,vehicle):
        for floor in self.parking_floors:
            if floor.park_vehicle(vehicle):
                return True
        return False

    def remove_vehicle(self,vehicle):
        for floor in self.parking_floors:
            if floor.get_vehicle_sports(vehicle):
                floor.remove_vehicle(vehicle)
                return True
        return False

import datetime
import math 

class ParkingSystem:
    def __init__(self, parkingGarage, hourlyRate):
        self.parkingGrage = parkingGarage
        self.hourlyRate = hourlyRate
        self.timeParked = {}

    def park_vehicle(self, driver):
        currentHour = datetime.datetime.now().hour
        isParked = self.parkingGrage.park_vehicle(driver.get_vehicle())
        if isParked:
            self.timeParked[driver.get_id()]= currentHour
        return isParked
    
    def remove_vehicle(self,driver):
        if driver.get_id() not in self.timeParked:
            return False
        currentHour = datetime.datetime.now().hour
        timeParked = math.ceil(currentHour - self.timeParked[driver.get_id()])
        driver.charge(timeParked * self.hourlyRate)

        del self.timeParked[driver.get_if()]
        return self.parkingGrage.remove_vehicle(driver.get_vehicle())

ParkingGarage = ParkingGarage(3, 2)
ParkingSystem = ParkingSystem(ParkingGarage, 5)

driver1= driver(1, car())
driver2= driver(2, limo())
driver3= driver(3, SemiTruck())



print(ParkingSystem.park_vehicle(driver1))      #true
print(ParkingSystem.park_vehicle(driver2))      #true
print(ParkingSystem.park_vehicle(driver3))      #false

print(ParkingSystem.remove_vehicle(driver1))     #true
print(ParkingSystem.remove_vehicle(driver2))     #true
print(ParkingSystem.remove_vehicle(driver3))     #false