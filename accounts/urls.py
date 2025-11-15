from django.urls import path

urlpatterns = [
    # سيتم إضافة المسارات لاحقاً
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
]
