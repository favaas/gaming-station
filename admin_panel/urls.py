from django.urls import path
from .import views

urlpatterns = [

    path('customers', views.customers,name= 'customers'),
    path('dashboard', views.dashboard,name= 'dashboard'),
    path('feedbacks', views.feedbacks,name= 'feedbacks'),
    path('login', views.login,name= 'login'),
    path('messages', views.messages,name= 'messages'),
    path('pending_bookings', views.pending_bookings,name= 'pending_bookings'),
    path('service_history', views.service_history,name= 'service_history'),
    path('total_booking', views.total_booking,name= 'total_booking'),
    path('admin_cancel_booking/<int:id>', views.admin_cancel_booking,name= 'admin_cancel_booking'),
    
]