from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('contact',views.contact, name='contact'),
    path('about',views.about, name='about'),
    path('tours',views.tours, name='tours'),
    path('seemore/<int:id>', views.seemore, name='seemore'),

]