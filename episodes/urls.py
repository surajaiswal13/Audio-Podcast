from django.urls import path
from .views import EpisodeAPIView, EpisodeDetailView, ViewAllShowEpisodes

app_name = 'episode'

urlpatterns = [
    # path('episode/', EpisodeAPIView.as_view()),
    # path('episode/<slug:slug>', EpisodeDetailView.as_view()),
    path('create/', EpisodeAPIView.as_view()),
    path('update/<slug:slug>', EpisodeDetailView.as_view()),
    path('view/all', EpisodeAPIView.as_view()),
    path('view/<slug:slug>', EpisodeDetailView.as_view()),
    path('delete/<slug:slug>', EpisodeDetailView.as_view()),
    path('show/<slug:slug>', ViewAllShowEpisodes.as_view()),
]