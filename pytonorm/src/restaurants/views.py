import random
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView

from .models import RestaurantLocation

# Create your views here.

# Restaurant list view 
# def restaurant_listview(request):
# 	template_name = 'restaurants/restaurant_list.html'
# 	queryset = RestaurantLocation.objects.all()
# 	context = {
# 		"object_list" : queryset
# 	}
# 	return render(request, template_name, context)

#ListView QuerySet
class RestaurantListView(ListView):
	#template_name = 'restaurants/restaurant_list.html'

	def get_queryset(self):
		slug = self.kwargs.get("slug")
		if slug:
			#queryset = RestaurantLocation.objects.filter(category__icontains=slug)
			queryset = RestaurantLocation.objects.filter(
					Q(category__iexact=slug) |
					Q(category__icontains=slug) 
				)
		else:
			queryset = RestaurantLocation.objects.all()
		return queryset 


class RestaurantDetailView(DetailView):
	queryset = RestaurantLocation.objects.all()
	
	def get_context_data(self, *args, **kwargs):
		print(self.kwargs)
		context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
		print(context)
		return context


# class SearchRestaurantListView(ListView):
# 	template_name = 'restaurants/restaurant_list.html'

# 	def get_queryset(self):
# 		print(self.kwargs)
# 		slug = self.kwargs.get("slug")
# 		if slug:
# 			#queryset = RestaurantLocation.objects.filter(category__icontains=slug)
# 			queryset = RestaurantLocation.objects.filter(
# 					Q(category__iexact=slug) |
# 					Q(category__icontains=slug) 
# 				)
# 		else:
# 			queryset = RestaurantLocation.objects.none()
# 		return queryset 

# class NewariRestaurantListView(ListView):
# 	queryset = RestaurantLocation.objects.filter(category__icontains='Newari')
# 	#queryset = RestaurantLocation.objects.filter(category__iexact='Newari')
# 	template_name = 'restaurants/restaurant_list.html'

# class BakeryRestaurantListView(ListView):
# 	queryset = RestaurantLocation.objects.filter(category__icontains='Bakery')
# 	template_name = 'restaurants/restaurant_list.html'

# Template Based Views
class HomeView(TemplateView):
	template_name = "home.html"

	def get_context_data(self, *args, **kwargs):
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		num = random.randint(0,100000)
		some_list = [num, random.randint(0,100000), random.randint(0,100000), random.randint(0,100000)]
		context = {
					}
		#print(context)
		return context

class ContactView(TemplateView):
	template_name = "contact.html"

class AboutView(TemplateView):
	template_name = "about.html"


# Function based view
# def home(request):
# 	#html_var = 'f strings'
# 	num = random.randint(0,100000)
# 	some_list = [num, random.randint(0,100000), random.randint(0,100000), random.randint(0,100000)]
# 	context = {
# 				"html_var":"context variable", 
# 				"boolean_value" : True, 
# 				"result":"You can pass!", 
# 				"num":num,
# 				"some_list":some_list
# 				}

	#return a response
	#return HttpResponse("hello")
	#return render(request, "template", {context for the template in terms of a dictionary})

	#return render(request, "base.html", {"html_var":"context variable", "boolean_value" : True, "result":"You can pass!", "num":num}) 

# 	return render(request, "home.html", context) 

# def about(request):
# 	context = {
# 			}
# 	return render(request, "about.html", context) 

# def contact(request):
# 	context = {
# 			}
# 	return render(request, "contact.html", context) 

# Class Based Views
# class ContactView(View):
# 	def get(self, request, *args, **kwargs):
# 		context = {}
# 		return render(request, "contact.html", context)

	# def post(self, request, *args, **kwargs):
	# 	context = {}
	# 	return render(request, "contact.html", context)
	
	# def put(self, request, *args, **kwargs):
	# 	context = {}
	# 	return render(request, "contact.html", context)



		
