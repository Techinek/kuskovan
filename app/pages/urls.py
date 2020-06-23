from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:page_slug>/', views.SinglePage.as_view(), name='page')
]