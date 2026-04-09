from django.contrib import admin
from django.urls import path
from home import views
from .views import HomeView
from .views import StudentListView

urlpatterns = [
   path("h", views.index, name = "home"),
   path("about", views.about, name = "about"),
   path("services", views.services, name = "services"),
   path("contact", views.contact, name = "contact"),
   
   path('cmd', HomeView.as_view(), name='home1'),
   path('view/<int:id>/<str:std>', views.student, name='view'),
    
   path("html/", views.home, name = "html"),
   path("add/", views.add_std, name = "add"),
   path("show/", views.show_std, name = "show"),
   path("filter/", views.filter_std, name = "filter"),
   path("get/", views.get_std, name = "get"),
   path("update/", views.update_std, name = "update"),
   path("delete/", views.delete_std, name = "delete"),
   path("form/", views.addstd, name = "form"),
   path('register/', views.register, name="register"),
   path('', views.user_login, name="login"),
   path('logout/', views.user_logout, name="logout"),
   path('change-password/', views.change_password, name="change_password"),
   path('std-list', StudentListView.as_view(), name="std-list"),
   
   
   
   
   
   
   
   
]

