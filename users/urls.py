from django.urls import path
from .import views

urlpatterns = [
    path('login', views.login,name= 'login'),
    path('index', views.index,name= 'index'),
    path('home', views.home,name= 'home'),
    path('register', views.register,name= 'register'),
    path('booking', views.booking,name ='booking'),
    path('logout', views.logout,name ='logout'),
    path('booking_detail', views.booking_detail,name ='booking_detail'),
    path('cancel_booking/<int:id>', views.cancel_booking,name ='cancel_booking'),
    
]