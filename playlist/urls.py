from django.urls import path
from .views import *

app_name = 'playlist'

urlpatterns = [
    path('', HomeViews, name='home'),
    path('video-down/', VideoPostView.as_view(), name='video-download-page'),
    # path('download/', youtube, name='download_video'),
    path('youtube/', home.as_view(),name="home-dev"),
    path('<slug:slug>/', VideoDetailView.as_view(), name='detail'),
]