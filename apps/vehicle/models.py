from django.db import models

class VehicleType(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

class Park(models.Model):
    SPACES = [
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
        ("6","6"),
        ("7","7"),
        ("8","8"),
        ("9","9"),
        ("10","10"),
        ("11","11"),
        ("12","12"),
        ("13","13"),
        ("14","14"),
        ("15","15"),
    ]
    parkingspace = models.CharField(max_length=4, choices=SPACES)
    def __str__(self):
        return self.parkingspace

class Vehicle(models.Model):
    Vehicle_type = models.ForeignKey(VehicleType, on_delete = models.PROTECT)
    plate = models.CharField(max_length=10)
    color = models.TextField(max_length=10)
    spot = models.ManyToManyField(Park, through="Asign")

    def __str__(self):
        return self.plate

class Asign(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    spot = models.ForeignKey(Park, on_delete=models.CASCADE)
    start_hour = models.TimeField()
    end_hour = models.TimeField()

    def __str__(self):
        return self.vehicle.plate



    
