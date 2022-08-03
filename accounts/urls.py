from django.urls import path
from accounts.views import login, register, profile, edit_profile
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html'), name= 'logout')
]
