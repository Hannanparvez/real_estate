from django.urls import path 
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('agents/',views.agents,name='agents'),
    path('search',views.search,name='search'),
    path('contact',views.contact,name='contact'),

]