from django.db import models
from django.db.models.query import QuerySet


class PersionAbove(models.Manager):
    def above(self):
        return self.filter(age__gt=18)
    
    # def get_queryset(self) -> QuerySet:
    #     return super().get_queryset().filter(age__gt=18)