# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
import datetime
from markdown import markdown


VIEWABLE_STATUS = [3, 4]

class ViewableManager(models.Manager):
    def get_query_set(self):
	default_queryset = super(ViewableManager, self).get_query_set()
	return default_queryset.filter(status__in=VIEWABLE_STATUS)


# Create your models here.
class Category(models.Model):
    label = models.CharField(blank=True, max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.label

    @models.permalink
    def get_absolute_url(self):
        return ('category', (), {'slug': self.slug})


class Story(models.Model):
    STATUS_CHOICES = (
        (1, 'Needs Edit'),
        (2, 'Needs Approval'),
        (3, 'Published'),
        (4, 'Archived'),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ForeignKey(Category)
    markdown_content = models.TextField()
    html_content = models.TextField(editable=False)
    owner = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ('modified', )
        verbose_name_plural = 'stories'

    def save(self):
        self.html_content = markdown(self.markdown_content)
        self.modified = datetime.datetime.now()
        super(Story, self).save()

    admin_objects = models.Manager()
    objects = ViewableManager()

    @models.permalink
    def get_absolute_url(self):
        return ('mycms-story', (), {'slug': self.slug})
