from django.db import models


# Tank model created for simulation.


class Tank(models.Model):
    name = models.TextField()
    barrel_caliber = models.DecimalField(decimal_places=2, max_digits=4)
    barrel_rate_of_fire = models.IntegerField()
    turret = models.BooleanField()
    turret_caliber = models.DecimalField(
        decimal_places=2, max_digits=4, blank=True)
    front_armor = models.BooleanField()
    side_armor = models.BooleanField()
