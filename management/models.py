import uuid
from django.db import models
from django.utils import timezone



class UUIDPrimaryKey(models.Model):
    """
    An abstract base class model that provides
    primary key id as uuid.
    """
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class Client(UUIDPrimaryKey):
    """
    Model that represents the clients
    """
    name = models.CharField(max_length=80)
    rut = models.CharField(
        'RUT',
        max_length=20,
        blank=True,
        null=True,
    )
    address = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )
    phone = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    email = models.EmailField(
        blank=True,
        null=True,
    )
    n_of_companions = models.PositiveIntegerField(
       default=0,
    )

    def __str__(self):
        return self.name


class  Room(UUIDPrimaryKey):
    name = models.CharField(max_length=80)
    capacity = models.PositiveIntegerField(
       blank=True,
       null=True,
    )
    status = models.CharField(max_length=80)


class Booking(UUIDPrimaryKey):
    """
    Model that represents the employees in the slack workspace
    """
    client = models.ForeignKey(
        Client,
        on_delete=models.CASCADE,
        related_name='bookings',
    )

    room = models.ForeignKey(
        Room,
        on_delete=models.CASCADE,
        related_name='bookings',
        blank=True,
        null=True,
    )
    payment_method =  models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    source = models.CharField(
        max_length=30,
        blank=True,
        null=True,
    )
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

