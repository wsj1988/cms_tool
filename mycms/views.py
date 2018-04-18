# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import Q
from models import Story, Category

# Create your views here.
class StoryList(ListView):
    model = Story
    template_name = 'mycms/story_list.html'

    
class StoryDetail(DetailView):
    model = Story
    template_name = 'mycms/story_detail.html'


def category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    story_list = Story.objects.filter(category=category)
    heading = 'Category: %s' % category.label
    return render(request, 'mycms/story_list.html', locals())

def search(request):
    if 'q' in request.GET:
        term = request.GET['q']
        story_list = Story.objects.filter(Q(title__contains=term)|Q(markdown_content__contains=term))
        heading = 'Search results'
    return render(request, 'mycms/story_list.html', locals())
