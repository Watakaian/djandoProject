from django.contrib import admin
from django.urls import path
from hospitalapp import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('inner/', views.inner, name='inner'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('details/',views.appointments,name='appointments'),
    path('member/',views.members,name='members'),
    path('users/',views.users,name='users'),
    path('products/',views.products,name='products'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('adminHome/',views.adminhome,name='adminHome')
]
