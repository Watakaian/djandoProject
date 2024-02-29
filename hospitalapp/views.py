from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from hospitalapp.models import Member, Appointment,Contact,Users


# Create your views here.
def index(request):
    if request.method == 'POST':
        if request.POST.get('form_type') == 'formOne':
            appoint = Appointment(
                name=request.POST['name'],
                email=request.POST['email'],
                phone=request.POST['phone'],
                date=request.POST['date'],
                department=request.POST['department'],
                doctor=request.POST['doctor'],
                message=request.POST['message'],
            )
            appoint.save()
            messages.info(request, 'Appointment created in back-end')
        elif request.POST.get('form_type') == 'formTwo':
            cont=Contact(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message'],
            )
            cont.save()
            messages.success(request,'Message sent successfully')
        return redirect('/')
    else:
        return render(request,'index.html',)
def inner(request):
    return render(request,'inner-page.html',)
def login(request):
    return render(request,'login.html',)
def register(request):
    if request.method == 'POST':
        member = Member(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
            )
        member.save()
        return redirect('/register')
    else:
        return render(request,'register.html')
def upload(request):
    return render(request,'upload.html',)
def appointments(request):
    myappoint = Appointment.objects.all()
    return render(request,'appointmentDetails.html',{'myappoint': myappoint})
def members(request):
    mymembers = Member.objects.all()
    return render(request,'member.html',{'mymembers': mymembers})
def users(request):
    users= Users.objects.all()
    return render(request,'users.html',{'users': users})

