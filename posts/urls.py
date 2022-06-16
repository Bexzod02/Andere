from django.urls import path
from .views import hom_view, fash_view,travel_view,about_view,single_view
app_name='posts'    # {% url 'app_name:urlname' %}

urlpatterns = [
    path('', hom_view, name = 'home'),
    path('single/<slug:slug>/', single_view, name='single'),
    path('fashion/', fash_view, name='fashion'),
    path('travel/', travel_view, name='travel'),
    path('about/', about_view, name='about'),
]