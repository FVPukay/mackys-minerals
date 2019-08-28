from django.db import models
from django.db.models.functions import Lower


class Mineral(models.Model):
    name = models.CharField(max_length=255, unique=True)
    image_filename = models.CharField(max_length=255, unique=True)
    image_caption = models.CharField(max_length=500)
    category = models.CharField(max_length=500)
    group = models.CharField(max_length=500)

    formula = models.CharField(max_length=500, default='', blank=True)
    strunz_classification = models.CharField(
        max_length=500, default='', blank=True
    )
    crystal_system = models.CharField(max_length=500, default='', blank=True)
    unit_cell = models.CharField(max_length=500, default='', blank=True)
    color = models.CharField(max_length=500, default='', blank=True)
    crystal_symmetry = models.CharField(max_length=500, default='', blank=True)
    cleavage = models.CharField(max_length=500, default='', blank=True)
    mohs_scale_hardness = models.CharField(
        max_length=500, default='', blank=True
    )
    luster = models.CharField(max_length=500, default='', blank=True)
    streak = models.CharField(max_length=500, default='', blank=True)
    diaphaneity = models.CharField(max_length=500, default='', blank=True)
    optical_properties = models.CharField(
        max_length=500, default='', blank=True
    )
    refractive_index = models.CharField(max_length=500, default='', blank=True)
    crystal_habit = models.CharField(max_length=500, default='', blank=True)
    specific_gravity = models.CharField(max_length=500, default='', blank=True)

    class Meta:
        indexes = [models.Index(fields=['name'])]
        ordering = [Lower("name")]

    def __str__(self):
        return f"{self.name}"
