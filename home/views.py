from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from .models import Student 
from .forms import stdmodelform
from django.contrib.auth import authenticate, login
from .forms import RegisterForm

from django.contrib.auth import logout

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView





# Create your views here.
def index(request):
    return HttpResponse("this is home page")

def services(request):
    return HttpResponse("this is services page")
def contact(request):
    return render(request,"contActUs.html")

class HomeView(View):
    def get(self, request):
        return HttpResponse("Hello, this is a class based view")
def student(request,id,std):
    return HttpResponse(f"<h1>Student id is {id} and Student Name is {std} </h1>")  


@login_required
def home(request):
    data = {
        "name": "harshit",
        "age":21,
        "std": ["Python", "Django", "React", "MySQL"]
    }
    
    return render(request,"home.html",data)
def about(request):
    return render(request, "about.html")
def add_std(request):
    Student.objects.create(name="ayush", age=23)
    return HttpResponse("student is added")

def show_std(request):
    Students = Student.objects.all()
    return render(request,"data.html",{"Students":Students})
def filter_std(request):
    Students = Student.objects.filter(age__gt=20)#gt= greater then
    return render(request,"data.html",{"Students":Students})

def get_std(request):
    Students = Student.objects.get(age = 21)
    return HttpResponse(Students.name)

def update_std(request):
    Students = Student.objects.get(age = 21)
    Students.name="Rudra"
    Students.save()
    return HttpResponse("name Updated")
    
def delete_std(request):
    
    Students = Student.objects.get(age = 20)
    Students.delete()    
    return HttpResponse("user Deleted")


def addstd(request):
    form = stdmodelform()
    if(request.method =="POST"):
        form = stdmodelform(request.POST)
        if form.is_valid():
            form.save()
    return  render(request,'forms.html',{'form':form})




def register(request):

    form = RegisterForm()

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()
            user.set_password(user.password)
            user.save()

            return redirect('login')
    return render(request, "register.html", {"form": form})




def user_login(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)

            return redirect('html')

    return render(request, "login.html")


def user_logout(request):

    logout(request)

    return redirect('/login')


def change_password(request):

    form = PasswordChangeForm(request.user)

    if request.method == "POST":

        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(request, user)

            return redirect('html')

    return render(request, "change_password.html", {"form": form})




class StudentListView(ListView):

    model = Student

    template_name = "student_list.html"
            

                       