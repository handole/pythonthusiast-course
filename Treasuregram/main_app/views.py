# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Treasure

def index(request):
	queryset = Treasure.objects.all()
	context = {
		"object_list": queryset,
		"name": "List"
	}
	return render(request, "index.html", context)

def detail(request, slug=None):
	instance = get_object_or_404(Treasure, slug=slug)
	context = {
		"name": instance.name,
		"instance": instance,
	}
	return render(request, "detail.html", context)