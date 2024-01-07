from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register,name='register'),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('detail/',views.detail,name='detail'),
    path('form/',views.form,name='form'),
    path('newpage/', views.newpage, name='newpage'),
    path('logout/', views.logout, name='logout'),

]