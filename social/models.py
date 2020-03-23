from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.core.validators import MinValueValidator, RegexValidator


class MyProfile(models.Model):
    name = models.CharField(max_length=100)
    user = models.OneToOneField(to=User, on_delete=CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(18)])
    address = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, default="single", choices=(
        ("single", "single"), ("married", "married"), ("widow", "widow"), ("seprated", "seprated"),
        ("commited", "commited")))
    gender = models.CharField(max_length=20, default="other", choices=(("male", "male"), ("female", "female"), ("other", "other")))
    phone_no = models.CharField(validators=[RegexValidator("^0?[5-9]{1}\d{9}$")], max_length=15, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pic = models.ImageField(upload_to="images", null=True)

    def __str__(self):
        return f"{self.user}"


class MyPost(models.Model):
    pic = models.ImageField(upload_to="images", null=True)
    subject = models.CharField(max_length=200)
    msg = models.TextField(null=True, blank=True)
    cr_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.subject}"


class PostComment(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    msg = models.TextField()
    commented_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)
    flag = models.CharField(max_length=20, null=True, blank=True,
                            choices=(("racist", "racist"), ("abbusing", "abbusing")))

    def __str__(self):
        return f"{self.msg}"


class PostLike(models.Model):
    post = models.ForeignKey(to=MyPost, on_delete=CASCADE)
    liked_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE)
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.liked_by}"


class FollowUser(models.Model):
    profile = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="profile")
    followed_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, related_name="followed_by")

    def __str__(self):
        return f"{self.profile} is followed by {self.followed_by}"


class Feedback(models.Model):
    uploaded_by = models.ForeignKey(to=MyProfile, on_delete=CASCADE, null=True, blank=True, related_name="feed")
    feedback = models.TextField()
    cr_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.uploaded_by}"