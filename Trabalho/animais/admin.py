from django.contrib import admin
from .models import Animal
class AnimalAdmin(admin.ModelAdmin):
    list_display = ("especie","raca")
admin.site.register(Animal,AnimalAdmin)
