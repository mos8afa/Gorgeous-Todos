from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
    
class ToDo(models.Model):
    name = models.CharField(verbose_name='ToDo',max_length=500)
    created_at = models.DateTimeField(verbose_name='Created At',default=timezone.now)
    is_done = models.BooleanField(verbose_name='Done',default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

