from django.db import models
from model_utils.models import TimeStampedModel
from uuid import uuid4
from applications.meals.models import Meal

class Order(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    user = models.CharField("Usuario", max_length = 1000)
    details = models.TextField("Detalles")
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, to_field="id", verbose_name="Meal", related_name="Meal")

    class Meta:
        verbose_name = "Orden"
        verbose_name_plural = "Ordenes"
    
    def __unicode__(self):
        return self.id
    
    def __str__(self):
        return self.details
