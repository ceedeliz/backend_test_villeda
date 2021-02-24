from django.db import models
from model_utils.models import TimeStampedModel
from uuid import uuid4
from applications.menu.models import Menu

class Meal(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    description = models.CharField("Descripcion", max_length = 300)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, to_field="id", verbose_name="Menu", related_name="Menu")

    class Meta:
        verbose_name = "Meal"
        verbose_name_plural = "Meals"
    
    def __unicode__(self):
        return self.id
    
    def __str__(self):
        return self.description
