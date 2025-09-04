from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='Profile Picture',upload_to='profile/',null=True,blank=True)
    phone = models.CharField(verbose_name='Phone number',max_length=13)

    def __str__(self):
        return self.user.username
    
@receiver(post_save,sender = User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)


