from django.db import models

# Create your models here.

from django.db import models


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    jersey = models.IntegerField()
    position = models.CharField(max_length=100, blank=True)
    parents = models.CharField(max_length=100, blank=True)
    school = models.CharField(max_length=100, blank=True)
    # headshot = models.ImageField(upload_to="headshots/", blank=True)  # no default yet
    headshot = models.ImageField(null=True, blank=True, default='no_user.svg')

    def __str__(self):
          return self.first_name + ' # ' + str(self.jersey)


class Coach(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True)
    role = models.CharField(max_length=100)

    def __str__(self):
          return self.first_name


# null=True sets NULL (versus NOT NULL) on the column in your DB. Blank values for Django field types such as DateTimeField
# or ForeignKey will be stored as NULL in the DB.

# blank determines whether the field will be required in forms. This includes the admin and your custom forms.
# If blank=True then the field will not be required, whereas if it's False the field cannot be blank.

# The combo of the two is so frequent because typically if you're going to allow a field to be blank in your form,
# you're going to also need your database to allow NULL values for that field. The exception is CharFields and TextFields,
# which in Django are never saved as NULL. Blank values are stored in the DB as an empty string ('').
