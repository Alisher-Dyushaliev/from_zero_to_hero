from django import template
from newskg.models import Purpose
from django.db.models import Count, F
from django.core.cache import cache

register=template.Library()

@register.simple_tag(name='get_list_purposes')
def get_purposes ():
    return Purpose.objects.all ()

@register.inclusion_tag('newskg/list_purposes.html')
def show_purposes (arg_1="Language's", arg_2="Purposes"):
    # purposes = cache.get ('purposes')
    # if not purposes:
        # purposes = Purpose.objects.annotate(ct=Count('get_langs', filter=F('get_langs__is_published'))).filter(ct__gt=0)
        # cache.set ('purposes', purposes, 30)
        # cache.get_or_set ('purposes', Purpose.objects.annotate(ct=Count('get_langs', filter=F('get_langs__is_published'))).filter(ct__gt=0), 30)
    # purposes = Purpose.objects.all ()
    # purposes = Purpose.objects.annotate (ct = Count ('get_langs')).filter (ct__gt = 0)
    purposes = Purpose.objects.annotate(ct=Count('get_langs', filter=F('get_langs__is_published'))).filter(ct__gt=0)
    return { 'purposes': purposes, 'arg_1': arg_1, 'arg_2': arg_2 }