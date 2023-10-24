from django import template
from home.models import Car

register = template.Library()

@register.simple_tag
def cars():
    return Car.objects.all()