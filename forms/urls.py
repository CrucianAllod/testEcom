from django.urls import path
from .views import SendFormAPI

urlpatterns = [
    path('sendForm/', SendFormAPI.as_view(), name='send'),
]
