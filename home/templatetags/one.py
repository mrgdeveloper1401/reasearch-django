from django import template
from django.template.defaultfilters import stringfilter




register = template.Library()

@register.filter(name='text_up')
@stringfilter
def up(value):
    return value.upper()