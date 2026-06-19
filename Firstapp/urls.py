

from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('home/', views.homepage),
    path('maildemo/', views.mailsenddemo),
    path('about/', views.aboutpage),
    path('contact/', views.contactpage, name='contact'),
    path('contactprocess/', views.contactpageprocess, name='contactprocess'),
    path('contactcalc/', views.contactprocess, name='contactcalc'),

    path('cake/', views.contactpage),
    path('cake/ahmedabad/', views.contactpage),
    path('cake/rajkot/', views.contactpage),

    path('shop/', views.shoppage),

    path('saveSession/', views.saveSessionData),
    path('getSession/', views.getSessionData),
    path('getSession2/', views.getSessionData2),
    path('removeSession/', views.deleteSessionData),

    path('login/', views.loginpage),
    path('loginprocess/', views.loginprocess),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout),

    path('process/', views.mailsendprocess, name='process'),
    path('contactpageprocess/', views.contactpageprocess),
    path('addstudent', views.addstudentform),
    path('add-student-process/', views.addstudentformprocess),
    path('display-student/', views.displayStudent),
    path('delete-student/<int:id>/', views.deleteStudent),
    path('maildemo', views.mailsenddemo),
]
