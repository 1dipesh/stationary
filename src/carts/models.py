# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db.models.signals import pre_save, post_save, m2m_changed

from products.models import Product

from django.db import models

# Create your models here.


User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
	def new_or_get(self,request):
		cart_id = request.session.get("cart_id",None)
		qs = self.get_queryset().filter(id=cart_id)
		if qs.count() == 1:
			new_obj = False
			# print('cart id exists')
			cart_obj = qs.first()
			if request.user.is_authenticated() and cart_obj.user is None:
				cart_obj.user = request.user
				cart_obj.save()

		else:
			cart_obj = Cart.objects.new(user=request.user)
			new_obj = True
			request.session['cart_id']	= cart_obj.id
		return cart_obj, new_obj

	def new(self, user=None):
		user_obj = None
		if user is not None:
			if user.is_authenticated():
				user_obj = user
		return self.model.objects.create(user=user_obj)

class Cart(models.Model):
	user 		= models.ForeignKey(User, null=True, blank=True)
	products 	= models.ManyToManyField(Product)
	total 		= models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
	updated 	= models.DateTimeField(auto_now=True)
	timestamp 	= models.DateTimeField(auto_now_add=True)

	objects = CartManager()

	def __str__(self):
		return str(self.id)


 

def pre_save_cart_receiver(sender, instance, action, *args, **kwargs):
	if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
		products = instance.products.all()
		total = 0
		for x in products:
			total += x.price
		instance.total = total
		instance.save()

m2m_changed.connect(pre_save_cart_receiver, sender=Cart.products.through)



class CartItem(models.Model):
	cart 		= models.ForeignKey("Cart")
	products 	= models.ForeignKey(Product)
	quantity 	= models.PositiveIntegerField(default=1)

	def __str__(self):
		return self.products.name

	@property
	def item_name(self):
		return self.products.get_title()

	def remove(self):
		return self.products.remove_from_cart()

	@property	
	def item_total(self):
		return self.products.get_price() * self.quantity	
	