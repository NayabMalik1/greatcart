from django.shortcuts import render
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages
from django.shortcuts import redirect

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            username=email.split('@')[0],
            password = form.cleaned_data['password']
            
            user=Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )
            user.phone_number = phone_number
            user.save()
            messages.success(request, 'Registration successful')
            return redirect('register')
            # Optionally, you can log the user in after registration
            # Redirect or do something after successful registration
    else:
      form= RegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)
# Create your views here.
def login(request):
    # Logic for login
    return render(request, 'accounts/login.html')
def logout(request):
    # Logic for logout
    return render(request, 'accounts/logout.html')