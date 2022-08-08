from django.db import models

# Create your models here.
class message(models.Model):
    name = models.CharField(max_length=20, verbose_name="user name", primary_key=True)
    email = models.EmailField(verbose_name="email address")
    address = models.CharField(max_length=100, verbose_name="address")
    message = models.TextField(verbose_name="message")

    class Meta:
        verbose_name = "message"
        verbose_name_plural = verbose_name
        db_table = "message"
