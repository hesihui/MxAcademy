from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime

GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female")
)

# use inheritance to share the base value
#  => created a base model at the lowest level of data
class BaseModel(models.Model):
    created_time = models.DateTimeField(default=datetime.datetime.now(tz=timezone.utc), verbose_name="created time")

    class Meta:
        abstract = True

class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name="nick name", default="")
    birthday = models.DateField(verbose_name="birthday", null=True, blank=True)
    gender = models.CharField(verbose_name="gender", choices=GENDER_CHOICES, max_length=6)
    address = models.CharField(max_length=100, verbose_name="address", default="")
    mobile = models.CharField(max_length=11, verbose_name="cell phone number")
    image = models.ImageField(upload_to="avatar/%Y/%m", verbose_name="avatar", default="default.jpg")

    class Meta:
        verbose_name = "user profile"
        verbose_name_plural = verbose_name

    def _str_(self):
        if self.nick_name:
            return self.nick_name
        else:
            return self.username
