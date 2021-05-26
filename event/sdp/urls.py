from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from .import views

urlpatterns = [
    path('',views.index, name='index'),
    path('home/',views.home, name='home'),
    path('home/update',views.update, name='update'),
    path('home/updateuser',views.updateuser, name='updateuser'),
    path('home/birthday',views.birthday, name='birthday'),
    path('home/payment',views.payment, name='payment'),
    path('home/college',views.college, name='college'),
    path('home/marriage',views.marriage, name='marriage'),
    path('home/bussiness',views.bussiness, name='bussiness'),
    path('home/public_events/payment/successfull',views.successfull, name='successfull'),
    path('home/public_events/payment',views.payment, name='payment'),
    path('home/public_events/payment/index',views.home, name='home'),
    path('ticket/',views.ticket, name='ticket'),
    path('home/public_events/ticket',views.ticket, name='ticket'),
    path('home/public_events/ticket1',views.ticket1, name='ticket1'),
    path('home/payment',views.payment, name='payment'),
    path('home/payment/events',views.events, name='events'),
    path('home/payment/successfull/',views.successfull, name='successfull'),
    path('home/payment/successfull/events',views.events, name='events'),
    path('home/payment/successfull/index',views.home, name='index'),
    path('home/public_events/payment/events',views.events, name='events'),
    path('home/public_events/payment/aboutus',views.aboutus, name='aboutus'),
    path('home/public_events/payment/gallery',views.gallery, name='gallery'),
    path('home/booking',views.booking, name='booking'),
    path('home/aboutus',views.aboutus, name='aboutus'),
    path('home/gallery',views.gallery, name='gallery'),
    path('home/events',views.events, name='events'),
    path('gallery/',views.gallery, name='gallery'),
    path('payment/',views.payment, name='payment'),
    path('booking/payment/successfull',views.successfull, name='successfull'),
    path('events/',views.events, name='events'),
    path('home/public_events/',views.public_events, name='public_events'),
    path('events/booking',views.booking, name='booking'),
    path('aboutus/',views.aboutus, name='aboutus'),
    path('booking/',views.booking, name='booking'),
    path('booking/payment',views.payment, name='payment'),
    path('events/payment/',views.payment, name='payment'),
    path('full-width/',views.fullwidth, name='full-width'),
    path('sidebar-left/',views.sidebarleft, name='sidebar-left'),
    path('sidebar-right/',views.sidebarright, name='sidebar-right'),
    path('login/',views.login, name='login'),
    path('signup/',views.signup, name='signup'),
    path('signup/register',views.register, name='register'),
    path('signup/signup',views.signup, name='signup'),
    path('login/login',views.login, name='login'),
    path('basic-grid/',views.basicgrid, name='basic-grid')

]

urlpatterns += staticfiles_urlpatterns()