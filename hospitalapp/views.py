from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from hospitalapp.forms import ImageUploadForm
from hospitalapp.models import Member, Appointment, Contact, Users, Products,ImageModel


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
            return redirect('/')

        elif request.POST.get('form_type') == 'formTwo':
            cont = Contact(
                name=request.POST['name'],
                email=request.POST['email'],
                subject=request.POST['subject'],
                message=request.POST['message'],
            )
            cont.save()
            messages.success(request, 'Message sent successfully')
        return redirect('/')
    else:
        return render(request, 'index.html', )


def inner(request):
    return render(request, 'inner-page.html', )


def login(request):
    return render(request, 'login.html', )


def register(request):
    if request.method == 'POST':
        member = Member(
            username=request.POST['username'],
            email=request.POST['email'],
            password=request.POST['password'],
        )
        member.save()
        return redirect('/login')
    else:
        return render(request, 'register.html')

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_images.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')


def appointments(request):
    myappoint = Appointment.objects.all()
    return render(request, 'appointmentDetails.html', {'myappoint': myappoint})


def members(request):
    mymembers = Member.objects.all()
    return render(request, 'member.html', {'mymembers': mymembers})


def users(request):
    users = Users.objects.all()
    return render(request, 'users.html', {'users': users})


def products(request):
    products = Products.objects.all()
    return render(request, 'products.html', {'products': products})


def adminhome(request):
    if request.method == 'POST':
        if Member.objects.filter(
                username=request.POST['username'],
                password=request.POST['password']).exists():
            member = Member.objects.get(
                username=request.POST['username'],
                password=request.POST['password']
            )
            return render(request, 'adminHome.html', {'member': member})
        else:
            return render(request, 'login.html')
            messages.error(request, 'No such member')
    else:
        return render(request, 'login.html')
    messages.error(request, 'No such member')

