from django.db import models
from django.urls import reverse

# Create your models here.

MEALS = (
  ('I', 'Insects'),
  ('C', 'Cactus'),
  ('S', 'Seeds'),
  ('T', 'Trash')
)

class Finch(models.Model):
  name = models.CharField(max_length=100)
  diet = models.CharField(max_length=100)
  beak = models.CharField(max_length=100)
  habitat = models.CharField(max_length=100)
  description = models.TextField(max_length=250)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('finch-detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
  date = models.DateField("Feeding Date")
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  
  class Meta:
    ordering = ['-date']