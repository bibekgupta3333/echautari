from django.contrib import admin
from .models import FollowUser, MyPost, MyProfile, PostComment, PostLike, Feedback
from django.contrib.admin.options import ModelAdmin


class FeedbackAdmin(ModelAdmin):
    list_display = ["uploaded_by", "cr_date"]
    search_fields = ["uploaded_by", "feedback"]
    list_filter = ["cr_date"]


admin.site.register(Feedback, FeedbackAdmin)


class MyPostAdmin(ModelAdmin):
    list_display = ["subject", "cr_date", "uploaded_by"]
    search_fields = ["subject", "msg", "uploaded_by"]
    list_filter = ["cr_date", "uploaded_by"]


admin.site.register(MyPost, MyPostAdmin)


class MyProfileAdmin(ModelAdmin):
    list_display = ["name"]
    search_fields = ["name", "status", "phone_no"]
    list_filter = ["status", "gender"]


admin.site.register(MyProfile, MyProfileAdmin)


class PostCommentAdmin(ModelAdmin):
    list_display = ["post", "msg"]
    search_fields = ["msg", "post", "commented_by"]
    list_filter = ["cr_date", "flag"]


admin.site.register(PostComment, PostCommentAdmin)


class PostLikeAdmin(ModelAdmin):
    list_display = ["post", "liked_by"]
    search_fields = ["post", "liked_by"]
    list_filter = ["cr_date"]


admin.site.register(PostLike, PostLikeAdmin)
