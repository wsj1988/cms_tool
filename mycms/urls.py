# -*- coding: utf-8 -*-

from django.conf.urls import url
from models import Story
from views import StoryList, StoryDetail, category, search


urlpatterns = [
    url(r'^category/(?P<slug>[-\w]+)/$', category, name='mycms-category'),
    url(r'^search/', search, name='mycms-search'),
    url(r'^(?P<slug>[-\w]+)/$', StoryDetail.as_view(), name='mycms-story'),
    url(r'^$', StoryList.as_view(), name='mycms-home'),
]
