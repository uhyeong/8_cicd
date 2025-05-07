from django.urls import path
from .views import Helloworldview
urlpatterns = [
    path('helloworld/', Helloworldview.as_view(), name='api-helloworld'),
]