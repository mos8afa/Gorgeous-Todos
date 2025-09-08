from django.urls import path
from .views import profile,edit_profile,signup,activate

app_name = 'accounts'

urlpatterns = [
    path('profile/',profile,name='profile'),
    path('edit/',edit_profile,name='edit_profile'),
    path('signup/',signup,name='signup'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
]
