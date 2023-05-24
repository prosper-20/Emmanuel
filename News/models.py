from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="news_pictures", blank=True, null=True)
    slug = models.SlugField()
    date_reported = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "News"


    def __str__(self):
        return self.title
    

@receiver(post_save, sender=User)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
    


    
