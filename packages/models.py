from enum import unique
from django.db import models

class Package(models.Model):
    type_choices = (
        (0, 'Inalámbrico'),
        (1, 'Fibra óptica')
    )

    name = models.CharField(max_length=10)
    type = models.IntegerField(default=0, choices=type_choices)
    speed_in_mbps = models.IntegerField() #In MBps
    price = models.IntegerField()

    def get_bandwidth(self):
        return '{} {}'.format(self.speed_in_mbps, 'Mb')

    def __str__(self):
        return '{} {} {}'.format(self.name, self.get_bandwidth(), self.get_type_display())

    class Meta:
        ordering = ['type', 'price']
        unique_together = ['type', 'speed_in_mbps']
