from django.db import models
from model_utils.models import TimeStampedModel
from uuid import uuid4

# Create your models here.
class Menu(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField("Menu", max_length = 1000)
    description = models.TextField("Descripción")
    day = models.DateField("Dia")

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"
    
    def __unicode__(self):
        return self.id
    
    def __str__(self):
        return self.name
