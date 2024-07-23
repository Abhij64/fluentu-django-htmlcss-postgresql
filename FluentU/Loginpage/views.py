from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages

# Create your views here.
def register(request):
    return render(request,'loginpage.html')
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 == password2:
            user = User.objects.create_user(username=username,email=email,password=password1)
            user.save()
            messages.info(request,"User Created")
            return redirect('/')
        else:
            messages.info(request,"Password Not Matching")
            return redirect('register/signup')
    else:
        return render(request,'loginpage.html')
    
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('register')
    else:
        return render(request,'loginpage.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
