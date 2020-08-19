from django.db import models


class Car(models.Model):
    MANUAL = 0
    AUTOMATIC = 1
    ROBOT = 2
    TRANSMISSION = [
        (MANUAL, "Ручная"),
        (AUTOMATIC, "Автомат"),
        (ROBOT, "Робот")
    ]

    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.PositiveIntegerField(default=2020)
    color = models.CharField(max_length=255)
    transmission = models.PositiveSmallIntegerField(choices=TRANSMISSION, default=MANUAL)

    def __str__(self):
        return "{} {}".format(self.manufacturer, self.model)