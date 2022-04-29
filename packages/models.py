from django.db import models

class Package(models.Model):
    bandwidth_unit_choices = (
        ('Mbps', 'Mbps'),
        ('Gbps', 'Gbps')
    )
    name = models.CharField(max_length=10)
    bandwidth_quantity = models.IntegerField()
    bandwidth_unit = models.CharField(choices=bandwidth_unit_choices, max_length=4)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def get_bandwidth(self):
        return '{} {}'.format(self.bandwidth_quantity, self.bandwidth_unit)
