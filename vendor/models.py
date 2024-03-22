from django.db import models
from accounts.models import *
# Create your models here.
class Vendor(models.Model):
    user = models.OneToOneField(User, related_name='user', on_delete = models.CASCADE)
    user_profile = models.OneToOneField(userProfile, related_name = 'userprofile', on_delete = models.CASCADE)
    vendor_name = models.CharField(max_length = 50)
    vendor_liscence = models.ImageField(upload_to = 'vendor/liscence')
    is_approved = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.vendor_name