from django.db import models
from packages.models import Package


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Person(models.Model):
    first_name = models.CharField(max_length=20, verbose_name='Nombre')
    last_name = models.CharField(max_length=20, verbose_name='Apellidos')
    email = models.EmailField(verbose_name='Correo electronico')
    phone_number = models.CharField(max_length=10, verbose_name='Telefono') 

    class Meta:
        abstract = True


class Address(models.Model):
    street_address = models.CharField(max_length=50, verbose_name='Calle y número')
    location = models.CharField(max_length=30, verbose_name='Colonia')
    city = models.CharField(max_length=50, verbose_name='Ciudad')
    zip_code = models.CharField(max_length=5, verbose_name='Codigo Postal')


    def __str__(self):
        return ' '.join([self.street_address,
                        self.city,
                        self.zip_code])

    class Meta:
        verbose_name_plural = "Addresses"


class Quote(TimeStampedModel, Person):
    status_choices = (
        (0, 'Pendient'),
        (1, 'Answered'),
    )
    package = models.ForeignKey(Package, on_delete=models.CASCADE, verbose_name='Paquete')
    status = models.IntegerField(choices=status_choices, default=0)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    def __str__(self):
        return 'Quote #{}'.format(self.pk)