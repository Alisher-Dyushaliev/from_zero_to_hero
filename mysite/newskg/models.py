from django.db import models
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey


class Newskg (models.Model):
    title = models.CharField (max_length=150, verbose_name= 'Language')
    content = models.TextField (verbose_name= 'Framework')
    info = models.TextField (blank=True, verbose_name='Information')
    created_at = models.DateTimeField (auto_now_add=True)
    updated_at = models.DateTimeField (auto_now=True)
    photo = models.ImageField (upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField (default=True)
    purpose = models.ForeignKey ('Purpose', on_delete=models.PROTECT, null=True, related_name='get_langs')
    browsing = models.IntegerField (default=0)
    tags = models.ManyToManyField ('Tag', blank=True, related_name='get_langs')

    def get_absolute_url (self):
        return reverse ('framework', kwargs={ 'pk': self.pk })

    def __str__(self):
        return self.title + ' & ' + self.content

    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'
        ordering = ['created_at']


class Purpose (models.Model):
    title = models.CharField (max_length=150, db_index=True)

    def get_absolute_url (self):
        return reverse ('purpose', kwargs={ 'purpose_id': self.pk })

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Purpose'
        verbose_name_plural = 'Purposes'
        ordering = ['id']


class Tag (models.Model):
    title = models.CharField (max_length=100)
    slug = models.SlugField (max_length=100, verbose_name='Url', unique=True)

    def get_absolute_url (self):
        return reverse ('tag', kwargs={ 'slug': self.slug })

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Tree (MPTTModel):
    name = models.CharField (max_length=50, unique=True)
    parent = TreeForeignKey ('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def get_absolute_url (self):
        return reverse ('tree', kwargs={ 'pk': self.pk })

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']


class Store (models.Model):
    name = models.CharField (max_length=50)
    sequence = TreeForeignKey (Tree, on_delete=models.PROTECT)

    def __str__(self):
        return self.name