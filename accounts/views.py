from django.shortcuts import render
from . models import Profile

def profile(request):
    user = request.user
    return render(request,'accounts/profile.html',{'user': user})