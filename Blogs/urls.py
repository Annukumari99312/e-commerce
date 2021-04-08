from django.urls import path
from .views import Blogview
urlpatterns = [
    path('blogs', Blogview.as_view(), name='blog'),
]
