from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth

# Create your views here.
def home(request):
    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
     
        user = User.objects.create_user(username = username, email= email)
        user.save()
        print('user created')
        return redirect('/')

    else:
         return render(request, 'index.html', )
