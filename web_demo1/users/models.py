from django.db import models

# Create your models here.
class web_db(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    gender = models.BooleanField(default=False, null=True)

    class Meta:
        db_table = "users"
