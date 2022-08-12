from django.db import models


class Shirt(models.Model):
    """
    Puppy Model
    Defines the attributes of a clothe
    """
    name = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_type(self):
        return self.name + ' is a ' + self.type + '.'

    def __repr__(self):
        return self.name + ' is added.'
