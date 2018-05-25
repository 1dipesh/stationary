# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, Http404
from django.views.generic import ListView, DetailView, TemplateView
from .models import Product, Category
from carts.models import Cart


# Create your views here.

class ProductListView(ListView):
	template_name = "products/list.html"
	queryset = Product.objects.all()

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context


class ProductDetailView(DetailView):
	template_name = "products/detail.html"
	queryset = Product.objects.all()

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context


class ProductDetailSlugView(DetailView):
	template_name = "products/detail.html"
	queryset = Product.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super(ProductDetailSlugView, self).get_context_data(*args, **kwargs)
		cart_obj, new_obj = Cart.objects.new_or_get(self.request)
		context['cart'] = cart_obj
		return context



class ProductFeaturedListView(ListView):
	template_name = "home_page.html"

	def get(self, *args, **kwargs):
		request = self.request
		featured = Product.objects.featured()
		return render (request, self.template_name, {'featured':featured})

class ProductFeaturedDetailView(DetailView):
	template_name = "products/featured-detail.html"
	queryset = Product.objects.all()

	

	
class CategoryListView(ListView):
	template_name = "home_page.html"

	def get(self, request):
		request = self.request
		category = Category.objects.all()
		return render(request, self.template_name,{'category':category})

	# def get_context_data(self, *args, **kwargs):
	# 	context = super(CategoryListView, self).get_context_data(*args, **kwargs)
	# 	print(context)
	# 	return context


class CategoryListSlugView(ListView):
	template_name = "home_page.html"
	queryset = Category.objects.all()



class PenListView(ListView):
	template_name = "products/pen.html"

	def get(self, *args, **kwargs):
		request = self.request
		pen = Product.objects.pen()
		return render(request, self.template_name, {'pen':pen})





	