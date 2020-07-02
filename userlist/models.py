from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=25)
    role = models.CharField(max_length=25, blank=True)
    registration_date = models.DateField()

    def __str__(self):
        return self.user
