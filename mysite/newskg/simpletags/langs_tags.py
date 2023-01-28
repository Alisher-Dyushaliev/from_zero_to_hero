from django import template
from newskg.models import Purpose

register = template.Library ()

@register.simple_tag ()
def get_purposes ():
    return Purpose.objects.all ()