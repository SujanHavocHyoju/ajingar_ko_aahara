"""pytonorm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic.base import TemplateView

from restaurants.views import(
	HomeView, 
	AboutView, 
	ContactView,
	RestaurantListView,
	#NewariRestaurantListView,
	#BakeryRestaurantListView,
	#SearchRestaurantListView,
	RestaurantDetailView,
	)

#from restaurants.views import home, about, contact, ContactView

#from restaurants.views import HomeView, AboutView, ContactView, restaurant_listview

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', home),
    url(r'^$', HomeView.as_view()),
    #url(r'^$', TemplateView.as_view(template_name='home.html')),
    #url(r'^about/$', about),
    url(r'^about/$', AboutView.as_view()),
    #url(r'^about/$', TemplateView.as_view(template_name='about.html')),  //Use only If you do not have any contexxt to show
    #url(r'^contact/$', contact),
    url(r'^contact/$', ContactView.as_view()),
    #url(r'^contact/$', TemplateView.as_view(template_name='contact.html')),  //Use only If you do not have any contexxt to show
    #url(r'^contact/(?P<id>\d+)/$', ContactView.as_view()),
    url(r'^restaurants/$', RestaurantListView.as_view()),
    #url(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    #url(r'^restaurants/(?P<pk>\w+)/$', RestaurantDetailView.as_view()),
    #url(r'^restaurants/(?P<rest_id>\w+)/$', RestaurantDetailView.as_view()),
    url(r'^restaurants/(?P<slug>[\w-]+)/$', RestaurantDetailView.as_view()),
    #url(r'^restaurants/bakery/$', BakeryRestaurantListView.as_view()),
    #url(r'^restaurants/newari/$', NewariRestaurantListView.as_view())
    #url(r'^restaurants/(?P<slug>\w+)/$', SearchRestaurantListView.as_view()),
]
