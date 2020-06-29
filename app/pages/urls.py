from django.urls import path
from django.conf.urls import handler404

from . import views

urlpatterns = [
    path('', views.get_home, name='home'),
    path('contacts/', views.ContactPage.as_view(), name='contacts'),
    path('<slug:page_slug>/', views.SinglePage.as_view(), name='page')
]

handler404 = 'pages.views.error_404'