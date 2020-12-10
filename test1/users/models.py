from django.db import models

# Create your models here.
class web_db1(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=128)
    age = models.IntegerField(default=18)
    gender = models.BooleanField(default=False)
    tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'web_db1'
