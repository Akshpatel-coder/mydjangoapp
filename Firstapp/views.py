from urllib import request

from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
from . models import Student
import random
# Create your views here.

def contactpageview(request):
    return render(request, 'contact.html')

def addstudentform(request):
    return render(request, 'add-student.html')

def addstudentformprocess(request):
    txt1 = request.POST['txt1']
    txt2 = request.POST['txt2']
    txt3 = request.POST['txt3']
    txt4 = request.POST['txt4']
    Student.objects.create(name=txt1, mobile=txt2, email=txt3, address=txt4)
    return HttpResponse("Thank you")
def mailsendprocess(request):
    subject = request.POST['txt2']
    message = request.POST['txt3']
    recipient_list = [request.POST['txt1'],]
    email_from = settings.EMAIL_HOST_USER
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Mail Sent")


def homepage(request):
    return render(request,"home.html")

def mailsenddemo(request):
    subject = 'Django Mail Demo'    
    message = ' Hello How are you ?'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['akash.padhiyar123@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponse("Mail Sent")

def aboutpage(request):
    return render(request,"about.html")
def shop(request):
    return render(request,"shop.html")
def shoppage(request):
    return render(request,"shop.html")
def contactpage(request):
    return render(request,"contact.html")
def saveSessionData(request):
    request.session['username'] = "Aksh"
    return HttpResponse("Session created")
 
def getSessionData(request):
    if request.session.has_key('username'):
       msg = request.session['username']
       return HttpResponse(msg)
    else:
       return HttpResponse("Session Variable not Present")
    
def deleteSessionData(request):
    del request.session['username']
    return HttpResponse("Session Removed")

def getSessionData2(request):
    msg = request.session.get('Username', 'No username')
    return HttpResponse(msg)

def contactprocess(request):
    if request.method != 'POST':
        return render(request, 'contact.html')

    try:
        a = int(request.POST.get('txt1', '0'))
        b = int(request.POST.get('txt2', '0'))
    except ValueError:
        return HttpResponse("Please enter valid numbers for No1 and No2.")

    c = a + b
    d = f"Addition of {a} and {b} is {c}"
    return render(request, 'ans.html', {'mya': a, 'myb': b, 'myc': c, 'myd': d})


def contactpageprocess(request):
    txt1 = request.POST.get('txt1', '').strip()
    txt2 = request.POST.get('txt2', '').strip()
    txt3 = request.POST.get('txt3', '').strip()

    if not txt1 or not txt2 or not txt3:
        return HttpResponse("Please fill in all fields before submitting the contact form.")

    mymsg = f"Hello has Contact you {txt1} Mobile No is {txt2} Message is {txt3}"
    subject = 'Contact us From Website'
    email_from = settings.EMAIL_HOST_USER or 'no-reply@example.com'
    recipient_list = ['akash.padhiyar@gmail.com']
    send_mail(subject, mymsg, email_from, recipient_list)
    return HttpResponse("Thank you for Contacting us.")

def loginpage(request):
    return render(request, 'login.html')

def loginprocess(request):
    txt1 = request.POST['email']
    request.session['myemail'] = txt1
    return redirect(dashboard)

def dashboard(request):
    if request.session.has_key('myemail'):
        return render(request, "dashboard.html")
    else:
        return redirect(loginpage)

def logout(request):
    del request.session['myemail']
    return redirect(loginpage)

def displayStudent(request):
    mydata = Student.objects.all()
    return render(request, 'display-student.html', {'mydata': mydata})


def deleteStudent(request, id):
    Student.objects.filter(id=id).delete()
    return redirect(displayStudent)
