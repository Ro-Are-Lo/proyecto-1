from django.urls import path
from .views import LoginView, UserDetailView  

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),  
    path('user/', UserDetailView.as_view(), name='user-detail'),