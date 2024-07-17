from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.detail import DetailView

# Create your views here.
def home(req):
    return render(req, 'playlist/index.html', {'salom': 'salaomaaaa'})


from playlist.models import VideoModel


def HomeViews(request):
    video=VideoModel.objects.all()
    return render(request, 'playlist/index.html', {'video': video})


class GeeksDetailView(DetailView):
    model = VideoModel
    template_name = 'playlist/detail.html'
    context_object_name = 'video'