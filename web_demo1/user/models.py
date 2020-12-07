from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    gender = models.BooleanField(default=False)
    age = models.IntegerField(default=18)
    mobiles = models.CharField(max_length=11, null=True)

    class Meta:
        db_table = 'practice_users'