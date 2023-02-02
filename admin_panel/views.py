from django.shortcuts import render,redirect
from users.models import Users,Bookings

# Create your views here.

# def completed_booking(request):
#     bookingObj = Bookings.objects.filter(status='Completed')
#     return render(request,'completed_booking.html',{'data':bookingObj})


def customers(request):
    return render(request,'customers.html')


def dashboard(request):
    return render(request,'dashboard.html')


def feedbacks(request):
    return render(request,'feedbacks.html')


def login(request):
    return render(request,'login.html')


def messages(request):
    return render(request,'messages.html')


def pending_bookings(request):
    bookingObj = Bookings.objects.filter(status='Pending')
    return render(request,'pending_bookings.html',{'data':bookingObj})


def service_history(request):
    return render(request,'service_history.html')


def total_booking(request):
    bookingsObj = Bookings.objects.all()
    return render(request,'total_booking.html',{'data':bookingsObj})


def admin_cancel_booking(request,id=0):
    Bookings.objects.get(id=id).delete()
    return redirect('total_booking')