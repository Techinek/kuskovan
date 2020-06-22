from django.urls import path

from . import views

urlpatterns = [
    path("blog/", views.Posts.as_view(), name='home'),
    path("categories/<slug:category_slug>/", views.PostsByCategory.as_view(), name='category'),
    path("tags/<slug:tag_slug>/", views.PostsByTag.as_view(), name='tag'),
    path("search/", views.Search.as_view(), name='search'),
    path("<slug:category_slug>/<slug:post_slug>/", views.PostDetail.as_view(), name='post'),

]