from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    login = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    email = models.EmailField(null=True)
    def create_user(self, name, email, login, password):
        self.email = email
        self.login = login
        self.name = name
        self.set_password(password)
        self.save()

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"


class Record(models.Model):
    name = models.CharField(max_length=50)
    text = models.TextField(max_length=500)
    published_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to='User', on_delete=models.CASCADE, auto_created=True)