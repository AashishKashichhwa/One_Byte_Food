from django.contrib import admin
from django.urls import path, include
from OneByteFood import views
from authentication import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),  # Homepage
    path('reservation/', views.reservation, name='reservation'),  # Homepage
    path('about/', views.about, name='about'),  # About page
    path('services/', views.services, name='services'),  # Services page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('signup/', auth_views.signup, name='signup'),
    path('signup', auth_views.signup, name='signup'),
    path('signin/', auth_views.signin, name='signin'),
    path('signin', auth_views.signin, name='signin'),
    path('authentication/signin', auth_views.signin, name='signin'),
    path('authentication/signin/', auth_views.signin, name='signin'),
    path('activate/<uidb64>/<token>/', auth_views.activate, name='activate'),
    path('signout/', auth_views.signout, name='signout'),
    path('admin_dashboard/', auth_views.admin_dashboard, name='admin_dashboard'),
    path('user_dashboard/', auth_views.user_dashboard, name='user_dashboard'),
]
