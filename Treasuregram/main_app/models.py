# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)

class Treasure(models.Model):
	name = models.CharField(max_length=100)
	value = models.DecimalField(max_digits=10,decimal_places=2)
	material = models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	image = models.ImageField(upload_to=upload_location)
	slug = models.SlugField(unique=True)

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("main_app:detail", kwargs={"slug": self.slug})

	

def create_slug(instance, new_slug=None):
	slug = slugify(instance.name)
	if new_slug is not None:
		slug = new_slug
	qs = Treasure.objects.filter(slug=slug).order_by("-id")
	exists = qs.exists()
	if exists:
		new_slug = "%s-%s" %(slug, qs.first().id)
		return create_slug(instance, new_slug=new_slug)
	return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
	if not instance.slug:
		instance.slug = create_slug(instance)