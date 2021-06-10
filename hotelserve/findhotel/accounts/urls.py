from django.urls import path
from .import views

app_name = 'accounts'

urlpatterns = [
    path('edithotel/<int:id>', views.edit_hotel, name='edithotel'),
    path('register', views.register, name='register'),
    path('signin', views.sign_in, name='signin'),
    path('signout', views.signout, name='signout'),
    path('editprofile', views.edit_profile, name='editprofile'),
    path('addhotel', views.add_hotel, name='addhotel'),


]