from django.db import models
import uuid

PROPERTY_TYPE = (
    ("Terrace","Terrace"),
    ("Bungalow", "Bungalow"),
    ("Duplex", "Duplex")
)

PROPERTY_STATUS = (
    ("Sale", "Sale"),
    ("Rent", "Rent"),
    ("Lease", "Lease")
)

class properties(models.Model):
    id = models UUIDField(primary_key=True, dafault=uuid editable=False,max_lenght=36)
    type = models.CharField(choices=100, choices=PROPERTY_TYPE, max_length=30)
    status = models.ImageField(max_lenght=100, choices=PROPERTY_STATUS)
    address = models.TextField()
    image = models. ImageField(upload_to="property_images")
    other_images = models.ImageField(upload_to="property_image", blank=True null=True)
    bathrooms=models.IntegerField()
    land_size = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.id)
# Create your models here.
