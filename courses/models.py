from django.db import models
from django.utils.translation import gettext_lazy as _
# from django.contrib.auth.models import User
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.contenttypes.fields import GenericForeignKey



# class Courses(models.Model):
#     title = models.CharField(_('Title'), max_length=100)
#     lenght = models.PositiveIntegerField()
    
#     def __str__(self) -> str:
#         return self.title
    
# class Onepart(models.Model):
#     title = models.CharField(_('Title'), max_length=100)
#     description = models.TextField()
    
#     def __str__(self) -> str:
#         return self.title
    
    
# class Article(models.Model):
#     title = models.CharField(_('Title'), max_length=100)
#     body = models.TextField()
    
#     def __str__(self):
#         return self.title
        
    
# class Comment(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
#     body = models.TextField()
#     article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='articles')
    
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_objects = GenericForeignKey('content_type', 'object_id')