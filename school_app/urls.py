from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('contactUs/', views.contactus, name='contactus'),
    path('login/admin/', views.adminLogin, name='adminLogin'),
    path('login/parent/', views.parentLogin, name='parentLogin'),
    path('parent/track/', views.parentTrack, name='parentTrack'),
    path('logout/', views.log_out, name="logout"),
    path('adddriver/', views.addDriver, name='addDriver'),
    path('addstudent/', views.addStudent, name='addStudent'),
    path('adminPage/', views.admin, name='adminPage'),
]