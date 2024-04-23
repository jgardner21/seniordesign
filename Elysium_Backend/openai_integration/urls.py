from django.urls import path
from .views import PlaylistGeneratorView

urlpatterns = [
    path('generate-playlist/', PlaylistGeneratorView.as_view(), name='generate-playlist'),
]
