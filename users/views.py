from django.shortcuts import render,redirect
from users.models import Users,Bookings

# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']  
        try:
            user = Users.objects.get(email=username,password=password)
            # if user.email == username and user.password == password:
            request.session['userId'] = user.id
            print(request.session['userId'])
            return redirect('home')

        except Exception as e:
            print(e)
            return render(request,'users/login.html',{'message':'Invalid Email or Password'})
    return render(request,'users/login.html')

def logout(request):
    del request.session['userId']
    return redirect('login')

def index(request):
    return render(request,'users/index.html')


def home(request):
    return render(request,'users/home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        userobj = Users(name=name, email=email, phone=phone, password=password)
        userobj.save()
    return render(request,'users/register.html')


def booking(request):
    if request.method == 'POST':
        date = request.POST['date']
        time = request.POST['time']
        userid = request.session['userId']
        userobj = Bookings(date=date, time=time, userid_id = userid)
        userobj.save()
    return render(request,'users/booking.html')    

    

def booking_detail(request):
    print(request.session['userId'])
    bookingObj = Bookings.objects.filter(userid=request.session['userId'])
    return render(request,'users/booking_detail.html',{'data':bookingObj})

def cancel_booking(request,id=0):
    Bookings.objects.get(id=id).delete()
    return redirect('booking_detail')