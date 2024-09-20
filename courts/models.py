from datetime import datetime
from django.db import models



class Court(models.Model):
  number = models.PositiveIntegerField(unique=True)
  is_occupied = models.BooleanField(default=False)
  time_of_occupation = models.DateTimeField(null=True, blank=True)
  updated = models.DateTimeField(auto_now=True, null=True)
  created = models.DateTimeField(auto_now_add=True, null=True)
  
  
  def save(self, *args, **kwargs):
    if self.is_occupied:  # Update the time only if the court is occupied
        self.time_of_occupation = datetime.now()
    else:
        self.time_of_occupation = None  # Optionally reset the time when the court is not occupied
    super().save(*args, **kwargs)

  def __str__(self):
    return f"Court:{self.number} is occupied:{self.is_occupied}"