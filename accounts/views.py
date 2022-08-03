
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from accounts.models import Avatar
from.forms import MyUserCreationForm, MyUserEditForm
from django.contrib.auth.decorators import login_required


def login(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                django_login(request, user)
                return redirect('index')
            else:
                return redirect(request, 'accounts/login.html', {'form': form})
                
        else:
            return render(request, 'accounts/login.html', {'form': form})
            
    form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def register(request):
    
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'accounts/register.html', {'form': form})

    form = MyUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


@login_required
def edit_profile(request):
    
    user = request.user
    avatar, _ = Avatar.objects.get_or_create(user=user)
    
    if request.method == 'POST':
        form = MyUserEditForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            if data.get('first_name'):
                user.first_name = data.get('first_name')
            if data.get('last_name'):
                user.last_name = data.get('last_name')
            if data.get('email'):
                user.email = data.get('email')
            
            avatar.image = data.get('avatar') if data.get('avatar') else avatar.image
            
            if data.get('password1') and data.get('password1') == data.get('password2'):
                user.set_password(data.get('password1'))
            avatar.save()
            user.save()
            
            return redirect('profile')

        else:
            return render(request, 'accounts/edit.html', {'form': form})
        
    form = MyUserEditForm(
        initial={
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'avatar': avatar.image
        })
    
    return render(request, 'accounts/edit.html', {'form': form})
    
    