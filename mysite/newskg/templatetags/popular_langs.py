from django import template
from newskg.models import Newskg, Tag
from django.db.models import Count, F
from django.core.cache import cache

register=template.Library()

@register.inclusion_tag('newskg/list_popularity.html')
def get_popular (count=5):
    langs = Newskg.objects.order_by ('-browsing') [:count]
    return {'langs': langs}

@register.inclusion_tag('newskg/list_tags.html')
def get_tags ():
    tags = Tag.objects.all ()
    return {'tags': tags}