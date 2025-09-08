from django.shortcuts import render , redirect
from . models import Profile
from . forms  import ProfileForm, userForm, UserCreate
from django.urls import reverse
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from django.contrib.auth import login
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_str, force_bytes
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import render_to_string
from django.views.decorators.csrf import csrf_exempt

@permission_classes([IsAuthenticated])
def profile(request):
    user = request.user
    return render(request,'accounts/profile.html',{'user': user})

@permission_classes([IsAuthenticated])
def edit_profile(request):
    my_profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        user_form = userForm(request.POST, instance=request.user) 
        profile_form = ProfileForm(request.POST, request.FILES, instance=my_profile)  

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()

            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()

            return redirect(reverse('accounts:profile'))
    else:
        user_form = userForm(instance=request.user)
        profile_form = ProfileForm(instance=my_profile)

    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@csrf_exempt
def signup(request):
    if request.method == 'POST':
        form = UserCreate(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_activate = False
            user.save()

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            mail_subject = 'Activate your account'
            activation_link = f"http://127.0.0.1:8000/accounts/activate/{uid}/{token}/"
            message = f"Hi {user.username},\n\nPlease click the link below to activate your account:\n{activation_link}\n\nIf this email isn't yours, please ignore this message."

            send_mail(mail_subject, message, None, [user.email], fail_silently=False)
            
            messages.success(request, 'Please confirm your email to complete registration.')
            return render(request, 'registration/confirm_email.html')
        
    else:
        form = UserCreate()
    
    return render(request,'registration/signup.html',{'form':form})

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk = uid)

    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_activate = True
        user.save()
        return redirect('login')    
    else:
        return render(request, 'activation_invalid.html')
