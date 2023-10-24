from django.db import models
from .managers import PersionAbove
from django.utils.translation import gettext_lazy as _



# class Car(models.Model):
#     name = models.CharField(max_length=100)
#     owner = models.CharField(max_length=100)
#     year = models.PositiveSmallIntegerField()
#     slug = models.SlugField()
#     created_at = models.DateTimeField(_('created car'), auto_now_add=True)
    
    
#     def __str__(self):
#         return self.name
    
    
# class Authore(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     print_year = models.PositiveSmallIntegerField(null=True)
    
#     def __str__(self) -> str:
#         return self.first_name + ' ' + self.last_name
    
    
# class Book(models.Model):
#     title = models.CharField(max_length=100)
#     authore = models.ManyToManyField(Authore, related_name='books')
    
#     def __str__(self):
#         return self.title
    
    
    
class Person(models.Model):
    full_name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField()
    bio = models.CharField(max_length=255)
    create_person = models.DateTimeField(auto_now_add=True)
    
    objects = PersionAbove()
    
    def __str__(self):
        return f'{self.full_name} - {self.age}'
    
    # def is_above(self):
    #     if self.age > 18:
    #         return True
    #     return False
    
    
    
# class Todo(models.Model):
#     title = models.CharField(max_length=100)
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
    
#     def str(self):
#         return self.title