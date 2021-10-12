from django.urls import path
from .views import ShowAPIView, ShowDetailView

app_name = 'show'

urlpatterns = [
    path('create/', ShowAPIView.as_view()),
    path('update/<slug:slug>', ShowDetailView.as_view()),
    path('view/all', ShowAPIView.as_view()),
    path('view/<slug:slug>', ShowDetailView.as_view()),
    path('delete/<slug:slug>', ShowDetailView.as_view()),
]