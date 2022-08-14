from django.db import models

from django.contrib.auth import get_user_model

from apps.users.models import BaseModel
from apps.courses.models import Course

# check if the app uses the default user provided by django
UserProfile = get_user_model()


class UserAsk(BaseModel):
    name = models.CharField(max_length=20, verbose_name="name")
    mobile = models.CharField(max_length=11, verbose_name="phone number")
    course_name = models.CharField(max_length=50, verbose_name="course name")

    class Meta:
        verbose_name = "user ask"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}_{course}({mobile})".format(name=self.name, course=self.course_name, mobile=self.mobile)


class CourseComments(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="course")
    comments = models.CharField(max_length=200, verbose_name="comment contents")

    class Meta:
        verbose_name = "course comments"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.comments


class UserFavorite(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user")
    fav_id = models.IntegerField(verbose_name="data id")
    fav_type = models.IntegerField(choices=((1, "course"), (2, "course organization"), (3, "instructor")),
                                   default=1, verbose_name="favorite/saved type")

    class Meta:
        verbose_name = "user favorite"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{user}_{id}".format(user=self.user.username, id=self.fav_id)


class UserMessage(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user")
    message = models.CharField(max_length=200, verbose_name="message contents")
    has_read = models.BooleanField(default=False, verbose_name="if the message has read")

    class Meta:
        verbose_name = "user message"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


# what course users have studied
class UserCourse(BaseModel):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name="user")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="courses that users have studied")

    class Meta:
        verbose_name = "courses that users have studied"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.course.name