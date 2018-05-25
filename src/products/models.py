# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db.models.signals import pre_save

from django.db import models
from django.db.models import Q
from ecommerce.utils import unique_slug_generator


# Create your models here.
class ProductQuerySet(models.query.QuerySet):
	def featured(self):
		return self.filter(featured=True)


class ProductManager(models.Manager):
	def get_queryset(self):
		return ProductQuerySet(self.model, using=self._db)

	def featured(self):
		return self.get_queryset().filter(featured=True)

	def pen(self):
		return self.get_queryset().filter(categories="Pen")
			


class Product(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(null=True, blank=True, unique=True)
	price = models.PositiveIntegerField()
	no_of_stock = models.PositiveIntegerField()
	description = models.TextField(blank=True, max_length=500)
	categories = models.ManyToManyField('Category', blank=True)
	image = models.ImageField(upload_to="products/", blank=True, null=True )
	featured = models.BooleanField(default=False)

	objects = ProductManager()
	

	def get_absolute_url(self):
		return "/products/{slug}/".format(slug=self.slug)


	def __str__(self):
		return self.name


class Category(models.Model):
	name = models.CharField(max_length=100, primary_key=True)
	slug = models.SlugField(null=True, blank=True, unique=True)


	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return "/{slug}/".format(slug=self.slug)	





def product_pre_save_receiver(sender, instance, *args, **kwargs):		
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver, sender=Product)


def category_pre_save_receiver(sender, instance, *args, **kwargs):		
	if not instance.slug:
		instance.slug = unique_slug_generator(instance)

pre_save.connect(category_pre_save_receiver, sender=Category)
				