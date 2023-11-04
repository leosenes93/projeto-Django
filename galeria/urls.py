from django.urls import path
from galeria.views import index

urlpatters = [
    path ('', index)
]