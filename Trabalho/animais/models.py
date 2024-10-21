from django.db import models

class Animal(models.Model):
 especie = models.CharField(max_length=50)
 raca = models.CharField(max_length=50)
 cor = models.CharField(max_length=50)
 def __str__(self):
  return f"{self.especie} {self.raca} {self.cor}"
 