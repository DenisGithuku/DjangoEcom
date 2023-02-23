from django.db import models

# Create your models here.
class UserModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.username