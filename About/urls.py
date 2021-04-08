from django.urls import path
from .views import Aboutview
urlpatterns = [
    path('abouts', Aboutview.as_view(), name='about'),
]
