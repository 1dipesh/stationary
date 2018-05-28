# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from billing.models import BillingProfile

# Create your models here.

ADDRESS_TYPES = (
	('billing', 'Billing'),
	('shipping', 'Shipping'),
)

class Address(models.Model):
	billing_profile = models.ForeignKey(BillingProfile)
	address_type 	= models.CharField(max_length=120, choices=ADDRESS_TYPES)
	address_line_1  = models.CharField(max_length=120)
	address_line_2  = models.CharField(max_length=120, null=True, blank=True)
	city  			= models.CharField(max_length=120)

	def __str__(self):
		return str(self.billing_profile)

	def	get_address(self):
		return "{line1},\n{line2},\n{city}".format(
			line1 = self.address_line_1,
			line2 = self.address_line_2,
			city  = self.city,

			)
