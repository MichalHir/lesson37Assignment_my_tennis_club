from django.db import models

from courts.models import Court
import members

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True, blank=True)
  joined_date = models.DateField(null=True, blank=True)
  court = models.ForeignKey('courts.Court', on_delete=models.SET_NULL, related_name='members', null=True, blank=True)

  def __str__(self):
    return f"{self.firstname}-{self.lastname}({self.id})"