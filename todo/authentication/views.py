from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from validate_email import validate_email
from django.contrib import messages,auth
from django.core.exceptions import ValidationError
from django.http import JsonResponse


def check_auth_status(request):
    return JsonResponse({'is_authenticated': request.user.is_authenticated})

class RegistrationView(View):
    def get(self,request):
        return render(request,'authentication/register.html')
    
    def post(self,request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        context = {
            'fieldsValues': request.POST
        }

        if not User.objects.filter(username=username).exists():
            if not User.objects.filter(email=email).exists():
                # Validate passwords using Django's built-in password validation
                try:
                    validate_password(password, user=User)
                except ValidationError as e:
                    print(e)
                    for message in e.messages:
                        messages.error(request,message)
                    return render(request, 'authentication/register.html', context)

                #Create The User
                user = User.objects.create_user(username=username,email=email)
                user.set_password(password)
                user.is_active = True
                user.save()

                messages.success(request,"Account Succefully created")
                return render(request,'authentication/register.html')

        return render(request,'authentication/register.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'authentication/login.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                #messages.success(request, f"Welcome, {user.username}. You are now logged in.")
                return redirect('tasks')
            else:
                messages.error(request, "Invalid credentials. Please try again.")     
        else : 
            messages.error(request, "Please fill in all fields.")
        return render(request, 'authentication/login.html')

class LogoutView(View):
    def post(self, request):
        auth.logout(request)
        messages.success(request,"You have been logged out")
        return redirect('login')