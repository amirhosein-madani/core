from django.db import models
from django.db.models.signals import post_save 
from django.dispatch import receiver    
from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField( max_length=50 , null= True , blank= True)
    last_name = models.CharField( max_length=50 , blank= True , null= True)
    date_of_birth = models.DateField(null=True , blank= True)
    created_date = models.DateTimeField( auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    profile_picture = models.ImageField( upload_to="profile_Pictures", blank=True , null=True)
    description = models.TextField(blank=True , null=True)


    def __str__(self):
        return f"{self.user.username}"
    
@receiver(post_save , sender= User)
def save_profile(sender, instance , created , **kwargs):
        if created:
            Profile.objects.create(user = instance)
        