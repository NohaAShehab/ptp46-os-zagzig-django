from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    # null = true --> db, blank -- admin dashboard
    about = models.TextField(null=True, blank=True)
    logo = models.ImageField(upload_to='departments/logos',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


    def __str__(self):
        return f'{self.name}'

    @property
    def logo_url(self):
        return  f'/media/{self.logo}'
