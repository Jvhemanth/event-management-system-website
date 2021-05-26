from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def index(request):
    return render(request, 'index.html')

def update(request):
    return render(request, 'update.html')

def updateuser():
	uid=1
	password="hari123"
	db_cursor = mysql.connection.cursor()
	flag=db_cursor.execute("UPDATE registration set password=%s where id=%s",(password,uid,))
	mysql.connection.commit()
	if flag:
		return "Updation done successfully"
	else:
		return "ID not found"

def gallery(request):
    return render(request, 'gallery.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def birthday(request):
    return render(request, 'birthday.html')
def college(request):
    return render(request, 'college.html')
def bussiness(request):
    return render(request, 'bussiness.html')
def marriage(request):
    return render(request, 'marriage.html')


def events(request):
    return render(request, 'events.html')

def fullwidth(request):
    return render(request, 'full-width.html')

def sidebarleft(request):
    return render(request, 'sidebar-left.html')

def sidebarright(request):
    return render(request, 'sidebar-right.html')

def basicgrid(request):
    return render(request, 'basic-grid.html')

def payment(request):
    return render(request, 'payment.html')

def booking(request):
    return render(request, 'booking.html')
def successfull(request):
    return render(request, 'successfull.html')
def home(request):
    return render(request, 'home.html')
def ticket(request):
    return render(request, 'ticket.html')
def ticket1(request):
    return render(request, 'ticket1.html')
def public_events(request):
    return render(request, 'public_events.html')

def login(request):
    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("home")
        else:
            messages.info(request,'invalid credentials')
            return redirect('signup')

    else:
        return render(request,'login.html')   

def signup(request):
    return render(request, 'signup.html')

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('signup')
            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                
                user.save();
                print('user created')
                return redirect('home')

        else:
            messages.info(request,'password not matching..')    
            return redirect('signup')
        return redirect('/')
        


def register1(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    username = request.POST.get('username')
    password1 = request.POST.get('password1')
    password2 = request.POST.get('password2')
    
    if password1==password2:
        if User.objects.filter(username=username).exists():
            messages.info(request,'username Taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email Taken')
            return redirect('register')
        else:
            user = User(username=username,password=password1 , email=email , first_name=first_name , last_name=last_name)
            user.save();
            print("User created")
    else:
        print("password not matching..")
        return redirect('register')
    return render(request, 'index.html')

