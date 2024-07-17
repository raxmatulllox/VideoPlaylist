from django.urls import path
from .views import home, HomeViews, GeeksDetailView

app_name = 'playlist'

urlpatterns = [
    path('', HomeViews),
    path('<slug:slug>/', GeeksDetailView.as_view(), name='detail'),
]