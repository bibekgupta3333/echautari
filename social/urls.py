from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from social import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('contact/', views.ContactView.as_view()),

    path('profile/edit/<int:pk>', views.MyProfileUpdateView.as_view(success_url="/social/home")),

    path('mypost/create/', views.MyPostCreate.as_view(success_url="/social/mypost")),
    path('mypost/delete/<int:pk>', views.MyPostDeleteView.as_view(success_url="/social/mypost")),
    path('mypost/', views.MyPostListView.as_view()),
    path('mypost/<int:pk>', views.MyPostDetailView.as_view()),

    path('mypost/like/<int:pk>', views.like),
    path('mypost/unlike/<int:pk>', views.unlike),

    path('myprofile/', views.MyProfileListView.as_view()),
    path('myprofile/<int:pk>', views.MyProfileDetailView.as_view()),
    path('myprofile/follow/<int:pk>', views.follow),
    path('myprofile/unfollow/<int:pk>', views.unfollow),

    path('feedback/', views.FeedbackCreate.as_view(success_url="/social/home")),

    path('', RedirectView.as_view(url="home/")),

    #     path('mylist/', views.MyList.as_view()),
    #     path('profile/edit/<int:pk>', views.ProfileUpdateView.as_view(success_url="/college/home")),
]
